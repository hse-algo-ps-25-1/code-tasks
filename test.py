import unittest

from linked_list import LinkedList
"""
TODO: некоторые идеи для тестов:
1.Проверить работу с разными типами данных(которые входят в аннотацию) их добавление и удаление. None заслуживает отдельного внимания
2.Проверить краевые случаи, когда индекс равен нулю или size-1 
3.Убедиться что size работает корректно, и нет способа вывалиться за границы массива с его помощью
Удалить этот комментарий, когда работа будет закончена
"""

class TestLinkedList(unittest.TestCase):
    """Набор тестов для класса LinkedList."""

    def test_empty_init(self):
        """Новый список пустой: длина 0, head = None."""
        lst = LinkedList()
        self.assertEqual(lst.size, 0)
        self.assertIsNone(lst.head)

    def test_lists_independent(self):
        """Два новых списка создаются независимо друг от друга."""
        first = LinkedList()
        second = LinkedList()

        first.append(10)

        self.assertEqual(first.size, 1)
        self.assertEqual(second.size, 0)
        self.assertIsNone(second.head)
    
    def test_append_one(self):
        """append добавляет один элемент в конец."""
        lst = LinkedList()
        lst.append(10)
        self.assertEqual(len(lst), 1)
        self.assertEqual(list(lst), [10])

    def test_append_many(self):
        """append несколько раз сохраняет порядок элементов."""
        lst = LinkedList()
        for val in [1, 2, 3]:
            lst.append(val)
        self.assertEqual(lst.size, 3)
        self.assertEqual(list(lst), [1, 2, 3])

    def test_append_order_next(self):
        """append правильно связывает узлы и не меняет первый узел"""
        lst = LinkedList()

        lst.append(10)
        first_node = lst.head

        lst.append(20)
        lst.append(30)

        self.assertIs(lst.head, first_node)
        self.assertEqual(lst.head.value, 10)
        self.assertEqual(lst.head.next.value, 20)
        self.assertEqual(lst.head.next.next.value, 30)
        self.assertIsNone(lst.head.next.next.next)

    def test_append_different_value_types(self):
        """append сохраняет значения разных типов."""
        lst = LinkedList()

        lst.append(10)
        lst.append(9.14)
        lst.append("text")
        lst.append(True)
        lst.append(None)
        lst.append([1, 2])
        lst.append({"a": 1})
        self.assertEqual(
            list(lst),
            [10, 9.14, "text", True, None, [1, 2], {"a": 1}],
        )

    def test_insert_empty(self):
        """insert по индексу 0 добавляет первый элемент в пустой список."""
        lst = LinkedList()

        lst.insert(0, 10)

        self.assertEqual(list(lst), [10])
        self.assertEqual(lst.head.value, 10)
        self.assertEqual(lst.size, 1)
    
    def test_insert_last(self):
        """insert по индексу size добавляет элемент в конец."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        lst.insert(lst.size, 30)

        self.assertEqual(list(lst), [10, 20, 30])
        self.assertEqual(lst.size, 3)

    def test_insert_invalid_indexes(self):
        """insert вызывает IndexError для индексов вне диапазона 0 <= index <= size."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        for index in [-1, -10, 3, 10]:
            with self.assertRaises(IndexError):
                lst.insert(index, 5)

        self.assertEqual(list(lst), [10, 20])
        self.assertEqual(lst.size, 2)

    def test_insert_links(self):
        """insert корректно вставляет узел в середину и сохраняет связи между узлами"""
        lst = LinkedList()

        lst.append(10)
        lst.append(30)

        old_second = lst.head.next

        lst.insert(1, 20)

        self.assertEqual(lst.head.value, 10)
        self.assertEqual(lst.head.next.value, 20)
        self.assertIs(lst.head.next.next, old_second)
        self.assertEqual(lst.head.next.next.value, 30)
        self.assertIsNone(lst.head.next.next.next)

    def test_insert_many_at_zero(self):
        """insert многократно корректно вставляет элементы в начало."""
        lst = LinkedList()

        lst.insert(0, 10)
        lst.insert(0, 20)
        lst.insert(0, 30)
        lst.insert(0, 40)

        self.assertEqual(list(lst), [40, 30, 20, 10])
        self.assertEqual(lst.size, 4)
        self.assertEqual(lst.head.value, 40)

    def test_remove_only_element(self):
        """remove корректно удаляет единственный элемент списка."""
        lst = LinkedList()

        lst.append(10)

        lst.remove(10)

        self.assertEqual(list(lst), [])
        self.assertIsNone(lst.head)
        self.assertEqual(lst.size, 0)

    def test_remove_first(self):
        """remove удаляет первый элемент и корректно меняет head."""
        lst = LinkedList()

        for val in [10, 20, 30]:
            lst.append(val)

        lst.remove(10)

        self.assertEqual(list(lst), [20, 30])
        self.assertEqual(lst.head.value, 20)
        self.assertEqual(lst.size, 2)

    def test_remove_first_duplicate(self):
        """remove удаляет только первое вхождение значения."""
        lst = LinkedList()

        for val in [10, 20, 20, 30]:
            lst.append(val)

        lst.remove(20)

        self.assertEqual(list(lst), [10, 20, 30])
        self.assertEqual(lst.size, 3)

    def test_remove_last(self):
        """remove корректно удаляет последний элемент."""
        lst = LinkedList()

        for val in [10, 20, 30]:
            lst.append(val)

        lst.remove(30)

        self.assertEqual(list(lst), [10, 20])
        self.assertEqual(lst.size, 2)
        self.assertIsNone(lst.head.next.next)

    def test_remove_missing_value(self):
        """remove вызывает ValueError и не изменяет список, если значения нет."""
        lst = LinkedList()

        for val in [10, 20, 30]:
            lst.append(val)

        with self.assertRaises(ValueError):
            lst.remove(99)

        self.assertEqual(list(lst), [10, 20, 30])
        self.assertEqual(lst.size, 3)

    def test_index_returns_correct_index(self):
        """index корректно возвращает индексы и обрабатывает особые случаи."""
        lst = LinkedList()

        self.assertIsNone(lst.index(10))

        for val in [None, 10, 20, 10, 30]:
            lst.append(val)

        self.assertEqual(lst.index(None), 0)
        self.assertEqual(lst.index(10), 1)
        self.assertEqual(lst.index(20), 2)
        self.assertEqual(lst.index(30), 4)
        self.assertIsNone(lst.index(999))

    def test_index_tracks_changes(self):
        """index корректно отслеживает изменения списка."""
        lst = LinkedList()

        for val in [10, 20, 30, 20, 40]:
            lst.append(val)

        self.assertEqual(lst.index(20), 1)

        lst.insert(0, 5)
        self.assertEqual(lst.index(20), 2)

        lst.remove(10)
        self.assertEqual(lst.index(20), 1)

        lst.remove(20)
        self.assertEqual(lst.index(20), 2)
    
    def test_iteration(self):
        """Итерация по списку возвращает значения в порядке следования."""
        lst = LinkedList()
        for val in [1, 2, 3]:
            lst.append(val)
        self.assertEqual([x for x in lst], [1, 2, 3])

    def test_iteration_empty(self):

        """Итерация по пустому списку не возвращает элементов."""
        lst = LinkedList()

        self.assertEqual(list(lst), [])

    def test_iteration_after_changes(self):
        """Итерация возвращает правильные значения после insert и remove."""
        lst = LinkedList()

        for val in [10, 30, 40]:
            lst.append(val)

        lst.insert(1, 20)
        lst.remove(30)

        self.assertEqual(list(lst), [10, 20, 40])

    def test_iteration_reusable(self):
        """Итерацию по списку можно выполнять повторно."""
        lst = LinkedList()

        for val in [10, 20, 30]:
            lst.append(val)

        self.assertEqual(list(lst), [10, 20, 30])
        self.assertEqual(list(lst), [10, 20, 30])

    def test_str_output(self):
        """str возвращает правильное строковое представление списка."""
        lst = LinkedList()

        self.assertEqual(str(lst), "[]")

        for val in [10, 20, 30]:
            lst.append(val)

        self.assertEqual(str(lst), "[10 -> 20 -> 30]")

if __name__ == "__main__":
    unittest.main()
