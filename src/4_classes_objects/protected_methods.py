"""
What are private methods / attributes?

Private attributes / methods are meant to be used within a class only.

Lesson: Only override protected methods/attributes in subclasses and if you are intentional
"""

import confluent_kafka


class Producer:
    def __init__(self, config: dict[str, str]):
        self._producer = confluent_kafka.Producer(config)
        self._topic: str = "raw_search_results"

    # Valid use of self._producer and self._topic within the Producer class
    def send(self, message: str):
        self._producer.produce(topic=self._topic, value=message)


# Technically possible, but not recommended as invalid usage outside class
config: dict[str, str] = {"example": "config"}
p = Producer(config)
p._topic = "raw_search_results"


# if want to use outside class make it non-private instead:
class Producer2:
    def __init__(self, config2: dict[str, str]):
        self.producer = confluent_kafka.Producer(config2)
        self.topic: str = "raw_search_results"
