import grpc
from google.protobuf.json_format import MessageToDict
from protos import auth_pb2 as pb2
from protos import auth_pb2_grpc as pb2_grpc

class AuthClient():

    channel = grpc.insecure_channel('localhost:50050')
    stub = pb2_grpc.AuthStub(channel)

    def signup_case_a(self):
        try:
            data = {
                'email': "jorgelo_9@hotmail.com",
                "username": "decode91",
                'password': 'Luisbas12.',
                'role': '000'
            }

            request = pb2.SignupRequest(**data)

            response = self.stub.signup(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def signup_case_b(self):
        try:
            data = {
                'email': "jorge@hotmail.com",
                "username": "decode912",
                'password': '',
                'role': '000'
            }
            
            request = pb2.SignupRequest(**data)

            response = self.stub.signup(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def signup_case_c(self):
        try:
            data = {
                'email': "jorgelo_9@hotmail.com",
                "username": "decode91",
                'role': '000'
            }
            
            request = pb2.SignupRequest(**data)

            response = self.stub.signup(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def signin_case_a(self):
        try:
            data = {
                "username": "decode91",
                'password': 'Luisbas12.',
            }

            request = pb2.SigninRequest(**data)

            response = self.stub.signin(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def signin_case_b(self):
        try:
            data = {
                "username": "jorge@hotmail.com",
                'password': 'Luisbas12.',
            }

            request = pb2.SigninRequest(**data)

            response = self.stub.signin(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def signin_case_c(self):
        try:
            data = {
                "username": "decode91",
                'password': '',
            }

            request = pb2.SigninRequest(**data)

            response = self.stub.signin(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def signin_case_d(self):
        try:
            data = {
                "username": "decode91",
            }

            request = pb2.SigninRequest(**data)

            response = self.stub.signin(request)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def signup_case_f(self):
        try:
            data = {
                'email': "testuser1@mail.com",
                'password': '12345678',
                'role': '001'
            }

            request = pb2.SignupRequest(**data)
            response = self.stub.signup(request)

            return MessageToDict(response)

        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def signup_case_g(self):
        try:
            data = {
                'email': "testuser2@mail.com",
                'password': '12345678',
                'role': '001',
                'profile': {}
            }

            request = pb2.SignupRequest(**data)
            response = self.stub.signup(request)

            return MessageToDict(response)

        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def signup_case_h(self):
        try:
            data = {
                'email': "testuser3@mail.com",
                'password': '12345678',
                'role': '001',
                'profile': {
                    'name': 'Test',
                    'lastname': 'User'
                }
            }

            request = pb2.SignupRequest(**data)
            response = self.stub.signup(request)

            return MessageToDict(response)

        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
        

client = AuthClient()

#print(client.signup_case_a())
#print(client.signup_case_b())
#print(client.signup_case_c())
#print(client.signin_case_a())
#print(client.signin_case_b())
#print(client.signin_case_c())
#print(client.signin_case_d())
