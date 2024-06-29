# How to start with KAFKA:
Quick start with Kafka KRaft

Get the docker image from docker hub:

    ```bash
    docker pull apache/kafka:3.7.0
    ```

Start a Docker Container for KAFKA:

    ```bash
    docker run -p 9092:9092 apache/kafka:3.7.0
    ```
    #           PORT int/ext   Image Name/Version
    
Check if container is running or not:

    ```bash
    docker ps
    ```

Now Copy the container name and run following command:
Will enter in container.

    ```bash
    docker exec -it <container-name> /bin/bash
    ```
    #      execute 
    # docker exec -it 2b53c2e5ef9f /bin/bash
we can check the list of folders with " ls" command

Note: Kafka commands are in this directory in the container

So move to this directory by using "cd /opt/kafka/bin"
Then use "ls" to show what is in this directory.
There will be a file named "kafka-topics.sh"

    ```bash
    /opt/kafka/bin
    ```


CREATE A TOPIC TO STORE YOUR EVENTS

Kafka is a distributed event streaming platform that lets you read, write, store, and process events (also called records or messages in the documentation) across many machines.

Example events are payment transactions, geolocation updates from mobile phones, shipping orders, sensor measurements from IoT devices or medical equipment, and much more. These events are organized and stored in topics. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder.

So before you can write your first events, you must create a topic. Open another terminal session and run:

    ```bash
    /opt/kafka/bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
    ```

It will create an event with name of "quickstart-events"

Now run the following command to describe the event created above.

    ```bash
    /opt/kafka/bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
    ```

Result:

Topic: quickstart-events        TopicId: vnouS60vSLqxJDqjRFkUMg PartitionCount: 1       ReplicationFactor: 1                   Configs: segment.bytes=1073741824
        Topic: quickstart-events        Partition: 0    Leader: 1       Replicas: 1     Isr: 1


WRITE SOME EVENTS INTO THE TOPIC

A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need—even forever.

Run the console producer client to write a few events into your topic. By default, each line you enter will result in a separate event being written to the topic.
We can stop the producer client with Ctrl-C at any time.


    ```bash
    /opt/kafka/bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
    ```
Now write events, i.e.
    First event of Afraz
    Second event of Afraz

NOW OPEN A NEW TERMINAL AND RUN CONSUMER TO READ THE EVENTS, WE HAVE JUST CREATED:
Open a new terminal and go into the /opt/...

    ```bash
    /opt/kafka/bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
    ```
Now if you write a new event, it will be shown live stream.
We can stop the consumer client with Ctrl-C at any time.


Feel free to experiment: for example, switch back to your producer terminal (previous step) to write additional events, and see how the events immediately show up in your consumer terminal.

Because events are durably stored in Kafka, they can be read as many times and by as many consumers as you want. You can easily verify this by opening yet another terminal session and re-running the previous command again.

# KAFKA UI

This is a popular open-source web UI specifically designed for viewing Kafka topics, messages, brokers, consumer groups, and even lets you create new topics. It's known for being lightweight, easy to set up, and supports secure connections. You can find the project on Github here:

[Kafka Github UI Documentation](https://github.com/provectus/kafka-ui)

[Kafka Github UI Documentation](https://github.com/provectus/kafka-ui?tab=readme-ov-file#getting-started)


# Kafka UI in Short:

```bash
docker network create -d bridge kafka-net # network name i.e. kafka-net

docker network ls

docker run -p 9092:9092 --network kafka-net --name mykafka apache/kafka:3.7.0 # container name i.e. mykafka

docker run -it -p 8080:8080 --network kafka-net -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui
```

# KAFKA UI step by step:

Create a bridge.

    ```bash
    docker network create -d bridge kafka-net # network name i.e. kafka-net
    ```

Frist Run the Kafka Container:
#                                                  Name of container (KafkaC)
    ```bash
    docker run -p 9092:9092 --network kafka-net --name KafkaC apache/kafka:3.7.0
    ```

Enter in container:

    ```bash
    docker exec -it KafkaC /bin/bash
    ```

Create Topic:

#                                             Name of topic (KafkaC-events)

    ```bash
    /opt/kafka/bin/kafka-topics.sh --create --topic KafkaC-events --bootstrap-server localhost:9092
    ```
Result:
    Created topic KafkaC-events.

Describe Topis:

    ```bash
    /opt/kafka/bin/kafka-topics.sh --describe --topic KafkaC-events --bootstrap-server localhost:9092
    ```
Result:
    Topic: KafkaC-events    TopicId: HYOtBsxyStGELvqpCirP2Q PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: KafkaC-events    Partition: 0    Leader: 1       Replicas: 1     Isr: 1

Write Events (Producer):

    ```bash
    /opt/kafka/bin/kafka-console-producer.sh --topic KafkaC-events --bootstrap-server localhost:9092
    ```

Show Events (Consumer):

    ```bash
    /opt/kafka/bin/kafka-console-consumer.sh --topic KafkaC-events --from-beginning --bootstrap-server localhost:9092
    ```

Run command for Kafka UI:

    ```bash
    docker run -it -p 8080:8080 --network kafka-net -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui
    ```

Now run localhost:8080, which is mentioned in our command to open the UI in browser.
