"""
Demonstration of how to make an asynchronous api call with aiohttp library.
"""

import asyncio
import logging
import time

import aiohttp
from tenacity import retry, wait_fixed, stop_after_attempt

logger: logging.Logger = logging.Logger(__name__)
handler: logging.Handler = logging.StreamHandler()
formatter: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


@retry(
    wait=wait_fixed(0.01),  # ~10ms between attempts
    stop=stop_after_attempt(5),  # 5 retries
    reraise=True,  # re-raise last exception if all retries fail
)
async def async_request(url: str) -> str:
    headers: dict[str, str] = {
        "accept": "application/json",
    }
    params: dict[str, str] = {
        "include_platform": "True",
    }
    try:
        async with aiohttp.ClientSession() as sess:
            async with sess.get(
                url, headers=headers, params=params, ssl=False
            ) as response:
                if response.status == 200:
                    response_text: str = await response.text()
                    return response_text
                else:
                    logger.error(f"Encountered status code: {response.status}")
                    return ""
    except aiohttp.ClientError as e:
        logger.error(f"Failed with {e}")
        raise e


if __name__ == "__main__":
    url: str = "https://api.coingecko.com/api/v3/coins/list"
    event_loop = asyncio.new_event_loop()
    start_time = time.time()  # Record the start time
    response: str = event_loop.run_until_complete(async_request(url))
    end_time = time.time()  # Record the start time
    print(response)
    print(f"Execution time: {end_time - start_time} seconds")
    # logger.info(response)
