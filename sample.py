from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create SparkSession
spark = SparkSession.builder \
    .appName("Filter_sampledata") \
    .getOrCreate()

# Load CSV data
df = spark.read.csv("C:/Users/asus/OneDrive/Desktop/sample.csv", header=True, inferSchema=True)

# Show initial data
print("Original Data:")
df.show()

# Filter rows where Quantity > 10
filtered_df = df.filter(col("age") > 30)

# Show filtered data
print("Filtered Data (age > 30):")
filtered_df.show()

# Stop the Spark session
spark.stop()
