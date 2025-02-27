"""
Implement the logic of a priority queue
"""

from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self.queue: deque[tuple[int, T]] = deque()

    def __len__(self) -> int:
        return len(self.queue)

    def __repr__(self) -> str:
        return f"PriorityQueue({list(self.queue)})"

    def push(self, item: T, priority: int) -> None:
        entry: tuple[int, T] = (priority, item)
        if not self.queue:
            self.queue.append(entry)
        else:
            inserted: bool = False
            for i in range(len(self.queue)):
                # if similar priority, follows a typical queue, append at last of all similar priority
                if entry[0] < self.queue[i][0]:
                    self.queue.insert(i, entry)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(entry)

    def pop(self) -> T:
        if not self.queue:
            raise ValueError("Priority Queue is empty!")
        return self.queue.popleft()[1]

    def peek(self) -> T:
        if not self.queue:
            raise ValueError("Priority Queue is empty!")
        return self.queue[0][1]


if __name__ == "__main__":
    my_queue: PriorityQueue = PriorityQueue()

    # Adding new entries
    my_queue.push(10, 4)
    my_queue.push(20, 2)
    my_queue.push(30, 1)
    my_queue.push(40, 3)

    # Remove the most prioritised item
    my_queue.pop()

    # See the most prioritise item without removing
    print(my_queue.peek())
    print(my_queue)
