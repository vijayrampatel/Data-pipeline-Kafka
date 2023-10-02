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





