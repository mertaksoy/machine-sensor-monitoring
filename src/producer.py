from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
	value_serializer=lambda x: 
	dumps(x).encode('utf-8'))


def getHealthyOilTemp():
	return random.randint(75,85)

def getDangerOilTemp():
	return random.randint(85,100)

def getHealthyPressure():
	return random.randint(25,35)

def getDangerPressure():
	return random.randint(35,70)


messages = []

for i in range(1000):
	for i in range(random.randint(10,20)):
		messages.append({'oilTemp': getHealthyOilTemp(), 'pressure': getHealthyPressure()})

	for i in range(random.randint(3,6)):
		messages.append({'oilTemp': getHealthyOilTemp(), 'pressure': getDangerPressure()})

	for i in range(random.randint(10,20)):
		messages.append({'oilTemp': getHealthyOilTemp(), 'pressure': getHealthyPressure()})

	for i in range(random.randint(3,6)):
		messages.append({'oilTemp': getDangerOilTemp(), 'pressure': getHealthyPressure()})

for msg in messages:
	producer.send('test', value=msg)
	sleep(5)

