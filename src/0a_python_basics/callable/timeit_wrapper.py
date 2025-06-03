"""
A callable object in python is a function. We are now creating a function as an object, to be called
to alter logic of our code. In this example, we explore the use of the timeit function as a callable object
to other parts of your code

The timeit functions aims to time how long will the function run from start to end. This is a way of benchmarking
how this function performs.
"""


import functools
from typing import Callable, Any
from time import perf_counter


# ... means any number of params, any type
def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    # functools.wraps comprehensively ensures the new wrapped function
    # inherits all dunder attributes of the old function
    @functools.wraps(func)
    def timed_func(*args, **kwargs) -> Any:
        start_s: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_s: float = perf_counter()
        print(f"function: {func.__name__} took {end_s - start_s} s")
        return result

    return timed_func


@timeit
def loop(start: int, end: int) -> None:
    """
    Loops from start to end
    """
    for i in range(start, end + 1):
        print(i)


loop(start=1, end=100000)
