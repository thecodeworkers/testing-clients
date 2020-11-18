import grpc
from google.protobuf.json_format import MessageToDict
from protos import state_pb2
from protos import state_pb2_grpc

class StateClient():
	channel = grpc.insecure_channel('localhost:50053')
	
	stub = state_pb2_grpc.StateStub(channel)

	metadata = [('auth_token', 'tlOg1oSp8eo6E4hwQ8Ax2ico1FBTA6')]

	def get_all(self):
		try:
			request = state_pb2.StateEmpty()

			response = self.stub.get_all(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def get_one_case_a(self):
		try:
			request = state_pb2.StateIdRequest(id='5f3594f129ab93682403d8f7')
			response = self.stub.get(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def get_one_case_b(self):
		try:
			request = state_pb2.StateIdRequest(id='5f3594f129ab93682403d899')
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
			request = state_pb2.StateIdRequest(id='5f3594f129ab93682403d89')
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
				'country': '5f3594f129ab93682403d8c0',
				'name': 'Testing'
			}

			request = state_pb2.StateNotIdRequest(**data)

			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details)
		except Exception as e:
			print(e.args)

	def save_case_b(self):
		try:
			data = {
				'country': '',
				'name': ''
			}

			request = state_pb2.StateNotIdRequest(**data)
			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def save_case_c(self):
		try:
			data = {
				'country': '5f3594f129ab93682403d8c0'
			}

			request = state_pb2.StateNotIdRequest(**data)
			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_a(self):
		try:
			data = {
				'id': '5fb38eb6a97757f5af9eae18',
				'country': '5f3594f129ab93682403d8c0',
				'name': 'Testing2'
			}

			request = state_pb2.StateRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_b(self):
		try:
			data = {
				'id': '5fb38eb6a97757f5af9eae18',
				'country': '',
				'name': 'Testing2'
			}

			request = state_pb2.StateRequest(**data)

			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_c(self):
		try:
			data = {
				'id': '5fb38eb6a97757f5af9eae18',
				'country': '5f3594f129ab93682403d8c0',
				'name': ''
			}

			request = state_pb2.StateRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_d(self):
		try:
			data = {
				'id': '5fb38eb6a97757f5af9eae18',
				'country': '5f3594f129ab93682403d8c0'
			}

			request = state_pb2.StateRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def delete_case_a(self):
		try:
			request = state_pb2.StateIdRequest(id='5fb38eb6a97757f5af9eae18')
			response = self.stub.delete(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)
	
	def delete_case_b(self):
		try:
			request = state_pb2.StateIdRequest(id='5fb38eb6a97757f5af9eae99')
			response = self.stub.delete(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

client = StateClient()

# print(client.get_all())
# print(client.get_one_case_a())
# print(client.get_one_case_b())
# print(client.get_one_case_c())
# print(client.save_case_a())
# print(client.save_case_b())
# print(client.save_case_c())
# print(client.update_case_a())
# print(client.update_case_b())
# print(client.update_case_c())
#print(client.update_case_d())
# print(client.delete_case_a())
# print(client.delete_case_b())