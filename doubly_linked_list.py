from doubly_list_node import DoublyListNode


class DoublyLinkedList:
    """
    Класс, реализующий двусвязный список.

    Атрибуты:
        head (DoublyListNode | None): ссылка на первый узел списка.
        tail (DoublyListNode | None): ссылка на последний узел списка.
        size (int): количество элементов в списке.

    Поддерживает базовые операции:
        - добавление элемента в конец (append),
        - вставка по индексу (insert),
        - удаление элемента по значению (remove),
        - поиск индекса элемента (index),
        - получение длины (__len__),
        - прямой обход (__iter__),
        - обратный обход (__reversed__),
        - строковое представление (__str__).
    """

    def __init__(self):
        """Создаёт пустой двусвязный список."""
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        """
        Добавляет элемент в конец списка.

        Аргументы:
            value: значение нового элемента.
        """
        self.insert(self.size, value)

    def insert(self, index, value):
        """
        Вставляет элемент по указанному индексу.

        Аргументы:
            index (int): позиция вставки (0 ≤ index ≤ len).
            value: значение нового элемента.

        Исключения:
            IndexError — если индекс вне диапазона.
        """
        if index < 0 or index > self.size:
            raise IndexError(f"индекс {index} вне диапазона от 0 до {self.size}")

        new_node = DoublyListNode(value)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        else:
            next_node = self._node_at(index)
            previous_node = next_node.prev
            new_node.prev = previous_node
            new_node.next = next_node
            previous_node.next = new_node
            next_node.prev = new_node

        self.size += 1

    def _node_at(self, index):
        """
        Возвращает узел по индексу, проходя от ближнего конца списка.

        Аргументы:
            index (int): позиция узла (0 ≤ index < len).

        Возвращает:
            DoublyListNode: узел на этой позиции.
        """
        if index < self.size // 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - 1 - index):
                node = node.prev
        return node

    def remove(self, value):
        """
        Удаляет первый элемент с указанным значением.

        Аргументы:
            value: значение для удаления.

        Исключения:
            ValueError — если элемента с таким значением нет.
        """
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            raise ValueError(f"{value} нет в списке")

        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.prev = None
        node.next = None
        self.size -= 1

    def index(self, value):
        """
        Возвращает индекс первого элемента с указанным значением.

        Аргументы:
            value: искомое значение.

        Возвращает:
            int: индекс элемента, если найден.
            None: если элемент отсутствует.
        """
        for position, element in enumerate(self):
            if element == value:
                return position
        return None

    def __len__(self):
        """Возвращает количество элементов в списке."""
        return self.size

    def __iter__(self):
        """
        Позволяет итерироваться по значениям элементов списка в цикле for
        от головы к хвосту.

        Использование:
            for x in my_list:
                ...
        """
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __reversed__(self):
        """
        Позволяет итерироваться по значениям элементов списка
        от хвоста к голове.

        Использование:
            for x in reversed(my_list):
                ...
        """
        node = self.tail
        while node is not None:
            yield node.value
            node = node.prev

    def __str__(self):
        """
        Возвращает строковое представление списка.

        Формат:
            [elem1 <-> elem2 <-> elem3]

        Пустой список:
            []
        """
        values = [str(v) for v in self]
        return "[" + " <-> ".join(values) + "]"
