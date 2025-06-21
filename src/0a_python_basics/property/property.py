"""
Key Concepts:
1. A property is a function that behaves like an attribute. The only difference is that it allows you to implement
certain logic before returning the attribute to when you call it.
2. Used when you create a class with various attributes and the attributes are internally linked to one another such
that changing one affects the other, consider using property
"""


# Bad example, when you update length, self._area is not updated
class Square:
    def __init__(self, length: int) -> None:
        self.length = length
        self.area = length ** 2


# Good example, when you update length, area is changed automatically when you call it:
class Square2:
    def __init__(self, length: int) -> None:
        self.length = length

    @property
    def area(self) -> int:
        return self.length ** 2


if __name__ == "__main__":
    square_1: Square = Square(5)
    print(square_1.area)   # 25
    square_1.length = 10   # update length
    print(square_1.area)   # still 25

    square_2: Square2 = Square2(5)
    print(square_2.area)    # 25
    square_2.length = 10    # update length
    print(square_2.area)    # changed to 100
