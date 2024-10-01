import unittest
from module_custom_list import CustomList


class CustomListTestCase(unittest.TestCase):

    def setUp(self):
        self.lst_1 = CustomList([1, 2, 3])
        self.lst_2 = CustomList([3, 2, 1])
        self.lst_empty = CustomList([])

    def compare(self, lst1, lst2):
        """ element-by-element because of '__eq__' """
        return all(lst1[i] == lst2[i] for i in range(len(lst1)))

    def test_01(self):
        """ 01. add test """
        add_01 = CustomList([1, 2, 3]) + CustomList([2, 1])

        add_02 = CustomList([1, 2, 3]) + [2, 1]
        add_03 = CustomList([1, 2, 3]) + [4, 3, 2, 5]
        add_04 = CustomList([0]) + [1, 2, 3]
        add_05 = CustomList([]) + CustomList([1, 2, 3])
        add_06 = CustomList([10, 20]) + 10

        add_07 = [2, 1] + CustomList([1, 2, 3])
        add_08 = [4, 3, 2, 5] + CustomList([1, 2, 3])
        add_09 = [1, 2, 3] + CustomList([0])
        add_10 = CustomList([1, 2, 3]) + CustomList([])
        add_11 = 10 + CustomList([10, 20])

        self.assertTrue(self.compare(add_01, CustomList([3, 3, 3])))

        self.assertTrue(self.compare(add_02, CustomList([3, 3, 3])))
        self.assertTrue(self.compare(add_03, CustomList([5, 5, 5, 5])))
        self.assertTrue(self.compare(add_04, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(add_05, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(add_06, CustomList([20, 30])))

        self.assertTrue(self.compare(add_07, add_02))
        self.assertTrue(self.compare(add_08, add_03))
        self.assertTrue(self.compare(add_09, add_04))
        self.assertTrue(self.compare(add_10, add_05))
        self.assertTrue(self.compare(add_11, add_06))

    def test_02(self):
        """ 02. subtract test """
        sub_01 = CustomList([1, 2, 3]) - CustomList([2, 1])

        sub_02 = CustomList([1, 2, 3]) - [2, 1]
        sub_03 = CustomList([1, 2, 3]) - [4, 3, 2, 5]
        sub_04 = CustomList([0]) - [1, 2, 3]
        sub_05 = CustomList([]) - CustomList([1, 2, 3])
        sub_06 = CustomList([10, 20]) - 10

        sub_07 = [2, 1] - CustomList([1, 2, 3])
        sub_08 = [4, 3, 2, 5] - CustomList([1, 2, 3])
        sub_09 = [1, 2, 3] - CustomList([0])
        sub_10 = CustomList([1, 2, 3]) - CustomList([])
        sub_11 = 10 - CustomList([10, 20])

        self.assertTrue(self.compare(sub_01, CustomList([-1, 1, 3])))

        self.assertTrue(self.compare(sub_02, CustomList([-1, 1, 3])))
        self.assertTrue(self.compare(sub_03, CustomList([-3, -1, 1, -5])))
        self.assertTrue(self.compare(sub_04, CustomList([-1, -2, -3])))
        self.assertTrue(self.compare(sub_05, CustomList([-1, -2, -3])))
        self.assertTrue(self.compare(sub_06, CustomList([0, 10])))

        self.assertTrue(self.compare(sub_07, CustomList([1, -1, -3])))
        self.assertTrue(self.compare(sub_08, CustomList([3, 1, -1, 5])))
        self.assertTrue(self.compare(sub_09, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(sub_10, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(sub_11, CustomList([0, -10])))

    def test_03(self):
        """ 03. '__eq__' test """
        self.assertEqual(self.lst_1, CustomList([1, 2, 3]))
        self.assertEqual(self.lst_1, self.lst_2)
        self.assertEqual(self.lst_1, CustomList([3, 3]))
        self.assertEqual(self.lst_1, CustomList([6]))
        self.assertEqual(self.lst_empty, CustomList([0, 0]))
        self.assertEqual(self.lst_empty, CustomList([-1, 1]))

    def test_04(self):
        """ 04. '__ne__' test """
        self.assertNotEqual(self.lst_1, CustomList([3, 3, 3]))

    def test_05(self):
        """ 05. '__gt__' test """
        self.assertTrue(self.lst_1 > CustomList([1, 2]))
        self.assertTrue(self.lst_1 > self.lst_empty)
        self.assertTrue(self.lst_1 > CustomList([3, 1, 1, 1, -1]))
        self.assertTrue(CustomList([7]) > self.lst_1)

        self.assertFalse(self.lst_empty > CustomList([-1, 1]))
        self.assertFalse(self.lst_1 > CustomList([1, 2, 3]))
        self.assertFalse(self.lst_1 > self.lst_2)
        self.assertFalse(self.lst_1 > CustomList([6]))

    def test_06(self):
        """ 06. '__ge__' test """
        self.assertTrue(self.lst_1 >= CustomList([1, 2]))
        self.assertTrue(self.lst_1 >= self.lst_empty)
        self.assertTrue(self.lst_1 >= CustomList([3, 1, 1, 1, -1]))
        self.assertTrue(CustomList([7]) > self.lst_1)

        self.assertTrue(self.lst_1 >= CustomList([1, 2, 3]))
        self.assertTrue(self.lst_1 >= self.lst_2)
        self.assertTrue(self.lst_1 >= CustomList([6]))
        self.assertTrue(self.lst_empty >= CustomList([-1, 1]))

    def test_07(self):
        """ 07. '__lt__' test """
        self.assertTrue(self.lst_1 < CustomList([1, 2, 4]))
        self.assertTrue(self.lst_empty < self.lst_1)
        self.assertTrue(CustomList([3, 1, 1, 1, -1]) < self.lst_1)
        self.assertTrue(self.lst_1 < CustomList([7]))

        self.assertFalse(self.lst_empty < CustomList([-1, 1]))
        self.assertFalse(self.lst_1 < CustomList([1, 2, 3]))
        self.assertFalse(self.lst_1 < self.lst_2)
        self.assertFalse(self.lst_1 < CustomList([6]))

    def test_08(self):
        """ 08. '__le__' test """
        self.assertTrue(self.lst_1 <= CustomList([1, 2, 4]))
        self.assertTrue(self.lst_empty <= self.lst_1)
        self.assertTrue(CustomList([3, 1, 1, 1, -1]) <= self.lst_1)
        self.assertTrue(self.lst_1 <= CustomList([7]))

        self.assertTrue(self.lst_empty <= CustomList([-1, 1]))
        self.assertTrue(self.lst_1 <= CustomList([1, 2, 3]))
        self.assertTrue(self.lst_1 <= self.lst_2)
        self.assertTrue(self.lst_1 <= CustomList([6]))

    def test_09(self):
        """ 09. '__str__" test """
        lst_1 = str(self.lst_1)
        lst_e = str(self.lst_empty)

        self.assertEqual(lst_1, "[1, 2, 3], 6")
        self.assertEqual(lst_e, "[], 0")

    def test_10(self):
        """ 10. new object test """
        res_sum = self.lst_1 + self.lst_2
        res_sub = self.lst_1 - self.lst_2

        self.assertIsNot(res_sum, self.lst_1)
        self.assertIsNot(res_sum, self.lst_2)

        self.assertIsNot(res_sub, self.lst_1)
        self.assertIsNot(res_sub, self.lst_2)


if __name__ == "__main__":
    unittest.main()
