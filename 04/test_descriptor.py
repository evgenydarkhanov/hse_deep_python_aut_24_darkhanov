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
        with self.assertRaises(TypeError):
            Data(10.0, "product", 20)

        data = Data(10, "product", 20)

        with self.assertRaises(TypeError):
            data.num = 10.0

        with self.assertRaises(TypeError):
            data.name = 10

        with self.assertRaises(TypeError):
            data.price = -10

    def test_03(self):
        """ 03. instances are different """
        data1 = Data(10, "product", 20)
        data2 = Data(10, "product", 20)
        data2_id = id(data2)
        self.assertNotEqual(id(data1), id(data2))

        data2.num = 100
        self.assertNotEqual(id(data1.num), id(data2.num))
        self.assertEqual(id(data2), data2_id)
        self.assertEqual(data1.num, 10)
        self.assertEqual(data2.num, 100)


if __name__ == "__main__":
    unittest.main()
