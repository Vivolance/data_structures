"""
Pandas UDFs
- Eliminates costly conversion of code and data
- Does not need to be registered to the SparkSession
- Use Pandas capabilities for large datasets
"""
from typing import Any

from pyspark.shell import spark
from pyspark.sql import DataFrame
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

data: list[dict[str, Any]] = [
    {"id": 1, "name": "Elson", "temp_in_f": 200.09},
    {"id": 2, "name": "Clement", "temp_in_f": 180.20},
    {"id": 3, "name": "Eugene", "temp_in_f": 100.77},

]

scheme = StructType(
    [
        StructField("id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("temp_in_f", FloatType(), True)
    ]
)

user_temp_df: DataFrame = spark.createDataFrame(data, scheme)


@pandas_udf(FloatType())
def f_to_c(column):
    return (column - 32) * 5.0/9.0


# Call the pandas_udf function on the temp_in_f column
user_temp_df_in_c = user_temp_df.withColumn("temp_in_c", f_to_c(user_temp_df["temp_in_f"]))
user_temp_df_in_c.show()
