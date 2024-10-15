import unittest
from unittest.mock import patch, call
from module_retry_deco import retry_deco


class RetryDecoTestCase(unittest.TestCase):

    @patch('builtins.print')
    def test_01(self, mock_print):
        """ 01. general functionality """
        @retry_deco(3)
        def add(a, b):
            return a + b

        add(4, 2)
        log_string = 'run "add" with positional args = (4, 2), ' \
                     'keyword kwargs = {}, attempt = 1, result = 6'
        mock_print.assert_called_with(log_string)

        add(4, b=3)
        log_string = 'run "add" with positional args = (4,), ' \
                     'keyword kwargs = {\'b\': 3}, attempt = 1, result = 7'
        mock_print.assert_called_with(log_string)

        @retry_deco(3)
        def check_str(value=None):
            if value is None:
                raise ValueError()
            return isinstance(value, str)

        check_str(value='123')
        log_string = 'run "check_str" with positional args = (), ' \
                     'keyword kwargs = {\'value\': \'123\'}, ' \
                     'attempt = 1, result = True'
        mock_print.assert_called_with(log_string)

        check_str(value=1)
        log_string = 'run "check_str" with positional args = (), ' \
                     'keyword kwargs = {\'value\': 1}, ' \
                     'attempt = 1, result = False'
        mock_print.assert_called_with(log_string)

        check_str(value=None)
        self.assertEqual(7, mock_print.call_count)
        # 7, потому что вызовы были ранее

        @retry_deco(2, [ValueError])
        def check_int(value=None):
            if value is None:
                raise ValueError()
            return isinstance(value, int)

        check_int(value=1)
        log_string = 'run "check_int" with positional args = (), ' \
                     'keyword kwargs = {\'value\': 1}, ' \
                     'attempt = 1, result = True'
        mock_print.assert_called_with(log_string)

        check_int(value=None)
        log_string = 'run "check_int" with positional args = (), ' \
                     'keyword kwargs = {\'value\': None}, ' \
                     'attempt = 1, exception = ValueError'
        mock_print.assert_called_with(log_string)

    @patch('builtins.print')
    def test_02(self, mock_print):
        """ 02. decorator without parameters """
        @retry_deco()
        def return_one():
            return 1

        return_one()
        log_string = 'run "return_one" with positional args = (), ' \
                     'keyword kwargs = {}, attempt = 1, result = 1'

        mock_print.assert_called_with(log_string)

    @patch('builtins.print')
    def test_03(self, mock_print):
        """ 03. decorator with repeat """
        @retry_deco(2)
        def check_str(value=None):
            if value is None:
                raise ValueError()
            return isinstance(value, str)

        check_str()
        calls = [
            call(
                'run "check_str" with positional args = (), ' +
                'keyword kwargs = {}, attempt = 1, exception = ValueError'
            ),
            call(
                'run "check_str" with positional args = (), ' +
                'keyword kwargs = {}, attempt = 2, exception = ValueError'
            ),
        ]
        self.assertEqual(calls, mock_print.mock_calls)

    @patch('builtins.print')
    def test_04(self, mock_print):
        """ 04. decorator with errors """
        @retry_deco(repeat=None, errors=[ValueError])
        def raise_error():
            raise ValueError()

        raise_error()
        log_string = 'run "raise_error" with positional args = (), ' \
                     'keyword kwargs = {}, attempt = 1, exception = ValueError'

        mock_print.assert_called_with(log_string)

    @patch('builtins.print')
    def test_05(self, mock_print):
        """ 05. decorator with both """
        @retry_deco(2, [ValueError])
        def raise_type_error():
            raise TypeError()

        raise_type_error()
        self.assertEqual(2, mock_print.call_count)

        @retry_deco(2, [ValueError])
        def raise_value_error():
            raise ValueError()

        raise_value_error()
        log_string = 'run "raise_value_error" with positional args = (), ' \
                     'keyword kwargs = {}, attempt = 1, exception = ValueError'

        mock_print.assert_called_with(log_string)

    @patch('builtins.print')
    def test_06(self, mock_print):
        """ 06. decorator with repeat=0, repeat=1"""
        @retry_deco(0)
        def return_one():
            return 1

        return_one()
        mock_print.assert_not_called()

        @retry_deco(1)
        def return_two():
            return 2

        return_two()
        self.assertEqual(1, mock_print.call_count)

    @patch('builtins.print')
    def test_07(self, mock_print):
        """ 07. decorator with errors=[] """
        @retry_deco(100, [])
        def raise_type_error():
            raise TypeError()

        raise_type_error()
        self.assertEqual(100, mock_print.call_count)

    @patch('builtins.print')
    def test_08(self, mock_print):
        """ 08. decorator with custom exception """
        class CustomException(Exception):
            pass

        @retry_deco(3, [CustomException])
        def raise_custom():
            raise CustomException()

        raise_custom()
        log_string = 'run "raise_custom" with positional args = (), ' \
                     'keyword kwargs = {}, attempt = 1, ' \
                     'exception = CustomException'

        mock_print.assert_called_with(log_string)


if __name__ == "__main__":
    unittest.main()
