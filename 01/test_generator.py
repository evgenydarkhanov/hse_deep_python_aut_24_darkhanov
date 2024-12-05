import unittest
from module_generator import read_text


class GeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = '01/texts.txt'

    def test_01(self):
        """ 01. general functionality, filename """
        search = ['и']
        stop = ['Python']
        result = list(read_text(self.filename, search, stop))
        wolf = ['волк слабее льва и тигра но в цирке не выступает']
        self.assertEqual(result, wolf)

    def test_02(self):
        """ 02. general functionality, file object """
        search = ['и']
        stop = ['Python']
        wolf = ['волк слабее льва и тигра но в цирке не выступает']
        with open(self.filename, 'r', encoding='utf=8') as file:
            result = list(read_text(file, search, stop))
        self.assertEqual(result, wolf)

    def test_03(self):
        """ 03. errors """
        with self.assertRaises(TypeError):
            _ = list(read_text(123, [], []))

        with self.assertRaises(TypeError):
            _ = list(read_text(self.filename, (), []))

        with self.assertRaises(TypeError):
            _ = list(read_text(self.filename, [], {}))

        with self.assertRaises(TypeError):
            _ = list(read_text(self.filename, [123], []))

        with self.assertRaises(TypeError):
            _ = list(read_text(self.filename, [], [123]))

    def test_04(self):
        """ 04. search all lines """
        check = []
        with open(self.filename, 'r', encoding='utf-8') as f:
            check = [line.rstrip() for line in f]

        search = ['сЪешь', 'волк', 'три', 'Python', 'всегда', 'word']

        result_1 = list(read_text(self.filename, search, []))
        result_2 = list(read_text(self.filename, search, ['']))
        result_3 = list(read_text(self.filename, search, ['', '']))
        result_4 = list(read_text(self.filename, search, ['abcd', 'efgh']))

        self.assertEqual(result_1, check)
        self.assertEqual(result_2, check)
        self.assertEqual(result_3, check)
        self.assertEqual(result_4, check)

    def test_05(self):
        """ 05. search no lines """
        stop = ['сЪешь', 'волк', 'три', 'Python', 'всегда', 'word']

        result_1 = list(read_text(self.filename, [], stop))
        result_2 = list(read_text(self.filename, [''], stop))
        result_3 = list(read_text(self.filename, ['', ''], stop))
        result_4 = list(read_text(self.filename, ['abcd', 'efgh'], stop))
        result_5 = list(read_text(self.filename, stop, stop))
        result_6 = list(read_text(self.filename, [], []))
        result_7 = list(read_text(self.filename, [''], ['']))
        result_8 = list(read_text(self.filename, ['abcd'], ['efgh']))
        result_9 = list(read_text(self.filename, ['abcd', 'efgh'], []))

        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])
        self.assertEqual(result_3, [])
        self.assertEqual(result_4, [])
        self.assertEqual(result_5, [])
        self.assertEqual(result_6, [])
        self.assertEqual(result_7, [])
        self.assertEqual(result_8, [])
        self.assertEqual(result_9, [])

    def test_06(self):
        """ 06. several matching words """
        search = ['съешь', 'французских', 'чаю']
        expected = ['съешь же ещё этих мягких французских булок да выпей чаю']

        result_1 = list(read_text(self.filename, search, []))
        result_2 = list(read_text(self.filename, search, ['']))
        result_3 = list(read_text(self.filename, search, ['', '']))
        result_4 = list(read_text(self.filename, search, ['abcd', 'efgh']))

        self.assertEqual(result_1, expected)
        self.assertEqual(result_2, expected)
        self.assertEqual(result_3, expected)
        self.assertEqual(result_4, expected)

    def test_07(self):
        """ 07. whole line """
        line = ['три слова это два слова']

        result_1 = list(read_text(self.filename, line, []))
        result_2 = list(read_text(self.filename, [], line))
        result_3 = list(read_text(self.filename, line, line))

        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])
        self.assertEqual(result_3, [])

    def test_08(self):
        """ 08. font register """
        expected = ['Всегда бери с собой рюкзак']

        result_1 = list(read_text(self.filename, ['Всегда'], []))
        result_2 = list(read_text(self.filename, ['всегда'], []))
        result_3 = list(read_text(self.filename, ['бЕрИ'], []))
        result_4 = list(read_text(self.filename, ['РЮКЗАК'], []))

        self.assertEqual(result_1, expected)
        self.assertEqual(result_2, expected)
        self.assertEqual(result_3, expected)
        self.assertEqual(result_4, expected)

    def test_09(self):
        """ line == one word """
        result_1 = list(read_text(self.filename, ['word'], []))
        result_2 = list(read_text(self.filename, ['wOrD'], []))

        self.assertEqual(result_1, ['word'])
        self.assertEqual(result_2, ['word'])

        result_3 = list(read_text(self.filename, ['word'], ['word']))
        result_4 = list(read_text(self.filename, ['WoRd'], ['wOrD']))

        self.assertEqual(result_3, [])
        self.assertEqual(result_4, [])


if __name__ == "__main__":
    unittest.main()
