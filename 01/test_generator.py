import unittest
from generator import read_text, check_line


class GeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = '/texts.txt'
        self.wolf = ['волк']
        self.words = ['с', 'в', 'это', 'же']

    def test_01(self):
        """ 01. TEST 'filename' is 'str' """
        lines = []
        for line in read_text(self.filename, self.wolf, []):
            check_result = check_line(line, self.wolf, [])
            if check_result is not None:
                lines.append(check_result)

        self.assertEqual(lines, ['волк слабее льва и тигра но в цирке не выступает'])

    def test_02(self):
        """ 02. TEST 'filename' is 'io.TextIOWrapper' """
        with open(self.filename, 'r', encoding='utf-8') as f:
            lines = []
            for line in read_text(f, self.wolf, []):
                check_result = check_line(line, self.wolf, [])
                if check_result is not None:
                    lines.append(check_result)

            self.assertEqual(lines, ['волк слабее льва и тигра но в цирке не выступает'])

    def test_03(self):
        """ 03. TEST 'filename' TypeError """
        with self.assertRaises(TypeError):
            list(read_text(123, self.wolf, []))

    def test_04(self):
        """ 04. TEST 'search_words' TypeError """
        with self.assertRaises(TypeError):
            list(read_text(self.filename, 'wolf', []))

    def test_05(self):
        """ 05. TEST 'stop_words' TypeError """
        with self.assertRaises(TypeError):
            list(read_text(self.filename, self.wolf, ''))

    def test_06(self):
        """ 06. TEST 'search_words' elements TypeError """
        with self.assertRaises(TypeError):
            list(read_text(self.filename, [123], []))

    def test_07(self):
        """ 07. TEST 'stop_words' elements TypeError """
        with self.assertRaises(TypeError):
            list(read_text(self.filename, self.wolf, [123]))

    def test_08(self):
        """ 08. TEST search all lines """
        lines = []
        for line in read_text(self.filename, self.words, []):
            check_result = check_line(line, self.words, [])
            if check_result is not None:
                lines.append(check_result)

        lines_to_check = []
        with open(self.filename, 'r', encoding='utf-8') as f:
            lines_to_check = [line.rstrip() for line in f]

        self.assertEqual(lines, lines_to_check)

    def test_09(self):
        """ 09. TEST search no lines"""
        lines = []
        for line in read_text(self.filename, self.words, self.words):
            check_result = check_line(line, self.words, self.words)
            if check_result is not None:
                lines.append(check_result)

        self.assertEqual(lines, [])


if __name__ == "__main__":
    unittest.main()
