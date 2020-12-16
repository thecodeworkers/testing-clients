
import grpc
from google.protobuf.json_format import MessageToDict
from protos import european_banks_pb2 as pb2
from protos import european_banks_pb2_grpc as pb2_grpc

class EuropeanBankClient():

    channel = grpc.insecure_channel('localhost:50054')

    stub = pb2_grpc.EuropeanBanksStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    

    def get_all(self):
        try:
            request = pb2.EuropeanBankEmpty()

            response = self.stub.get_all(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
        
    def get_table(self):
        try:
            data = {
				'page': 1,
				'per_page': 15,
				'search': '5f973f93ee05687f6130b9c2'
			}
            
            request = pb2.EuropeanBanksTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def get_one_case_a(self):

        try:
            request = pb2.EuropeanBankIdRequest(id="5f973f93ee05687f6130b9c2")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = pb2.EuropeanBankIdRequest(id="5f973f93ee05687f6130b9c7")

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
            request = pb2.EuropeanBankIdRequest(id="5f973f93ee05687f6130b9")

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
                'country': 'MamaMia',
                'iban': "987646521",
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A',
            }

            request = pb2.EuropeanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'country': 'MamaMia',
                'iban': "987646521",
                'bankName': 'FaceBank',
                'swift': '',
            }

            request = pb2.EuropeanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'country': 'MamaMia',
                'iban': "987646521",
                'bankName': 'FaceBank',
            }

            request = pb2.EuropeanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fac3fde640eefd9bc6c7fd7',
                'country': 'MamadeEl',
                'iban': "987646521",
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A',
            }

            request = pb2.EuropeanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fac3fde640eefd9bc6c7fd8',
                'country': 'MamadeEl',
                'iban': "987646521",
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A',
            }

            request = pb2.EuropeanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fac3fde640eefd9bc6c7fd7',
                'country': 'MamadeEl',
                'iban': "987646521",
                'bankName': 'FaceBank',
                'swift': '',
            }

            request = pb2.EuropeanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fac3fde640eefd9bc6c7fd7',
                'country': 'MamadeEl',
                'iban': "987646521",
                'bankName': 'FaceBank'
            }

            request = pb2.EuropeanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.EuropeanBankIdRequest(id='5fac3fde640eefd9bc6c7fd7')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.EuropeanBankIdRequest(id='5fac3fde640eefd9bc6c7fd7')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = EuropeanBankClient()

#print(client.get_all())
print(client.get_table())
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