"""
Building on top of previous lesson, this lesson demonstrates how to use yield with an assignment, allowing the caller
to send in a value to the generator

Key Concepts:
1. Generator logic pauses at yield keyword
2. calling next() realises the yield content and resumes the code
3. calling .send() sends a value into the assigned var to the yield content, as well as resuming the code up until it
yielded once.
"""

import time
from typing import Generator


def my_generator() -> Generator[int, int | None, int]:
    """
    A generator that gives back 1, then double everytime you send in a value
    """
    starting_value: int = 1
    while True:
        time.sleep(1)
        print("Generator is on")
        received: int = yield starting_value
        print(f"Generator receives value: {received}")
        if received:
            starting_value = received * 2
        else:
            starting_value = 1


if __name__ == "__main__":
    my_gen: Generator[int, int | None, int] = my_generator()
    value: int = my_gen.send(None)
    print(f"Caller receives: {value}")
    value = my_gen.send(10)  # sends 10 to received, resumes
    print(f"Caller received: {value}")

    # Output:
    # >>> Generator is on
    # >>> Caller receives 1
    # >>> Generator receives value: 10
    # >>> Generator is on
    # >>> Caller received: 20
