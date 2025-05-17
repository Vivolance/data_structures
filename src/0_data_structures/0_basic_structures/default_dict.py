"""
A default dictionary is a dictionary that auto creates itself when a key that does not exist is passed in.
"""

from collections import defaultdict
from typing import Any

# initialise default dict, note that key is Any unless specified
my_dict: defaultdict[Any, int] = defaultdict(int)

# 1. Creating a key apple if not exist
my_dict["apple"] += 1
print(my_dict)
# output: {'apple': 1}

# 2. Word counting
words: list[str] = ["orange", "pear", "pineapple", "guava", "orange", "pear", "pear"]
for word in words:
    my_dict[word] += 1
print(my_dict)
# output : {'apple': 1, 'orange': 2, 'pear': 3, 'pineapple': 1, 'guava': 1})
