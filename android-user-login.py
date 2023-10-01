#importing the required libraries
from confluent_kafka import Consumer, KafkaError
from datetime import datetime
import json

#Defining the Kafka consumer configuration
conf = {'bootstrap.servers': 'localhost:29092',      #assigning the bootstrap to the port
        'group.id': 'android_users',                 #assigning the consumer to the Consumer Group
        'auto.offset.reset': 'earliest' }            #letting know from where should it begin to read

#Creating a Kafka consumer instance
android_consumer = Consumer(conf)

#Subscribing to the android-user-login topic
android_consumer.subscribe(['android-users-login'])  

try:
    while 1==1: #infinity while loop
        message = android_consumer.poll(timeout = 1.0)  #Adjusting the polling timeout as needed
        if message is None:  
            print(f"{datetime.now().strftime('%m-%d-%y %H:%M:%S')}: no new message") #Executed only if the message is none
            continue
        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of partition")
            else:
                print(f"Error: {message.error()}")
        else:
            print(f"android user: {message.value().decode('utf-8')}") #prints the message

except KeyboardInterrupt:
    pass

finally:
    android_consumer.close() 