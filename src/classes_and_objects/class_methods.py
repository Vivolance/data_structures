"""
Key Points:
1. Class methods act as alternative constructor of the class. It allows you
to predefine an object of certain inputs so as to allow users of the class to create
this specific type of object easily.
"""


class Pizza:
    def __init__(self, ingredients: list[str]):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["cheese", "tomato"])

    @classmethod
    def pepperoni(cls):
        return cls(["cheese", "tomato", "pepperoni"])


if __name__ == "__main__":
    pizza1: Pizza = Pizza.margherita()
    pizza2: Pizza = Pizza.pepperoni()

    # As oppose to doing it like this:
    pizza3: Pizza = Pizza(["cheese", "tomato"])
    pizza4: Pizza = Pizza(["cheese", "tomato", "pepperoni"])
