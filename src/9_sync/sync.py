"""
Key Concepts:

1. Synchronous is the default architecture of all scripts. The main script runs as one single main thread. Tasks are
executed sequentially by lines
"""

import time


def brew_coffee() -> str:
    print("Start brewing coffee")
    time.sleep(2)
    print("Coffee brewing...")
    return "Coffee Served"


def toast_bread() -> str:
    print("Start toasting bread")
    time.sleep(2)
    print("Bread toasting...")
    return "Bread Toasted"


def main() -> str:
    start_time = time.perf_counter()
    result_coffee: str = brew_coffee()
    print(result_coffee)
    result_bread: str = toast_bread()
    print(result_bread)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return f"Total time taken = {elapsed_time}"


if __name__ == "__main__":
    print(main())

    # Output = ~4s because they run synchronously
