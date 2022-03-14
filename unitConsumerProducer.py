from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")  #converts dict into json so the KafkaProducer can output json

consumer = KafkaConsumer('myTopic', auto_offset_reset='earliest')  #auto_offset_reset='earliest' is the equivalent of --from-begining in the consumer generated directly by kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=json_serializer)

dataList = {}
timeThreshold = 0

for msg in consumer:
    json_object = json.loads(msg.value.decode("utf-8")) #the value message attribute that we get from KafkaConsumer is type bytes, we decode it and perform json.load to get json

    if timeThreshold == 0 or json_object['ts'] > timeThreshold: #if the timeThreshold is initialised for the first time or timestamp is above current timeThreshold
        if json_object['ts'] > timeThreshold != 0:              #if the timestamp is above the timeThreshold and its not the initial if loop when we set the first timeThreshold
            report = {                                          #create a report for sending results, number of messages in the minute we observed messages judging by their timestamps
                "numberOfUsers": len(dataList),
                "ts": timeThreshold
            }
            producer.send("myResultTopic", report)
            dataList.clear()                                    #clean the dictionary dataList so we dont fill up the memory
        timeThreshold = json_object['ts'] + (60 - json_object['ts'] % 60)  #threshold is the whole minut, where the whole minute depends on the clock time

    if json_object['uid'] not in dataList:                      #the for loop goes trough every message that is recived from the topic, and populates the dataList dictionary with unique uid, determaning by the key
        dataList[json_object['uid']] = json_object

    print(json_object) #outputs data from topic myTopic, producer generated directly by kafka is pushing messages that were extracted from stream.jsonl.gz