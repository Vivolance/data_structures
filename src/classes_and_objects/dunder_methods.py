"""
Dunder methods are special methods in Python that does an action upon calling the,. They are set default by Python.

1. __init__ -> Automatically called as a constructor when an object is initialized

2. __str__ -> Gives a string representation when calling print(), pretty version of __repr__

3. __repr__ -> Python falls back to this when __str__ is not defined, printing an actual representation of the object,
typically used by developers when debugging

4. __add__ -> Called when '+' is called

5. __getitem__ -> Called when you access an element by its key

6. __iter__ -> Called when you do a for loop

7. __name__ -> Used on functions/classes/modules to get their name, when running a python file
__name__ is automatically set to "__main__".

8. __main__ -> A special value that is assigned to __name__ when a file is run directly

9. __enter__/__aenter -> Called at the start when with is called. Enter a context manager

10. __exit__/__aexit__ Called at the end of a with block to exit and close the context managers
"""
