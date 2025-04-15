"""
Objective:
Create a YARN spark mode, used for testing functionalities, learning spark technicals

1. Reading CSV data with Spark.
2. Data exploration and cleaning.
3. Performing transformations and aggregations.
4. Using both the DataFrame API and Spark SQL.
5. Writing the results to an output directory.
"""

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("WorkforceEmploymentAnalysis(YARN)")
    .master("yarn")
    .config("spark.submit.deployMode", "client")
    .getOrCreate()
)

# set log level to WARN
spark.sparkContext.setLogLevel("WARN")


file_path: str = ""
