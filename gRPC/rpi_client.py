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

import grpc
import rpi_pb2
import rpi_pb2_grpc

# Dynamic ip address and port
ipaddr = "localhost"
port = "50051"

try:
    ipaddr = sys.argv[0]
    port = sys.argv[1]
except:
    print("No arguments detected, using default: 'localhost:50051'")

channel_to_use = ipaddr+":"+port

# Initiation of cached items
client_log_json = {}

def loadJson():
    global client_log_json
    # open file for reading, "r" 
    
    client_log_path = os.getcwd() + "\gRPC\client_log.json"
    with open(client_log_path, "r") as file:
        # load json object into dictionary
        client_log_json = json.load(file)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with sstatement does not fit the needs
    # of the code.
    with grpc.insecure_channel(channel_to_use) as channel:
        stub = rpi_pb2_grpc.RPIStub(channel)

        while True:
            
            # Reading of Configurations File
            config_file = os.getcwd() + "\gRPC\client_config.txt"
            f = open(config_file, "r")
            configs = f.readlines()
            f.close()
            print("CONFIGURATIONS:\n", configs)

            # Assigning Configurations
            interval_duration = configs[0].replace('\n', '').split('=')
            room = configs[1].replace('\n', '').split('=')

            data = loadJson()
            response = stub.processRoomData(rpi_pb2.Request(room, data))

            # (PLACEHOLDER FOR INSTRUCTIONS FROM SERVER)
            print(str(response.res))

            # Sleep duration between sending of data
            sleep(interval_duration)


if __name__ == '__main__':
    logging.basicConfig()
    run()
