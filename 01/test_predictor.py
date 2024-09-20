import unittest
from unittest.mock import Mock
from predictor import GreaterEqualError, SomeModel, predict_message_mood


class PredictorTestCase(unittest.TestCase):

    def setUp(self):
        self.model = Mock(spec=SomeModel)

    def test_01_norm(self):
        """ 01. TEST 'норм' """
        self.model.predict.return_value = 0.5
        result = predict_message_mood(self.model, 'test')
        self.assertEqual(result, 'норм')

    def test_02_otl(self):
        """ 02. TEST 'отл' """
        self.model.predict.return_value = 0.9
        result = predict_message_mood(self.model, 'test')
        self.assertEqual(result, 'отл')

    def test_03_neud(self):
        """ 03. TEST 'неуд' """
        self.model.predict.return_value = 0.1
        result = predict_message_mood(self.model, 'test')
        self.assertEqual(result, 'неуд')

    def test_04_not_equal(self):
        """ 04. TEST 'неуд' != 'отл' """
        self.model.predict.return_value = 0.1
        result = predict_message_mood(self.model, 'test')
        self.assertNotEqual(result, 'отл')

    def test_05_message_not_str(self):
        """ 05. TEST исключение 'message' """
        with self.assertRaises(TypeError):
            predict_message_mood(self.model, 123)

    def test_06_bad_not_float(self):
        """ 06. TEST исключение 'bad_thresholds' """
        with self.assertRaises(TypeError):
            predict_message_mood(self.model, 'test', bad_thresholds=1)

    def test_07_good_not_float(self):
        """ 07. TEST исключение 'good_thresholds' """
        with self.assertRaises(TypeError):
            predict_message_mood(self.model, 'test', good_thresholds=1)

    def test_08_bad_greater_good(self):
        """ 08. TEST исключение 'bad_thresholds' > 'good_thresholds' """
        with self.assertRaises(GreaterEqualError):
            predict_message_mood(self.model, 'test', bad_thresholds=0.9, good_thresholds=0.8)

    def test_09_bad_equal_good(self):
        """ 09. TEST исключение 'bad_thresholds' == 'good_thresholds' """
        with self.assertRaises(GreaterEqualError):
            predict_message_mood(self.model, 'test', bad_thresholds=0.8, good_thresholds=0.8)


if __name__ == "__main__":
    unittest.main()
