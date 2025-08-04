"""
Implement a singly linked list with append, pop, insert, reverse
"""

from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, value: int, next: Optional["SinglyLinkedListNode"]) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, head: Optional[SinglyLinkedListNode] = None) -> None:
        self.head = head
        self.__length: int = 0 if not self.head else 1

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> list[str]:
        if self.head is None:
            return [""]
        else:
            linked_list_str: list[str] = []
            curr_ptr: SinglyLinkedListNode = self.head
            while curr_ptr.next:
                linked_list_str.append(str(curr_ptr.value))
                curr_ptr = curr_ptr.next
            linked_list_str.append(str(curr_ptr.value))
            return linked_list_str

    def append(self, value: int) -> None:
        """
        Traverse to end
        """
        new_node: SinglyLinkedListNode = SinglyLinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            curr_ptr: SinglyLinkedListNode = self.head
            while curr_ptr.next:
                curr_ptr = curr_ptr.next
            curr_ptr.next = new_node
            self.__length += 1

    def insert(self, value: int, index: int) -> None:
        new_node: SinglyLinkedListNode = SinglyLinkedListNode(value)
        if 0 <= index <= self.__length:
            curr_ptr: SinglyLinkedListNode = self.head

            if self.head is None:
                self.head = new_node
            elif index < self.__length:
                for _ in range(index):
                    curr_ptr = curr_ptr.next
                temp_ptr: SinglyLinkedListNode = curr_ptr.next
                curr_ptr.next = new_node
                new_node.next = temp_ptr
            # same as append
            else:
                while curr_ptr.next:
                    curr_ptr = curr_ptr.next
                curr_ptr.next = new_node

        else:
            raise ValueError("Index out of range")

    def reverse(self) -> None:
        if self.head is None:
            return
        else:
            curr_ptr: SinglyLinkedListNode = self.head
            prev_ptr = None
            while curr_ptr.next:
                next_ptr = curr_ptr.next
                curr_ptr.next = prev_ptr
                prev_ptr = curr_ptr
                curr_ptr = next_ptr
            curr_ptr.next = prev_ptr
            self.head = curr_ptr


