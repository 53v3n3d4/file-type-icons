import importlib

from unittest import TestCase
from unittest.mock import Mock

constants_icons_themes = importlib.import_module(
    'Zukan-Icon-Theme.tests.mocks.constants_icons_themes'
)
search_themes = importlib.import_module(
    'Zukan-Icon-Theme.src.zukan_icon_theme.helpers.search_themes'
)


class TestFilterResourcesThemes(TestCase):
    def test_mock_filter_resources_themes(self):
        filter_themes_list = ['a', 'b', 'c']
        mock = Mock()
        mock.search_themes.filter_resources_themes(filter_themes_list)
        mock.search_themes.filter_resources_themes.assert_called_with(
            filter_themes_list
        )

    def test_filter_resources_themes(self):
        result = search_themes.filter_resources_themes(
            constants_icons_themes.TEST_FILTER_THEMES_LIST
        )
        self.assertEqual(
            result, constants_icons_themes.TEST_FILTER_THEMES_LIST_EXPECTED
        )


class TestSearchResourcesSublimeThemes(TestCase):
    def test_mock_search_resources_sublime_themes(self):
        filter_themes_list = ['a', 'b', 'c']
        mock = Mock()
        mock.search_themes.search_resources_sublime_themes(filter_themes_list)
        mock.search_themes.search_resources_sublime_themes.assert_called_with(
            filter_themes_list
        )


class TestFilterThemes(TestCase):
    def test_filter_resources_themes_params(self):
        search_themes.filter_resources_themes(
            constants_icons_themes.TEST_FILTER_THEMES_LIST
        )
        self.assertIsInstance(constants_icons_themes.TEST_FILTER_THEMES_LIST, list)
        self.assertNotIsInstance(constants_icons_themes.TEST_FILTER_THEMES_LIST, int)
        self.assertNotIsInstance(constants_icons_themes.TEST_FILTER_THEMES_LIST, str)
        self.assertNotIsInstance(constants_icons_themes.TEST_FILTER_THEMES_LIST, bool)
        self.assertNotIsInstance(constants_icons_themes.TEST_FILTER_THEMES_LIST, dict)
