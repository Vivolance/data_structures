"""
Key Points:
1. A wrapper function is a function that modifies the behaviour of another function
"""

import functools
from typing import Callable, Any


def wrapper_function(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def modify_func(*args, **kwargs) -> Any:
        print("This is happening BEFORE the actual function")
        func(*args, **kwargs)
        print("This is happening AFTER the actual function")
        return

    return modify_func


@wrapper_function
def greeting(name: str) -> None:
    print(f"Hello {name} !")


if __name__ == "__main__":
    print(greeting("Elson"))
