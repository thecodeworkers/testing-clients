
import grpc
from google.protobuf.json_format import MessageToDict
from protos import session_pb2 as pb2
from protos import session_pb2_grpc as pb2_grpc

class SessionClient():

    channel = grpc.insecure_channel('localhost:50056')

    stub = pb2_grpc.SessionStub(channel)
    
    metadata = [('auth_token', 'oEBh7jcZ8QBF8iLYKT7nSc8Pj0DUcZ')]
    

    def get_all(self):
        try:
            request = pb2.SessionEmpty()

            response = self.stub.get_all(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
        
    
    def get_one_case_a(self):

        try:

            data = {
                'ip': '120.0.0.0',
                'userAgent': 'su casa'
            }

            request = pb2.SessionOneRequest(**data)

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

        
    
    def get_one_case_b(self):

        try:

            data = {
                'ip': '120.0.0.1',
                'userAgent': 'su casa'
            }
            request = pb2.SessionOneRequest(**data)

            response = self.stub.get(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
            return e.details()
        except Exception as e:
            print(e.args)
            return e.args[0]

    #def get_one_case_c(self):
    #
    #    try:
    #        request = pb2.SessionIdRequest(id="5fa59e5959b108b64090f6")
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
                'app': "tumamafuemia",
                'ip': '120.0.0.0',
                'location':'la pepas',
                'userAgent': 'pepeto',
                'valid': False,
                'active': False,
            }

            request = pb2.SessionNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_b(self):

        try:

            data = {
                'app': "",
                'ip': '120.0.0.0',
                'location':'la pepara',
                'userAgent': 'pepeto',
                'valid': False,
                'active': False,
            }

            request = pb2.SessionNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)
    
    def save_case_c(self):

        try:

            data = {
                'app': "",
                'ip': '120.0.0.2',
                'location':'la pepa',
                'userAgent': 'pepeto',
                'valid': False,
                'active': False,
            }

            request = pb2.SessionNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def save_case_d(self):

        try:

            data = {
                'app': "tumamafuemia",
                'ip': '120.0.0.0',
                'location':'la pepa',
                'userAgent': 'pepeto',
                'valid': True,
                'active': True,
            }

            request = pb2.SessionNotIdRequest(**data)

            response = self.stub.save(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_a(self):

        try:

            data = {
                'id': '5fb5565a47c0e54420b6e4a3',
                'valid': False,
                'active': False,
            }

            request = pb2.SessionRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_b(self):

        try:

            data = {
                'id': '5fb5565a47c0e54420b6e4',
                'valid': False,
                'active': False,
            }

            request = pb2.SessionRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_c(self):

        try:

            data = {
                'id': '5fb5565a47c0e54420b6e4a3',
                'app': '',
                'valid': False,
                'active': False,
            }

            request = pb2.SessionRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def update_case_d(self):

        try:

            data = {
                'id': '5fb5565a47c0e54420b6e4a3',
                'app': '',
                'valid': False,
            }

            request = pb2.SessionRequest(**data)

            response = self.stub.update(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_a(self):

        try:

            request = pb2.SessionIdRequest(id='5fb5565a47c0e54420b6e4a3')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

    def delete_case_b(self):

        try:

            request = pb2.SessionIdRequest(id='5fb5565a47c0e54420b6e4a3')

            response = self.stub.delete(request=request, metadata=self.metadata)

            return MessageToDict(response)
        except grpc.RpcError as e:
            print(e.details())
        except Exception as e:
            print(e.args)

client = SessionClient()

#print(client.get_all())
#print(client.get_one_case_a())
#print(client.get_one_case_b())
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