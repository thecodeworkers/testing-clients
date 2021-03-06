# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app.protos import european_banks_pb2 as european__banks__pb2


class EuropeanBanksStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.table = channel.unary_unary(
                '/EuropeanBanks/table',
                request_serializer=european__banks__pb2.EuropeanBanksTableRequest.SerializeToString,
                response_deserializer=european__banks__pb2.EuropeanBanksTableResponse.FromString,
                )
        self.get_all = channel.unary_unary(
                '/EuropeanBanks/get_all',
                request_serializer=european__banks__pb2.EuropeanBankEmpty.SerializeToString,
                response_deserializer=european__banks__pb2.EuropeanBanksMultipleResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/EuropeanBanks/get',
                request_serializer=european__banks__pb2.EuropeanBankIdRequest.SerializeToString,
                response_deserializer=european__banks__pb2.EuropeanBanksResponse.FromString,
                )
        self.save = channel.unary_unary(
                '/EuropeanBanks/save',
                request_serializer=european__banks__pb2.EuropeanBankNotIdRequest.SerializeToString,
                response_deserializer=european__banks__pb2.EuropeanBanksResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/EuropeanBanks/update',
                request_serializer=european__banks__pb2.EuropeanBankRequest.SerializeToString,
                response_deserializer=european__banks__pb2.EuropeanBanksResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/EuropeanBanks/delete',
                request_serializer=european__banks__pb2.EuropeanBankIdRequest.SerializeToString,
                response_deserializer=european__banks__pb2.EuropeanBanksResponse.FromString,
                )


class EuropeanBanksServicer(object):
    """Missing associated documentation comment in .proto file."""

    def table(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EuropeanBanksServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'table': grpc.unary_unary_rpc_method_handler(
                    servicer.table,
                    request_deserializer=european__banks__pb2.EuropeanBanksTableRequest.FromString,
                    response_serializer=european__banks__pb2.EuropeanBanksTableResponse.SerializeToString,
            ),
            'get_all': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all,
                    request_deserializer=european__banks__pb2.EuropeanBankEmpty.FromString,
                    response_serializer=european__banks__pb2.EuropeanBanksMultipleResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=european__banks__pb2.EuropeanBankIdRequest.FromString,
                    response_serializer=european__banks__pb2.EuropeanBanksResponse.SerializeToString,
            ),
            'save': grpc.unary_unary_rpc_method_handler(
                    servicer.save,
                    request_deserializer=european__banks__pb2.EuropeanBankNotIdRequest.FromString,
                    response_serializer=european__banks__pb2.EuropeanBanksResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=european__banks__pb2.EuropeanBankRequest.FromString,
                    response_serializer=european__banks__pb2.EuropeanBanksResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=european__banks__pb2.EuropeanBankIdRequest.FromString,
                    response_serializer=european__banks__pb2.EuropeanBanksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EuropeanBanks', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EuropeanBanks(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def table(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EuropeanBanks/table',
            european__banks__pb2.EuropeanBanksTableRequest.SerializeToString,
            european__banks__pb2.EuropeanBanksTableResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EuropeanBanks/get_all',
            european__banks__pb2.EuropeanBankEmpty.SerializeToString,
            european__banks__pb2.EuropeanBanksMultipleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EuropeanBanks/get',
            european__banks__pb2.EuropeanBankIdRequest.SerializeToString,
            european__banks__pb2.EuropeanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EuropeanBanks/save',
            european__banks__pb2.EuropeanBankNotIdRequest.SerializeToString,
            european__banks__pb2.EuropeanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EuropeanBanks/update',
            european__banks__pb2.EuropeanBankRequest.SerializeToString,
            european__banks__pb2.EuropeanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EuropeanBanks/delete',
            european__banks__pb2.EuropeanBankIdRequest.SerializeToString,
            european__banks__pb2.EuropeanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
