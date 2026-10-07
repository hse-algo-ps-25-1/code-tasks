import unittest

from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    """Набор тестов для класса DoublyLinkedList."""

    def test_empty_init(self):
        """Новый список пустой: длина 0, head и tail = None."""
        lst = DoublyLinkedList()
        self.assertEqual(len(lst), 0)
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)

    def test_append_one(self):
        """append добавляет один элемент в конец."""
        lst = DoublyLinkedList()
        lst.append(10)
        self.assertEqual(len(lst), 1)
        self.assertEqual(list(lst), [10])

    def test_append_many(self):
        """append несколько раз сохраняет порядок элементов."""
        lst = DoublyLinkedList()
        for val in [1, 2, 3]:
            lst.append(val)
        self.assertEqual(len(lst), 3)
        self.assertEqual(list(lst), [1, 2, 3])

    def test_insert_middle(self):
        """insert вставляет элемент в середину списка."""
        for values, index, value, expected in [
            ([1, 3], 1, 2, [1, 2, 3]),
            ([1, 3, 4, 5, 6], 1, 2, [1, 2, 3, 4, 5, 6]),
            ([1, 2, 3, 5, 6], 3, 4, [1, 2, 3, 4, 5, 6]),
        ]:
            with self.subTest(values=values, index=index):
                lst = make_list(values)
                lst.insert(index, value)
                self.assertEqual(list(lst), expected)
                self.assert_structure(lst, expected)

    def test_insert_boundaries(self):
        """insert в пустой список, в начало и в конец сохраняет связи."""
        for values, index, value, expected in [
            ([], 0, 1, [1]),
            ([2, 3], 0, 1, [1, 2, 3]),
            ([1, 2], 2, 3, [1, 2, 3]),
        ]:
            with self.subTest(values=values, index=index):
                lst = make_list(values)
                lst.insert(index, value)
                self.assert_structure(lst, expected)

    def test_insert_out_of_range(self):
        """insert вызывает IndexError для индекса вне диапазона, не меняя список."""
        for index in [-1, 4]:
            with self.subTest(index=index):
                lst = make_list([1, 2, 3])
                self.assertRaises(IndexError, lst.insert, index, 0)
                self.assert_structure(lst, [1, 2, 3])

    def test_index_found(self):
        """index возвращает индекс первого найденного элемента."""
        lst = DoublyLinkedList()
        for val in ["a", "b", "c"]:
            lst.append(val)
        self.assertEqual(lst.index("b"), 1)

    def test_index_first_occurrence(self):
        """index для повторяющегося значения возвращает индекс первого вхождения."""
        lst = make_list(["a", "b", "a"])
        self.assertEqual(lst.index("a"), 0)

    def test_index_missing(self):
        """index возвращает None для отсутствующего значения."""
        for values in [[], [1, 2, 3]]:
            with self.subTest(values=values):
                lst = make_list(values)
                self.assertIsNone(lst.index(4))

    def test_iteration(self):
        """Итерация по списку возвращает значения от головы к хвосту."""
        lst = DoublyLinkedList()
        for val in [1, 2, 3]:
            lst.append(val)
        self.assertEqual([x for x in lst], [1, 2, 3])

    def test_reversed(self):
        """Обратный обход возвращает значения от хвоста к голове."""
        for values in [[], [1], [1, 2, 3], [None, "a", "a"]]:
            with self.subTest(values=values):
                lst = make_list(values)
                self.assertEqual(list(reversed(lst)), values[::-1])
                self.assert_structure(lst, values)

    def test_str(self):
        """str выводит элементы через <->, пустой список как []."""
        for values, expected in [([], "[]"), ([1, 2, 3], "[1 <-> 2 <-> 3]")]:
            with self.subTest(values=values):
                lst = make_list(values)
                self.assertEqual(str(lst), expected)

    def test_remove_head(self):
        """remove удаляет первый узел и обновляет голову списка."""
        lst = make_list([1, 2, 3])
        self.assertIsNone(lst.remove(1))
        self.assert_structure(lst, [2, 3])

    def test_remove_middle(self):
        """remove удаляет узел в середине и связывает соседние узлы."""
        lst = make_list([1, 2, 3])
        lst.remove(2)
        self.assert_structure(lst, [1, 3])

    def test_remove_tail(self):
        """remove удаляет последний узел и обновляет хвост списка."""
        lst = make_list([1, 2, 3])
        lst.remove(3)
        self.assert_structure(lst, [1, 2])

    def test_remove_only_node(self):
        """После удаления единственного узла длина 0, head и tail = None."""
        lst = make_list([1])
        lst.remove(1)
        self.assert_structure(lst, [])

    def test_remove_first_duplicate(self):
        """remove удаляет только первое вхождение повторяющегося значения."""
        lst = make_list([1, 2, 1])
        lst.remove(1)
        self.assert_structure(lst, [2, 1])

    def test_remove_missing(self):
        """remove вызывает ValueError для отсутствующего значения, не меняя список."""
        for values in [[], [1, 2, 3]]:
            with self.subTest(values=values):
                lst = make_list(values)
                self.assertRaises(ValueError, lst.remove, 4)
                self.assert_structure(lst, values)

    def assert_structure(self, lst, expected):
        self.assertEqual(len(lst), len(expected))
        values = []
        previous = None
        node = lst.head
        while node is not None:
            self.assertLess(len(values), len(expected))
            self.assertIs(node.prev, previous)
            values.append(node.value)
            previous = node
            node = node.next
        self.assertEqual(values, expected)
        self.assertIs(lst.tail, previous)
        self.assertEqual(list(reversed(lst)), expected[::-1])


def make_list(values):
    lst = DoublyLinkedList()
    for value in values:
        lst.append(value)
    return lst


if __name__ == "__main__":
    unittest.main()
