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

import logging
from urllib import request

import grpc
import bookReview_pb2
import bookReview_pb2_grpc
#TODO: import _pb2 and _pb2_grpc



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with sstatement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bookReview_pb2_grpc.BookReviewStub(channel)

        while True:
            print ("""

            1. Add Book Review
            2. Retrieve list of all books
            3. Query review of book

            """)

            option = input("Enter an option number: ") 

            if option=="1": 
                bookInput = input("Enter Book Name: ") 
                reviewInput = input("Enter Review: ") 
                response = stub.addReview(bookReview_pb2.Request(book=bookInput, review=reviewInput))
                print(str(response.res))

            #  Regular user check out
            elif option=="2":
                response = stub.retrieveBooks(bookReview_pb2.RequestRetrieve())
                print("These are the books in the review list: \n" + str(response.res))

            elif option=="3":
                bookInput = input("Enter Book Name: ") 
                response = stub.queryReview(bookReview_pb2.RequestBookReview(book=bookInput))
                print(response.res)

            else:
                print("\n Not Valid Choice Try again\n") 


if __name__ == '__main__':
    logging.basicConfig()
    run()
