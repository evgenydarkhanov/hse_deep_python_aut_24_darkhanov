import json
import unittest
from unittest.mock import Mock, call
from module_process_json import process_json


class ProcessJsonTestCase(unittest.TestCase):

    def setUp(self):
        self.json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        self.required_keys = ['key1', 'KEY2']
        self.tokens = ['WORD1', 'word2']
        self.callback_mock = Mock()

    def test_01(self):
        """ 01. general functionality """
        process_json(
            self.json_str,
            self.required_keys,
            self.tokens,
            self.callback_mock
        )

        calls = [
            call('key1', 'WORD1'),
            call('key1', 'word2'),
        ]

        self.assertEqual(calls, self.callback_mock.mock_calls)

    def test_02(self):
        """ 02. errors """
        with self.assertRaises(TypeError):
            process_json(
                12345,
                self.required_keys,
                self.tokens,
                self.callback_mock
            )

        with self.assertRaises(json.decoder.JSONDecodeError):
            process_json(
                'hello world',
                self.required_keys,
                self.tokens,
                self.callback_mock
            )

    def test_03(self):
        """ 03. return None """
        self.assertIsNone(process_json(self.json_str))
        self.assertIsNone(process_json(self.json_str, [], []))
        self.assertIsNone(process_json(self.json_str, [''], ['']))
        self.assertIsNone(
            process_json(
                '{}',
                self.required_keys,
                self.tokens,
                self.callback_mock
            )
        )

        self.assertIsNone(
            process_json(
                self.json_str,
                self.required_keys,
                self.tokens
            )
        )

        self.assertIsNone(
            process_json(
                self.json_str,
                self.required_keys,
                [],
                self.callback_mock
            )
        )

        self.assertIsNone(
            process_json(
                self.json_str,
                [],
                self.tokens,
                self.callback_mock
            )
        )

        self.assertIsNone(
            process_json(
                self.json_str,
                ['key10', 'key20'],
                self.tokens,
                self.callback_mock
            )
        )
        self.callback_mock.assert_not_called()

        self.assertIsNone(
            process_json(
                self.json_str,
                self.required_keys,
                ['WORD10', 'WORD20'],
                self.callback_mock
            )
        )
        self.callback_mock.assert_not_called()

    def test_04(self):
        """ 04. font register"""
        process_json(
            self.json_str,
            ['KeY1'],
            ['word1'],
            self.callback_mock
        )
        self.callback_mock.assert_not_called()

        process_json(
            self.json_str,
            ['key1'],
            ['word1'],
            self.callback_mock
        )
        self.callback_mock.assert_called_with('key1', 'word1')

        process_json(
            self.json_str,
            ['key1'],
            ['wOrD1'],
            self.callback_mock
        )
        self.callback_mock.assert_called_with('key1', 'wOrD1')


if __name__ == "__main__":
    unittest.main()
