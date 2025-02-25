"""
Implement a Single Linked list structure with the methods append, pop, insert and reverse
"""
from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, value: int, next: Optional["SinglyLinkedListNode"] = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, head: Optional[SinglyLinkedListNode] = None) -> None:
        self.head = head
        self.__length: int = 0 if not self.head else 1

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
        if self.head is None:
            return ""
        else:
            linked_list_str: list[str] = []
            curr_ptr: SinglyLinkedListNode = self.head
            while curr_ptr.next:
                linked_list_str.append(str(curr_ptr.value))
                curr_ptr = curr_ptr.next
            linked_list_str.append(str(curr_ptr.value))
            return ", ".join(linked_list_str)

    def append(self, value: int) -> None:
        """
        Appending a value to the back of the linked list
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

    def pop(self) -> None:
        """
        Removes the last element of the linked list
        """
        if self.head is None:
            raise ValueError("Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            curr_ptr: SinglyLinkedListNode = self.head
            while curr_ptr.next.next:
                curr_ptr = curr_ptr.next
            curr_ptr.next = None
        self.__length -= 1

    def insert(self, value: int, position: int) -> None:
        new_node: SinglyLinkedListNode = SinglyLinkedListNode(value)
        if 0 <= position <= self.__length:
            if self.head is None:
                self.head = new_node
            elif position < self.__length:
                curr_ptr: SinglyLinkedListNode = self.head
                for i in range(position):
                    curr_ptr = curr_ptr.next
                third_ptr: SinglyLinkedListNode = curr_ptr.next
                curr_ptr.next = new_node
                new_node.next = third_ptr
            else:
                curr_ptr: SinglyLinkedListNode = self.head
                while curr_ptr.next:
                    curr_ptr = curr_ptr.next
                curr_ptr.next = new_node
            self.__length += 1

        else:
            raise ValueError("position is not within length of linked list")

    def reverse(self) -> None:
        if self.head is None:
            raise ValueError("Linked list is empty")
        else:
            curr_ptr: SinglyLinkedListNode = self.head
            prev_ptr = None
            """
            Alternative:
            while curr is not None:
                next_node = curr.next  # Save the next node
                curr.next = prev       # Reverse the pointer
                prev = curr            # Move prev one step ahead
                curr = next_node       # Move curr one step ahead
            self.head = prev           # Reset head to the new front of the list
            """
            while curr_ptr.next:
                next_ptr = curr_ptr.next
                curr_ptr.next = prev_ptr
                prev_ptr = curr_ptr
                curr_ptr = next_ptr
            curr_ptr.next = prev_ptr
            self.head = curr_ptr


if __name__ == "__main__":
    linked_list: SinglyLinkedList = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.pop()
    linked_list.insert(15, 1)
    linked_list.insert(22, 3)
    linked_list.reverse()
    print(linked_list)
    print(len(linked_list))