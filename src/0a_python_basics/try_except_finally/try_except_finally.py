"""
Example of how try except evaluates if used in a nested way.

Key Lesson:
1. Except blocks catches any exception raised, providing further logic to be implemented, preventing program from
crashing
2. If there is no except block, anything that is raises bubble outwards
3. Finally block may continue on from 2 if exist.
"""


class CustomError(Exception):
    pass


def tricky():
    try:
        raise CustomError("First")
    except CustomError:
        try:
            raise CustomError("Second")
        finally:
            print("Finally", end=", ")
        # this will not be reached because the error raised in the second try bubbles up
        print("End try", end=", ")
    finally:
        print("Finish", end=", ")


if __name__ == "__main__":
    tricky()
