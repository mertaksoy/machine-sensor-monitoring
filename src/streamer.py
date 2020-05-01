from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
import time
from influxdb_client import InfluxDBClient

INFLUX_TOKEN = "your_token"
INFLUX_CLOUD_URL = "https://cloud_url_provided_by_influx.com"
INFLUX_ORGANIZATION_ID = "your_org_id"
INFLUX_BUCKET_ID = "your_bucket_id"

client = InfluxDBClient(url=INFLUX_CLOUD_URL, token=INFLUX_TOKEN)
write_api = client.write_api()

def printAndStoreMessage(msg):
	fluxData = "myMeasurement,host=myHost oilTemp=" + str(msg['oilTemp']) + ",pressure=" + str(msg['pressure']) + " " + str(int(time.time_ns()));
	print(fluxData)
	write_api.write(INFLUX_BUCKET_ID, INFLUX_ORGANIZATION_ID, fluxData)
	return msg

sc = SparkContext(appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 5)

kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'test', {'test':1})

parsed = kafkaStream.map(lambda v: json.loads(v[1]))
parsed.count().map(lambda x: 'Data in this batch: %s' % x).pprint()
parsed.map(lambda x: printAndStoreMessage(x)).pprint()

ssc.start()
ssc.awaitTermination()
