from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('myResultTopic', auto_offset_reset='earliest')

for msg in consumer:

    print(json.loads(msg.value)) #output the result data from myResultTopic topic to stdout
