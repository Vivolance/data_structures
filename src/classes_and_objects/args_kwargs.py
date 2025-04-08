"""
Key Points:
1. *args represents  any number of arguments. Arguments are passed in as a tuple
2. **kwargs represents any number of keyword arguments, Arguments are passed in as a dictionary
3. Kwargs serve as a clearer illustration, allowing the user to know what is exactly being passed in, for eg
age=2, letting the user now that 2 is an age
4. You can use * and ** to unpack tuple and dicts
"""
from typing import Any


def multiply(*args, **kwargs) -> int:
    """
    Allows the user to pass in any number of arguments and keyword arguments
    """
    acc: int = 1
    for arg in args:
        acc *= arg
    for key, value in kwargs.items():
        acc *= value

    return acc


def addition(*, a: int, b: int) -> int:
    """
    Forces the developer to indicated a and b as keyword arguments
    """
    return a + b


def unpacking_vars(name: str, age: int) -> str:
    return f"My name is {name} and my age is {age}"


if __name__ == "__main__":
    # Allows you to have the choice of passing or not passing in args or kwargs
    print(multiply(2, 3, 4))
    print(multiply(2, 3, 4, a=2, b=3))
    print(addition(a=2, b=3))
    # Error:
    # print(addition(2, c=3))

    my_details: tuple[str, int] = ("Elson", 30)
    my_details_keyword: dict[str, Any] = {"name": "Clement", "age" : 29}
    print(unpacking_vars(*my_details))
    print(unpacking_vars(**my_details_keyword))
