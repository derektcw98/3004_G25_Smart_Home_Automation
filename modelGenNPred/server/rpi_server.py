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

from concurrent import futures
import logging
import sys
from pathlib import Path
from datetime import datetime, timedelta
from io import StringIO
import pandas as pd
from dataInsert import insert
from predictClass import predictClass

import grpc
import rpi_pb2
import rpi_pb2_grpc

# Dynamic ip address and port
ipaddr = "[::]"
port = "50051"

try:
    ipaddr = sys.argv[1]
    port = sys.argv[2]
except:
    print("No arguments detected, using default: '[::]:50051'")

channel_to_use = ipaddr+":"+port
print(channel_to_use)

class RPI(rpi_pb2_grpc.RPIServicer):

    def sendSensorData(self, request, context):
        #Upload data to database
        room_name = request.roomName
        room_data = request.csvdata
        startOfWeek_dmy = datetime.now().strftime("%d%m%Y")
        cwd = Path(os.getcwd())    
        file_path = str(cwd.parent.absolute())+"/sharedDirectory/"+room_name + "_" + str(startOfWeek_dmy) + ".csv"
        file_path = Path(file_path)
        file_path.touch(exist_ok=True)
        with  open(file_path, 'w') as file:
            file.write(room_data)
        
        insert(file_path)

        result = "Data has been successfully received by server"
        return rpi_pb2.Reply(res=result)

    def askBehavior(self, request, context):
        # Get prediction based on request.data
        result = predictClass(request.roomName, request.data)
        return rpi_pb2.Reply(res=result)
       
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
