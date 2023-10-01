#importing the required libraries
from confluent_kafka import Consumer, KafkaError, Producer
from datetime import datetime
import json

#Defining the Kafka consumer configuration
consumer_conf = {'bootstrap.servers': 'localhost:29092',    #assigning the bootstrap to the port
                 'group.id': 'fetching_data',               #assigning the consumer to the Consumer Group
                 'auto.offset.reset': 'earliest'}           #letting know from where should it begin to read


#Creating a Kafka consumer instance
fetching_consumer = Consumer(consumer_conf)

#Subscribing to the user-login topic to consume data
fetching_consumer.subscribe(['user-login'])

producer_conf = {'bootstrap.servers': 'localhost:29092'} #Defining the producer configuration

#Creating a Kafka prducer instance
producer = Producer(producer_conf)

#initialising diffrent topic for data pipeline 
ios_user_topic = 'ios-user-login'
android_users_topic = 'android-users-login'
missing_data_topic = 'missing-data-login'

try:
    while True:  #infinity while loop
        msg = fetching_consumer.poll(1.0)  #Adjusting the polling timeout as needed
        if msg is None:
            print(f"{datetime.now().strftime('%m-%d-%y %H:%M:%S')}: no new message") #Executed only if the message is none
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of partition")
            else:
                print(f"Error: {msg.error()}")
        else:

            #performing data transformation
            x = msg.value().decode('utf-8')
            x = json.loads(x) #converting string to dictionary
            if len(x) == 7: #will check if all the 7 columns are present
                if x["user_id"] is None:
                    continue
                else:
                    x["timestamp"] = str(datetime.fromtimestamp (x["timestamp"])) #converting timestamp to datetime

                    if x["device_type"] == "iOS": #segregating iOS users
                        print(x)
                        processed_data = json.dumps(x)
                        producer.produce(ios_user_topic, key=None, value=processed_data)
                    elif x["device_type"] == "android": #segregating android users
                        print(x)
                        processed_data = json.dumps(x)
                        producer.produce(android_users_topic, key=None, value=processed_data) 
            else:
                print(x)
                processed_data = json.dumps(x)
                producer.produce(missing_data_topic, key=None, value=processed_data) 

           
except KeyboardInterrupt:
    pass

finally:
    fetching_consumer.close()