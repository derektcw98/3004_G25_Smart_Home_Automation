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
import os
import sys
import json
from pathlib import Path

import grpc
import rpi_pb2
import rpi_pb2_grpc

# Dynamic ip address and port
ipaddr = "localhost"
port = "50051"

try:
    ipaddr = sys.argv[1]
    port = sys.argv[2]
except:
    print("No arguments detected, using default: 'localhost:50051'")
    
channel_to_use = ipaddr+":"+port
print(channel_to_use)

# Initiation of cached items
events_log_json = {}

def loadJson(path):
    global events_log_json
    # open file for reading, "r" 
    
    with open(path, "r") as file:
        # load json object into dictionary
        events_log_json = json.load(file)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with sstatement does not fit the needs
    # of the code.
    with grpc.insecure_channel(channel_to_use) as channel:
        stub = rpi_pb2_grpc.RPIStub(channel)

        while True:
            
            # Reading of Configurations File
            config_file = Path('client_config.txt')
            f = open(config_file, "r")
            configs = f.readlines()
            f.close()
            print("CONFIGURATIONS:\n", configs)

            # Assigning Configurations
            interval_duration = str(configs[1]).replace('\n', '').split('=')
            interval_duration = int(interval_duration[1])
            room = str(configs[0]).replace('\n', '').split('=')
            room = str(room[1])

            # Load data from JSON log and submit to server
            events_log_path = Path('events_log.json')
            with open(events_log_path, "r+") as file:
            # try loading contents as a json dictionary
                try:
                    data = json.load(file)
                    print("data: \n", data)
                except:
                    print("Empty Json File.")
                file.close()

            response = stub.processRoomData(rpi_pb2.Request(roomName = room, data = str(data)))

            # Server Instructions
            print(str(response.res))

            # 
            # TODO: PROCEED TO ACT/CARRY OUT INSTRUCTIONS HERE
            # 

            # Sleep duration between sending of data
            sleep(interval_duration)


if __name__ == '__main__':
    logging.basicConfig()
    run()
