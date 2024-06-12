import logging
import os
import sublime
import threading

from .install import InstallEvent
from ..lib.icons_preferences import ZukanPreference
from ..lib.icons_syntaxes import ZukanSyntax
from ..lib.icons_themes import ZukanTheme
from ..helpers.read_write_data import dump_json_data
from ..helpers.thread_progress import ThreadProgress
from ..utils.zukan_dir_paths import (  # noqa: E402
    ZUKAN_PKG_ICONS_PREFERENCES_PATH,
    ZUKAN_PKG_ICONS_SYNTAXES_PATH,
    ZUKAN_VERSION_FILE,
)

logger = logging.getLogger(__name__)


class SettingsEvent:
    def get_user_theme():
        logger.debug('Preferences.sublime-settings changed')
        theme_name = sublime.load_settings('Preferences.sublime-settings').get('theme')

        if theme_name not in ZukanTheme.list_created_icons_themes():
            # Delete preferences to avoid error unable to decode 'icon_file_type'
            # Example of extensions that this errors show: HAML, LICENSE, README, Makefile
            if any(
                syntax.endswith('.sublime-syntax')
                for syntax in os.listdir(ZUKAN_PKG_ICONS_SYNTAXES_PATH)
            ):
                ZukanSyntax.delete_icons_syntaxes()
            if any(
                preferences.endswith('.tmPreferences')
                for preferences in os.listdir(ZUKAN_PKG_ICONS_PREFERENCES_PATH)
            ):
                ZukanPreference.delete_icons_preferences()

        if theme_name in ZukanTheme.list_created_icons_themes():
            if not any(
                preferences.endswith('.tmPreferences')
                for preferences in os.listdir(ZUKAN_PKG_ICONS_PREFERENCES_PATH)
            ):
                threading.Thread(target=ZukanPreference.build_icons_preferences).start()

            if not any(
                syntax.endswith('.sublime-syntax')
                for syntax in os.listdir(ZUKAN_PKG_ICONS_SYNTAXES_PATH)
            ):
                ts = threading.Thread(target=ZukanSyntax.build_icons_syntaxes)
                ts.start()
                ThreadProgress(ts, 'Building zukan files', 'Build done')

    def upgrade_zukan_files(auto_upgraded: bool):
        logger.debug('If package upgraded, begin rebuild...')
        pkg_version = sublime.load_settings('Zukan Icon Theme.sublime-settings').get(
            'version'
        )

        if os.path.exists(ZUKAN_VERSION_FILE) and auto_upgraded is True:
            installed_pkg_version = sublime.load_settings(
                'zukan-version.sublime-settings'
            ).get('version')
            if pkg_version == installed_pkg_version:
                logger.debug('no need to update.')

            if pkg_version != installed_pkg_version:
                logger.info('updating package...')
                InstallEvent.install_upgrade_thread()

                content = {'version': pkg_version}
                dump_json_data(content, ZUKAN_VERSION_FILE)

        if not os.path.exists(ZUKAN_VERSION_FILE):
            content = {'version': pkg_version}
            dump_json_data(content, ZUKAN_VERSION_FILE)

    def zukan_options_settings():
        # auto_upgraded setting
        auto_upgraded = sublime.load_settings('Zukan Icon Theme.sublime-settings').get(
            'rebuild_on_upgrade'
        )

        if auto_upgraded is True:
            SettingsEvent.upgrade_zukan_files(auto_upgraded)

    def user_preferences_changed():
        user_preferences = sublime.load_settings('Preferences.sublime-settings')

        user_preferences.add_on_change('Preferences', SettingsEvent.get_user_theme)

    def zukan_preferences_changed():
        # if version changed, upgrade rebuild syntax and preferences.
        zukan_pkg_version = sublime.load_settings('Zukan Icon Theme.sublime-settings')

        zukan_pkg_version.add_on_change(
            'Zukan Icon Theme', SettingsEvent.zukan_options_settings
        )
