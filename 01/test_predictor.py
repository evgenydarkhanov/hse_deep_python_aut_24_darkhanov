import unittest
from unittest.mock import patch
from module_predictor import GreaterEqualError, SomeModel, predict_message_mood


class PredictorTestCase(unittest.TestCase):

    def test_01(self):
        """ 01. general functionality """
        result = predict_message_mood("Чапаев и пустота", 0.1, 0.2)
        self.assertEqual(result, "отл")

        result = predict_message_mood("Чапаев и пустота")
        self.assertEqual(result, "норм")

        result = predict_message_mood("Вулкан", 0.8, 0.9)
        self.assertEqual(result, "неуд")

    @patch.object(SomeModel, 'predict')
    def test_02(self, mock_predict):
        """ 02. general functionality with mock """
        mock_predict.return_value = 0.9
        result = predict_message_mood("Чапаев и пустота")
        self.assertEqual(result, "отл")

        mock_predict.return_value = 0.85
        result = predict_message_mood("Чапаев и пустота", 0.8, 0.99)
        self.assertEqual(result, "норм")

        mock_predict.return_value = 0.1
        result = predict_message_mood("Вулкан")
        self.assertEqual(result, "неуд")

        mock_predict.return_value = 0.1
        result = predict_message_mood('test')
        self.assertEqual(result, "неуд")

        mock_predict.return_value = 0.5
        result = predict_message_mood('test')
        self.assertEqual(result, "норм")

        mock_predict.return_value = 0.9
        result = predict_message_mood('test')
        self.assertEqual(result, "отл")

        mock_predict.return_value = 0.5
        result = predict_message_mood('test')
        self.assertNotEqual(result, "отл")

    def test_03(self):
        """ 03. errors """
        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 0.8, 0.8)

        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 0.00001, 0.00001)

        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 10000.0, 10000.0)

        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 0.9, 0.8)

        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 0.99999, 0.99998)

        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 10000.0, 0.99999)

        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 10000.0, 9999.9)

        with self.assertRaises(TypeError):
            _ = predict_message_mood(message=12345)

        with self.assertRaises(TypeError):
            _ = predict_message_mood('test', bad_thresholds='0.3')

        with self.assertRaises(TypeError):
            _ = predict_message_mood('test', good_thresholds='0.8')

    @patch.object(SomeModel, 'predict')
    def test_04(self, mock_predict):
        """ 04. different thresholds """
        mock_predict.return_value = 1.0
        result = predict_message_mood('test', 10.0, 20.0)
        self.assertEqual(result, 'неуд')

        mock_predict.return_value = -10.0
        result = predict_message_mood('test', -20.0, 0.0)
        self.assertEqual(result, 'норм')

        mock_predict.return_value = 12345
        result = predict_message_mood('test', -20.0, 0.0)
        self.assertEqual(result, 'отл')

        mock_predict.return_value = 10.0
        result = predict_message_mood('test', -20.0, 10.0)
        self.assertEqual(result, 'норм')

        mock_predict.return_value = -10.0
        result = predict_message_mood('test', -10.0, 0.0)
        self.assertEqual(result, 'норм')

        mock_predict.return_value = 10.0
        with self.assertRaises(GreaterEqualError):
            _ = predict_message_mood('test', 10.0, 10.0)

        mock_predict.return_value = 1.00001
        result = predict_message_mood('test', 0.99999, 1.0)
        self.assertEqual(result, 'отл')

        mock_predict.return_value = 1.0
        result = predict_message_mood('test', 0.99999, 1.00001)
        self.assertEqual(result, 'норм')

        mock_predict.return_value = 1.0
        result = predict_message_mood('test', 0.99999, 1.0)
        self.assertEqual(result, 'норм')

        mock_predict.return_value = 0.99999
        result = predict_message_mood('test', 0.99999, 1.0)
        self.assertEqual(result, 'норм')

        mock_predict.return_value = 0.99999
        result = predict_message_mood('test', 1.0, 1.00001)
        self.assertEqual(result, 'неуд')

    @patch.object(SomeModel, 'predict')
    def test_05(self, mock_predict):
        """ messages """
        mock_predict.return_value = 0.5
        with self.assertRaises(TypeError) as ctx:
            _ = predict_message_mood(message=12345)

        mock_predict.assert_not_called()
        self.assertEqual("message should be 'str'", str(ctx.exception))

        message = 'Hello, world!'
        predict_message_mood(message)
        mock_predict.assert_called_once_with(message)

        predict_message_mood('test_1')
        predict_message_mood('test_2')
        predict_message_mood('test_3')

        expected = [
            unittest.mock.call('Hello, world!'),
            unittest.mock.call('test_1'),
            unittest.mock.call('test_2'),
            unittest.mock.call('test_3'),
        ]
        self.assertEqual(expected, mock_predict.mock_calls)


if __name__ == "__main__":
    unittest.main()
