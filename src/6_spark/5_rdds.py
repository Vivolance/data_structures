"""
Creating an RDD
"""

from typing import Optional

from pyspark import SparkContext
from pyspark.sql import SparkSession, DataFrame

spark: SparkSession = SparkSession.builder.appName("RDDExample").getOrCreate()

# 1. Create a data frame from a CSV
workforce_employment_df: DataFrame = spark.read.csv(
    "src/6_spark/input/workforce_employment_dataset.csv"
)

# Create a RDD from the df
workforce_employment_rdd = workforce_employment_df.rdd
# Using collect may cause oom error as collect loads the entire rdd into memory
# data_collected = workforce_employment_rdd.collect()
# Use take instead to show a part of the RDD, assign it to a var as Spark is lazy
results = workforce_employment_rdd.take(10)
print(results)

# 2. Create a RDD using parallelize, takes in an iterable
# Create or get a SparkContext instance
sc = SparkContext.getOrCreate()
rdd_1 = sc.parallelize([1, 2, 3, 4])


# 3. Create a rdd using a logfile as an RDD of strings. Useful for unstructured data
sc_2 = SparkContext.getOrCreate()
logs_rdd = sc_2.textFile("src/6_spark/input/custom_log.txt")


# Define a custom parsing function that extracts the error_code from each line
def parse_log_line(line):
    parts: Optional[str] = line.split("|")
    # Assume the error_code is the second element in the line
    error_code = parts[1].strip() if len(parts) > 1 else "unknown"
    # Returns a tuple with the error_code and a count of 1 for each row
    return (error_code, 1)


# Apply the function to each line, creating an RDD of (error_code, 1) pairs
error_pairs_rdd = logs_rdd.map(parse_log_line)

# Aggregate (Sum) the counts for each error code using reduceByKey
error_counts_rdd = error_pairs_rdd.reduceByKey(lambda x, y: x + y)

# Collect and print the result
print(error_counts_rdd.collect())
