"""
Advanced dataframe operations such as:
1. Joins
2. Arrays and Maps
"""


from typing import Any

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, array, lit
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, MapType

# Create a Spark session
spark = SparkSession.builder.appName("advanced_dataframe_operations").getOrCreate()

# Define an explicit schema with the desired column order, if this is not defined,
# spark create dataframe will not guarantee specific order
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("country", StringType(), True)
])

user_data: list[dict[str, Any]] = [
    {"id": 1, "name": "elson", "age": 24, "country": None},
    {"id": 2, "name": "clement", "age": 34, "country": "Singapore"},
    {"id": 3, "name": "joyce", "age": None, "country": "Malaysia"},
]

user_data_2: list[dict[str, Any]] = [
    {"id": 4, "name": "john", "age": 72, "country": "USA"},
    {"id": 5, "name": "Judy", "age": 44, "country": "Holland"},
]

jobs_data: list[dict[str, Any]] = [
    {"id": 1, "occupation": "professor"},
    {"id": 2, "occupation": "teacher"},
    {"id": 3, "occupation": "student"},
    {"id": 4, "occupation": "engineer"}
]

# Create a spark dataframe from raw data
user_df = spark.createDataFrame(user_data, schema)
user_df_2 = spark.createDataFrame(user_data_2, schema)
jobs_df = spark.createDataFrame(jobs_data)

# 1. Joining on id column using inner join. (left, right)
df_joined: DataFrame = user_df.join(jobs_df, on="id", how="inner")
df_joined.show()

# 2. Union of 2 dataframes with similar schemas
df_union = user_df.union(user_df_2)
df_union.show()

# 3. Handling complex nested data (Arrays and Maps)
# Create and array column
df_with_array = user_df.withColumn("scores", array(lit(85), lit(90), lit(58)))
df_with_array.show()

# 4. Define a schema with a nexted column properties
schema = StructType([
    StructField("name", StructType(), True),
    StructField("properties", MapType(StructType(), StringType()), True)
])
