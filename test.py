import math
import unittest

from main import (
    NOT_LIST_ERROR_MSG,
    generate_permutations_iter,
    generate_permutations_rec,
)

PERMUTATION_FUNCTIONS = (generate_permutations_rec, generate_permutations_iter)


def _same_items(left, right):
    pending = list(right)
    for item in left:
        for index, candidate in enumerate(pending):
            if candidate == item:
                del pending[index]
                break
        else:
            return False
    return not pending


def _assert_all_permutations(test_case, permutations, elements):
    test_case.assertEqual(len(permutations), math.factorial(len(elements)))
    seen = []
    for permutation in permutations:
        test_case.assertIsInstance(permutation, list)
        test_case.assertTrue(_same_items(permutation, elements))
        snapshot = list(permutation)
        test_case.assertNotIn(snapshot, seen)
        seen.append(snapshot)


class TestPermutations(unittest.TestCase):
    """Набор тестов генерации перестановок."""

    def test_empty_list(self):
        """Пустой список возвращает список из одной пустой перестановки."""
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                self.assertEqual(function([]), [[]])

    def test_single_element(self):
        """Список из одного элемента."""
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                self.assertEqual(function([42]), [[42]])

    def test_two_letters(self):
        """Обе перестановки двух букв."""
        expected = [["a", "b"], ["b", "a"]]
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                self.assertTrue(_same_items(function(["a", "b"]), expected))

    def test_three_letters(self):
        """Все шесть перестановок трёх букв."""
        elements = ["a", "b", "c"]
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                _assert_all_permutations(self, function(elements), elements)

    def test_four_numbers(self):
        """Все 24 перестановки четырёх чисел."""
        elements = [1, 2, 3, 4]
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                _assert_all_permutations(self, function(elements), elements)

    def test_mixed_and_unhashable_elements(self):
        """Разнородные и нехешируемые элементы (списки, словари, None)."""
        elements = [1, "a", [2, 3], {"key": "val"}, None]
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                _assert_all_permutations(self, function(elements), elements)

    def test_input_not_mutated(self):
        """Исходный список не изменяется после вызова функции."""
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                elements = [1, 2, 3]
                original_copy = list(elements)
                result = function(elements)
                self.assertEqual(elements, original_copy)
                for perm in result:
                    self.assertIsNot(perm, elements)

    def test_not_a_list_raises_type_error(self):
        """Передача не списка вызывает TypeError."""
        invalid_inputs = (None, 123, "abc", (1, 2), {1, 2}, {"a": 1}, True)
        for function in PERMUTATION_FUNCTIONS:
            for invalid in invalid_inputs:
                with self.subTest(function=function.__name__, invalid=invalid):
                    with self.assertRaises(TypeError):
                        function(invalid)

    def test_count_is_factorial(self):
        """Количество перестановок равно факториалу длины списка."""
        for function in PERMUTATION_FUNCTIONS:
            for n in range(7):
                with self.subTest(function=function.__name__, n=n):
                    elements = list(range(n))
                    _assert_all_permutations(self, function(elements), elements)

    def test_rec_and_iter_agree(self):
        """Обе функции дают одинаковый набор перестановок."""
        elements = ["a", "b", "c", "d", "e"]
        rec = generate_permutations_rec(elements)
        iter_ = generate_permutations_iter(elements)
        self.assertEqual(sorted(rec), sorted(iter_))

    def test_error_message(self):
        """Текст ошибки для аргумента не-списка."""
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                with self.assertRaises(TypeError) as error:
                    function((1, 2))
                self.assertEqual(str(error.exception), NOT_LIST_ERROR_MSG)

    def test_repeated_elements(self):
        """Одинаковые элементы различаются по позициям: перестановок всё равно n!."""
        elements = [1, 1, 2]
        expected = [[1, 1, 2], [1, 1, 2], [1, 2, 1], [1, 2, 1], [2, 1, 1], [2, 1, 1]]
        for function in PERMUTATION_FUNCTIONS:
            with self.subTest(function=function.__name__):
                self.assertEqual(sorted(function(elements)), expected)


if __name__ == "__main__":
    unittest.main()
