"""
Key Concepts:

1. All variables created in python are pointers to the object. The object are created as well when we do:
my_int: int = 5. 5 lives on the heap.

2. For immutable objects, everytime we create one, a new object is created on the heap.

3. For mutable objects, various references (variables) can be pointing to the same object on the heap, amending them
will amend all other references to it since the they all point to the same object.

4. In Python, the integers -5 to 256 are considered global objects, meaning if we have 2 difference references pointing
to the same number between this range, they are pointing to the same object (i.e behaves like mutable objects)
"""


# Example 1
my_first_int: int = 300
my_second_int = 300
print(my_first_int is my_second_int)    # False, do this on terminal. Pycharm has some functionalities that returns True

# Example 2
my_first_list: list[str] = []
my_second_list: list[str] = my_first_list
my_second_list.append("1")
print(my_first_list)    # ["1"] because we are mutating the same object on the heap

