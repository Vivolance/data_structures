"""
Implement a double linked list with append, insert, delete, reverse
"""

from typing import Optional


class DoubleLinkedListNode:
    def __init__(
        self,
        value: int,
        prev: Optional["DoubleLinkedListNode"] = None,
        next: Optional["DoubleLinkedListNode"] = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next

    @staticmethod
    def move_ptr_to_end(
        curr_ptr: "DoubleLinkedListNode",
    ) -> "DoubleLinkedListNode":
        if not curr_ptr.next:
            return curr_ptr
        else:
            return DoubleLinkedListNode.move_ptr_to_end(curr_ptr.next)


class DoubleLinkedList:
    def __init__(
        self,
        head: Optional[DoubleLinkedListNode] = None,
        tail: Optional[DoubleLinkedListNode] = None,
    ) -> None:
        self.head = head
        self.tail = tail
        self.__length = 0 if self.head is None else 1
