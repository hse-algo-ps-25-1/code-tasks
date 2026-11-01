import unittest

from main import is_brackets_balanced


class TestBrackets(unittest.TestCase):
    """Публичные примеры проверки скобок."""

    def test_balanced_expression(self):
        """Скобки в арифметическом выражении согласованы."""
        self.assertTrue(is_brackets_balanced("3 + 2 * (5 - [4 / {2 + 1}])"))

    def test_extra_closing(self):
        """Лишняя закрывающая скобка."""
        for expression in ("(]", "())"):
            with self.subTest(expression=expression):
                self.assertFalse(is_brackets_balanced(expression))

    def test_without_brackets(self):
        """Пустая строка и строка без скобок согласованы."""
        for expression in ("", "1 < 2"):
            with self.subTest(expression=expression):
                self.assertTrue(is_brackets_balanced(expression))

    def test_sequential_pairs(self):
        """Пары, идущие подряд, согласованы."""
        self.assertTrue(is_brackets_balanced("()[]{}"))

    def test_unclosed_opening(self):
        """Открывающая скобка осталась незакрытой."""
        self.assertFalse(is_brackets_balanced("("))

    def test_crossed_pairs(self):
        """Пары скобок пересекаются."""
        self.assertFalse(is_brackets_balanced("([)]"))

    def test_not_string(self):
        """Аргумент не строка дает TypeError."""
        for expression in (None, ["(", ")"]):
            with self.subTest(expression=expression):
                self.assertRaises(TypeError, is_brackets_balanced, expression)


if __name__ == "__main__":
    unittest.main()
