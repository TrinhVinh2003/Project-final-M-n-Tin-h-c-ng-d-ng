from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("SparkSQL CRUD Operations") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


df = spark.read.format("jdbc").option("url", f"jdbc:sqlite:/home/database.db").option("dbtable", "my_database").load()


df.createOrReplaceTempView("my_database")
#Creat

new_data = [(4, 'Bob', 28, 'Analyst'), (5, 'Charlie', 35, 'Manager')]
columns = ['id', 'name', 'age', 'position']
new_df = spark.createDataFrame(new_data, columns)

# Chèn vào bảng my_database
df_new = df.union(new_df)
df_new.createOrReplaceTempView("my_database")
time_start = time.time()

result = spark.sql("select * from my_database ")

time_end = time.time()

result.show(10)

print("run time: ",time_end - time_start)