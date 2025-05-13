"""
Private attributes / methods are not to be overridden, technically there is a way but
as developers defined it as a private attr / method, we are telling others not to override it
at all.

Private attributes / methods are to prevent subclass collisions and accidental access.
"""


class Producer:
    def __init__(self):
        self._producer = "private producer"
        # name mangling to prevent clashes with subclass
        self.__producer = "secret private producer"


"""
p = Producer()
print(p._producer)  # works
print(p.__producer)  # AttributeError
# calling __producer renames it to _Classname__method = _Producer__producer
print(p._Producer__producer)  # Works but anti-pattern
"""


class BaseProducer:
    def __init__(self):
        self._producer = "Base Kafka Producer"
        self.__secret_producer = "Base Secret Producer"

    def print_producers(self):
        print("Base _producer:", self._producer)
        print("Base __secret_producer:", self.__secret_producer)


class CustomProducer(BaseProducer):
    def __init__(self):
        super().__init__()
        self._producer = "Custom Kafka Producer"  # Overrides parent _producer
        self.__secret_producer = (
            "Custom Secret Producer"  # Does not override! Creates a new one
        )


p = CustomProducer()
p.print_producers()

# Output:
# Base _producer: Custom Kafka Producer
# Base __secret_producer: Base Secret Producer
