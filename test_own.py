import unittest

from main import (
    LENGTH_NOT_INT,
    LENGTH_NOT_POS,
    NOT_LIST,
    check_zero_one_strings,
    generate_strings_naive,
)


class TestNaiveGenerator(unittest.TestCase):
    def test_length_two(self):
        self.assertCountEqual(generate_strings_naive(2), ["01", "10", "11"])

    def test_not_int_length(self):
        with self.assertRaises(TypeError) as error:
            generate_strings_naive(2.0)
        self.assertEqual(LENGTH_NOT_INT, str(error.exception))

    def test_validator_accepts_result(self):
        strings = generate_strings_naive(3)
        self.assertTrue(check_zero_one_strings(3, strings))


class TestZeroOneValidator(unittest.TestCase):
    def test_length_two(self):
        self.assertTrue(check_zero_one_strings(2, ["01", "10", "11"]))

    def test_lecture_example(self):
        strings = ["010", "011", "110", "101", "111"]
        self.assertTrue(check_zero_one_strings(3, strings))

    def test_missing_string(self):
        self.assertFalse(check_zero_one_strings(2, ["01", "11"]))

    def test_not_int_length(self):
        with self.assertRaises(TypeError) as error:
            check_zero_one_strings(1.5, ["0", "1"])
        self.assertEqual(LENGTH_NOT_INT, str(error.exception))

    def test_negative_length(self):
        with self.assertRaises(ValueError) as error:
            check_zero_one_strings(-1, [])
        self.assertEqual(LENGTH_NOT_POS, str(error.exception))

    def test_not_list(self):
        with self.assertRaises(TypeError) as error:
            check_zero_one_strings(2, "01")
        self.assertEqual(NOT_LIST, str(error.exception))


if __name__ == "__main__":
    unittest.main()
