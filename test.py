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
        self.assertEqual(len(lst), 0)
        self.assertIsNone(lst.head)

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

    def test_insert_middle(self):
        """insert вставляет элемент в середину списка."""
        lst = LinkedList()
        for val in [1, 3]:
            lst.append(val)
        lst.insert(1, 2)
        self.assertEqual(list(lst), [1, 2, 3])

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
