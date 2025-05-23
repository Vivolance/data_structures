# Concepts on Databricks

## Introduction
Historically, we use data lakes (e.g S3) for storing raw unstructured data. Data lakes are great for their flexibiity and support
of all data types, but do not have great performance and can often become messy.

This prompted the birth of a new architectural design called the Lake House. Lake house builds on top of the data lake,
giving your architecture more flexibility for all data types and workloads while getting better performance and
governance benefits from the data warehouse design.

Databricks provides a single platform that can deliver the lakehouse architecture simply and at scale, allowing data
teams that can deliver every use case on any dataset without having to worry about how to manage these different tech
stacks.

## Components
1. Workspaces
Unified user interface for development. An overview of all components.

2. Clusters
Cluster management for distributed frameworks such as Spark

3. Notebooks
Similar to Jupyter notebooks, an interactive environment for you to do development work, support multiple languages,
great for prototyping

4. Jobs
Schedule automate, autoscaling of jobs, or workflows

5. Databricks SQL/Lakehouse/Delta Lake
- SQL -> Query layer for BI, dashboards
- Delta Lake -> Transactional storage layers that adds ACID, schema enforcement and time travel to cloud object storage
(parquet)
- Lakehouse -> Unified analytics architecture combining data lake flexibility with data warehouse performance

6. Data Management and Flow
Tables, database, schemas, used for organizing, securing, and discovering data essential for both compliance and
productivity