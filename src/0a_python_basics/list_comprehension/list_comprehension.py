"""
List comprehension is another form of iterating through an iterable without using a for loop.

Key Concepts:
1. Built in C-level optimization, resulting in faster execution as C is compiled into byte code directly
2. Fewer function lookup, for example appending in a for loop, python has to constantly lookup append()
"""

import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result

    return wrapper


@timeit
def list_comprehension():
    for _ in range(10000):
        squares = [x**2 for x in range(1000)]


@timeit
def for_loop():
    for _ in range(10000):
        squares = []
        for x in range(1000):
            squares.append(x**2)


if __name__ == "__main__":
    list_comprehension()
    for_loop()

# list_comprehension took 0.323199 seconds (faster)
# for_loop took 0.345148 seconds
