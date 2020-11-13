
import grpc
from google.protobuf.json_format import MessageToDict
from protos import bank_account_pb2 as pb2
from protos import bank_account_pb2_grpc as pb2_grpc

class BankAccountClient():

    channel = grpc.insecure_channel('localhost:50055')

    stub = pb2_grpc.BankAccountStub(channel)
    
    metadata = [('auth_token', 'v4gxva8SaBsC9v69zK92YpcE92BpiM')]
    

    def get_all(self):
        try:
            request = pb2.BankAccountEmpty()

            response = self.stub.get_all(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
        
    
    #def get_one_case_a(self):
    #
    #    try:
    #        request = pb2.BankAccountIdRequest(id="5fad855f9d7522d4371a61cf")
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
    #        request = pb2.BankAccountIdRequest(id="5f973f93ee05687f6130b9bf")
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
    #        request = pb2.BankAccountIdRequest(id="5f973f93ee05687f613")
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
                'chase': 'nose',
                'branchAddress': 'la casa de pepe',
                'routingNumber': "987646521",
                'bank': '5f973f93ee05687f6130b9c1',
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'chase': 'nose',
                'branchAddress': '',
                'routingNumber': "",
                'bank': '5f973f93ee05687f6130b9c1',
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'chase': 'nose',
                'branchAddress': 'la casa de pepe',
                'routingNumber': "987646521",
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fad855f9d7522d4371a61cf',
                'chase': 'nose',
                'branchAddress': 'la casa de pepita',
                'routingNumber': "987646521",
                'bank': '5f973f93ee05687f6130b9c1',
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fabfab9c291b373338722',
                'chase': 'nose',
                'branchAddress': 'la casa de pepita',
                'routingNumber': "987646521",
                'bank': '5f973f93ee05687f6130b9c1',
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fad855f9d7522d4371a61cf',
                'chase': 'nose',
                'branchAddress': '',
                'routingNumber': "",
                'bank': '5f973f93ee05687f6130b9c1',
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fad855f9d7522d4371a61cf',
                'chase': 'nose',
                'branchAddress': 'la casa de pepita',
                'bank': '5f973f93ee05687f6130b9c1',
                'checkingAccount': 'true'
            }

            request = pb2.BankAccountRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.BankAccountIdRequest(id='5fad855f9d7522d4371a61cf')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.BankAccountIdRequest(id='5fad855f9d7522d4371a61cf')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = BankAccountClient()

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