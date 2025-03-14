# Spark Notes

## Optimizations
### Why is Spark faster than Pandas in read csv?
1. Parallelism:
Spark splits the file into partitions and processes them in parallel across multiple cores (or even multiple machines in a cluster). In contrast, pandas’ read_csv typically runs in a single thread.

2. Optimized I/O:
Spark’s CSV reader is implemented in Scala/Java and benefits from the JVM’s optimizations. It can read and parse large files efficiently by using optimized I/O libraries.

3. Lazy Evaluation:
Note that Spark uses lazy evaluation. Although calling spark.read.csv creates a DataFrame immediately, the actual file reading might be deferred until an action (like show() or count()) is triggered. If you’re timing just the creation of the DataFrame, it might not be a direct one-to-one comparison with pandas.

4. Overhead Differences:
While Spark’s overhead (e.g., session initialization) can sometimes make it slower for very small datasets, when the data is sufficiently large or when parallel processing kicks in, Spark can outperform pandas.


## Local Spark VS Spark Connect
### When to use Which?
- Use Classic PySpark When:

You’re running jobs in a more traditional Spark environment where your driver and executors are co-located or tightly integrated.
You need the full breadth of Spark’s features and are comfortable with the classic execution model.
You’re writing batch jobs or simple applications that run on your local cluster or a managed Spark cluster without the need for remote interaction.

- Use Spark Connect When:

You want to decouple your client application from the Spark cluster. For example, you might build a web application or microservice that interacts with Spark remotely.
You are in an environment where you need a thin client—perhaps for better resource isolation or to enable interactive notebooks to communicate with a remote Spark service.
Your architecture benefits from a client–server approach, which can simplify cluster management, allow for better scaling of client applications, or integrate with different languages more seamlessly.
Spark connect requires grpcio, pyarrow, protobuf library