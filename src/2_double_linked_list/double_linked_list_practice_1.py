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

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
        if self.head is None:
            return ""
        else:
            curr_ptr: DoubleLinkedListNode = self.head
            list_string: list[str] = []
            while curr_ptr.next:
                list_string.append(str(curr_ptr.value))
                curr_ptr = curr_ptr.next
            list_string.append(str(curr_ptr.value))
            return ", ".join(list_string)

    def enqueue(self, value: int) -> None:
        new_node: DoubleLinkedListNode = DoubleLinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            curr_ptr: DoubleLinkedListNode = self.head
            while curr_ptr.next:
                curr_ptr = curr_ptr.next
            curr_ptr.next = new_node
            new_node.prev = curr_ptr
            self.tail = new_node
        self.__length += 1

    def dequeue(self) -> None:
        if self.head is None:
            raise ValueError("Nothing to delete")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            curr_ptr: DoubleLinkedListNode = self.head
            while curr_ptr.next.next:
                curr_ptr = curr_ptr.next
            curr_ptr.next = None
            self.tail = curr_ptr

    def reverse(self) -> None:
        if self.head is None:
            raise ValueError("Linked list is empty")
        else:
            curr_ptr: DoubleLinkedListNode = self.head
            while curr_ptr:
                curr_ptr.next, curr_ptr.prev = curr_ptr.prev, curr_ptr.next
                curr_ptr = curr_ptr.prev
            self.head = self.tail
            self.tail = self.head


if __name__ == "__main__":
    dbl_linked_list: DoubleLinkedList = DoubleLinkedList()
    dbl_linked_list.enqueue(1)
    dbl_linked_list.enqueue(2)
    dbl_linked_list.enqueue(3)
    dbl_linked_list.dequeue()
    dbl_linked_list.enqueue(3)
    dbl_linked_list.reverse()
    print(dbl_linked_list)
    print(dbl_linked_list.tail.value)
