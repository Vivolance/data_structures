"""
A lambda expression in Python is a short, anonymous function defined with the lambda keyword. Used informally to
define a throwaway function without defining using a def keyword

Key Concepts:
1. lambda arguments: expression
"""

# squaring a number
square = lambda x: x**2
print(square(5))  # Output: 25

# Using inside map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]

# sorting with a custome key
pairs = [(1, 2), (3, 1), (5, 0)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(5, 0), (3, 1), (1, 2)]
