"""
1. A dictionary allows you to search in O(1) time as all items in the dict are indexed

2. If a hash collision occurs, it means two keys have produced the same hash value and are vying for the same slot in
the underlying array

3. Python uses open addressing with a probing algorithm (a variant of quadratic probing with a perturbation factor).
This means that if the computed slot is already occupied, the dictionary will search for the next available slot in a
predictable sequence.

4. Unlike linear probing (which checks sequentially and can create long runs of occupied slots), quadratic probing jumps
around the table in a quadratic pattern, which helps to reduce clustering.
"""
from collections import defaultdict

my_dict: dict[str, int] = {}

my_dict["Jason"] = 1
my_dict["Clement"] = 2
my_dict["Jeff"] = 2
print(my_dict)


# Using a defaultdict, takes in a type, creates a dict based on a condition
my_list: list[int] = [10, 15, 9, 2, 19, 10, 15, 3, 2, 1, 0, 0, 10, 10]
my_dict: dict[int, int] = defaultdict(int)
for item in my_list:
    my_dict[item] += 1
print(my_dict)


