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

from __future__ import print_function
from concurrent.futures import thread

import logging
from time import sleep
from urllib import request
import sys
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

def sensorDataSend(stub, string):
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

        sensorDataThread = Thread(target=sensorDataSend, args=(stub,"start"))
        sensorDataThread.start()
        sensorDataThread.join()

        while True:
            now = datetime.now()
            dayOfWeek = int(now.weekday())

            # get filepath of start of week records
            if dayOfWeek!=0:
                startOfWeek_dmy = (now - timedelta(days=dayOfWeek)).strftime("%d%m%Y")
                file_path = room + "_" + str(startOfWeek_dmy) + ".csv"
            else: 
                file_path = room + "_" + str(now.strftime("%d%m%Y")) + ".csv"
                
            # Every 10mins run the following (1min after csv updated)
            curr_min = int(now.strftime("%M")[1:])            
            if curr_min==1:
                # for days besides monday, assign file_path to monday's date
                with open(file_path, 'r') as f:
                    lines = f.read().splitlines()
                    latest_data = lines[-1]
                    print("latest record: ", latest_data)
                
                response = stub.askBehavior(rpi_pb2.RequestBehavior(roomName = room, data = latest_data))

            # Behavior returned
            returned_label = response.res
            print(returned_label)

            # TODO: Change states on RPI
            if returned_label != latest_data:
                if returned_label[0] == 'g':
                    AC_State = 1
                elif returned_label[0] == 'n':
                    AC_State = 0

                if returned_label[2] == 'g':
                    Light_State = 1
                elif returned_label[2] == 'n':
                    Light_State = 0
            
            # write to states file

            # system sleep for a minute
            sleep(1*60)
        
            


if __name__ == '__main__':
    logging.basicConfig()
    run()
