from typing import Any, Iterator

from list_node import ListNode


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

    def __init__(self) -> None:
        """Создаёт пустой связный список."""
        self.head: ListNode | None = None
        self.size: int = 0

    def append(self, value: Any) -> None:
        """
        Добавляет элемент в конец списка.

        Аргументы:
            value: значение нового элемента.
        """
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        self.size += 1

    def insert(self, index: int, value: Any) -> None:
        """
        Вставляет элемент по указанному индексу.

        Аргументы:
            index (int): позиция вставки (0 ≤ index ≤ len).
            value: значение нового элемента.

        Исключения:
            IndexError — если индекс вне диапазона.
        """
        if not (0 <= index <= self.size):
            raise IndexError("Индекс вне диапазона")

        new_node = ListNode(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

        self.size += 1

    def remove(self, value: Any) -> None:
        """
        Удаляет первый элемент с указанным значением.

        Аргументы:
            value: значение для удаления.

        Исключения:
            ValueError — если элемента с таким значением нет.
        """
        if self.head is None:
            raise ValueError("Невозможно удалить значение из пустого списка")

        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.size -= 1
                return
            current_node = current_node.next

        raise ValueError(f"Значение {value!r} отсутствует")

    def index(self, value: Any) -> int | None:
        """
        Возвращает индекс первого элемента с указанным значением.

        Аргументы:
            value: искомое значение.

        Возвращает:
            int: индекс элемента, если найден.
            None: если элемент отсутствует.
        """
        current_node = self.head
        for idx in range(self.size):
            if current_node.value == value:
                return idx
            current_node = current_node.next

        return None

    def __len__(self) -> int:
        """Возвращает количество элементов в списке."""
        return self.size

    def __iter__(self) -> Iterator[Any]:
        """
        Позволяет итерироваться по значениям элементов списка в цикле for.

        Использование:
            for x in my_list:
                ...
        """
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __str__(self) -> str:
        """
        Возвращает строковое представление списка.

        Формат:
            [elem1 -> elem2 -> elem3]

        Пустой список:
            []
        """
        values = [str(v) for v in self]
        return "[" + " -> ".join(values) + "]"