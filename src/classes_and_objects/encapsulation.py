"""
Key Points:
1. Use private or protected attributes to prevent accidental access of
attributes outside the class
2. Python uses name mangling for __age -> _ClassName_age, so that we cant
do obj.__age and change its state easily.
"""


class Anything:
    """
    NEGATIVE EXAMPLE
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Anything2:
    """
    POSITIVE EXAMPLE
    """

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.__age = age

    def get_age(self) -> int:
        return self.__age

    def set_age(self, value: int) -> None:
        self.__age = value


if __name__ == "__main__":

    # NEGATIVE EXAMPLE
    obj = Anything("Clement", 25)
    print(obj.age)  # prints 2
    # Changes the attribute easily
    obj.age = 100
    print(obj.age)  # prints 100

    # POSITIVE EXAMPLE
    obj2 = Anything2("Clement", 25)
    # Safely accessing the age
    print(obj2.get_age())  # returns 25
    # Safely changes the age
    obj2.set_age(30)
    print(obj2.get_age())  # returns 30
