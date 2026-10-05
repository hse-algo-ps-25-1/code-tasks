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
        self.assertEqual(len(lst), 3)
        self.assertEqual(list(lst), [1, 2, 3])

    def test_append_order_next(self):
        """append правильно связывает узлы через next."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)
        lst.append(30)

        self.assertEqual(lst.head.value, 10)
        self.assertEqual(lst.head.next.value, 20)
        self.assertEqual(lst.head.next.next.value, 30)
        self.assertIsNone(lst.head.next.next.next)

    def test_append_size(self):
        """append увеличивает size на один после каждого добавления."""
        lst = LinkedList()

        self.assertEqual(lst.size, 0)

        lst.append(10)
        self.assertEqual(lst.size, 1)

        lst.append(20)
        self.assertEqual(lst.size, 2)

        lst.append(30)
        self.assertEqual(lst.size, 3)

        lst.append(40)
        self.assertEqual(lst.size, 4)

    def test_append_duplicate_values(self):
        """append сохраняет повторяющиеся значения как отдельные узлы."""
        lst = LinkedList()

        lst.append(15)
        lst.append(15)
        lst.append(15)

        self.assertEqual(list(lst), [15, 15, 15])
        self.assertEqual(len(lst), 3)

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

    def test_append_head_unchanged(self):
        """append не меняет первый узел после последующих добавлений."""
        lst = LinkedList()

        lst.append(10)
        first_node = lst.head

        lst.append(20)
        lst.append(30)

        self.assertIs(lst.head, first_node)

    def test_append_last_next_is_none(self):
        """После append последний узел имеет next = None."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)
        lst.append(30)

        last_node = lst.head.next.next

        self.assertEqual(last_node.value, 30)
        self.assertIsNone(last_node.next)

    def test_append_updates_last_next(self):
        """append связывает предыдущий последний узел с новым."""
        lst = LinkedList()

        lst.append(10)
        old_last = lst.head

        lst.append(20)

        self.assertEqual(old_last.next.value, 20)
        self.assertIsNone(old_last.next.next)


    def test_insert_empty(self):
        """insert по индексу 0 добавляет первый элемент в пустой список."""
        lst = LinkedList()

        lst.insert(0, 10)

        self.assertEqual(list(lst), [10])
        self.assertEqual(lst.head.value, 10)
        self.assertEqual(lst.size, 1)

    def test_insert_first(self):
        """insert по индексу 0 добавляет элемент в начало."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        lst.insert(0, 5)

        self.assertEqual(list(lst), [5, 10, 20])
        self.assertEqual(lst.head.value, 5)
        self.assertEqual(lst.size, 3)
    
    def test_insert_middle(self):
        """insert вставляет элемент в середину списка."""
        lst = LinkedList()
        for val in [1, 3]:
            lst.append(val)
        lst.insert(1, 2)
        self.assertEqual(list(lst), [1, 2, 3])

    def test_insert_last(self):
        """insert по индексу size добавляет элемент в конец."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        lst.insert(lst.size, 30)

        self.assertEqual(list(lst), [10, 20, 30])
        self.assertEqual(lst.size, 3)

    def test_insert_negative_index(self):
        """insert с отрицательным индексом вызывает IndexError."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        with self.assertRaises(IndexError):
            lst.insert(-1, 5)

        self.assertEqual(list(lst), [10, 20])
        self.assertEqual(lst.size, 2)

    def test_insert_index_too_large(self):
        """insert с индексом больше size вызывает IndexError."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        with self.assertRaises(IndexError):
            lst.insert(3, 30)

        self.assertEqual(list(lst), [10, 20])
        self.assertEqual(lst.size, 2)

    def test_insert_links(self):
        """insert правильно меняет связи между узлами."""
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


    def test_insert_none(self):
        """insert вставляет None как обычное значение."""
        lst = LinkedList()

        lst.append(10)
        lst.append(20)

        lst.insert(1, None)

        self.assertEqual(list(lst), [10, None, 20])
        self.assertEqual(lst.size, 3)

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

    def test_insert_many_operations(self):
        """insert сохраняет правильный порядок после большого числа вставок."""
        lst = LinkedList()

        for value in range(100):
            lst.insert(lst.size, value)

        self.assertEqual(list(lst), list(range(100)))
        self.assertEqual(lst.size, 100)
        
    def test_index_found(self):
        """index возвращает индекс первого найденного элемента."""
        lst = LinkedList()
        for val in ["a", "b", "c"]:
            lst.append(val)
        self.assertEqual(lst.index("b"), 1)

    def test_iteration(self):
        """Итерация по списку возвращает значения в порядке следования."""
        lst = LinkedList()
        for val in [1, 2, 3]:
            lst.append(val)
        self.assertEqual([x for x in lst], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
