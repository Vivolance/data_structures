"""
Key concepts:

1. Functions are objects in python as well, they are called Callables.
2. We can create a function as an object, and then use this function to wrap around other functions, to modify
its behaviour. One such useful case is to time the execution of a function]
3. @functools.wraps allow us to comprehensively ensures the wrapped function inherits all dunder attributes of the old
function
"""

import functools
import time
from typing import Any, Callable


def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    # func refers to the function you want to wrap around
    @functools.wraps(func)
    def timed_function(*args, **kwargs) -> Any:
        start_s: float = time.perf_counter()
        # call the actual func here
        result: Any = func(*args, **kwargs)
        end_s: float = time.perf_counter()
        print(f"function: {func.__name__} took {end_s - start_s} s")
        return result

    return timed_function


@timeit
def loop(start: int, end: int) -> None:
    for i in range(start, end):
        print(i)


if __name__ == "__main__":
    loop(start=0, end=99999)
