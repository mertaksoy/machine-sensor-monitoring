# machine-sensor-monitoring


### Before starting
Install required packages:
  - pip install kafka-python
  - pip install kafka-utils
 
[Download](https://kafka.apache.org/downloads.html) Kafka and un-tar it. (The version which i am using is 2.5.0)
```sh
$ tar -xzf kafka_2.12-2.5.0.tgz
$ cd kafka_2.12-2.5.0
```

### Start Zookeper
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
