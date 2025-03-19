"""
User Defined Functions
 - Custom function to work with data using PySpark DataFrames. They are very useful in Spark when you need to apply
 custom logic that isn’t available in Spark’s built-in functions. They let you write your own transformations in Python
 (or Scala/Java) and apply them to each row of a DataFrame.
"""

from typing import Any

from pyspark.shell import spark
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, StructType, StructField, IntegerType

"""
Example Using PySpark UDFs.
- Costly conversion of code and data
- Expensive when dealing with large datasets
"""
df: list[dict[str, Any]] = [
    {"id": 1, "name": "elson", "age": 24, "country": None},
    {"id": 2, "name": "clement", "age": 34, "country": "Singapore"},
    {"id": 3, "name": "joyce", "age": None, "country": "Malaysia"},
]

schema = StructType(
    [
        StructField("id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("country", StringType(), True),
    ]
)

user_df = spark.createDataFrame(df, schema)


# Example of creating a UDFs using PySpark
def to_uppercase(s):
    return s.upper() if s else None


# Register the function
to_uppercase_udf = udf(to_uppercase, StringType())

# Apply UDF to the DataFrame
upper_df = user_df.withColumn("name", to_uppercase_udf(user_df["name"]))

upper_df.show()
