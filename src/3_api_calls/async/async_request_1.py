import asyncio
import logging

import aiohttp
from tenacity import retry, wait_fixed, stop_after_attempt

# creates the logger object, with the current file name as its name
logger: logging.Logger = logging.Logger(__name__)
# allows log to be stream in the console
handler: logging.Handler = logging.StreamHandler()
# defines the structure of the log
# example output: 2025-06-26 21:45:00,123 - INFO - Starting application...
formatter: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


@retry(wait=wait_fixed(0.01), stop=stop_after_attempt(5), reraise=True)
async def async_request(url: str) -> str:
    headers: dict[str, str] = {"accept": "application/json"}
    params: dict[str, str] = {"include_platform": "True"}
    try:
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    response_text: str = await response.text()
                    return response_text
                else:
                    logger.error(
                        f"Encountered non 200 status, status code: {response.status}"
                    )
                    return ""
    except aiohttp.ClientError as e:
        logger.error(f"failed with {e}")
        raise e


if __name__ == "__main__":
    url: str = "https://api.coingecko.com/api/v3/coins/list"
    event_loop = asyncio.new_event_loop()
    response: str = event_loop.run_until_complete(async_request(url))
    print(response)
