"""
Spark DataFrame API for data manipulation
"""

from typing import Any

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create a Spark session
spark = SparkSession.builder.appName("basic_dataframe_operations").getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("country", StringType(), True)
])

data: list[dict[str, Any]] = [
    {"name": "elson", "age": 24, "country": None},
    {"name": "clement", "age": 34, "country": "Singapore"},
    {"name": "joyce", "age": None, "country": "Malaysia"},
]
# 1. Handling missing data

# Create a DataFrame from the list of dictionaries
# type checker sound off, but a list[dict] is a valid input type for creteDataFrame()
df = spark.createDataFrame(data, schema)

# 2. Use .na.drop() to remove rows with null values
# Drop rows with any nulls
df_cleaned = df.na.drop()
df_cleaned.show()

# 3. Filter out nulls for a specific column
df_filtered = df.where(col("country").isNotNull())
df_filtered.show()

# 4. Use .na.fill({"column": value}) to replace nulls with a specific value
# Fill nulls in the 'age' column with the value 0
df_filled = df.na.fill({"age": 0, "country": "No Citizen"})
df_filled.show()

# 5. Create a new column 'age_plus_5' (modifies df in place)
df = df.withColumn("age_plus_5", df["age"] + 2)
df.show()

# 6. Rename the 'age' column to 'years'
df = df.withColumnRenamed("age", "years")
df.show()

# 7. Drop column
df = df.drop("country")
df.show()

# 8. Filter and show only row with condition where years > 30
df = df.filter(df["years"] > 30)
df.show()
