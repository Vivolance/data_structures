"""
Creating an RDD
"""
from pyspark.sql import SparkSession, DataFrame

spark: SparkSession = SparkSession.builder.appName("RDDExample").getOrCreate()

# Create a data frame from a CSV
workforce_employment_df: DataFrame = spark.read.csv("src/6_spark/input/workforce_employment_dataset.csv")

# Create a RDD from the df
workforce_employment_rdd = workforce_employment_df.rdd
# Using collect may cause oom error as collect loads the entire rdd into memory
# data_collected = workforce_employment_rdd.collect()
# Use take instead to show a part of the RDD, assign it to a var as Spark is lazy
results = workforce_employment_rdd.take(10)
print(results)
