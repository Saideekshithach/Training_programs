import os
from pyspark.sql import SparkSession

# Fix for Windows (if python3 not recognized)
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

# Start Spark session
spark = SparkSession.builder \
    .appName("Repartition Sales Example") \
    .getOrCreate()

# Sample product sales data
sales_data = [
    (101, "T-Shirt", "Clothing", 250),
    (102, "Sneakers", "Footwear", 1200),
    (103, "Perfume", "Cosmetics", 600),
    (104, "Jeans", "Clothing", 1500),
    (105, "Laptop", "Electronics", 55000),
    (106, "Foundation", "Cosmetics", 1200),
    (107, "Sandals", "Footwear", 900),
    (108, "Smartphone", "Electronics", 30000),
    (109, "Face Wash", "Cosmetics", 300),
    (110, "Jacket", "Clothing", 2000)
]

columns = ["product_id", "product_name", "category", "price"]

# Create DataFrame
df = spark.createDataFrame(sales_data, columns)

print("Initial Partitions:", df.rdd.getNumPartitions())

# Repartition DataFrame by category
df_repartitioned = df.repartition(5, df["category"])
print("After Repartition by 'category':", df_repartitioned.rdd.getNumPartitions())

# Save output for visual check (optional)
df_repartitioned.write.mode("overwrite").csv("output_sales_by_category")

# Done
spark.stop()
