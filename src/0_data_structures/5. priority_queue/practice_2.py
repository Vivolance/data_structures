"""
Implement a priority queue with the following methods
(The higher the weight, the higher the priority)
1. push (if similar priority, append to the end)
2. pop
3. peek

Key points:
1. A priority queue is essentially a queue with a logic for prioritising.
We adopt the logic of putting a weighted value into the queue, on top of
the data itself.

2. Use a deque data structure, with a tuple containing data and weight. The
weight will be used to cross compare other weights in the queue to know which
place it belongs to.
"""

from collections import deque
from typing import TypeVar

# instantiate T to be of any type placeable in a priority queue
T = TypeVar("T")


class PriorityQueue:
    def __init__(self) -> None:
        self.queue: deque[tuple[int, T]] = deque()

    def __len__(self) -> int:
        return len(self.queue)

    def __repr__(self) -> str:
        return f"Priority Queue = {list(self.queue)}"

    def push(self, priority: int, item: T) -> None:
        entry: tuple[int, T] = (priority, item)
        if not self.queue:
            self.queue.append(entry)
        else:
            # Flag to flag if item is inserted
            inserted: bool = False
            for i in range(len(self.queue)):
                if entry[0] > self.queue[i][0]:
                    self.queue.insert(i, entry)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(entry)

    def pop(self) -> T:
        """
        Pops the element with the highest priority
        """
        if not self.queue:
            raise ValueError("Priority Queue is empty")
        return self.queue.popleft()[1]

    def peek(self) -> T:
        if not self.queue:
            raise ValueError("Priority Queue is empty")
        return self.queue[0][1]


if __name__ == "__main__":
    priority_queue: PriorityQueue = PriorityQueue()

    priority_queue.push(10, "A")
    priority_queue.push(40, "B")
    priority_queue.push(20, "C")
    priority_queue.push(30, "D")

    # remove item with the most priority
    priority_queue.pop()

    # add item with similar priority, should appear behind "C"
    priority_queue.push(20, "E")

    # peek at the top priority item
    print(priority_queue.peek())

    print(priority_queue)
