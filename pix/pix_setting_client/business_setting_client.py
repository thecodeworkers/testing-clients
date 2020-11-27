
import grpc
from google.protobuf.json_format import MessageToDict
from protos import business_setting_pb2 as pb2
from protos import business_setting_pb2_grpc as pb2_grpc

class BusinessSettingClient():

    channel = grpc.insecure_channel('localhost:50056')

    stub = pb2_grpc.BusinessSettingStub(channel)
    
    metadata = [('auth_token', 'oEBh7jcZ8QBF8iLYKT7nSc8Pj0DUcZ')]
    

    def get_all(self):
        try:
            request = pb2.BusinessSettingEmpty()

            response = self.stub.get_all(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
        
    
    def get_one_case_a(self):

        try:
            request = pb2.BusinessSettingIdRequest(id="5fa5815af3ec54c3cb4f1f97")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = pb2.BusinessSettingIdRequest(id="5fa5815af3ec54c3cb4f1f98")

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
            request = pb2.BusinessSettingIdRequest(id="5fa5815af3ec54c3cb4f1")

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
                'app': "987646521",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': 'tipejo',
                'limitType': 'limitante'
            }

            request = pb2.BusinessSettingNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'app': "987646521",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': '',
                'limitType': 'limitante'
            }

            request = pb2.BusinessSettingNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'app': "987646521",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': '',
            }

            request = pb2.BusinessSettingNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fb482e6df4e3d747f07cc33',
                'app': "tata",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': 'tipejo',
                'limitType': 'limitante'
            }

            request = pb2.BusinessSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fb482e6df4e3d747f07cc',
                'app': "tata",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': 'tipejo',
                'limitType': 'limitante'
            }

            request = pb2.BusinessSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fb482e6df4e3d747f07cc33',
                'app': "987646521",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': '',
                'limitType': 'limitante'
            }

            request = pb2.BusinessSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fb482e6df4e3d747f07cc33',
                'app': "987646521",
                'fee': [
                    {
                        'feeType': 'tipejo',    
                        'number': 250,
                        'calculationType': 'division'
                    }
                ],
                'limit': [
                    {
                        'limitType': 'limitante',
                        'minimum': 2,
                        'maximum': 10,
                    }
                ],
                'feeType': 'tipejo',
            }

            request = pb2.BusinessSettingRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.BusinessSettingIdRequest(id='5fb482e6df4e3d747f07cc33')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.BusinessSettingIdRequest(id='5fb482e6df4e3d747f07cc33')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = BusinessSettingClient()

print(client.get_all())
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