from list_node import ListNode


# TODO:перепроверить всё на свежую голову, провести первые тесты
class LinkedList:
    """
    Класс, реализующий односвязный список.

    Атрибуты:
        head (ListNode | None): ссылка на первый узел списка.
        size (int): количество элементов в списке.

    Поддерживает базовые операции:
        - добавление элемента в конец (append),
        - вставка по индексу (insert),
        - удаление элемента по значению (remove),
        - поиск индекса элемента (index),
        - получение длины (__len__),
        - итерация (__iter__),
        - строковое представление (__str__).
    """

    def __init__(self):
        """Создаёт пустой связный список."""
        self.head = None
        self.size = 0

    def append(self, value):
        """
        Добавляет элемент в конец списка.

        Аргументы:
            value: значение нового элемента.
        """
        if self.size == 0:
            self.head = ListNode(value)
            self.size += 1
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = ListNode(value)
        self.size += 1

    def insert(self, index, value):
        """
        Вставляет элемент по указанному индексу.

        Аргументы:
            index (int): позиция вставки (0 ≤ index ≤ len).
            value: значение нового элемента.

        Исключения:
            IndexError — если индекс вне диапазона.
        """
        if index > self.size:
            raise IndexError("Индекс вне диапазона")
        for current_index in range(index):
            if current_index == 0:
                current_node = self.head
            else:
                current_node = current_node.next
        current_node.next = ListNode(value, current_node.next)
        self.size += 1

    def remove(self, value):
        """
        Удаляет первый элемент с указанным значением.

        Аргументы:
            value: значение для удаления.

        Исключения:
            ValueError — если элемента с таким значением нет.
        """
        if self.size == 0:
            raise ValueError("Невозможно удалить значение из пустого списка")

        if self.head.value == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        raise ValueError("Указанное значение отсутствует")

    def index(self, value):
        """
        Возвращает индекс первого элемента с указанным значением.

        Аргументы:
            value: искомое значение.

        Возвращает:
            int: индекс элемента, если найден.
            None: если элемент отсутствует.
        """
        target_val = None
        current_node = self.head
        for idx in range(self.size):
            if current_node.value == value:
                target_val = current_node.value
                break
        return idx

    def __len__(self):
        """Возвращает количество элементов в списке."""
        return self.size

    def __iter__(self):
        """
        Позволяет итерироваться по значениям элементов списка в цикле for.

        Использование:
            for x in my_list:
                ...
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        """
        Возвращает строковое представление списка.

        Формат:
            [elem1 -> elem2 -> elem3]

        Пустой список:
            []
        """
        values = [str(v) for v in self]
        return "[" + " -> ".join(values) + "]"
