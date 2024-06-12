FROM ubuntu:20.04
# Cài đặt các gói cần thiết
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    wget \
    tar \
    curl \
    python3-pip \
    sqlite3 \
    vim \
    nano \
 && ln -s /usr/bin/python3 /usr/bin/python \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
# Tải xuống và cài đặt Apache Spark
RUN wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
RUN tar xvf spark-3.5.1-bin-hadoop3.tgz
RUN mv spark-3.5.1-bin-hadoop3 /opt/spark
RUN rm spark-3.5.1-bin-hadoop3.tgz

# Thiết lập biến môi trường cho Spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

# Tải xuống JDBC driver cho SQLite
RUN wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.34.0/sqlite-jdbc-3.34.0.jar
#pyspark
RUN pip install pyspark

COPY data.csv /home/data.csv
# Thiết lập thư mục làm việc mặc định
WORKDIR /home