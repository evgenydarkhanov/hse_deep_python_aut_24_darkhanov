import unittest
from module_lru_cache import LRUCache


class LRUTestCase(unittest.TestCase):

    def test_01(self):
        """ 01. tests as in task """
        cache = LRUCache(2)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')

        self.assertIsNone(cache.get('k3'))
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k1'), 'val1')

        cache.set('k3', 'val3')
        self.assertEqual(cache.get('k3'), 'val3')
        self.assertIsNone(cache.get('k2'))
        self.assertEqual(cache.get('k1'), 'val1')

        # дополнительная проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k3'), 'val3')
        self.assertIsNone(cache.get('k2'))
        self.assertEqual(cache.get('k1'), 'val1')

    def test_02(self):
        """ 02. errors """
        with self.assertRaises(TypeError):
            _ = LRUCache(limit='42')

        with self.assertRaises(TypeError):
            _ = LRUCache(limit=42.0)

        with self.assertRaises(ValueError):
            _ = LRUCache(limit=-1)

        with self.assertRaises(TypeError):
            _ = LRUCache(limit=[1])

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

        # existing key
        self.assertEqual(cache.get('k2'), 'val2')

        # nonexistent key
        self.assertIsNone(cache.get('k3'))

        # removed key
        cache.set('k3', 'val3')
        self.assertIsNone(cache.get('k1'))

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k3'), 'val3')
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertIsNone(cache.get('k1'))

    def test_04(self):
        """ 04. last element """
        cache = LRUCache(limit=3)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        cache.set('k3', 'val3')

        # если 'k3' - последний, то после двух set/get станет первым на удаление
        cache.set('k1', 'value1')
        _ = cache.get('k2')

        cache.set('k4', 'val4')     # 'k3' как первый элемент должен удалиться
        self.assertIsNone(cache.get('k3'))

        # дополнительная проверка внутренних атрибутов, 'k4' - последний
        last = list(cache.cache.items())[-1]
        self.assertEqual(last, ('k4', 'val4'))

        # дополнительная проверка внутренних атрибутов, 'k1' - последний
        cache.get('k1')
        last = list(cache.cache.items())[-1]
        self.assertEqual(last, ('k1', 'value1'))

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k4'), 'val4')
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k1'), 'value1')
        self.assertIsNone(cache.get('k3'))

    def test_05(self):
        """ 05. first element """
        cache = LRUCache(limit=3)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        cache.set('k3', 'val3')
        cache.set('k4', 'val4')     # 'k1' как первый элемент должен удалиться

        self.assertIsNone(cache.get('k1'))
        self.assertEqual(cache.get('k4'), 'val4')

        cache.set('k5', 'val5')     # теперь удаляется 'k2'
        self.assertIsNone(cache.get('k2'))

        # дополнительная проверка внутренних атрибутов, 'k3' - первый
        first = list(cache.cache.items())[0]
        self.assertEqual(first, ('k3', 'val3'))

        # дополнительная проверка внутренних атрибутов, 'k4' - первый
        cache.get('k3')
        first = list(cache.cache.items())[0]
        self.assertEqual(first, ('k4', 'val4'))

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k5'), 'val5')
        self.assertEqual(cache.get('k4'), 'val4')
        self.assertEqual(cache.get('k3'), 'val3')
        self.assertIsNone(cache.get('k2'))
        self.assertIsNone(cache.get('k1'))

    def test_06(self):
        """ 06. value update """
        cache = LRUCache()

        cache.set('k1', 'value1')
        cache.set('k1', 'val1')
        self.assertEqual(cache.get('k1'), 'val1')

        cache.set('k2', 'value2')
        cache.set('k2', 'val2')
        self.assertEqual(cache.get('k2'), 'val2')

        cache.set('k1', 'val3')
        self.assertEqual(cache.get('k1'), 'val3')

        # дополнительная проверка внутренних атрибутов
        cache_lst = list(cache.cache.items())
        self.assertEqual(cache_lst, [('k2', 'val2'), ('k1', 'val3')])

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k1'), 'val3')

    def test_07(self):
        """ 07. limit=0 """
        cache = LRUCache(limit=0)
        with self.assertRaises(StopIteration):
            cache.set('k1', 'val1')

        # дополнительная проверка внутренних атрибутов
        cache_lst = list(cache.cache.items())
        self.assertEqual(cache_lst, [])

        # проверка всех вовлечённых ключей
        self.assertIsNone(cache.get('k1'))

    def test_08(self):
        """ 08. limit=1 """
        cache = LRUCache(limit=1)

        cache.set('k1', 'val1')
        self.assertEqual(cache.get('k1'), 'val1')

        cache.set('k2', 'val2')
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertIsNone(cache.get('k1'))

        # дополнительная проверка внутренних атрибутов
        cache_lst = list(cache.cache.items())
        self.assertEqual(cache_lst, [('k2', 'val2')])

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertIsNone(cache.get('k1'))

    def test_09(self):
        """ 09. updating and removal order """
        cache = LRUCache(3)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        cache.set('k3', 'val3')

        for key in ['k1', 'k2', 'k2', 'k1', 'k3', 'k2']:
            cache.set(key, 'val_' + key)

        cache.set('k4', 'val4')     # 'k1' как первый элемент должен удалиться
        self.assertIsNone(cache.get('k1'))

        # проверяем все ключи, меняем порядок
        self.assertEqual(cache.get('k2'), 'val_k2')
        self.assertEqual(cache.get('k3'), 'val_k3')
        self.assertEqual(cache.get('k4'), 'val4')

        # дополнительная проверка внутренних атрибутов
        cache_lst = list(cache.cache.items())
        check_lst = [('k2', 'val_k2'), ('k3', 'val_k3'), ('k4', 'val4')]
        self.assertEqual(cache_lst, check_lst)

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k4'), 'val4')
        self.assertEqual(cache.get('k3'), 'val_k3')
        self.assertEqual(cache.get('k2'), 'val_k2')
        self.assertIsNone(cache.get('k1'))

    def test_10(self):
        """ consequences of change """
        cache = LRUCache(3)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        cache.set('k3', 'val3')

        # меняем значения по всем ключам, кроме 'k3'
        for key in ['k2', 'k1', 'k2', 'k1']:
            cache.set(key, 'val_' + key)

        cache.set('k4', 'val4')     # ключ 'k3' должен удалиться
        self.assertIsNone(cache.get('k3'))

        # проверка всех вовлечённых ключей
        self.assertEqual(cache.get('k4'), 'val4')
        self.assertIsNone(cache.get('k3'))
        self.assertEqual(cache.get('k2'), 'val_k2')
        self.assertEqual(cache.get('k1'), 'val_k1')


if __name__ == "__main__":
    unittest.main()
