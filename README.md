# machine-sensor-monitoring

![Linear Regression](https://github.com/mertaksoy/machine-sensor-monitoring/blob/master/images/monitoring-influxdb.png "InfluxDB Dashboard")

### Before starting
Install required packages:
  - pip install kafka-python
  - pip install kafka-utils
  - pip install pyspark
  - pip install influxdb-client
 
[Download](https://kafka.apache.org/downloads.html) Kafka and un-tar it. (The version which i am using is 2.5.0)
```sh
$ tar -xzf kafka_2.12-2.5.0.tgz
```

[Download](https://spark.apache.org/downloads.html) Spark and un-tar it. (The version which i am using is 2.4.5)
```sh
$ tar -xzf spark-2.4.5-bin-hadoop2.7.tgz
```

Set Spark Home
```sh
$ export SPARK_HOME="/Users/maksoy/Development/Tools/spark-2.4.5-bin-hadoop2.7"
$ export PATH="$SPARK_HOME/bin:$PATH"
```

To test pyspark, run in terminal
```sh
$ pyspark
```
you should see
```sh
   ____              __
  / __/__  ___ _____/ /__
 _\ \/ _ \/ _ `/ __/  '_/
/__ / .__/\_,_/_/ /_/\_\   version 2.4.5
   /_/
```
[Download](https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-8-assembly_2.11) Spark Streaming Kafka Assembly jar (The version which i am using is 2.4.5). We will use it it to stream data from Kafka.
**Important:** The version must match with Spark


### Start Zookeper
switch to folder where you un-tar kafka_2.12-2.5.0 
```sh
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka Server
```sh
$ bin/kafka-server-start.sh config/server.properties
```

### Create Topic "test"
```sh
$ bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test
```

### (Optional) To Monitor Incoming Messages
```sh
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

### Producing Messages
run producer.py from this repo to produce messages
```sh
$ python3 producer.py
```

### Streaming Data
run streamer.py to stream data from Kafka to influxDB
```sh
$ spark-2.4.5-bin-hadoop2.7/bin/spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.5.jar /Users/maksoy/git/machine-sensor-monitoring/src/steamer.py
```
