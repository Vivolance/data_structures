"""
Show an example of how future works

A future is a promise by an API call to return the result. We do this because we may need to fire API calls in parallel,
allowing concurrent calls to be made and gathering its result at one shot. It reduces the need to fire an api call and
wait for each result to come back before firing the next. Having a future allows us to do this efficiently
"""

import asyncio
from asyncio import Future
from typing import Any


async def add(x: int, y: int) -> int:
    await asyncio.sleep(5)
    return x + y


async def main():
    """
    main thread
    """
    nums: list[int] = [1, 2, 3, 4, 5]
    futures: list[Future] = [
        asyncio.ensure_future(add(5, y=num)) for num in nums
    ]  # schedule task
    print("waiting for result")
    results: tuple[Any] = await asyncio.gather(*futures)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
