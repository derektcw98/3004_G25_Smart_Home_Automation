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
try:
    ipaddr = sys.argv[1]
    port = sys.argv[2]
except:
    print("No arguments detected, using default: 'localhost:50051'")
    
channel_to_use = ipaddr+":"+port
print(channel_to_use)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with sstatement does not fit the needs
    # of the code.
    with grpc.insecure_channel(channel_to_use) as channel:
        stub = rpi_pb2_grpc.RPIStub(channel)

        while True:
            pass
        


if __name__ == '__main__':
    logging.basicConfig()
    run()
