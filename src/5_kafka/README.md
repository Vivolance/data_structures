# Kafka Concepts:

## Introduction
### Concept 1:
- Kafka is a distributed message queue system across multiple kafka servers. Each server has its own CPU and RAM,
allowing equal distribution of workload and message streaming, making Kafka scalable. 
- A Kafka cluster contains of multiple servers
- Message Queue -> It is a queue containing messages
- These messages are defined by you as a user, and it can be anything, typically in a JSON format

### Concept 2: Kafka is append-only
- Any messages you add to the message queue, you can't delete as an operation
- A computer chunks your RAM into blocks. We call these pages of memory
- Kafka is designed like this, so it is fast; no need to skip memory pages -> Sequential I/O


### Concept 3: Kafka is for high-throughput, low-latency event-driven data pipelines. Zero Copy principle
- high-throughput -> can let hundreds of thousands, if not more, messages to be passed through kafka at a time
- low-latency -> the time taken to consume (read from kafka) or produce (insert into kafka) a message is very fast
- event-driven -> kafka is used to store event data, which is listened to by your software to process

## Key Points
1. A topic can be consumed by multiple consumers, but the consumers cannot be from the same consumer group
2. Multiple consumers from different consumer groups can consume form the same topic
3. Kafka is efficient as a real time event bus because it can handle upstream loads and downstream loads in a balanced
manner. This prevents the downstream from hyperventilating should there be a sudden surge in messages produced.
4. Kafka is a distributed real time streaming server as it allows workload to be distributed across clusters. a group of
brokers make a kafka cluster, each having its CPU and RAM. This allows Kafka to be scaled horizontally.
5. Kafka is quick due to its zero copy principle. It skips the copying of data from the ram to the application buffer and
to the socket, allowing data to directly load from the RAM buffer into the NIC buffer. Reducing the overhead required
for copying.