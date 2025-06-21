"""
For @property, when you call the function, it runs and returns a value. It returns a value everytime you call it

Key Concepts:
1. Cached property allows you to cache the result of the first run
2. The function is not re-executed unless you manually clear the cache or make a new instance.
3. Typically used when calculating this is expensive and should only be calculated when something affecting it changes
"""

from functools import cached_property


class Square:
    def __init__(self, length: int):
        self._length = length

    @cached_property
    def area(self):
        print("Calculating area...")
        return self._length**2

    @property
    def no_cache_area(self):
        print("Calculating area...")
        return self._length**2


if __name__ == "__main__":
    sq = Square(3)
    print(sq.no_cache_area)  # ÆCalculating area..." is printed
    print(sq.no_cache_area)  # "Calculating area..." is printed again

    print(sq.area)  # prints "Calculating area..." and 9
    print(sq.area)  # prints just 9 (no "Calculating..." — value is cached)
