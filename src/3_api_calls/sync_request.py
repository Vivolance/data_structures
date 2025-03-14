"""
Demonstration of how to make a synchronous api call with request library.
"""

import time

import requests
import logging
from retry import retry

logger: logging.Logger = logging.Logger(__name__)
# your logging output
handler: logging.Handler = logging.StreamHandler()
# create a formatter to set the format of your logs
formatter: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


@retry(
    exceptions=requests.HTTPError,
    tries=5,
    delay=0.01,
    jitter=(-0.01, 0.01),
    max_delay=0.05,
    backoff=2,
)
def sync_request(url: str) -> str:
    try:
        response: requests.Response = requests.get(url)
        response_text: str = response.text
        return response_text
    except requests.HTTPError as e:
        logger.error(e)
        raise e


if __name__ == "__main__":
    url: str = "https://api.coingecko.com/api/v3/coins/list"
    start_time = time.time()  # Record the start time
    coin_gecko_response: str = sync_request(url)
    end_time = time.time()  # Record the start time
    print(coin_gecko_response)
    print(f"Execution time: {end_time - start_time} seconds")
    # print general information about the response
    # logger.info(coin_gecko_response)
