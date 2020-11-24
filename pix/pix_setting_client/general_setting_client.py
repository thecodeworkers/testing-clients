
import grpc
from google.protobuf.json_format import MessageToDict
from protos import general_setting_pb2 as pb2
from protos import general_setting_pb2_grpc as pb2_grpc

class GeneralSettingClient():

    channel = grpc.insecure_channel('localhost:50056')

    stub = pb2_grpc.GeneralSettingStub(channel)
    
    metadata = [('auth_token', 'oEBh7jcZ8QBF8iLYKT7nSc8Pj0DUcZ')]
    

    def get_all(self):
        try:
            request = pb2.GeneralSettingEmpty()

            response = self.stub.get_all(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
        
    
    def get_one_case_a(self):

        try:
            request = pb2.GeneralSettingIdRequest(id="5fa59e5959b108b64090f69d")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = pb2.GeneralSettingIdRequest(id="5fa59e5959b108b64090f69f")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
            return e.details()
        except Exception as e:
            print(e.args)
            return e.args[0]

    def get_one_case_c(self):

        try:
            request = pb2.GeneralSettingIdRequest(id="5fa59e5959b108b64090f6")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
            return e.details()
        except Exception as e:
            print(e.args)
            return e.args[0]

    def save_case_a(self):

        try:

            data = {
                'app': "tumamafuemia",
                'sessionTime': 4000,
                'multiSession': False
            }

            request = pb2.GeneralSettingNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'app': "",
                'sessionTime': 4000,
                'multiSession': False
            }

            request = pb2.GeneralSettingNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'app': "tumamafuemia",
                'sessionTime': 4000,
            }

            request = pb2.GeneralSettingNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fb53b0829559513db16fae9',
                'app': "tumamafuedeel",
                'sessionTime': 4000,
                'multiSession': False
            }

            request = pb2.GeneralSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fb53b0829559513db16fa',
                'app': "tumamafuedeel",
                'sessionTime': 4000,
                'multiSession': False
            }

            request = pb2.GeneralSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fb53b0829559513db16fae9',
                'app': "",
                'sessionTime': 4000,
                'multiSession': False
            }

            request = pb2.GeneralSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fb53b0829559513db16fae9',
                'app': "tumamafuedeel",
                'sessionTime': 4000,
            }

            request = pb2.GeneralSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.GeneralSettingIdRequest(id='5fb53b0829559513db16fae9')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.GeneralSettingIdRequest(id='5fb53b0829559513db16fae9')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = GeneralSettingClient()

#print(client.get_all())
#print(client.get_one_case_a())
#print(client.get_one_case_b())
#print(client.get_one_case_c())
#print(client.save_case_a())
#print(client.save_case_b())
#print(client.save_case_c())
#print(client.update_case_a())
#print(client.update_case_b())
#print(client.update_case_c())
#print(client.update_case_d())
#print(client.delete_case_a())
#print(client.delete_case_b())