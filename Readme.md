#Starting points

- This project has been developed on Linux OS (Ubuntu ver 20.04 LTS), using PyCharm IDE and written in Python.
- The projects virtual environment has installed kafka-phyton, a Kafka client for Python. 
- Goal of the main script unitConsumerProducer.py is to receive a stream of logs data from Kafka via topic, 
  and depending on the user id and timestamp key values determine the number of unique users per minute.

#While in your IDE

- If you want to set up your IDE venv and run the .py scripts, make sure you install kafka python with command:

  
    pip install kafka-python

#While in your Kafka installation folder
  
- First you need to start Zookeeper by opening the new terminal and running:

  
    bin/zookeeper-server-start.sh config/zookeeper.properties

- Second you need to start the Kafka by opening the new terminal and running:

  
    bin/kafka-server-start.sh config/server.properties

- Both Zookeeper and Kafka are up and running, you need to register two new topics with Kafka by opening 
  a new terminal, and running commands one at a time:

  
    bin/kafka-topics.sh --delete --topic myTopic --bootstrap-server localhost:9092

  
    bin/kafka-topics.sh --delete --topic myResultTopic --bootstrap-server localhost:9092

#While in the project_planted folder

- Open a new terminal, and run the following command to extract the stream.jsonl.gz file
  (needs to be downloaded) and populate with message data the kafka producer, which outputs that data to topic myTopic:

  
    zcat stream.jsonl.gz | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic myTopic

#Executing the .py scripts

- To receive data from topic myTopic, process that data and output it as JSON to the topic 
  myResultTopic, run the unitConsumerProducer.py script in your IDE. Received messages from
  topic myTopic will be outputted to stdout.
- To output the data to stdout and view the results, received from the topic myResultTopic,
  run the consumer1.py script in your IDE.
  


  