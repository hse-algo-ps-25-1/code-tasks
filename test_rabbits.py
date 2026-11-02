import unittest
from queue import Queue

from main import rabbits, validate_args


def simulate(month, lifetime):
    """Прямое моделирование: список месяцев рождения всех живых пар."""
    pairs = [1]
    for t in range(2, month + 1):
        newborn = [t for birth in pairs if t >= birth + 2]
        pairs = [birth for birth in pairs if t < birth + lifetime] + newborn
    return len(pairs)


class TestRabbits(unittest.TestCase):
    """Публичные примеры задачи о кроликах."""

    def test_first_months(self):
        """До первой смерти численность совпадает с числами Фибоначчи."""
        self.assertEqual(rabbits(1, 2), 1)
        self.assertEqual(rabbits(2, 2), 1)
        self.assertEqual(rabbits(6, 8), 8)

    def test_first_death(self):
        """На 8-й месяц при жизни 7 месяцев остаётся 20 пар."""
        self.assertEqual(rabbits(8, 7), 20)

    def test_later_months(self):
        """Численность считается и после нескольких смертей."""
        self.assertEqual(rabbits(20, 7), 5266)
        self.assertEqual(rabbits(25, 7), 53515)


class TestRabbitsExtra(unittest.TestCase):
    """Дополнительные тесты команды."""

    def test_fibonacci_before_death(self):
        """Пока никто не умер, численность — числа Фибоначчи."""
        fib = [1, 1]
        while len(fib) < 30:
            fib.append(fib[-1] + fib[-2])
        for month in range(1, 31):
            self.assertEqual(rabbits(month, 100), fib[month - 1])

    def test_month_before_death(self):
        """В месяце lifetime исходная пара ещё жива."""
        self.assertEqual(rabbits(7, 7), 13)

    def test_lifetime_two(self):
        """При жизни 2 месяца каждая пара даёт одну пару и умирает."""
        for month in range(1, 20):
            self.assertEqual(rabbits(month, 2), 1)

    def test_lifetime_three(self):
        """При жизни 3 месяца численность — числа Падована."""
        expected = [1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
        for month, count in enumerate(expected, start=1):
            self.assertEqual(rabbits(month, 3), count)

    def test_against_simulation(self):
        """Ответ совпадает с прямым моделированием."""
        for lifetime in range(2, 10):
            for month in range(1, 25):
                with self.subTest(month=month, lifetime=lifetime):
                    self.assertEqual(
                        rabbits(month, lifetime), simulate(month, lifetime)
                    )

    def test_large_month(self):
        """Большие номера месяцев считаются без ошибок."""
        self.assertGreater(rabbits(200, 20), 0)

    def test_type_errors(self):
        """Не целые аргументы и bool дают TypeError."""
        for args in ((True, 7), (8, False), (8.0, 7), (8, 7.0), ("8", 7), (None, 7)):
            with self.subTest(args=args):
                with self.assertRaises(TypeError):
                    rabbits(*args)

    def test_value_errors(self):
        """month < 1 или lifetime < 2 дают ValueError."""
        for args in ((0, 7), (-1, 7), (8, 1), (8, 0), (8, -5)):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    rabbits(*args)

    def test_queue_used(self):
        """Очередь из queue.py — та же, что использует main."""
        import main

        self.assertIs(main.Queue, Queue)


class TestValidateArgs(unittest.TestCase):
    def test_valid(self):
        for args in ((1, 2), (8, 7), (10**20, 10**20)):
            with self.subTest(args=args):
                self.assertIsNone(validate_args(*args))

    def test_type_errors(self):
        for args in ((True, 7), (8, False), (8.0, 7), (8, "7"), (None, 7)):
            with self.subTest(args=args):
                with self.assertRaises(TypeError):
                    validate_args(*args)

    def test_value_errors(self):
        for args in ((0, 2), (1, 1), (-3, 7)):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    validate_args(*args)

    def test_type_error_before_value_error(self):
        with self.assertRaises(TypeError):
            validate_args(0, 7.0)
        with self.assertRaises(TypeError):
            validate_args(1.5, 0)


if __name__ == "__main__":
    unittest.main()
