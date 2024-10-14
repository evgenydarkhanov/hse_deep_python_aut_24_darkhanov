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
            predict_message_mood('test', 0.8, 0.8)

        with self.assertRaises(GreaterEqualError):
            predict_message_mood('test', 0.9, 0.8)

        with self.assertRaises(TypeError):
            predict_message_mood(message=12345)

        with self.assertRaises(TypeError):
            predict_message_mood('test', bad_thresholds='0.3')

        with self.assertRaises(TypeError):
            predict_message_mood('test', good_thresholds='0.8')

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
            predict_message_mood('test', 10.0, 10.0)


if __name__ == "__main__":
    unittest.main()
