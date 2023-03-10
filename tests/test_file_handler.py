import os
import pickle
import unittest
from parameterized import parameterized

from HyDGL.file_handler import FileHandler
from tests.utils import TEST_FILE_LALMER, TEST_FILE_QM_DATA_OREDIA, TEST_FILE_JSON, Utils


class TestFileHandler(unittest.TestCase):

    @parameterized.expand([

        [
            TEST_FILE_LALMER
        ]

    ])
    def test_read_file(self, file_path):

        result = FileHandler.read_file(file_path)

        f = open(file_path, 'r')
        expected = f.read()
        f.close()

        self.assertEqual(result, expected)

    @parameterized.expand([

        [
            './tests/files/not-existing-file',
            FileNotFoundError
        ],

        [
            './tests/files/',
            IsADirectoryError
        ],

    ])
    def test_read_file_with_invalid_input(self, file_path, expected_error):

        self.assertRaises(expected_error, FileHandler.read_file, file_path)

    @parameterized.expand([

        [
            'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwgc2'
            'VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBh'
            'bGlxdWEuIFV0IGVuaW0gYWQgbWluaW0gdmVuaWFtLCBxdWlzIG5vc3RydWQgZXhlcmNpdGF0aW9uIH'
            'VsbGFtY28gbGFib3JpcyBuaXNpIHV0IGFsaXF1aXAgZXggZWEgY29tbW9kbyBjb25zZXF1YXQuIER1'
            'aXMgYXV0ZSBpcnVyZSBkb2xvciBpbiByZXByZWhlbmRlcml0IGluIHZvbHVwdGF0ZSB2ZWxpdCBlc3'
            'NlIGNpbGx1bSBkb2xvcmUgZXUgZnVnaWF0IG51bGxhIHBhcmlhdHVyLiBFeGNlcHRldXIgc2ludCBv'
            'Y2NhZWNhdCBjdXBpZGF0YXQgbm9uIHByb2lkZW50LCBzdW50IGluIGN1bHBhIHF1aSBvZmZpY2lhIG'
            'Rlc2VydW50IG1vbGxpdCBhbmltIGlkIGVzdCBsYWJvcnVtLg=='
        ]

    ])
    def test_write_file(self, content):

        tmp_file_path = '/tmp/HyDGL-test-file.txt'

        FileHandler.write_file(tmp_file_path, content)
        result = FileHandler.read_file(tmp_file_path)
        self.assertEqual(content, result)

    @parameterized.expand([

        [
            './tests/files/not-existing-file',
            FileNotFoundError
        ],

        [
            './tests/files/',
            IsADirectoryError
        ],

    ])
    def test_read_binary_file_with_invalid_input(self, file_path, expected_error):

        self.assertRaises(expected_error, FileHandler.read_binary_file, file_path)

    @parameterized.expand([

        [
            TEST_FILE_QM_DATA_OREDIA
        ]

    ])
    def test_read_binary_file(self, file_path):

        result = FileHandler.read_binary_file(file_path)

        f = open(file_path, 'rb')
        expected = pickle.load(f)
        f.close()

        Utils.assert_are_almost_equal(result, expected)

    @parameterized.expand([

        [
            TEST_FILE_QM_DATA_OREDIA
        ]

    ])
    def test_write_binary_file(self, file_path):

        tmp_file_path = '/tmp/HyDGL-test-file.bin'

        content = FileHandler.read_binary_file(file_path)
        FileHandler.write_binary_file(tmp_file_path, content)

        result = FileHandler.read_binary_file(tmp_file_path)
        Utils.assert_are_almost_equal(content, result)

    @parameterized.expand([

        [
        ]

    ])
    def test_clear_directory(self):

        FileHandler.write_file('/tmp/HyDGL-test-file.txt', 'asdfasf')
        FileHandler.clear_directory('/tmp/', ['HyDGL-test-file.txt', 'HyDGL-test-file2.txt'])

        self.assertFalse(os.path.isfile('/tmp/HyDGL-test-file.txt'))
        self.assertFalse(os.path.isfile('/tmp/HyDGL-test-file2.txt'))

    @parameterized.expand([

        [
            TEST_FILE_JSON,
            {
                'age': 30,
                'matrix': [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                'name': 'John'
            }
        ]

    ])
    def test_read_dict_from_json_file(self, file_path, expected):

        result = FileHandler.read_dict_from_json_file(file_path)

        self.assertEqual(result, expected)

    @parameterized.expand([

        [
            TEST_FILE_JSON,
        ]

    ])
    def test_write_dict_to_json_file(self, file_path):

        tmp_file_path = '/tmp/HyDGL-test-file.json'

        content = FileHandler.read_dict_from_json_file(file_path)
        FileHandler.write_dict_to_json_file(tmp_file_path, content)

        result = FileHandler.read_dict_from_json_file(tmp_file_path)
        Utils.assert_are_almost_equal(content, result)

    @parameterized.expand([

        [
            './tests/files/not-existing-file',
            FileNotFoundError
        ],

        [
            './tests/files/',
            IsADirectoryError
        ],

    ])
    def test_read_dict_from_json_file_with_invalid_input(self, file_path, expected_error):

        self.assertRaises(expected_error, FileHandler.read_dict_from_json_file, file_path)
