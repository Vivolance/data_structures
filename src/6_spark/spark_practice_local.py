"""
Objective:
Create a LOCAL spark mode, used for testing functionalities, learning spark technicals

1. Reading CSV data with Spark.
2. Data exploration and cleaning.
3. Performing transformations and aggregations.
4. Using both the DataFrame API and Spark SQL.
5. Writing the results to an output directory.
"""

import time
import pandas as pd
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import avg, regexp_replace

# Setting up Spark Session (Entry Point)
spark = (
    SparkSession.builder.appName("WorkforceEmploymentAnalysis")
    # This states that this is running on local, if changed to a distributed env, use "yarn"
    .master("local[*]")
    .getOrCreate()
)

# set log level to WARN
spark.sparkContext.setLogLevel("WARN")

# Define the file path
file_path: str = "src/6_spark/input/workforce_employment_dataset.csv"

# Track the time taken for spark to read csv
start_time_spark: float = time.time()
# Read CSV into dataframe
df_spark: DataFrame = spark.read.csv(file_path, header=True, inferSchema=True)
end_time_spark: float = time.time()
spark_time_taken: float = end_time_spark - start_time_spark

"""
Compare Spark read csv to Pandas read csv
"""
start_time_pandas: float = time.time()
df_pandas: pd.DataFrame = pd.read_csv(
    "src/6_spark/input/workforce_employment_dataset.csv"
)
end_time_pandas: float = time.time()
pandas_time_taken: float = end_time_pandas - start_time_pandas
print(df_pandas.head(5))

# Print Schema (Columns)
df_spark.printSchema()
# Print first 5 rows in the csv
df_spark.show(5)
# Comparison of the time taken using spark and pandas
print(
    f"Spark read csv time taken: {spark_time_taken}, Pandas read csv time taken: {pandas_time_taken}"
)

"""
Case 1: using DataFrame API
"""

# Changing str type to double type in Base Column for aggregation
df_spark_clean = df_spark.withColumn(
    "Base Salary", regexp_replace(df_spark["Base Salary"], "[$,]", "").cast("double")
)

# Aggregation using DataFrame API, average Base Salary
avg_df_spark: DataFrame = df_spark_clean.groupby("Company Name").agg(avg("Base Salary"))
avg_df_spark.show(50)


"""
Case 2: Using Spark SQL

# Convert "Base Salary" from string to double
df_spark_clean = df_spark.withColumn(
    "Base Salary", regexp_replace(df_spark["Base Salary"], "[$,]", "").cast("double")
)

# Create a temporary view from the cleaned DataFrame
df_spark_clean.createOrReplaceTempView("company_data")

# Use Spark SQL to compute the average Base Salary by Company Name
avg_df_spark_sql = spark.sql("
    SELECT `Company Name`, AVG(`Base Salary`) AS avg_base_salary
    FROM company_data
    GROUP BY `Company Name`
")
"""
