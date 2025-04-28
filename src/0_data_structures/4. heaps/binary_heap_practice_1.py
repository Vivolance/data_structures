"""
Create a min heap and max heap with the following methods:
- heappop -> remove top item from the heap
- heappush -> append an item to the heap
- heapify -> create a min/max heap
- top -> display the top most item

Note:
1. heapify() -> smallest number is at index 0. We CANNOT assume the next smallest is at index 1.
2. USe negative sign to implement a max heap. Copy [-nums for num in nums] to do a max heap
3. After we do heappop() we are guarantee to always pop the smallest number. The heap then rearranges itself
calling index [0] will return the smallest of the reamining heap.
4. Time complexity:
    - heapify() -> O(N)
    - heappop() -> O(logN)
    - heappush() -> O(logN)
"""

import copy
import heapq
import random


def min_heap(my_list: list[int]) -> list[int]:
    deep_nums: list[int] = copy.copy(my_list)
    heapq.heapify(deep_nums)
    return deep_nums


def max_heap(my_list: list[int]) -> list[int]:
    deep_nums: list[int] = [-num for num in my_list]
    heapq.heapify(deep_nums)
    return deep_nums


if __name__ == "__main__":
    random.seed(20)
    nums: list[int] = [random.randint(0, 100) for _ in range(100)]
    print(nums)
    min_heap_list: list[int] = min_heap(nums)
    max_heap_list: list[int] = max_heap(nums)
    print(min_heap_list[0])
    print(-max_heap_list[0])

    # heappush
    heapq.heappush(min_heap_list, -10)
    print(min_heap_list[0])
    heapq.heappush(max_heap_list, -101)
    print(-max_heap_list[0])

    # heappop
    heapq.heappop(min_heap_list)  # pop -10
    print(min_heap_list[0])
