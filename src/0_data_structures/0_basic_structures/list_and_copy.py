"""
1. A list is a data structure that contains a series of elements. Each item in a list is a pointer to the object
on a heap.
2. The list's underlying storage is a contiguous block of memory that contains pointers to the actual objects.
This layout allows for fast indexing because the pointer to any element can be computed in constant time.
3. These references (pointers) are allocated to a memory block. When an append happens, the next reference just takes
up the next slow available in the block (O(1) time)
4. However, if a dynamic resizing were to occur due to the slots running out, the entire list of pointers will have to be
copied into another larger block of memory, potentially causing the time complexity to be O(N)

Copy:
DeepCopy - Creates an entirely new list of objects on the heap. Changing the reference to the object will not affect
other pointers.

ShallowCopy - Creates another set of references to the objects on the heap. Changing reference to the object on the heap
will cause other pointers reference to change as well.

***Note that this only applied for mutable objects within the list (for eg list[list[int]])***
"""

import copy

my_list: list[list[int]] = [[1, 2], [3, 4], [5, 6], [7, 8, 9]]
my_list.append([12, 13])
my_list.append([100])
my_list.pop()
print(my_list)

my_second_list: list[list[int]] = copy.copy(my_list)
my_second_list[0].append(99)
print(f"After appending 99 to the first inner list, my_list: {my_list}")
# affects both original list and itself
print(f"After appending 99 to the first inner list, my_second_list: {my_second_list}")

my_third_list: list[list[int]] = copy.deepcopy(my_list)
my_third_list[0].append(100)
print(f"After appending 100 to the first inner list, my_list: {my_list}")
# deep copy only changes itself, does not affect original list
print(f"After appending 100 to the first inner list, my_third_list: {my_third_list}")
