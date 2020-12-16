
import grpc
from google.protobuf.json_format import MessageToDict
from protos import credit_cards_pb2 as pb2
from protos import credit_cards_pb2_grpc as pb2_grpc

class CreditCardClient():

    channel = grpc.insecure_channel('localhost:50054')

    stub = pb2_grpc.CreditCardsStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    

    def get_all(self):
        try:
            request = pb2.CreditCardEmpty()

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
				'search': 'Bank of America'
			}
            
            request = pb2.CreditCardTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def get_one_case_a(self):

        try:
            request = pb2.CreditCardIdRequest(id="5f973f93ee05687f6130b9c8")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = pb2.CreditCardIdRequest(id="5f973f93ee05687f6130b9c4")

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
            request = pb2.CreditCardIdRequest(id="5f973f93ee05687f6130b9")

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
                'entity': 'Bank Of America',
                'cvcValidation': 2,
                'numberValidation': 12,
                'regex': '[0-9]?'
            }

            request = pb2.CreditCardNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'entity': '',
                'cvcValidation': 2,
                'numberValidation': 12,
                'regex': '[0-9]?'
            }

            request = pb2.CreditCardNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'entity': 'Bank Of America',
                'cvcValidation': 2,
                'numberValidation': 12,
            }

            request = pb2.CreditCardNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fac598e5372177daef5aaed',
                'entity': 'Bank Of Americas',
                'cvcValidation': 2,
                'numberValidation': 12,
                'regex': '[0-9]?'
            }

            request = pb2.CreditCardRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fac598e5372177daef5aae',
                'entity': 'Bank Of America',
                'cvcValidation': 2,
                'numberValidation': 12,
                'regex': '[0-9]?'
            }

            request = pb2.CreditCardRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fac598e5372177daef5aaed',
                'entity': 'Bank Of America',
                'cvcValidation': 2,
                'numberValidation': 12,
                'regex': ''
            }

            request = pb2.CreditCardRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fac598e5372177daef5aaed',
                'entity': 'Bank Of America',
                'cvcValidation': 2,
                'numberValidation': 12,
            }

            request = pb2.CreditCardRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.CreditCardIdRequest(id='5fac598e5372177daef5aaed')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.CreditCardIdRequest(id='5fac598e5372177daef5aaed')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = CreditCardClient()

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