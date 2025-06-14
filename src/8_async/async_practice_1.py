"""
Key Concepts:

1. Async architecture leverages the time used for a waiting task such as IPC, making API calls, to context switch to
other tasks
2. There is no true context switching in python as python is limited by the GIL. Async does not work for computational
tasks. Only inter process communication can leverage async in python
3.

"""

import asyncio
import time


async def brewCoffee():
    print("Start brewing coffee")
    await asyncio.sleep(2)
    print("Coffee brewing...")
    return "Coffee Served"


async def toastBread():
    print("Start toasting bread")
    await asyncio.sleep(2)
    print("Bread toasting...")
    return "Bread Toasted"


async def main():
    start_time: time = time.perf_counter()
    batch = asyncio.gather(brewCoffee(), toastBread())
    result_coffee, result_bread = await batch
    end_time: time = time.perf_counter()
    elapsed_time: time = end_time - start_time

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bread}")
    print(f"Total executed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    new_event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_event_loop)
    new_event_loop.run_until_complete(main())

    # Output: total time taken 2s, instead of 4s
