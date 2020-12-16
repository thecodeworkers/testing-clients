
import grpc
from google.protobuf.json_format import MessageToDict
from protos import role_pb2 as pb2
from protos import role_pb2_grpc as pb2_grpc

class RoleClient():

    channel = grpc.insecure_channel('localhost:50050')

    stub = pb2_grpc.RoleStub(channel)
    
    metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]
    

    def get_all(self):
        try:
            request = pb2.RoleEmpty()

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
				'search': '5fad7dcb8b95abcc04e9d15e'
			}
            
            request = pb2.RoleTableRequest(**data)
            
            response = self.stub.table(request=request, metadata=self.metadata)
            
            return MessageToDict(response)
        
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def get_one_case_a(self):

        try:
            request = pb2.RoleIdRequest(id="5fa57c49a9075b215128ad4f")

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:
            request = pb2.RoleIdRequest(id="5fa57c49a9075b215128ad4k")

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
            request = pb2.RoleIdRequest(id="5fa57c49a9075b215128ad")

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
                'name': 'megaUser',
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleNotIdRequest(**data)

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
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_d(self):

        try:

            data = {
                'name': 'megaUser',
                'code': '002',
                'scopes': ['00_role_get'],
            }

            request = pb2.RoleNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fad4d7bf75b9fae9b957db6',
                'name': 'UserMega',
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fad4d7bf75b9fae9b957db7',
                'name': 'UserMega',
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fad4d7bf75b9fae9b957db6',
                'name': '',
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fad4d7bf75b9fae9b957db6',
                'code': '002',
                'scopes': ['00_role_table'],
            }

            request = pb2.RoleRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.RoleIdRequest(id='5fad7dcb8b95abcc04e9d15f')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.RoleIdRequest(id='5fad4d7bf75b9fae9b957db6')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_c(self):
        try:

            request = pb2.RoleIdRequest(id='5fad7dcb8b95abcc04e9d15e')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = RoleClient()

#print(client.get_all())
print(client.get_table())
#print(client.get_one_case_a())
#print(client.get_one_case_b())
#print(client.get_one_case_c())
#print(client.save_case_a())
#print(client.save_case_b())
#print(client.save_case_c())
#print(client.save_case_d())
#print(client.update_case_a())
#print(client.update_case_b())
#print(client.update_case_c())
#print(client.update_case_d())
#print(client.delete_case_a())
#print(client.delete_case_b())
#print(client.delete_case_c())