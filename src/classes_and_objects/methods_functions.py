"""
Key Points:
1. A function is a set of logic applied to the input parameters and returns or transforms the object
2. A method, similar to function, the only difference is that it is defined within a class
3. Functions/Methods in Python are also objects, they are of type Callable
"""


# A function
def multiply(a: int, b: int):
    return a * b


class Multiplication:
    # A method
    def mutiple(self, a: int, b: int) -> int:
        return a * b
