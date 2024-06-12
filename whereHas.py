from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("SparkSQL CRUD Operations") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


df = spark.read.format("jdbc").option("url", f"jdbc:sqlite:/home/database.db").option("dbtable", "my_database").load()


df.createOrReplaceTempView("my_database")

time_start = time.time()

result = spark.sql("select * from my_database where geo_count >300; ").count()

time_end = time.time()

result.show(10)

print("run time: ",time_end - time_start)
