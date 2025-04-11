"""
1. List/Set/Dictionary/Generator comprehensions are faster tha for loops as it is implemented in C
2. It is a clean and concise way to create lists in Python
"""

from typing import Generator

# List Comprehension
squares_list: list[int] = [(lambda x: x**2)(x) for x in range(5)]
print(squares_list)

# Set Comprehension
squares_set: set[int] = {x for x in range(5)}
print(squares_set)

# Dict Comprehension
squares_dict: dict[int, int] = {x: x * x for x in range(5)}
print(squares_dict)

# Generator Comprehension, lazy iterator, have to iterate to get the result
squares_generator: Generator[int, None, None] = (x * x for x in range(5))
for value in squares_generator:
    print(value)
