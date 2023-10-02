# Data-pipeline-Kafka

#Flow Chart
<img width="470" alt="image" src="https://github.com/vijayrampatel/Data-pipeline-Kafka/assets/145386038/52db37eb-7b2c-4c36-a678-13fd01a4b576">

Step 1:
Install python from this webiste: https://www.python.org/ 
Install docker from this website: https://www.docker.com/
Import confluent_kafka using command : pip install confluent_kafka

Step 2: 
Go to the directory where you have cloned the project
Run the docker-compose.yml file, which help you in receivng the data. using the command in linux : </b> docker-compose -f docker-compose.yml up -d </b>
This will get the kafka, zookeeper started. Also producer will start sending messages to the user-login topic which is created in the docker-compose.yml file.





