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
            while current_node.next is not None:
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
        # Создаю фиктивный узел для того, чтобы избежать отдельной обработки краевых случаев
        dummy = ListNode(None, self.head)
        prev = dummy

        for _ in range(index):
            prev = prev.next

        new_node = ListNode(value)
        new_node.next = prev.next
        prev.next = new_node
        self.head = dummy.next
        self.size += 1

    def remove(self, value: Any) -> None:
        """
        Удаляет первый элемент с указанным значением.

        Аргументы:
            value: значение для удаления.

        Исключения:
            ValueError — если элемента с таким значением нет.
        """
        dummy = ListNode(None, self.head)
        current = dummy

        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.head = dummy.next
                self.size -= 1
                return

            current = current.next

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
        return "[" + " -> ".join(str(v) for v in self) + "]"
