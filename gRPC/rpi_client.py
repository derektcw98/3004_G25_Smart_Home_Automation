# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
from concurrent.futures import thread

import logging
from time import sleep
from urllib import request
import sys
import json
from pathlib import Path

import grpc
import rpi_pb2
import rpi_pb2_grpc
from datetime import datetime, timedelta
import pandas as pd
from threading import Thread

# Dynamic ip address and port and room
ipaddr = "localhost"
port = "50051"
room = "default"
try:
    ipaddr = sys.argv[1]
    port = sys.argv[2]
    room = sys.argv[3]
except:
    print("No arguments detected, using default: 'localhost:50051', room: 'default'")
    
channel_to_use = ipaddr+":"+port
print(channel_to_use)

def sensorDataSend(stub,test):

    now = datetime.now()
    dayOfWeek = int(now.weekday())
    dayHour = int(datetime.now().strftime("%H"))
    # Check if client time matches : Monday 01:00
    if dayOfWeek==0 and dayHour == 1:
        startOfWeek_dmy = (datetime.now() - timedelta(days=7)).strftime("%d%m%Y")
        file_path = room + "_" + str(startOfWeek_dmy) + ".csv"
        csvString = ""
        with open(file_path, 'r') as file:
            for line in file:
                csvString += line
        response = stub.sendSensorData(rpi_pb2.RequestSensorData(roomName = room, csvdata = csvString))
        print(response.res)

        sleep(1*60*60)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with sstatement does not fit the needs
    # of the code.
    with grpc.insecure_channel(channel_to_use) as channel:
        stub = rpi_pb2_grpc.RPIStub(channel)

        sensorDataThread = Thread(target=sensorDataSend, args=(stub,"test"))
        sensorDataThread.start()
        sensorDataThread.join()
        while True:
            pass
        
            # response = stub.askBehavior(rpi_pb2.RequestBehavior(roomName = room, data = str(data)))

            # # Behavior
            # print(str(response.res))

            # 
            # TODO: PROCEED TO ACT/CARRY OUT INSTRUCTIONS HERE
            # 


if __name__ == '__main__':
    logging.basicConfig()
    run()
