import unittest
from module_lru_cache import LRUCache


class LRUTestCase(unittest.TestCase):

    def test_01(self):
        """ 01. general functionality test """
        cache = LRUCache()

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        self.assertIsNone(cache.get('k3'))
        self.assertEqual(cache.get('k2'), 'val2')

        cache.set('k3', 'val3')
        self.assertEqual(cache.get('k3'), 'val3')
        self.assertEqual(cache.get('k1'), 'val1')

    def test_02(self):
        """ 02. errors """
        with self.assertRaises(TypeError):
            LRUCache(limit='42')

        with self.assertRaises(TypeError):
            cache = LRUCache(limit=42.0)

        with self.assertRaises(ValueError):
            LRUCache(limit=-1)

        with self.assertRaises(KeyError):
            cache = LRUCache()
            cache.set(['k1'], 'val1')

        with self.assertRaises(KeyError):
            cache = LRUCache()
            cache.get(['k1'])

    def test_03(self):
        """ 03. key existing, nonexistent, removed """
        cache = LRUCache(limit=2)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertIsNone(cache.get('k3'))

        cache.set('k3', 'val3')
        self.assertIsNone(cache.get('k1'))

    def test_04(self):
        """ 04. last element """
        cache = LRUCache()

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        last = list(cache.cache.items())[-1]
        self.assertEqual(last, ('k2', 'val2'))

        cache.get('k1')
        last = list(cache.cache.items())[-1]
        self.assertEqual(last, ('k1', 'val1'))

    def test_05(self):
        """ 05. first element """
        cache = LRUCache()

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        last = list(cache.cache.items())[0]
        self.assertEqual(last, ('k1', 'val1'))

        cache.get('k1')
        last = list(cache.cache.items())[0]
        self.assertEqual(last, ('k2', 'val2'))

    def test_06(self):
        """ 06. value update """
        cache = LRUCache()

        cache.set('k1', 'val1')
        cache.set('k1', 'value1')
        self.assertEqual(cache.get('k1'), 'value1')

    def test_07(self):
        """ 07. limit=0 """
        cache = LRUCache(limit=0)
        with self.assertRaises(StopIteration):
            cache.set('k1', 'val1')


if __name__ == "__main__":
    unittest.main()
