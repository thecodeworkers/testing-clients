import grpc
from google.protobuf.json_format import MessageToDict
from protos import language_pb2 as pb2
from protos import language_pb2_grpc as pb2_grpc

class LanguageClient():

    channel = grpc.insecure_channel('localhost:50051')

    stub = pb2_grpc.LanguageStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    
    def get_all(self): 
          try:
              request = pb2.LanguageEmpty()

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
				'search': 'es'
			}
            
            request = pb2.LanguageTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
          
    def get_one_case_a(self):

        try:
            request = pb2.LanguageIdRequest(id="5fbec0867c6bee540d3c3358")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def get_one_case_b(self):

        try:
            request = pb2.LanguageIdRequest(id="5f3594a529ab9368240305f8")

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
            request = pb2.LanguageIdRequest(id="5fbe91247e0177f24465d4b5o")

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
                'name': 'Español',
                'prefix': 'es',
                'active': 1,
            }

            request = pb2.LanguageNotIdRequest(**data)

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
                'prefix': 'es',
                'active': 1,
            }

            request = pb2.LanguageNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:
            data = {
              'name': '',
            }

            request = pb2.LanguageNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
             'id': '5fbed5777e0177f24465d4b8',
             'name': 'Spanish',
             'prefix': 'esp',
             'active': 1,
            }

            request = pb2.LanguageRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
             'id': '5f3594a529ab9368240305f8',
             'name': '',
             'prefix': 'es',
             'active': 1
            }

            request = pb2.LanguageRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)


    def update_case_c(self):

        try:

            data = {
             'id': '5fbec0ae7c6bee540d3c3359',
             'name': '',
             'prefix': '',
             'active': 1
            }

            request = pb2.LanguageRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
             'id': '5f3594a529ab9368240305f8',
             'name': 'Español',
            #  'prefix': 'es',
            #  'active': 1
            }

            request = pb2.LanguageRequest(**data) 

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try: 

            request = pb2.LanguageIdRequest(id='5fbeddcf7e0177f24465d4bc')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.LanguageIdRequest(id='5f3594a529ab9368240305f8')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = LanguageClient()

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