"""
How to use Spark SQL
"""

from pyspark.sql import SparkSession

# Initialize Spark Session
spark: SparkSession = SparkSession.builder.appName("Spark SQL Example").getOrCreate()

# Sample DataFrame
data = [("Alice", "HR", 30), ("Bob", "IT", 40), ("Cathy", "HR", 28)]
columns = ["Name", "Department", "Age"]
df = spark.createDataFrame(data, schema=columns)

# Register the df as a temp view (Crucial step for using Spark SQL)
df.createOrReplaceTempView("people")

# Query using SQL
result = spark.sql("SELECT Name, Age FROM people WHERE Age > 30")
result.show()
