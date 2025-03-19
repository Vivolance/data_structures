"""
Pandas UDFs
- Eliminates costly conversion of code and data
- Does not need to be registered to the SparkSession
- Use Pandas capabilities for large datasets
"""
from pyspark.sql.functions import pandas_udf


@pandas_udf("float")
def f_to_c(temp: float) -> float:
    return (temp - 32) * 5.0/9.0
