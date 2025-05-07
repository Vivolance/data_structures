"""
Define a generator and its use case.

A generator is a lazy iterator which yields all result inside it. It is efficient as it does not yet consume memory
The list is only realised when we do next or we iterate through it, yielding a result one by one. Only when the
generator is iterated through will then be the object be realised.
"""


def countdown(n: int) -> str:
    while n > 0:
        yield n
        n -= 1
    yield "Lift off!"


if __name__ == "__main__":
    for num in countdown(10):
        if num == 5:
            # additional logic here, allows user to control the iterator with other logic
            print("halfway there!")
        print(num)
