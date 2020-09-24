# assignment1-cloud-computing

## Directions to properly execute the producer.py and consumer.py files according to assignment specifications

### Part 1: ChameleonCloud Instances and Security Group/UFW Specifications
There are a few setup steps that need to be completed for the environment to be correct (according to the specifications of the assignment). First, two VM instances need to be created on ChameleonCloud. Once the instances have been created and are up and running, the security groups for those VM instances need to include the port numbers 5984, 9092, and 2181. This is to allow the zookeeper, kafka server, and couchdb access around the firewall that is built around the ChameleonCloud. 

The instances witht the proper security groups have been created on ChameleonCloud with the following names:
* aryar-demo
* aryar-demo-2

Once the instances and security groups have been created, hop onto a terminal for both VMs. With the ufw command, go ahead and allow the zookeeper, couchdb, and kafka server access around the built in firewall for the VMs on ChameleonCloud.

Please refer to this link for addiitonal resources on UFW: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04

The commands to execute on both VMs' terminals are:
* sudo ufw allow 2181 
* sudo ufw allow 9092
* sudo ufw allow 5984
* sudo ufw status (to confirm the changes have been implemented for those three ports)

Once this part is setup, you are good to go on the next step!

### Part 2: Kafka Binary Download & server.properties Specifications
Now, on both VM instances on ChameleonCloud, Apache Kafka needs to be downloaded and extracted. Specfically, we are going to use the Scala 2.13 binary version. 

* wget "http://mirror.metrocast.net/apache/kafka/2.6.0/kafka_2.13-2.6.0.tgz" (to download this version)
* tar -xzvf [downloaded kafka folder name from above step] (to extract)

At this point Apache Kafka should be downloaded on both instances, but we still need to modify the server.proprties files to the correct specifications:

 **For the VM that you intend to run zookeeper on:**
 * set unique broker id (0)
 * uncomment listeners, advertised listeners, and listener security protocol map lines
 * listeners line should be: 
   * PLAINTEXT://:9092
 * advertised listeners line should be:
   * PLAINTEXT://<floating-point-ip-address-of-current-instance>:9092
 * listener security protocol map should be left on default
 * zookeeper.connect line should be:
   * [floating-point-ip-address-of-current-instance]:2181, [ip-net-address-of-current-instance]:2181, localhost:2181

 **For the second VM instance not running zookeeper:**
 * set unique broker id (1)
 * uncomment listeners, advertised listeners, and listener security protocol map lines
 * listeners line should be: 
   * PLAINTEXT://:9092
 * advertised listeners line should be:
   * PLAINTEXT://<floating-point-ip-address-of-current-instance>:9092
 * listener security protocol map should be left on default
 * zookeeper.connect line should be:
   * [floating-point-ip-address-of-the-other-instance]:2181, [ip-net-address-of-the-other-instance]:2181

After these steps have been completed, Apache Kafka and the server.properties files should be good to go!

### Part 3: Running zookeeper, kafka-servers, and creating topic

##### ssh/PUTTY may be needed to obtain multiple terminals to run multiple programs on an instance simultaneously

To start off, make sure you cd into the kafka folder from the binary download you made earlier...
Additionally, ensure that you download and install python3, couchdb library for python, kafka-python library, and couchdb itself

**On VM instance with broker id 0, start zookeeper with the following commmand:**
* bin/zookeeper-server-start.sh config/zookeeper.properties

**Next, on VM instance with broker id 1, run the following to start kafka server:**
* bin/kafka-server-start.sh config/server.properties

**Next, on VM instance with broker id 0, start kafka server:**
* bin/kafka-server-start.sh config/server.properties

**Next on VM instance with broker id 0, create topic:**
* bin/kafka-topics.sh --create --topic utilizations --bootstrap-server [floating-point-ip-address-of-current-instance]:9092

**Viewing topic properties on kafka servers:**
* bin/kafka-topics.sh --describe --topic utilizations --bootstrap-server [floating-point-ip-address-of-either-instance]:9092 

After the above steps have completed, everything should be in order for the final step!

### Part 4: CouchDB setup and running consumer and producer

Please refer to the following link to help setup CouchDB on the VM instance that has broker id 1 (not the zookeeper): https://techexpert.tips/couchdb/couchdb-installation-ubuntu-linux/

Once it has been properly installed, a database can be created easily with the proper credentials for the single node instance on CouchDB made from the tutorial above.

At this point, CouchDB should be installed and a database should exist. We can now start the producer and consumer python files, which should send the JSON data automatically to the database as documents.

For the final step, have the producer file on another local laptop or VM instance outside of the kafka server/chameleon network. On the Chameleon instance with a broker id of 0, go ahead and transfer the consumer python file over to here and execute the python file. Simultaneously, go ahead and run the producer file on your local VM or Ubuntu. At this point, the JSON formatted data should be logging and storing onto the database.

**As a quick disclaimer, ensure that the python files for consumer and producer have the appropriate floating point ip address and database name/couchdb link and credentials for your own purposes**

Congratulations! The process is complete!





