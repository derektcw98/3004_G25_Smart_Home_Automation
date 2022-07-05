# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rpi_pb2 as rpi__pb2


class RPIStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.askBehavior = channel.unary_unary(
                '/rpi.RPI/askBehavior',
                request_serializer=rpi__pb2.RequestBehavior.SerializeToString,
                response_deserializer=rpi__pb2.Reply.FromString,
                )
        self.sendSensorData = channel.unary_unary(
                '/rpi.RPI/sendSensorData',
                request_serializer=rpi__pb2.RequestSensorData.SerializeToString,
                response_deserializer=rpi__pb2.Reply.FromString,
                )


class RPIServicer(object):
    """The greeting service definition.
    """

    def askBehavior(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendSensorData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'askBehavior': grpc.unary_unary_rpc_method_handler(
                    servicer.askBehavior,
                    request_deserializer=rpi__pb2.RequestBehavior.FromString,
                    response_serializer=rpi__pb2.Reply.SerializeToString,
            ),
            'sendSensorData': grpc.unary_unary_rpc_method_handler(
                    servicer.sendSensorData,
                    request_deserializer=rpi__pb2.RequestSensorData.FromString,
                    response_serializer=rpi__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rpi.RPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPI(object):
    """The greeting service definition.
    """

    @staticmethod
    def askBehavior(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpi.RPI/askBehavior',
            rpi__pb2.RequestBehavior.SerializeToString,
            rpi__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendSensorData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpi.RPI/sendSensorData',
            rpi__pb2.RequestSensorData.SerializeToString,
            rpi__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
