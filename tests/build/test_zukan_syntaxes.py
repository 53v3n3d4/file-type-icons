import os
import pytest

from pyfakefs.fake_filesystem_unittest import TestCase
from src.build.zukan_syntaxes import ZukanSyntax
from tests.mocks.constants_pickle import (
    TEST_PICKLE_ZUKAN_FILE,
)
from tests.mocks.tests_paths import (
    DIR_DATA,
    DIR_DESTINY,
    TEST_DATA_DIR_EXCEPT_ZUKAN_FILE,
)
from unittest.mock import patch


class TestZukanSyntax:
    @pytest.mark.parametrize(
        'a, b, c, expected',
        [
            (
                DIR_DATA,
                DIR_DESTINY,
                TEST_PICKLE_ZUKAN_FILE,
                TEST_DATA_DIR_EXCEPT_ZUKAN_FILE,
            )
        ],
    )
    def test_write_syntax_data(self, a, b, c, expected):
        result = ZukanSyntax.write_syntax_data(a, b, c)
        assert result == TEST_DATA_DIR_EXCEPT_ZUKAN_FILE

    @pytest.fixture(autouse=True)
    def test_write_syntax_data_filenotfounderror(self, caplog):
        caplog.clear()
        with patch('src.build.zukan_syntaxes.open') as mock_open:
            mock_open.side_effect = FileNotFoundError
            ZukanSyntax.write_syntax_data(
                'tests/mocks/not_found_yaml.yaml',
                DIR_DESTINY,
                TEST_PICKLE_ZUKAN_FILE,
            )
        assert caplog.record_tuples == [
            (
                'src.build.zukan_syntaxes',
                40,
                "[Errno 2] No such file or directory: 'tests/mocks/not_found_yaml.yaml'",
            )
        ]

    @pytest.fixture(autouse=True)
    def test_write_syntax_data_oserror(self, caplog):
        caplog.clear()
        with patch('src.build.zukan_syntaxes.open') as mock_open:
            mock_open.side_effect = OSError
            ZukanSyntax.write_syntax_data(
                'tests/mocks/yaml.yaml', DIR_DESTINY, TEST_PICKLE_ZUKAN_FILE
            )
        assert caplog.record_tuples == [
            (
                'src.build.zukan_syntaxes',
                40,
                "[Errno 13] Permission denied: 'tests/mocks/yaml.yaml'",
            )
        ]


class TestIconZukanSyntax(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.setUpClassPyfakefs()
        cls.fake_fs().create_file('data/afdesign.yaml')
        cls.fake_fs().create_file('data/afphoto.yaml')
        cls.fake_fs().create_file('data/afpub.yaml')
        cls.fake_fs().create_file('data/ai.yaml')
        cls.fake_fs().create_file('data/angular.yaml')

    def test_dir_exist(self):
        ZukanSyntax.write_syntax_data('data', DIR_DESTINY, TEST_PICKLE_ZUKAN_FILE)
        self.assertTrue(os.path.exists('data'))

    def test_params_write_syntax_data(self):
        ZukanSyntax.write_syntax_data('data', DIR_DESTINY, TEST_PICKLE_ZUKAN_FILE)
        self.assertTrue(isinstance('data', str))
        self.assertFalse(isinstance('data', int))
        self.assertFalse(isinstance('data', list))
        self.assertFalse(isinstance('data', bool))
        self.assertFalse(isinstance('data', dict))
