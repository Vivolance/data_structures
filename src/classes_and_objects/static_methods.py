"""
Key Points:
1. A static method do not require an instance of the class to be created to be called

2. Used when the logic do not need to access the state of the object.

3. Great when it is just a piece of logic unrealted to the state of the class
"""


class MathUtils:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b


if __name__ == "__main__":
    # Does not require my_math_utils = MathUtils()
    print(MathUtils.multiply(3, 5))
