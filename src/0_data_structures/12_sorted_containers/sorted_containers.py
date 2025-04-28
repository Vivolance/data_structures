from sortedcontainers import SortedSet, SortedList, SortedDict

"""
Sorted Containers
1. sorted dicts
2. sorted set
3. sorted list

This allows us to create sorted data structures.
"""


# Sorted Sets
sorted_set: SortedSet = SortedSet()
sorted_set.add(100)
sorted_set.add(100)
sorted_set.add(101)

for item in sorted_set:
    print(item)
    # returns 100, 101


# Sorted List
# Creation
my_list: list[int] = [1, 2, 2, 2, 3, 4]
sorted_list: SortedList = SortedList(my_list)

# gets the next position where 2 is supposed to be added
bisect_right_2: int = sorted_list.bisect_right(2)
print(bisect_right_2)  # output: 4

# gets the next position where 2 is supposed to be added
bisect_left_2: int = sorted_list.bisect_left(2)
print(bisect_left_2)  # output: 1


# Sorted Dict
# Creation
sd = SortedDict()
sd["banana"] = 3
sd["apple"] = 5
sd["cherry"] = 2

print(sd)  # SortedDict({'apple': 5, 'banana': 3, 'cherry': 2})
print(list(sd.keys()))  # ['apple', 'banana', 'cherry']
print(list(sd.values()))  # [5, 3, 2]
print(list(sd.items()))  # [('apple', 5), ('banana', 3), ('cherry', 2)]
print(sd.bisect_left("blueberry"))  # 2 (after 'banana')
