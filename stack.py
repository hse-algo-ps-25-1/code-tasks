from linked_list import LinkedList


class Stack:
    """Стек на готовом односвязном списке.

    Элементы хранятся в объекте LinkedList. Вершина стека — голова списка.
    """

    def __init__(self):
        """Создаёт пустой стек."""
        self._items = LinkedList()

    def is_empty(self) -> bool:
        """Возвращает True, если стек пуст."""
        return self._items.head is None

    def __len__(self) -> int:
        """Возвращает число элементов."""
        return len(self._items)

    def push(self, value):
        """Кладёт элемент на вершину.

        :param value: новое значение вершины
        """
        self._items.insert(0, value)

    def pop(self):
        """Снимает и возвращает вершину.

        :raises IndexError: стек пуст
        :return: снятое значение
        """
        top_node = self._items.head
        if top_node is None:
            raise IndexError("Попытка удаления из пустого стека")
        self._items.remove(top_node.value)
        return top_node.value

    def peek(self):
        """Возвращает вершину, не снимая её.

        :raises IndexError: стек пуст
        :return: значение вершины
        """
        top_node = self._items.head
        if top_node is None:
            raise IndexError("Попытка вернуть вершину из пустого стека")
        return top_node.value
