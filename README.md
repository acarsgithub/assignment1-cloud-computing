# assignment1-cloud-computing

## Directions to run the producer.py and consumer.py files according to assignment specifications

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



