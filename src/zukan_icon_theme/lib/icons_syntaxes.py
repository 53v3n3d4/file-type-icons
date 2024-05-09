import logging
import os
import glob

from ..helpers.print_message import print_filenotfounderror, print_oserror
from ..helpers.read_write_data import dump_yaml_data, read_pickle_data
from ..utils.zukan_dir_paths import (
    ASSETS_PATH,
    ZUKAN_PKG_ICONS_SYNTAXES_PATH,
    ZUKAN_SYNTAXES_DATA_FILE,
)

logger = logging.getLogger(__name__)


class ZukanSyntax:
    """
    Create and remove sublime-syntaxes in icons_syntaxes folder.
    """

    def create_icons_syntaxes():
        """
        Create icons sublime-syntaxes files.
        """
        try:
            zukan_icons_syntaxes = read_pickle_data(ZUKAN_SYNTAXES_DATA_FILE)
            for s in zukan_icons_syntaxes:
                filename = s['name'] + '.sublime-syntax'
                syntax_file_path = os.path.join(ZUKAN_PKG_ICONS_SYNTAXES_PATH, filename)
                # print(syntax_file_path)
                dump_yaml_data(s, syntax_file_path)
            logger.info('sublime-syntaxes created.')
            return zukan_icons_syntaxes
        except FileNotFoundError:
            # print_filenotfounderror(filename)
            logger.error(
                '[Errno %d] %s: %r', errno.ENOENT, os.strerror(errno.ENOENT), filename
            )
        except OSError:
            # print_oserror(filename)
            logger.error(
                '[Errno %d] %s: %r', errno.EACCES, os.strerror(errno.EACCES), filename
            )

    def remove_icons_syntaxes():
        """
        Remove all sublime-syntaxes files, leaving pickle file.
        """
        try:
            for s in glob.iglob(
                os.path.join(ZUKAN_PKG_ICONS_SYNTAXES_PATH, '*.sublime-syntax')
            ):
                os.remove(s)
            logger.info('sublime-syntaxes removed.')
        except FileNotFoundError:
            # print_filenotfounderror(s)
            logger.error(
                '[Errno %d] %s: %r', errno.ENOENT, os.strerror(errno.ENOENT), s
            )
        except OSError:
            # print_oserror(s)
            logger.error(
                '[Errno %d] %s: %r', errno.EACCES, os.strerror(errno.EACCES), s
            )