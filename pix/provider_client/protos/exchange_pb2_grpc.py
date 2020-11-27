# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import exchange_pb2 as app_dot_services_dot_exchange_dot_exchange__pb2


class ExchangeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_crypto = channel.unary_unary(
                '/Exchange/send_crypto',
                request_serializer=app_dot_services_dot_exchange_dot_exchange__pb2.SendCryptoRequest.SerializeToString,
                response_deserializer=app_dot_services_dot_exchange_dot_exchange__pb2.SendCryptoResponse.FromString,
                )


class ExchangeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send_crypto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExchangeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send_crypto': grpc.unary_unary_rpc_method_handler(
                    servicer.send_crypto,
                    request_deserializer=app_dot_services_dot_exchange_dot_exchange__pb2.SendCryptoRequest.FromString,
                    response_serializer=app_dot_services_dot_exchange_dot_exchange__pb2.SendCryptoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Exchange', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Exchange(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send_crypto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Exchange/send_crypto',
            app_dot_services_dot_exchange_dot_exchange__pb2.SendCryptoRequest.SerializeToString,
            app_dot_services_dot_exchange_dot_exchange__pb2.SendCryptoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
