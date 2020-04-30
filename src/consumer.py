from kafka import KafkaConsumer
from json import loads


consumer = KafkaConsumer(
	'test',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
	print(message.value)