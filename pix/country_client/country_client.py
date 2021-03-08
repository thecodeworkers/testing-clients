import grpc
from google.protobuf.json_format import MessageToDict
from protos import country_pb2
from protos import country_pb2_grpc

class CountryClient():
	channel = grpc.insecure_channel('localhost:50053')
	
	stub = country_pb2_grpc.CountryStub(channel)

	metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]

	def get_all(self):
		try:
			request = country_pb2.CountryEmpty()

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
				'search': ''
			}

			request = country_pb2.CountryTableRequest(**data)

			response = self.stub.table(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def get_one_case_a(self):
		try:
			request = country_pb2.CountryIdRequest(id='5f3594a529ab9368240305f5')
			response = self.stub.get(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def get_one_case_b(self):
		try:
			request = country_pb2.CountryIdRequest(id='5f3594a529ab936824030500')
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
			request = country_pb2.CountryIdRequest(id='5f3594a529ab93682403050')
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
				'name': 'Testing',
				'phone_prefix': '11',
				'active': False,
				'code': 'B2'	
			}

			request = country_pb2.CountryNotIdRequest(**data)

			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details)
		except Exception as e:
			print(e.args)

	def save_case_b(self):
		try:
			data = {
				'name': '',
				'phone_prefix': '',
				'active': False,
				'states': ''
			}

			request = country_pb2.CountryNotIdRequest(**data)
			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def save_case_c(self):
		try:
			data = {
				'phone_prefix': '+11',
				'active': False
			}

			request = country_pb2.CountryNotIdRequest(**data)
			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_a(self):
		try:
			data = {
				'id': '5f3594a629ab936824030714',
				'name': 'Albanie',
				'phone_prefix': '+355',
				'active': True
			}

			request = country_pb2.CountryRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_b(self):
		try:
			data = {
				'id': '5fb38529a97757f5af9eae99',
				'name': 'Testing2',
				'phone_prefix': '12',
				'active': False
			}

			request = country_pb2.CountryRequest(**data)

			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_c(self):
		try:
			data = {
				'id': '5f3594a629ab936824030714',
				'name': '',
				'phone_prefix': '+355'
			}

			request = country_pb2.CountryRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_d(self):
		try:
			data = {
				'phone_prefix': '',
				'active': False
			}

			request = country_pb2.CountryRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def delete_case_a(self):
		try:
			request = country_pb2.CountryIdRequest(id='5f73be2974224a639799c939')
			response = self.stub.delete(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)
	
	def delete_case_b(self):
		try:
			request = country_pb2.CountryIdRequest(id='5fb38529a97757f5af9eae99')
			response = self.stub.delete(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

client = CountryClient()

# print(client.get_all())
# print(client.get_table())
# print(client.get_one_case_a())
# print(client.get_one_case_b())
# print(client.get_one_case_c())
print(client.save_case_a())
# print(client.save_case_b())
# print(client.save_case_c())
# print(client.update_case_a())
# print(client.update_case_b())
# print(client.update_case_c())
# print(client.update_case_d())
#print(client.delete_case_a())
# print(client.delete_case_b())