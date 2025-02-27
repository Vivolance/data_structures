"""
Create a min heap and max heap with the following methods:
- heappop -> remove top item from the heap
- heappush -> append an item to the heap
- heapify -> create a min/max heap
- top -> display the top most item
"""
import copy
import heapq
import random


def min_heap(my_list: list[int]) -> list[int]:
    deep_nums: list[int] = copy.deepcopy(my_list)
    heapq.heapify(deep_nums)
    return deep_nums


def max_heap(my_list: list[int]) -> list[int]:
    deep_nums: list[int] = [-num for num in my_list]
    heapq.heapify(deep_nums)
    final_list: list[int] = [-num for num in deep_nums]
    return final_list


if __name__ == "__main__":
    random.seed(20)
    nums: list[int] = [random.randint(0, 100) for _ in range(100)]
    print(nums)
    min_heap_list: list[int] = min_heap(nums)
    max_heap_list: list[int] = max_heap(nums)
    print(min_heap_list[0])
    print(max_heap_list[0])








