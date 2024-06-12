from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("SparkSQL CRUD Operations") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


df = spark.read.format("jdbc").option("url", f"jdbc:sqlite:/home/database.db").option("dbtable", "my_database").load()


df.createOrReplaceTempView("my_database")

time_start = time.time()

result = spark.sql("""SELECT COUNT(*) AS count,AVG(geo_count) AS avg_geo, anzsic06 
                   WHERE geo_count > 300
                   FROM my_database 
                   GROUP BY anzsic06    
                   ORDER BY avg_geo DESC""").count()

time_end = time.time()

result.show()

print("run time: ",time_end - time_start)
