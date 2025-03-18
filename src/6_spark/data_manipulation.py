"""
Spark DataFrame API for data manipulation
"""

from typing import Any

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Create a Spark session
spark = SparkSession.builder.appName("data_manipulation").getOrCreate()

data: list[dict[str, Any]] = [
    {"name": "elson", "age": 24, "country": None},
    {"name": "clement", "age": 34, "country": "Singapore"},
    {"name": "joyce", "age": None, "country": "Malaysia"},
]
# 1. Handling missing data

# Create a DataFrame from the list of dictionaries
# type checker sound off, but a list[dict] is a valid input type for creteDataFrame()
df = spark.createDataFrame(data)

# Use .na.drop() to remove rows with null values
# Drop rows with any nulls
df_cleaned = df.na.drop()
df_cleaned.show()

# Filter out nulls for a specific column
df_filtered = df_cleaned.where(col("country").isNotNull())
df_filtered.show()

# Use .na.fill({"column": value}) to replace nulls with a specific value
# Fill nulls in the 'age' column with the value 0
df_filled = df.na.fill({"age": 0, "country": "No Citizen"})
df_filled.show()
