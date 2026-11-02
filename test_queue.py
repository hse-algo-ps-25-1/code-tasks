import math
import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    """Публичные примеры очереди."""

    def test_fifo(self):
        """Первый поставленный элемент выходит первым."""
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertFalse(queue.is_empty())
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.is_empty())

    def test_empty_queue(self):
        """У пустой очереди нет начала."""
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()


class TestQueueExtra(unittest.TestCase):
    """Дополнительные тесты команды."""

    def test_duplicates(self):
        """Одинаковые значения выходят по одному, в порядке постановки."""
        queue = Queue()
        for value in (1, 2, 2, 1):
            queue.enqueue(value)
        self.assertEqual([queue.dequeue() for _ in range(4)], [1, 2, 2, 1])
        self.assertTrue(queue.is_empty())

    def test_interleaved(self):
        """Постановка и извлечение вперемешку сохраняют порядок FIFO."""
        queue = Queue()
        queue.enqueue("a")
        queue.enqueue("b")
        self.assertEqual(queue.dequeue(), "a")
        queue.enqueue("c")
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_reuse_after_empty(self):
        """Опустевшая очередь снова принимает элементы."""
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 2)
        self.assertEqual(len(queue), 1)

    def test_none_value(self):
        """None хранится как обычное значение."""
        queue = Queue()
        queue.enqueue(None)
        self.assertFalse(queue.is_empty())
        self.assertIsNone(queue.peek())
        self.assertIsNone(queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_peek_repeated(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        for _ in range(3):
            self.assertEqual(queue.peek(), 1)
            self.assertEqual(len(queue), 2)

    def test_single_element(self):
        queue = Queue()
        queue.enqueue("x")
        self.assertEqual(queue.dequeue(), "x")
        self.assertTrue(queue.is_empty())
        with self.assertRaises(IndexError):
            queue.peek()

    def test_nan(self):
        queue = Queue()
        queue.enqueue(float("nan"))
        queue.enqueue(1)
        self.assertTrue(math.isnan(queue.peek()))
        self.assertTrue(math.isnan(queue.dequeue()))
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertTrue(queue.is_empty())

    def test_same_object_twice(self):
        value = float("nan")
        queue = Queue()
        queue.enqueue(value)
        queue.enqueue(value)
        self.assertIs(queue.dequeue(), value)
        self.assertIs(queue.dequeue(), value)
        self.assertTrue(queue.is_empty())

    def test_never_equal_object(self):
        class NeverEqual:
            def __eq__(self, other):
                return False

            __hash__ = object.__hash__

        item = NeverEqual()
        queue = Queue()
        queue.enqueue(item)
        self.assertIs(queue.peek(), item)
        self.assertIs(queue.dequeue(), item)
        self.assertTrue(queue.is_empty())

    def test_comparison_raises(self):
        class Uncomparable:
            def __eq__(self, other):
                raise RuntimeError("сравнение запрещено")

            def __ne__(self, other):
                raise RuntimeError("сравнение запрещено")

            __hash__ = object.__hash__

        item = Uncomparable()
        queue = Queue()
        queue.enqueue(item)
        self.assertIs(queue.dequeue(), item)
        self.assertTrue(queue.is_empty())

    def test_many_elements(self):
        """Очередь корректно работает с большим числом элементов."""
        queue = Queue()
        for i in range(1000):
            queue.enqueue(i)
        self.assertEqual(len(queue), 1000)
        for i in range(1000):
            self.assertEqual(queue.dequeue(), i)
        self.assertTrue(queue.is_empty())


if __name__ == "__main__":
    unittest.main()
