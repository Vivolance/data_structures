"""
Key Concepts:

1. Args are params passed to functions without the argument name
2. Kwargs are params passed to functions with the argument name. These have to be placed at the end of a function signature
3. args is a tuple variable, kwargs is a dictionary variable
4. Putting * at the start of a function forces user to pass in params as kwargs. def function(*, a: int, b: int)
5. * unpacks the tuple, ** unpacks the dictionary into key-value pairs
"""


def multiply(*args, **kwargs) -> int:
    print(type(args), args)
    print(type(kwargs), kwargs)
    acc: int = 1
    for arg in args:
        acc *= arg
    for key, value in kwargs.items():
        acc *= value
    return acc


if __name__ == "__main__":
    result: int = multiply(2, 3, a=4, b=2, c=1)
    print(result)
