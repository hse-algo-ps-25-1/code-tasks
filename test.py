import unittest
from itertools import combinations
from unittest.mock import patch

from main import (
    LENGTH_NOT_INT,
    LENGTH_NOT_POS,
    NOT_LIST,
    check_zero_one_strings,
    generate_strings_naive,
)


def reference_strings(length):
    """Эталон строит только допустимые продолжения, без полного перебора."""
    if length == 0:
        return [""]
    strings = []
    for prefix in reference_strings(length - 1):
        if not prefix.endswith("0"):
            strings.append(prefix + "0")
        strings.append(prefix + "1")
    return strings


class TestNaiveGenerator(unittest.TestCase):
    """Набор тестов наивного генератора"""

    def test_length_two(self):
        """Длина 2"""
        self.assertCountEqual(generate_strings_naive(2), ["01", "10", "11"])

    def test_not_int_length(self):
        """Длина не целое"""
        with self.assertRaises(TypeError) as error:
            generate_strings_naive(2.0)
        self.assertEqual(LENGTH_NOT_INT, str(error.exception))

    def test_validator_accepts_result(self):
        """Валидатор принимает набор наивного генератора"""
        strings = generate_strings_naive(3)
        self.assertTrue(check_zero_one_strings(3, strings))

    def test_length_one(self):
        """Генератор возвращает обе строки длины 1."""
        self.assertCountEqual(generate_strings_naive(1), ["0", "1"])

    def test_lecture_example(self):
        """Генератор возвращает полный набор из примера длины 3."""
        self.assertCountEqual(
            generate_strings_naive(3), ["010", "011", "101", "110", "111"]
        )

    def test_matches_independent_reference(self):
        """Результаты длин 1–10 совпадают с независимым эталоном."""
        for length in range(1, 11):
            with self.subTest(length=length):
                self.assertCountEqual(
                    generate_strings_naive(length), reference_strings(length)
                )

    def test_leading_zero_is_preserved(self):
        """Генератор сохраняет ведущий ноль."""
        self.assertIn("0101", generate_strings_naive(4))

    def test_nonpositive_length(self):
        """Генератор отклоняет длины меньше 1 с нужным сообщением."""
        for length in [0, -1, -10]:
            with self.subTest(length=length):
                with self.assertRaises(ValueError) as error:
                    generate_strings_naive(length)
                self.assertEqual(str(error.exception), LENGTH_NOT_POS)

    def test_invalid_length_types(self):
        """Генератор отклоняет неверные типы длины, включая bool."""
        for length in [True, False, None, "3", 3.0, [], {}, 2 + 0j]:
            with self.subTest(length=length):
                with self.assertRaises(TypeError) as error:
                    generate_strings_naive(length)
                self.assertEqual(str(error.exception), LENGTH_NOT_INT)

    def test_calls_return_independent_lists(self):
        """Изменение результата не влияет на следующий вызов генератора."""
        first = generate_strings_naive(2)
        first.clear()
        self.assertCountEqual(generate_strings_naive(2), ["01", "10", "11"])


class TestZeroOneValidator(unittest.TestCase):
    """Набор тестов валидатора"""

    def test_length_two(self):
        """Полный набор длины 2"""
        self.assertTrue(check_zero_one_strings(2, ["01", "10", "11"]))

    def test_lecture_example(self):
        """Пример длины 3 с лекции"""
        strings = ["010", "011", "110", "101", "111"]
        self.assertTrue(check_zero_one_strings(3, strings))

    def test_missing_string(self):
        """Неполный набор"""
        self.assertFalse(check_zero_one_strings(2, ["01", "11"]))

    def test_not_int_length(self):
        """Длина не целое"""
        with self.assertRaises(TypeError) as error:
            check_zero_one_strings(1.5, ["0", "1"])
        self.assertEqual(LENGTH_NOT_INT, str(error.exception))

    def test_negative_length(self):
        """Отрицательная длина"""
        with self.assertRaises(ValueError) as error:
            check_zero_one_strings(-1, [])
        self.assertEqual(LENGTH_NOT_POS, str(error.exception))

    def test_length_one(self):
        """Валидатор принимает обе строки длины 1 в обратном порядке."""
        self.assertTrue(check_zero_one_strings(1, ["1", "0"]))

    def test_accepts_independent_reference_in_reverse_order(self):
        """Валидатор принимает эталонные наборы длин 1–10 в любом порядке."""
        for length in range(1, 11):
            with self.subTest(length=length):
                strings = list(reversed(reference_strings(length)))
                self.assertTrue(check_zero_one_strings(length, strings))

    def test_every_subset_of_length_three(self):
        """Из всех подмножеств строк длины 3 принимается только полное."""
        full = reference_strings(3)
        for size in range(len(full) + 1):
            for subset in combinations(full, size):
                with self.subTest(subset=subset):
                    self.assertEqual(
                        check_zero_one_strings(3, list(subset)), size == len(full)
                    )

    def test_duplicate_replaces_missing_string(self):
        """Дубликат не компенсирует отсутствие допустимой строки."""
        self.assertFalse(check_zero_one_strings(2, ["01", "01", "11"]))

    def test_extra_string(self):
        """Валидатор отклоняет набор с лишней строкой."""
        self.assertFalse(check_zero_one_strings(2, ["01", "10", "11", "00"]))

    def test_extra_duplicate(self):
        """Валидатор отклоняет набор с лишним дубликатом."""
        self.assertFalse(check_zero_one_strings(2, ["01", "10", "11", "11"]))

    def test_consecutive_zeros_at_each_position(self):
        """Соседние нули отклоняются при правильном размере набора."""
        for string in ["001", "100", "000"]:
            with self.subTest(string=string):
                strings = reference_strings(3)
                strings[0] = string
                self.assertFalse(check_zero_one_strings(3, strings))

    def test_wrong_length_at_correct_cardinality(self):
        """Валидатор отклоняет строку другой длины в наборе нужного размера."""
        for string in ["", "1", "010"]:
            with self.subTest(string=string):
                self.assertFalse(check_zero_one_strings(2, ["01", "10", string]))

    def test_wrong_alphabet_at_correct_cardinality(self):
        """Валидатор отклоняет символы вне алфавита 0/1."""
        for string in ["02", "1a", "1 ", "1\n", "０1", "١1"]:
            with self.subTest(string=string):
                self.assertFalse(check_zero_one_strings(2, ["01", "10", string]))

    def test_nonstring_elements_do_not_raise(self):
        """Нестроковый элемент даёт False без исключения."""
        for element in [None, 11, True, b"11", ["1", "1"], {"1": 1}, {"11"}]:
            with self.subTest(element=element):
                self.assertFalse(check_zero_one_strings(2, ["01", "10", element]))

    def test_not_a_list(self):
        """Набор другого типа вызывает TypeError с нужным сообщением."""
        for strings in [None, ("0", "1"), {"0", "1"}, "01", {}, 2]:
            with self.subTest(strings=strings):
                with self.assertRaises(TypeError) as error:
                    check_zero_one_strings(1, strings)
                self.assertEqual(str(error.exception), NOT_LIST)

    def test_invalid_length_types(self):
        """Валидатор отклоняет неверные типы длины, включая bool."""
        for length in [True, False, None, "3", 3.0, [], {}, 2 + 0j]:
            with self.subTest(length=length):
                with self.assertRaises(TypeError) as error:
                    check_zero_one_strings(length, [])
                self.assertEqual(str(error.exception), LENGTH_NOT_INT)

    def test_nonpositive_length(self):
        """Валидатор отклоняет длины меньше 1 с нужным сообщением."""
        for length in [0, -1, -10]:
            with self.subTest(length=length):
                with self.assertRaises(ValueError) as error:
                    check_zero_one_strings(length, [])
                self.assertEqual(str(error.exception), LENGTH_NOT_POS)

    def test_length_validation_precedes_collection_validation(self):
        """Ошибка длины проверяется раньше ошибки типа набора."""
        for length, exception, message in [
            (2.0, TypeError, LENGTH_NOT_INT),
            (0, ValueError, LENGTH_NOT_POS),
        ]:
            with self.subTest(length=length):
                with self.assertRaises(exception) as error:
                    check_zero_one_strings(length, None)
                self.assertEqual(str(error.exception), message)

    def test_does_not_mutate_input(self):
        """Валидатор не меняет корректный или некорректный входной список."""
        strings = ["11", "01", "10"]
        original = strings.copy()
        self.assertTrue(check_zero_one_strings(2, strings))
        self.assertEqual(strings, original)
        strings[0] = "00"
        original = strings.copy()
        self.assertFalse(check_zero_one_strings(2, strings))
        self.assertEqual(strings, original)

    def test_validation_does_not_call_naive_generator(self):
        """Для проверки полноты не вызывается наивный генератор."""
        strings = reference_strings(8)
        with patch("main.generate_strings_naive", side_effect=AssertionError):
            self.assertTrue(check_zero_one_strings(8, strings))

    def test_large_length_with_small_list(self):
        """Малый неполный набор быстро отклоняется даже при большой длине."""
        self.assertFalse(check_zero_one_strings(10**9, ["0", "1"]))


if __name__ == "__main__":
    unittest.main()
