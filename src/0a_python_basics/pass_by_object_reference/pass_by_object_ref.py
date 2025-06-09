"""
Key Concepts:

1. All variables created in python are pointers to the object. The object are created as well when we do:
my_int: int = 5. 5 lives on the heap.

2. For immutable objects, everytime we create one, a new object is created on the heap.

3. For mutable objects, various references (variables) can be pointing to the same object on the heap, amending them
will amend all other references to it since they all point to the same object.

4. Python caches small integers between -5 and 256 to optimize memory and speed. This means any integer in this range
will reference the same object in memory.
"""

# Example 1
my_first_int: int = 300
my_second_int = 300
print(my_first_int is my_second_int)  # False, do this on terminal.
# Interpreter may sometimes reuse the same object in the current session of checking the above bool,
# hence returning true

# Example 2
my_first_list: list[str] = []
my_second_list: list[str] = my_first_list
my_second_list.append("1")
print(my_first_list)  # ["1"] because we are mutating the same object on the heap

# Example 3
my_dict: dict[str, set[str]] = {}
my_dict["CCK"] = set()
my_set: set[str] = my_dict["CCK"]
my_set.add("5")

print(
    my_dict["CCK"]
)  # return {"5"} because sets are mutable, hence my_set changes the value in my_dict as well
