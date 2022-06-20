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

import grpc
import bookReview_pb2
import bookReview_pb2_grpc

reviewRecords = {}

class BookReview(bookReview_pb2_grpc.BookReviewServicer):

    def addReview(self, request, context):
        global reviewRecords
        reviewString = "" #To Store existing array
        if request.book not in reviewRecords.keys():
            reviewRecords[request.book] = request.review
        else:
            for books in reviewRecords:
                if books is request.book:
                    reviewString = reviewRecords[request.book] #add original reviews in records
                    reviewString += "\n" + request.review #add new review in new line
                    reviewRecords[request.book] = reviewString 
        print(reviewRecords)
        return bookReview_pb2.Reply(res="Review for " + request.book + " has been added.")

    def retrieveBooks(self, request, context):
        global reviewRecords
        books = ""
        for book in reviewRecords:
            books += " " + str(book)
            print(books)
        return bookReview_pb2.Reply(res=books)

    def queryReview(self, request, context):
        global reviewRecords
        if request.book not in reviewRecords:
            return bookReview_pb2.Reply(res= "Book does not exist in records")
        else:
            return bookReview_pb2.Reply(res=request.book + " reviews are: \n" + reviewRecords[request.book])

#basic step to run the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bookReview_pb2_grpc.add_BookReviewServicer_to_server(BookReview(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
