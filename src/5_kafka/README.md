# Kafka Concepts:

## Introduction
- Kafka is a distributed message queue system across multiple kafka servers. Each server has its own CPU and RAM,
allowing equal distribution of workload and message streaming, making Kafka scalable. 
- A Kafka cluster contains of multiple servers
- Message Queue -> It is a queue containing messages
- These messages are defined by you as a user, and it can be anything, typically in a JSON format


## Key Points
1. A topic can be consumed by multiple consumers, but the consumers cannot be from the same consumer group
2. Multiple consumers from different consumer groups can consume form the same topic