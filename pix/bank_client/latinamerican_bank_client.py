
import grpc
from google.protobuf.json_format import MessageToDict
from protos import latinamerican_banks_pb2 as pb2
from protos import latinamerican_banks_pb2_grpc as pb2_grpc

class LatinAmericanBankClient():

    channel = grpc.insecure_channel('localhost:50054')

    stub = pb2_grpc.LatinAmericanBanksStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    

    def get_all(self):
        try:
            request = pb2.LatinAmericanBankEmpty()

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
				'search': '5f973f93ee05687f6130b9c5'
			}
            
            request = pb2.LatinAmericanBanksTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def get_one_case_a(self):

        try:
            request = pb2.LatinAmericanBankIdRequest(id="5f973f93ee05687f6130b9c5")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = pb2.LatinAmericanBankIdRequest(id="5f973f93ee05687f6130b9c4")

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
            request = pb2.LatinAmericanBankIdRequest(id="5f973f93ee05687f6130b")

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
                'country': 'Veneca',
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A',
            }

            request = pb2.LatinAmericanBankNotIdRequest(**data)

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
                'bankName': 'FaceBank',
                'swift': '',
            }

            request = pb2.LatinAmericanBankNotIdRequest(**data)

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
                'bankName': 'FaceBank',
            }

            request = pb2.LatinAmericanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fac46b05372177daef5aaeb',
                'country': 'MamadeEl',
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A',
            }

            request = pb2.LatinAmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fac46b05372177daef5aa',
                'country': 'MamadeEl',
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A',
            }

            request = pb2.LatinAmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fac46b05372177daef5aaeb',
                'country': 'MamadeEl',
                'bankName': 'FaceBank',
                'swift': '',
            }

            request = pb2.LatinAmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fac46b05372177daef5aaeb',
                'country': 'MamadeEl',
                'bankName': 'FaceBank'
            }

            request = pb2.LatinAmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.LatinAmericanBankIdRequest(id='5fac46b05372177daef5aaeb')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.LatinAmericanBankIdRequest(id='5fac46b05372177daef5aaeb')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = LatinAmericanBankClient()

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