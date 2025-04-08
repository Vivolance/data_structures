"""
Key Points:
1. Method Resolution Order is the order of how python looks for methods
or attributes when you access them on a class instance.
2. Important when dealing with multiple inheritance of a class from parents classes
"""


class A:
    def greet(self) -> None:
        print("Hello from A")


class B:
    def greet(self) -> None:
        print("Hello from B")


class C(A, B):
    pass


if __name__ == "__main__":
    class_c: C = C()
    print(class_c.greet())
    # Prints the order of resolution
    print(C.__mro__)
