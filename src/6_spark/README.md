# Spark Notes

## Spark Concepts
### 1. Spark Session
The main entry point of Spark. To create a spark session to begin ingesting data and execute data manipulation, always begin with
a Spark Session

```python
from pyspark.sql import SparkSession, DataFrame


spark = spark.builder.appName("MySparkSession").getOrCreate()

# set log level to WARN
spark.sparkContext.setLogLevel("WARN")
```

### 2. Spark DataFrames
Similar to Pandas, Spark has its own data frames which wraps table like data into a DataFrame type, allowing data manipulation
to be done on it. Note that Spark DataFrames are immutable, which means we cannot modify the DataFrame in place, but only
create a new DataFrame whenever we execute an operation to it.

#### Useful functions on DataFrames
1. .agg("column_name", "max") Takes in a dict of column, function. Aggregate the max for each group
- Other functions include, avg, sum, count, variance, first, last etc
2. .groubpy("column_name") -> Group by a certain column
3. .describe().show() -> Describe to show an additional column of the count, std dev, sum etc.
4. .cast("int") -> Cast columns into other types used for aggregation
```python
df = df.withColumn("Salary", df["Salary"].cast("int"))
```
5. .filter(df.column_name == "some_conditions") -> Filter a column by certain conditions

To create a DataFrame:
```python
schema = StructType(
    [
        StructField("id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("country", StringType(), True),
    ]
)

data: list[dict[str, Any]] = [
    {"name": "elson", "age": 24, "country": None},
    {"name": "clement", "age": 34, "country": "Singapore"},
    {"name": "joyce", "age": None, "country": "Malaysia"},
]
# 1. Handling missing data

# Create a DataFrame from the list of dictionaries
# type checker sound off, but a list[dict] is a valid input type for creteDataFrame()
df = spark.createDataFrame(data, schema)
```

### 3. RDDs
RDDs are core building block of Spark. It represents a distributed collection of data across a cluster. RDDs allow fast data access
and analysis while DataFrames offer great user-friendliness due to simpler syntax and commands, though they can be slower.
RDDs are immutable, meaning once created, they cannot be changed
- Low-level more flexible but require more code for complex operations
- Type Safe, preserve data types
- No schema, harder to work with when dealing with structured data
- Large Scaling
- Extremely verbose, poor at analytics
- Best to use lambda functions on RDD

#### Useful functions
1. map() -> applies functions (including lambda functions) across EVERY element or row in the RDD, creating a new RDD
where each element is the result of that function applied to the corresponding row.
```python
# EG. 1 Maps the rdd into a tuple of (Department, Salary)
rdd.map(lambda row: (row["Department"], row["Salary"]))

# E.G 2 Groups all value sby key, then adding the 2 numbers
rdd_aggregated = rdd.reduceByKey(lambda x, y: x + y)
```
2. collect() -> collects data from across the cluster like rdd.collect()

```python
from pyspark.sql import SparkSession, DataFrame

spark: SparkSession = SparkSession.builder.appName("RDDExample").getOrCreate()

# Create a data frame from a CSV
workforce_employment_df: DataFrame = spark.read.csv("src/6_spark/input/workforce_employment_dataset.csv")

# Create a RDD from the df
workforce_employment_rdd = workforce_employment_df.rdd
```

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

### Why is Spark faster than Pandas in read csv?
1. Parallelism:
Spark splits the file into partitions and processes them in parallel across multiple cores (or even multiple machines in a cluster). In contrast, pandas’ read_csv typically runs in a single thread.

2. Optimized I/O:
Spark’s CSV reader is implemented in Scala/Java and benefits from the JVM’s optimizations. It can read and parse large files efficiently by using optimized I/O libraries.

3. Lazy Evaluation:
Note that Spark uses lazy evaluation. Although calling spark.read.csv creates a DataFrame immediately, the actual file reading might be deferred until an action (like show() or count()) is triggered. If you’re timing just the creation of the DataFrame, it might not be a direct one-to-one comparison with pandas.

4. Overhead Differences:
While Spark’s overhead (e.g., session initialization) can sometimes make it slower for very small datasets, when the data is sufficiently large or when parallel processing kicks in, Spark can outperform pandas.

## User Defined Functions
Custom function to work with data using PySpark DataFrames. They are very useful in Spark when you need to apply
custom logic that isn’t available in Spark’s built-in functions. They let you write your own transformations in Python
(or Scala/Java) and apply them to each row of a DataFrame.

1. Flexibility vs. Performance:
UDFs provide flexibility to handle complex transformations, but they tend to be slower than native Spark SQL functions. This is because they run outside of the Catalyst optimizer and don't benefit from Tungsten's optimizations.

2. Optimization Limitations:
Built-in functions are highly optimized and can be automatically inlined or vectorized. UDFs, on the other hand, are treated as black boxes during query optimization, which can hinder performance.

3. When to Use UDFs:
Use UDFs when there's no built-in function that meets your needs. If possible, try to use Spark SQL functions or DataFrame operations, which are generally more efficient.

### Pandas UDFs Optimizations (Why is Pandas UDFs faster for large datasets)
1. Reduced Python Overhead:
Traditional PySpark UDFs execute Python code row by row, which introduces significant overhead when processing large datasets. Pandas UDFs, on the other hand, process data in batches (Pandas Series or DataFrames) and leverage highly optimized vectorized operations in Pandas and NumPy.

2. Leverage Apache Arrow:
Pandas UDFs use Apache Arrow to efficiently convert data between the JVM and Python processes. This minimizes serialization/deserialization overhead, speeding up data transfer significantly.

3. Better Performance:
By working on batches, Pandas UDFs can utilize C-optimized libraries under the hood, leading to orders-of-magnitude improvements in performance compared to row-at-a-time UDFs.

4. Optimized Memory Usage:
Processing data in vectorized form is generally more memory efficient and takes better advantage of modern CPU architectures.

### When to use Pandas UDFs VS PySpark UDFs

#### Use Pandas UDFs when
- For large datasets
- Complex operations beyond simple data cleaning
- Specific row level changes over column level
- Can be called outside SparkSession

#### Use PySpark UDFs when
- For small datasets
- Simple transformations like data cleaning
- Changes at columnar level, not row level
- Must be registered to a SparkSession with UDFs

## Spark SQL
1. Module in Apache Spark for structured data processing
2. Allows us to run SQL queries alongside data processing tasks
3. Seamless combination of Python and SQL in one application
4. DataFrame Interfacing, provides programmatic access to structured data

### Temp Views
Temporary Views are the entry point for using SQL for data manipulation
```python
df.createOrReplaceTempView("table_view_name")
```
The view protects the underlying data while doing analytics. They are immediately destroyed when the session ends.

### Combining SQL and DataFrame Operations
```python
# SQL query result
query_result = spark.sql("SELECT Name, Salary FROM employees WHERE Salary > 3000")

# DataFrame transformation
high_earners = query_result.withColumn("Bonus", query_result.Salary * 0.1)
high_earners.show()
```

## Optimizations
### Best Practices for PySpark Aggregations
- Filter early to reduce data size before performing aggregations
- Handle data type: ensure data is clean and correctly types
- Avoid repeated operations that uses the entire dataset, minimize operations such as groupBy()
- Choose the right interface, prefer DataFrames due to their optimizations
- Monitor performance: Use explain() to inspect the execution plan and optimize accordingly

### Broadcast
To use all compute for smaller tasks
- Broadcast Joins to use all compute, even on smaller datasets
- When you broadcast a variable, Spark sends it once to each executor rather than shipping it with every single task. 
This minimizes network I/O and reduces overhead, especially in operations like joins where one dataset is small enough to broadcast.
- Reducing Data Shuffles:
In distributed operations, frequently transferring the same data between nodes can slow down performance. 
By broadcasting that data, every node can access the copy locally, thereby reducing the need to shuffle data around.

### Explain
The explain method allows us to view the execution plan of a physical query. This allows us to see the sequence the query
is executed at a more granular level, allowing developers to spot inefficiencies. As a rule of thumb,
store intermediate results and avoid using collect() or show() (Action queries) unless required.
```python
# Use explain() to view execution plans
df.filter(df.Age > 30).select("Name").explain()

# == Physical Plan ==
# *(1) Filter (isnotNull(Age) AND (Age > 30))
# +- Scan ExistingRDD[Name: String, Age: Int]
```

### Caching and Persisting
#### Caching
Stores data in memory for faster in memory processing for smaller datasets. 
Caching is lazy, only triggered when we call an action call ike show(), count(). 
As a rule of thumb:
1. Cache expensive operations such as joins or orderBy
2. Cache only if you are performing other transformations ont he datasets
```python
# Suppose df_features is the result of expensive feature engineering
df_features = raw_df.filter("age is not null").withColumn("normalized_salary", col("salary")/1000)

# Cache the DataFrame because it will be used in multiple iterations of a training loop
df_features.cache()
df_features.count()  # Triggers caching

for i in range(10):
    # Perform an iterative step, e.g., re-compute an aggregation or join using df_features
    result = df_features.groupBy("occupation").agg(avg("normalized_salary").alias("avg_salary"))
    result.show()
```

#### Persist
Stores data in different storage levels for larger datasets. Spark stores the overflow memory in disk.
Persist is a lower level cache() where it allows you to define the storage level.
```python
from pyspark import StorageLevel

df.persist(StorageLevel.MEMORY_AND_DISK)

# Perform Transformations
result = df.groupBy("column3").agg({"column4": "sum"})
result.show()

# Unpersist after use, to free up memory
df.unpersist()
```
