"""
A generator is a lazy iterator which yields all result inside it. It is efficient as it does not yet consume memory
The list is only realised when we do next() or we iterate through it, yielding a result one by one. Only when the
generator is iterated through will then be the object be realised.

Key Concepts:

1. yield passes a value to the caller, without terminating the function
2. next() calls the generator's implementation until the yield, yielding once, then pauses
3. send() resumes where you left off by sending a new value into the assignment, (or primes the generator if at the
beginning), then yield once and pauses
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
