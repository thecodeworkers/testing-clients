
import grpc
from google.protobuf.json_format import MessageToDict
from protos import american_banks_pb2
from protos import american_banks_pb2_grpc

class AmericanBankClient():

    channel = grpc.insecure_channel('localhost:50054')

    stub = american_banks_pb2_grpc.AmericanBanksStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    

    def get_all(self):
        try:
            request = american_banks_pb2.AmericanBankEmpty()

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
				'search': 'Bank'
			}
            
            request = american_banks_pb2.AmericanBanksTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def get_one_case_a(self):

        try:
            request = american_banks_pb2.AmericanBankIdRequest(id="5f973f93ee05687f6130b9bf")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = american_banks_pb2.AmericanBankIdRequest(id="5f973f93ee05687f6130b9b2")

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
            request = american_banks_pb2.AmericanBankIdRequest(id="5f973f93ee05687f613")

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
                'routingNumber': "987646521",
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A'
            }

            request = american_banks_pb2.AmericanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'routingNumber': "",
                'bankName': 'FaceBank',
                'swift': ''
            }

            request = american_banks_pb2.AmericanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'routingNumber': "",
                'bankName': 'FaceBank'
            }

            request = american_banks_pb2.AmericanBankNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fabfab9c291b373338722ad',
                'routingNumber': "123456",
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A'
            }

            request = american_banks_pb2.AmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fabfab9c291b373338722al',
                'routingNumber': "123456",
                'bankName': 'FaceBank',
                'swift': 'FACEUS1A'
            }

            request = american_banks_pb2.AmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fabfab9c291b373338722ad',
                'routingNumber': "123456",
                'bankName': 'FaceBank',
                'swift': ''
            }

            request = american_banks_pb2.AmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fabfab9c291b373338722ad',
                'routingNumber': "123456",
                'bankName': 'FaceBank',
            }

            request = american_banks_pb2.AmericanBankRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = american_banks_pb2.AmericanBankIdRequest(id='5fabfab9c291b373338722ad')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = american_banks_pb2.AmericanBankIdRequest(id='5fabfab9c291b373338722ad')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = AmericanBankClient()

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