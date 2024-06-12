# Spark không hỗ trợ UPDATE và DELETE trực tiếp trong DataFrame. Thay vào đó,  có thể tạo một DataFrame mới với các giá trị đã cập nhật và ghi đè bảng cũ.

from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("SparkSQL CRUD Operations") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


df = spark.read.format("jdbc").option("url", f"jdbc:sqlite:/home/database.db").option("dbtable", "my_database").load()


df.createOrReplaceTempView("my_database")

time_start = time.time()

result = spark.sql("select COUNT(*),year from my_database group by year")

time_end = time.time()

result.show(10)

print("run time: ",time_end - time_start)
