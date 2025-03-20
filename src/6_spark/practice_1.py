"""
Consolidation of what we have learned:

1. Create a spark session
2. Create a spark dataframe using the spark session created, ingesting raw data from a csv file
3. Rename "Title Description" to Occupation
4. Clean and Count the average salary for each company
5. Create a UDF that x1.3 to turn all avg salary by company into usd, renamed new columns as USD_Base_Salary
6. Apply the UDF to the DF
7. Sort the df in desc and cache it
8. Filter USD_Base_Salary > 300000 and display result
"""

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, regexp_replace, udf
from pyspark.sql.types import DoubleType

# 1
spark: SparkSession = SparkSession.builder.appName("spark_practice").getOrCreate()

# 2
file_path: str = "src/6_spark/input/workforce_employment_dataset.csv"
df: DataFrame = spark.read.csv(file_path, header=True, inferSchema=True)

# 3
df = df.withColumnRenamed("Title Description", "Occupation")
df.printSchema()

# 4
df_cleaned = df.na.drop()
# Clean base salary column to be a castable double
df_cleaned = df_cleaned.withColumn(
    "Base Salary Double", regexp_replace(col("Base Salary"), "[$]", "").cast("double")
)
# Find average base salary of each company
df_filtered = df_cleaned.groupby("Occupation").avg("Base Salary Double")
# df_filtered.show()


# 5
def convert_usd(base_salary):
    return base_salary * 1.3


# 6
# Register the UDF
to_usd_udf = udf(convert_usd, DoubleType())
# Creates a new column Base Salary Float USD if it does not exist
df_filtered_usd = df_filtered.withColumn(
    "Base Salary Double USD", to_usd_udf(df_filtered["avg(Base Salary Double)"])
)

# 7 caching expensive sorting operation
df_filter = df_filtered_usd.orderBy(col("Base Salary Double USD").desc()).cache()

# 8
df_filter.where(col("Base Salary Double USD") > 300000.00).show()
