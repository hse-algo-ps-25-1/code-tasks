import unittest

from main import stars_and_bars


class TestStarsAndBars(unittest.TestCase):
    """Набор тестов для проверки функции генерации строк «звёзды
    и перегородки»"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче None"""
        self.assertRaises(Exception, stars_and_bars, None, 2)
        self.assertRaises(Exception, stars_and_bars, 2, None)

    def test_invalid_n(self):
        """Проверяет, что функция выбрасывает исключение при n меньше 1"""
        for n in (0, -1):
            with self.subTest(n=n):
                self.assertRaises(Exception, stars_and_bars, n, 2)

    def test_negative_k(self):
        """Проверяет, что функция выбрасывает исключение при отрицательном k"""
        self.assertRaises(Exception, stars_and_bars, 3, -1)

    def test_invalid_types(self):
        """Проверяет, что функция выбрасывает исключение при передаче нецелых чисел"""
        for value in ("1", 1.0, True, False):
            with self.subTest(n=value):
                self.assertRaises(Exception, stars_and_bars, value, 1)
            with self.subTest(k=value):
                self.assertRaises(Exception, stars_and_bars, 1, value)

    def test_return_types(self):
        """Проверят, что функция возвращает список строк"""
        result = stars_and_bars(2, 2)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, str)

    def test_string_format_symbols(self):
        """Проверяет, что в каждой строке только
        допустимые символы перегородок и звездочек."""
        cases = [(1, 0), (2, 1), (3, 4), (4, 5), (5, 0)]
        for n, k in cases:
            with self.subTest(n=n, k=k):
                for s in stars_and_bars(n, k):
                    self.assertTrue(set(s) <= {"*", "|"})

    def test_strings_length_values(self):
        """Проверяет по формуле, что результат возвращает
        правильное суммарное количество символов."""
        cases = [(3, 0), (5, 2), (2, 5), (4, 2), (4, 5)]
        for n, k in cases:
            with self.subTest(n=n, k=k):
                for s in stars_and_bars(n, k):
                    self.assertEqual(len(s), n + k - 1)
                    self.assertEqual(s.count("*"), k)
                    self.assertEqual(s.count("|"), n - 1)

    def test_one_box(self):
        """Проверяет единственную строку при одном ящике"""
        self.assertEqual(stars_and_bars(1, 3), ["***"])
        self.assertEqual(stars_and_bars(1, 0), [""])

    def test_zero_items(self):
        """Проверяет распределение нуля предметов: только перегородки"""
        self.assertEqual(stars_and_bars(3, 0), ["||"])

    def test_two_boxes_two_items(self):
        """Проверяет все строки для двух ящиков и двух предметов"""
        self.assertCountEqual(stars_and_bars(2, 2), ["**|", "*|*", "|**"])

    def test_three_boxes_one_item(self):
        """Проверяет все строки для трёх ящиков и одного предмета"""
        self.assertCountEqual(stars_and_bars(3, 1), ["*||", "|*|", "||*"])


if __name__ == "__main__":
    unittest.main()
