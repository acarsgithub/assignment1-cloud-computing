#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Last modified: September 24, 2020 by Khoa Nguyen and Acar Ary 
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#

import os   # need this for popen
import time # for sleep
import json
from kafka import KafkaProducer  # producer of events
from datetime import datetime

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
producer = KafkaProducer (
  bootstrap_servers="129.114.25.26:9092", 
  acks=1, #wait for leader to write to log
  value_serializer=lambda v: json.dumps(v).encode('utf-8')
)  

# say we send the contents 100 times after a sleep of 1 sec in between
for i in range (100):
    
    # get the output of the top command
    process = os.popen ("top -n 1 -b")

    # read the contents that we wish to send as topic content
    contents = process.read ()

    # create timestamp
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # json data
    data = {
      "timestamp" : current_time,
      "value": contents
    }

    # send the contents under topic utilizations. Note that it expects
    # the contents in bytes so we convert it to bytes.
    #
    # Note that here I am not serializing the contents into JSON or anything
    # as such but just taking the output as received and sending it as bytes
    # You will need to modify it to send a JSON structure, say something
    # like <timestamp, contents of top>
    #
    producer.send ("utilizations", value=data)
    producer.flush ()   # try to empty the sending buffer

    # sleep a second
    time.sleep (1)

# we are done
producer.close ()
    






