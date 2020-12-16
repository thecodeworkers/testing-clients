import grpc
from google.protobuf.json_format import MessageToDict
from protos import city_pb2
from protos import city_pb2_grpc
import time
class CityClient():
	channel = grpc.insecure_channel('localhost:50053')
	
	stub = city_pb2_grpc.CityStub(channel)

	metadata = [('auth_token', 'oO85tpozsiVo6u0vukCufS4cp4ygmt')]

	def get_all(self):
		try:
			request = city_pb2.CityEmpty()

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
				'search': '5f3594f029ab93682403d6ce'
			}

			request = city_pb2.CityTableRequest(**data)

			response = self.stub.table(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)
			
	def get_one_case_a(self):
		try:
			request = city_pb2.CityIdRequest(id='5f3594f129ab93682403d902')
			response = self.stub.get(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def get_one_case_b(self):
		try:
			request = city_pb2.CityIdRequest(id='5f3594f129ab936824039999')
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
			request = city_pb2.CityRequest(id='5f3594f129ab93682403999')
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
				'state': '5f3594f129ab93682403d8ff',
				'name': 'Testing'
			}

			request = city_pb2.CityNotIdRequest(**data)

			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details)
		except Exception as e:
			print(e.args)

	def save_case_b(self):
		try:
			data = {
				'state': '5f3594f129ab93682403d8ff',
				'name': ''
			}

			request = city_pb2.CityNotIdRequest(**data)
			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def save_case_c(self):
		try:
			data = {
				'state': '5f3594f129ab93682403d8ff'
			}

			request = city_pb2.CityNotIdRequest(**data)
			response = self.stub.save(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_a(self):
		try:
			data = {
				'id': '5f3594f129ab93682403d904',
				'state': '5f3594f129ab93682403d8ff',
				'name': 'Testing2'
			}

			request = city_pb2.CityRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_b(self):
		try:
			data = {
				'id': '5f3594f129ab93682403999',
				'state': '5f3594f129ab93682403d8ff',
				'name': 'Testing2'
			}

			request = city_pb2.CityRequest(**data)

			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def update_case_c(self):
		try:
			data = {
				'id': '5f3594a529ab9368240305f8',
				'state': '5f3594a529ab9368240305f6',
				'name': ''
			}

			request = city_pb2.CityRequest(**data)
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
				'state': '5f3594a529ab9368240305f6'
			}

			request = city_pb2.CityRequest(**data)
			response = self.stub.update(request=request, metadata=self.metadata)

			return MessageToDict(response)

		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

	def delete_case_a(self):
		try:
			request = city_pb2.CityIdRequest(id='5f3594f129ab93682403d904')
			response = self.stub.delete(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)
	
	def delete_case_b(self):
		try:
			request = city_pb2.CityIdRequest(id='5f3594f129ab93682403d904')
			response = self.stub.delete(request=request, metadata=self.metadata)

			return MessageToDict(response)
		except grpc.RpcError as e:
			print(e.details())
		except Exception as e:
			print(e.args)

client = CityClient()
start_time = time.time()

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
print("--- %s seconds ---" % (time.time() - start_time))