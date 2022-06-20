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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import sys
import os
import json

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

class RPI(rpi_pb2_grpc.RPIServicer):

    def processRoomData(self, request, context):
        #process data

        room_name = request.roomName
        print(room_name)
        room_data = request.data
        print(room_data)

        interval = ""
        command = ""

        # set instructions to return to client
        instructions = interval + "," + command

        return rpi_pb2.Reply(res=instructions)




#basic step to run the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpi_pb2_grpc.add_RPIServicer_to_server(RPI(),server)
    server.add_insecure_port(channel_to_use)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
