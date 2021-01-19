import grpc
from google.protobuf.json_format import MessageToDict
from protos import currency_pb2 as pb2
from protos import currency_pb2_grpc as pb2_grpc

class CurrencyClient():

    channel = grpc.insecure_channel('localhost:50051')

    stub = pb2_grpc.CurrencyStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    
    def get_all(self): 
          try:
              request = pb2.CurrencyEmpty()

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
				'search': 'BTC'
			}
            
            request = pb2.CurrencyTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
          
    def get_one_case_a(self):

        try:
            request = pb2.CurrencyIdRequest(id="5f8e3d112c3795c5ce889915")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def get_one_case_b(self):

        try:
            request = pb2.CurrencyIdRequest(id="5f8e3d112c3795c5ce88991b")

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
            request = pb2.CurrencyIdRequest(id="5f973f93ee05687f6130b9")

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
                'name': 'Ripple',
                'color': '#212121',
                'gradients': ['#1976d2', '#FFFFFF', '#000000'],
                'active': 1,
                'type': 'CRYPTO',
                'symbol': 'RPL',
                'price': 10
            }

            request = pb2.CurrencyNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:
            data = {
             'name': '',
             'color': '#999999',
             'gradients': ['#1976d2', '#FFFFFF', '#000000'],
             'active': 1,
             'type': 'CRYPTO',
             'symbol': 'CRY',
             'price': 1
            }

            request = pb2.CurrencyNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:
            data = {
             'name': 'Monero',
             'color': '#212121',
             'gradients': ['#1976d2', '#FFFFFF', '#000000'],
             'active': 1,
             'type': 'CRYPTO',
             'symbol': 'XRP',
            #  'price': 1
            }

            request = pb2.CurrencyNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
             'id': '5fbd94b67e0177f24465d49a',
             'name': 'MONERO',
             'color': '#555555',
             'gradients': ['#1976d2', '#FFFFFF', '#000000'],
             'active': 1,
             'type': 'CRYPTO',
             'symbol': '',
             'price': 100
            }

            request = pb2.CurrencyRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
             'id': '5fbd94b67e0177f24465d49a',
             'name': 'MONERO',
             'color': '#555555',
             'gradients': ['#1976d2', '#FFFFFF', '#000000'],
             'active': 1,
             'type': 'CRYPTO',
             'symbol': '',
             'price': 100
            }

            request = pb2.CurrencyRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
             'id': '5fbda3537e0177f24465d4a2',
             'name': '',
             'color': '#1976d2',
             'gradients': ['#1976d2', '#FFFFFF', '#000000'],
             'active': 1,
             'type': 'CRYPTO',
             'symbol': 'CRY',
             'price': 1
            }

            request = pb2.CurrencyRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
             'id': '5fbda3537e0177f24465d4a2',
             'name': '',
             'color': '',
             'gradients': ['#1976d2', '#FFFFFF', '#000000'],
             'active': 1,
             'type': 'CRYPTO',
             'symbol': '',
            #  'price': 1
            }

            request = pb2.CurrencyRequest(**data) 

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try: 

            request = pb2.CurrencyIdRequest(id='5fbda3537e0177f24465d4a2')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.CurrencyIdRequest(id='5f3594a529ab9368240305f8')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = CurrencyClient()

#print(client.get_all())
print(client.get_table())
# print(client.get_one_case_a())
# print(client.get_one_case_b())
# print(client.get_one_case_c())
# print(client.save_case_a())
# print(client.save_case_b())
# print(client.save_case_c())
# print(client.update_case_a())
# print(client.update_case_b())
# print(client.update_case_c())
# print(client.update_case_d())
# print(client.delete_case_a())
# print(client.delete_case_b())