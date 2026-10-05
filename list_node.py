from __future__ import annotations
from typing import Any


class ListNode:
    """
    Класс, описывающий узел (элемент) связного списка.

    Атрибуты:
        value: значение, которое хранит узел.
        next (ListNode | None): ссылка на следующий узел списка
            (или None, если это последний элемент).
    """

    def __init__(self, value: Any, next: ListNode | None = None) -> None:
        self.value = value
        self.next = next
