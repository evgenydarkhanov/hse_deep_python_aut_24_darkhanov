import unittest
from module_custom_list import CustomList


class CustomListTestCase(unittest.TestCase):

    def compare(self, lst1, lst2):
        """ element-by-element because of '__eq__' """
        if len(lst1) != len(lst2):
            return False
        return all(lst1[i] == lst2[i] for i in range(len(lst1)))

    def test_compare(self):
        """ testing self.compare() """
        empty_list = CustomList([])
        test_list = CustomList([1, 2, 3])

        self.assertTrue(self.compare(empty_list, CustomList([])))
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        self.assertFalse(self.compare(test_list, CustomList([1, 1])))
        self.assertFalse(self.compare(test_list, CustomList([1, 1, 1])))
        self.assertFalse(self.compare(test_list, CustomList([1, 1, 1, 1])))

    def test_01(self):
        """ 01. add test """
        test_list = CustomList([1, 2, 3])

        add_list_01 = CustomList([2, 1])
        add_01 = test_list + add_list_01
        self.assertIsNot(add_01, test_list)
        self.assertTrue(self.compare(add_01, CustomList([3, 3, 3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(add_list_01, CustomList([2, 1])))

        add_02 = test_list + [2, 1]
        self.assertIsNot(add_02, test_list)
        self.assertTrue(self.compare(add_02, CustomList([3, 3, 3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        add_03 = test_list + [4, 3, 2, 5]
        self.assertIsNot(add_03, test_list)
        self.assertTrue(self.compare(add_03, CustomList([5, 5, 5, 5])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        add_list_04 = CustomList([0])
        add_04 = add_list_04 + [1, 2, 3]
        self.assertTrue(self.compare(add_04, CustomList([1, 2, 3])))
        # element-by-element
        self.assertTrue(self.compare(add_list_04, CustomList([0])))

        add_list_05 = CustomList([])
        add_05 = add_list_05 + test_list
        self.assertIsNot(add_05, test_list)
        self.assertTrue(self.compare(add_05, CustomList([1, 2, 3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(add_list_05, CustomList([])))

        add_list_06 = CustomList([10, 20])
        add_06 = add_list_06 + 10
        self.assertTrue(self.compare(add_06, CustomList([20, 30])))
        # element-by-element
        self.assertTrue(self.compare(add_list_06, CustomList([10, 20])))

        add_07 = [2, 1] + test_list
        self.assertIsNot(add_07, test_list)
        self.assertTrue(self.compare(add_07, add_02))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        add_08 = [4, 3, 2, 5] + test_list
        self.assertIsNot(add_08, test_list)
        self.assertTrue(self.compare(add_08, add_03))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        add_list_09 = CustomList([0])
        add_09 = [1, 2, 3] + add_list_09
        self.assertTrue(self.compare(add_09, add_04))
        # element-by-element
        self.assertTrue(self.compare(add_list_09, CustomList([0])))

        add_list_10 = CustomList([])
        add_10 = test_list + add_list_10
        self.assertIsNot(add_10, test_list)
        self.assertTrue(self.compare(add_10, add_05))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(add_list_10, CustomList([])))

        add_list_11 = CustomList([10, 20])
        add_11 = 10 + add_list_11
        self.assertTrue(self.compare(add_11, add_06))
        # element-by-element
        self.assertTrue(self.compare(add_list_11, CustomList([10, 20])))

    def test_02(self):
        """ 02. subtract test """
        test_list = CustomList([1, 2, 3])

        sub_list_01 = CustomList([2, 1])
        sub_01 = test_list - sub_list_01
        self.assertIsNot(sub_01, test_list)
        self.assertTrue(self.compare(sub_01, CustomList([-1, 1, 3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(sub_list_01, CustomList([2, 1])))

        sub_02 = test_list - [2, 1]
        self.assertIsNot(sub_02, test_list)
        self.assertTrue(self.compare(sub_02, CustomList([-1, 1, 3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        sub_03 = test_list - [4, 3, 2, 5]
        self.assertIsNot(sub_02, test_list)
        self.assertTrue(self.compare(sub_03, CustomList([-3, -1, 1, -5])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        sub_list_04 = CustomList([0])
        sub_04 = sub_list_04 - [1, 2, 3]
        self.assertTrue(self.compare(sub_04, CustomList([-1, -2, -3])))
        # element-by-element
        self.assertTrue(self.compare(sub_list_04, CustomList([0])))

        sub_list_05 = CustomList([])
        sub_05 = sub_list_05 - test_list
        self.assertIsNot(sub_05, test_list)
        self.assertTrue(self.compare(sub_05, CustomList([-1, -2, -3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(sub_list_05, CustomList([])))

        sub_list_06 = CustomList([10, 20])
        sub_06 = sub_list_06 - 10
        self.assertTrue(self.compare(sub_06, CustomList([0, 10])))
        # element-by-element
        self.assertTrue(self.compare(sub_list_06, CustomList([10, 20])))

        sub_07 = [2, 1] - test_list
        self.assertIsNot(sub_07, test_list)
        self.assertTrue(self.compare(sub_07, CustomList([1, -1, -3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        sub_08 = [4, 3, 2, 5] - test_list
        self.assertIsNot(sub_08, test_list)
        self.assertTrue(self.compare(sub_08, CustomList([3, 1, -1, 5])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))

        sub_list_09 = CustomList([0])
        sub_09 = [1, 2, 3] - sub_list_09
        self.assertTrue(self.compare(sub_09, CustomList([1, 2, 3])))
        # element-by-element
        self.assertTrue(self.compare(sub_list_09, CustomList([0])))

        sub_list_10 = CustomList([])
        sub_10 = test_list - sub_list_10
        self.assertIsNot(sub_01, test_list)
        self.assertTrue(self.compare(sub_10, CustomList([1, 2, 3])))
        # element-by-element
        self.assertTrue(self.compare(test_list, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(sub_list_10, CustomList([])))

        sub_list_11 = CustomList([10, 20])
        sub_11 = 10 - sub_list_11
        self.assertTrue(self.compare(sub_11, CustomList([0, -10])))
        # element-by-element
        self.assertTrue(self.compare(sub_list_11, CustomList([10, 20])))

    def test_03(self):
        """ 03. '__eq__' test """
        self.assertEqual(CustomList([1, 2, 3]), CustomList([1, 2, 3]))
        self.assertEqual(CustomList([3, 2, 1]), CustomList([1, 2, 3]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([3, 3]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([6]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([1, 1, 2, 1, 1]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([6, -6, 6]))
        self.assertEqual(CustomList([]), CustomList([0, 0]))
        self.assertEqual(CustomList([]), CustomList([-1, 1]))

    def test_04(self):
        """ 04. '__ne__' test """
        self.assertNotEqual(CustomList([1, 2, 3]), CustomList([3, 3, 3]))

    def test_05(self):
        """ 05. '__gt__' test """
        self.assertTrue(CustomList([1, 2, 3]) > CustomList([1, 2]))
        self.assertTrue(CustomList([1, 2, 3]) > CustomList([]))
        self.assertTrue(CustomList([1, 2, 3]) > CustomList([3, 1, 1, 1, -1]))
        self.assertTrue(CustomList([7]) > CustomList([1, 2, 3]))

        self.assertFalse(CustomList([]) > CustomList([-1, 1]))
        self.assertFalse(CustomList([1, 2, 3]) > CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) > CustomList([3, 2, 1]))
        self.assertFalse(CustomList([1, 2, 3]) > CustomList([6]))

    def test_06(self):
        """ 06. '__ge__' test """
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([1, 2]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([3, 1, 1, 1, -1]))
        self.assertTrue(CustomList([7]) > CustomList([1, 2, 3]))

        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([1, 2, 3]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([3, 2, 1]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([6]))
        self.assertTrue(CustomList([]) >= CustomList([-1, 1]))

    def test_07(self):
        """ 07. '__lt__' test """
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([1, 2, 4]))
        self.assertTrue(CustomList([]) < CustomList([1, 2, 3]))
        self.assertTrue(CustomList([3, 1, 1, 1, -1]) < CustomList([1, 2, 3]))
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([7]))

        self.assertFalse(CustomList([]) < CustomList([-1, 1]))
        self.assertFalse(CustomList([1, 2, 3]) < CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) < CustomList([3, 2, 1]))
        self.assertFalse(CustomList([1, 2, 3]) < CustomList([6]))

    def test_08(self):
        """ 08. '__le__' test """
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([1, 2, 4]))
        self.assertTrue(CustomList([]) <= CustomList([1, 2, 3]))
        self.assertTrue(CustomList([3, 1, 1, 1, -1]) <= CustomList([1, 2, 3]))
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([7]))

        self.assertTrue(CustomList([]) <= CustomList([-1, 1]))
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([1, 2, 3]))
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([3, 2, 1]))
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([6]))

    def test_09(self):
        """ 09. '__str__" test """
        test_list = str(CustomList([1, 2, 3]))
        empty_list = str(CustomList([]))
        plus_minus_list = str(CustomList([1, -1, 1, -1]))

        self.assertEqual(test_list, "[1, 2, 3], 6")
        self.assertEqual(empty_list, "[], 0")
        self.assertEqual(plus_minus_list, "[1, -1, 1, -1], 0")

    def test_10(self):
        """ 10. new object test """
        test_lst_1 = CustomList([1, 2, 3])
        test_lst_2 = CustomList([3, 2, 1])

        res_sum = test_lst_1 + test_lst_2
        res_sub = test_lst_1 - test_lst_2

        self.assertIsNot(res_sum, test_lst_1)
        self.assertIsNot(res_sum, test_lst_2)

        self.assertIsNot(res_sub, test_lst_1)
        self.assertIsNot(res_sub, test_lst_2)
        # element-by-element
        self.assertTrue(self.compare(test_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(self.compare(test_lst_2, CustomList([3, 2, 1])))


if __name__ == "__main__":
    assert 1 == 1
    unittest.main()
