
import grpc
from google.protobuf.json_format import MessageToDict
from protos import favorite_pb2 as pb2
from protos import favorite_pb2_grpc as pb2_grpc

class FavoriteClient():

    channel = grpc.insecure_channel('localhost:50055')

    stub = pb2_grpc.FavoriteStub(channel)
    
    metadata = [('auth_token', 'v4gxva8SaBsC9v69zK92YpcE92BpiM')]
    

    def get_all(self):
        try:
            request = pb2.FavoriteEmpty()

            response = self.stub.get_all(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
        
    
    #def get_one_case_a(self):
    #
    #    try:
    #        request = pb2.FavoriteIdRequest(id="5fad855f9d7522d4371a61cf")
    #
    #        response = self.stub.get(request=request, metadata=self.metadata)
    #
    #        return MessageToDict(response)
    #    except grpc.RpcError as e:
    #        print(e.details())
    #    except Exception as e:
    #        print(e.args)

        
    
    #def get_one_case_b(self):
    #
    #    try:
    #        request = pb2.FavoriteIdRequest(id="5f973f93ee05687f6130b9bf")
    #
    #        response = self.stub.get(request=request, metadata=self.metadata)
    #
    #        return MessageToDict(response)
    #    except grpc.RpcError as e:
    #        print(e.details())
    #        return e.details()
    #    except Exception as e:
    #        print(e.args)
    #        return e.args[0]

    #def get_one_case_c(self):
    #
    #    try:
    #        request = pb2.FavoriteIdRequest(id="5f973f93ee05687f613")
    #
    #        response = self.stub.get(request=request, metadata=self.metadata)
    #
    #        return MessageToDict(response)
    #    except grpc.RpcError as e:
    #        print(e.details())
    #        return e.details()
    #    except Exception as e:
    #        print(e.args)
    #        return e.args[0]

    def save_case_a(self):

        try:

            data = {
                'names': 'pepita',
                'username': 'decode9',
            }

            request = pb2.FavoriteNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'names': '',
                'username': 'decode9',
            }

            request = pb2.FavoriteNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'names': 'pepita',
            }

            request = pb2.FavoriteNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fad9cccc719aa40e5acef33',
                'names': 'pepe',
                'username': 'decode9',
            }

            request = pb2.FavoriteRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fad9cccc719aa40e5acef',
                'names': 'pepe',
                'username': 'decode9',
            }

            request = pb2.FavoriteRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fad9cccc719aa40e5acef33',
                'names': '',
                'username': 'decode9',
            }

            request = pb2.FavoriteRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fad9cccc719aa40e5acef33',
                'names': 'pepe'
            }

            request = pb2.FavoriteRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.FavoriteIdRequest(id='5fad9cccc719aa40e5acef33')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.FavoriteIdRequest(id='5fad9cccc719aa40e5acef33')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = FavoriteClient()

#print(client.get_all())
#print(client.save_case_a())
#print(client.save_case_b())
#print(client.save_case_c())
#print(client.update_case_a())
#print(client.update_case_b())
#print(client.update_case_c())
#print(client.update_case_d())
#print(client.delete_case_a())
#print(client.delete_case_b())