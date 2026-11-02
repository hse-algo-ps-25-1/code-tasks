from doubly_linked_list import DoublyLinkedList


class _QueueEntry:
    __slots__ = ("value",)

    def __init__(self, value):
        self.value = value


class Queue:
    """Структура данных Очередь"""

    def __init__(self):
        """Создаёт пустую очередь."""
        self._items = DoublyLinkedList()

    def is_empty(self) -> bool:
        """Возвращает True, если очередь пуста."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Возвращает число элементов."""
        return len(self._items)

    def enqueue(self, value):
        """Ставит элемент в конец очереди.

        :param value: новое значение
        """
        self._items.append(_QueueEntry(value))

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди.

        :raises IndexError: очередь пуста
        :return: удалённое значение
        """
        entry = self._head_entry()
        # remove удаляет первое вхождение значения, то есть голову списка
        self._items.remove(entry)
        return entry.value

    def peek(self):
        """Возвращает начало очереди, не удаляя его.

        :raises IndexError: очередь пуста
        :return: значение в начале
        """
        return self._head_entry().value

    def _head_entry(self) -> _QueueEntry:
        if self.is_empty():
            raise IndexError("очередь пуста")
        return self._items.head.value
