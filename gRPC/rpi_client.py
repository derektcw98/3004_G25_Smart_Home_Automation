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

import grpc
import rpi_pb2
import rpi_pb2_grpc
from sense_hat import SenseHat

interval_duration = 1

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with sstatement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rpi_pb2_grpc.RPIStub(channel)
        sense = SenseHat()

        room = input("Enter a room name")
        while True:
            temp = sense.get_temperature()
            temp_calibrated = temp - ((cpu_temp - temp)/5.466)
            humidity = sense.get_humidity()
            room = ""
            data = ""
            response = stub.processRoomData(rpi_pb2.Request(room, data))
            #set interval duration
            print(str(response.res))
            #sleep between sending of data
            sleep(60 * interval_duration)


if __name__ == '__main__':
    logging.basicConfig()
    run()
