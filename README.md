# Data-pipeline-Kafka

#Flow Chart <br>
<img width="470" alt="image" src="https://github.com/vijayrampatel/Data-pipeline-Kafka/assets/145386038/52db37eb-7b2c-4c36-a678-13fd01a4b576">

Step 1: <br>
Install python from this webiste: https://www.python.org/ <br>
Install docker from this website: https://www.docker.com/ <br>
Import confluent_kafka using command : pip install confluent_kafka

Step 2: <br>
Go to the directory where you have cloned the project<br>
Run the docker-compose.yml file, which help you in receivng the data. using the command in linux : </b> docker-compose -f docker-compose.yml up -d </b> <br>
This will get the kafka, zookeeper started. Also producer will start sending messages to the user-login topic which is created in the docker-compose.yml file.

Step 3: <br>
Execute the user-login-consumer.py file, from the same directory, you will be able to see that it is consuming the messages from the user-login topic. The code for this written in python  <br>
Code explanation<br>
Firstly we have imported the library, did the congifuration of the Kafka consumer, Producer, and created few kafka topics. <br>
We have converted the string message coming from the producer into the dictionary to operate on it, we have used the if conditioning to filter the data and by using the key values concept in python and push it to the partiton using the producer<br>
Converted the timestamp to the datetime<br>

Step4:<br>
Execute the 







