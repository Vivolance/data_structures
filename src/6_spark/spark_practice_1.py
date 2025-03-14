"""
Objective:

1. Reading CSV data with Spark.
2. Data exploration and cleaning.
3. Performing transformations and aggregations.
4. Using both the DataFrame API and Spark SQL.
5. Writing the results to an output directory.
"""
import time
import pandas as pd
from pyspark.sql import SparkSession

# Setting up Spark Session (Entry Point)
spark = SparkSession.builder.appName("WorkforceEmploymentAnalysis").master("local[*]").getOrCreate()

# log
spark.sparkContext.setLogLevel("WARN")

# Define the file path
file_path: str = "src/6_spark/input/workforce_employment_dataset.csv"

# Track the time taken for spark to read csv
start_time_spark = time.time()
# Read CSV into dataframe
df_spark = spark.read.csv(file_path, header=True, inferSchema=True)
end_time_spark = time.time()
spark_time_taken = end_time_spark - start_time_spark

"""
Compare Spark read csv to Pandas read csv
"""
start_time_pandas = time.time()
df_pandas: pd.DataFrame = pd.read_csv("src/6_spark/input/workforce_employment_dataset.csv")
end_time_pandas = time.time()
pandas_time_taken = end_time_pandas - start_time_pandas
print(df_pandas.head(5))

# Print Schema
df_spark.printSchema()
# Print first 5 rows in the csv
df_spark.show(5)
# Comparison of the time taken using spark and pandas
print(f"Spark read csv time taken: {spark_time_taken}, Pandas read csv time taken: {pandas_time_taken}")

