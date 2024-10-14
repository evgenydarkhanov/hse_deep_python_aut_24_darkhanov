import unittest
from module_custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class CustomClassTestCase(unittest.TestCase):
    def test_01(self):
        """ 01. general functionality """
        self.assertEqual(CustomClass.custom_x, 50)
        with self.assertRaises(AttributeError):
            CustomClass.x

        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(str(inst), "Custom_by_metaclass")

        with self.assertRaises(AttributeError):
            inst.x
        with self.assertRaises(AttributeError):
            inst.val
        with self.assertRaises(AttributeError):
            inst.line()
        with self.assertRaises(AttributeError):
            inst.yyy

        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            inst.dynamic

    def test_02(self):
        """ 02. attributes in __dict__ """
        class_dict = CustomClass.__dict__
        self.assertFalse('x' in class_dict)
        self.assertFalse('line' in class_dict)
        self.assertFalse('custom_init__' in class_dict)
        self.assertFalse('custom__init__' in class_dict)
        self.assertTrue('custom_x' in class_dict)
        self.assertTrue('custom_line' in class_dict)

        self.assertFalse('custom___init__' in class_dict)
        self.assertTrue('__init__' in class_dict)

        inst = CustomClass()
        self.assertEqual(inst.__dict__, {'custom_val': 99})

        inst.a = 'a'
        inst._a = '_a'
        inst._a_ = '_a_'
        inst.a_ = 'a_'
        inst.a__ = 'a__'
        inst._a__ = '_a__'
        self.assertFalse('a' in inst.__dict__)
        self.assertFalse('_a' in inst.__dict__)
        self.assertFalse('_a_' in inst.__dict__)
        self.assertFalse('a_' in inst.__dict__)
        self.assertFalse('a__' in inst.__dict__)
        self.assertFalse('_a__' in inst.__dict__)
        self.assertTrue('custom_a' in inst.__dict__)
        self.assertTrue('custom__a' in inst.__dict__)
        self.assertTrue('custom__a_' in inst.__dict__)
        self.assertTrue('custom_a_' in inst.__dict__)
        self.assertTrue('custom_a__' in inst.__dict__)
        self.assertTrue('custom__a__' in inst.__dict__)

        inst.__a__ = '__a__'
        self.assertFalse('custom___a__' in inst.__dict__)
        self.assertTrue('__a__' in inst.__dict__)

    def test_03(self):
        """ 03. magic attributes """
        class TmpClass(metaclass=CustomMeta):
            a = 'a'
            __a__ = '__a__'

            def b(self):
                pass

            def __b__(self):
                pass

        self.assertFalse('a' in TmpClass.__dict__)
        self.assertFalse('custom___a__' in TmpClass.__dict__)
        self.assertTrue('custom_a' in TmpClass.__dict__)
        self.assertTrue('__a__' in TmpClass.__dict__)

        self.assertFalse('b' in TmpClass.__dict__)
        self.assertFalse('custom___b__' in TmpClass.__dict__)
        self.assertTrue('custom_b' in TmpClass.__dict__)
        self.assertTrue('__b__' in TmpClass.__dict__)

    def test_04(self):
        """ 04. inheritance """
        class InheritedClass(CustomClass):
            a = 'a'
            __a__ = '__a__'

            def b(self):
                pass

            def __b__(self):
                pass

        self.assertFalse('a' in InheritedClass.__dict__)
        self.assertFalse('custom___a__' in InheritedClass.__dict__)
        self.assertTrue('custom_a' in InheritedClass.__dict__)
        self.assertTrue('__a__' in InheritedClass.__dict__)

        self.assertFalse('b' in InheritedClass.__dict__)
        self.assertFalse('custom___b__' in InheritedClass.__dict__)
        self.assertTrue('custom_b' in InheritedClass.__dict__)
        self.assertTrue('__b__' in InheritedClass.__dict__)


if __name__ == "__main__":
    unittest.main()
