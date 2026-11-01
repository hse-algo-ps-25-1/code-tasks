import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    """Публичные примеры стека."""

    def test_lifo(self):
        """Последний положенный элемент снимается первым."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)
        stack.push(1)
        stack.push(2)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_empty_stack(self):
        """У пустого стека нет вершины."""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()
        self.assertEqual(len(stack), 0)

    def test_pop_with_duplicates(self):
        """Равные значения снимаются с вершины по одному."""
        stack = Stack()
        for value in (1, 2, 2, 3, 1):
            stack.push(value)
        popped = [stack.pop() for _ in range(5)]
        self.assertEqual(popped, [1, 3, 2, 2, 1])

    def test_falsy_values(self):
        """None, 0 и пустая строка хранятся как обычные значения."""
        stack = Stack()
        for value in (None, 0, ""):
            stack.push(value)
        self.assertFalse(stack.is_empty())
        popped = [stack.pop() for _ in range(3)]
        self.assertEqual(popped, ["", 0, None])

    def test_stacks_independent(self):
        """Два стека не делят элементы."""
        first = Stack()
        second = Stack()
        first.push(1)
        self.assertTrue(second.is_empty())


if __name__ == "__main__":
    unittest.main()
