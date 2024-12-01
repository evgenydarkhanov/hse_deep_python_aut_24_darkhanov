import unittest
from module_descriptor import Data


class DescriptorTestCase(unittest.TestCase):

    def test_01(self):
        """ 01. general functionality """
        data1 = Data(10, "product", 20)
        data2 = Data(100, "PRODUCT", 200)
        self.assertEqual(data1.num, 10)
        self.assertEqual(data2.num, 100)

        data1.num = 50
        data1.price = 1000
        self.assertEqual(data1.num, 50)
        self.assertEqual(data2.num, 100)
        self.assertEqual(data1.price, 1000)

        del data1.num
        del data2.price
        data1_dict = {'name': 'product', 'price': 1000}
        data2_dict = {'num': 100, 'name': 'PRODUCT'}
        self.assertEqual(data1.__dict__, data1_dict)
        self.assertEqual(data2.__dict__, data2_dict)

    def test_02(self):
        """ 02. errors """
        num_field_str = "'num' must be an Integer"
        name_field_str = "'name' must be a String"
        price_field_str_1 = "'price' must be an Integer"
        price_field_str_2 = "'price' must be a PositiveInteger"

        with self.assertRaises(TypeError) as context:
            _ = Data(10.0, "product", 20)
        self.assertEqual(str(context.exception), num_field_str)

        with self.assertRaises(TypeError) as context:
            _ = Data(10, 1000, 20)
        self.assertEqual(str(context.exception), name_field_str)

        with self.assertRaises(TypeError) as context:
            _ = Data(10, "product", -20)
        self.assertEqual(str(context.exception), price_field_str_2)

        with self.assertRaises(TypeError) as context:
            _ = Data(10, "product", 20.0)
        self.assertEqual(str(context.exception), price_field_str_1)

        # валидные значения устанавливаются
        data = Data(10, "product", 20)
        data.num = 100
        data.name = "PRODUCT"
        data.price = 200

        num_field = data.num
        name_field = data.name
        price_field = data.price

        # невалидные значения не устанавливаются, фактические не меняются
        # num field
        with self.assertRaises(TypeError) as context:
            data.num = 10.0
        self.assertEqual(str(context.exception), num_field_str)

        with self.assertRaises(TypeError) as context:
            data.num = '10'
        self.assertEqual(str(context.exception), num_field_str)

        with self.assertRaises(TypeError) as context:
            data.num = [10]
        self.assertEqual(str(context.exception), num_field_str)

        self.assertEqual(data.num, num_field)
        self.assertEqual(id(data.num), id(num_field))
        self.assertIs(data.num, num_field)

        # name field
        with self.assertRaises(TypeError) as context:
            data.name = 10
        self.assertEqual(str(context.exception), name_field_str)

        with self.assertRaises(TypeError) as context:
            data.name = 10.0
        self.assertEqual(str(context.exception), name_field_str)

        with self.assertRaises(TypeError) as context:
            data.name = [10]
        self.assertEqual(str(context.exception), name_field_str)

        self.assertEqual(data.name, name_field)
        self.assertEqual(id(data.name), id(name_field))
        self.assertIs(data.name, name_field)

        # price field
        with self.assertRaises(TypeError) as context:
            data.price = -10
        self.assertEqual(str(context.exception), price_field_str_2)

        with self.assertRaises(TypeError) as context:
            data.price = 10.0
        self.assertEqual(str(context.exception), price_field_str_1)

        with self.assertRaises(TypeError) as context:
            data.price = '10'
        self.assertEqual(str(context.exception), price_field_str_1)

        self.assertEqual(data.price, price_field)
        self.assertIs(data.price, price_field)
        self.assertEqual(id(data.price), id(price_field))

    def test_03(self):
        """ 03. instances are different """
        data1 = Data(10, "product", 20)
        data2 = Data(10, "product", 20)
        self.assertIsNot(data1, data2)
        self.assertNotEqual(id(data1), id(data2))

        data2_id = id(data2)
        data2.num = 100
        self.assertNotEqual(id(data1.num), id(data2.num))
        self.assertEqual(id(data2), data2_id)
        self.assertEqual(data1.num, 10)
        self.assertEqual(data2.num, 100)


if __name__ == "__main__":
    unittest.main()
