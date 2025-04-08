"""
Key Points:
1. A lambda function is a to-go function defined as a one-liner, served to be used and throw away.
2. Lambda functions keeps the code clean and concise.
"""
from typing import Callable

my_tuple: tuple[int, int] = (10, 5)
multiply: Callable[[int, int], int] = lambda a, b: a * b
result: int = multiply(*my_tuple)
print(result)
