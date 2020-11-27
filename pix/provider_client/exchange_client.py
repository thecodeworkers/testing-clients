import grpc
from google.protobuf.json_format import MessageToDict
from protos import exchange_pb2
from protos import exchange_pb2_grpc

# NOTA: USAR LAS SIGUIENTES CREDENCIALES DE PRUEBAS PARA EL .ENV
# (SOLAMENTE EN CASO QUE NO SE QUIERA GENERAR UNAS CLAVES PROPIAS)
# OJO: PARA EL CASO B, SE DEBE ACCEDER A LA CUENTA DE LOCALBITCOINS Y CAMBIAR LOS PERMISOS DEL HMAC AUTH
# LOCALBITCOINS_APIKEY=3672261c83462214f34ac2210aee12be
# LOCALBITCOINS_APISECRET=e3d2fb627b2a742090baecc59a0316a578d48f8fb94786b87aaf9af15464035d

class ExchangeClient():
  channel = grpc.insecure_channel('localhost:50052')
  
  stub = exchange_pb2_grpc.ExchangeStub(channel)

  provider = [('provider', 'localbitcoins')]

  def send_crypto_case_c(self):
    try:
      data = {
        'currency': 'BTC',
        'address': 'ASouaiaoaosau93223j2323hhas',
        'amount': 1000
      }

      request = exchange_pb2.SendCryptoRequest(**data)
      response = self.stub.send_crypto(request=request, metadata=self.provider)

      return MessageToDict(response)

    except grpc.RpcError as e:
      print(e.details())
    except Exception as e:
      print(e.args)

  def send_crypto_case_d(self):
    try:
      data = {
        'currency': 'BTC',
        'address': '38GH4mZ5RZSPMooYrK1e6iQwCQaakRF6eC',
        'amount': 1000
      }

      request = exchange_pb2.SendCryptoRequest(**data)
      response = self.stub.send_crypto(request=request, metadata=self.provider)

      return MessageToDict(response)

    except grpc.RpcError as e:
      print(e.details())
    except Exception as e:
      print(e.args)

  def send_crypto_case_e(self):
    try:
      data = {
        'currency': 'BTC',
        'address': '38GH4mZ5RZSPMooYrK1e6iQwCQaakRF6eC',
        'amount': 0.000001
      }

      request = exchange_pb2.SendCryptoRequest(**data)
      response = self.stub.send_crypto(request=request, metadata=self.provider)

      return MessageToDict(response)

    except grpc.RpcError as e:
      print(e.details())
    except Exception as e:
      print(e.args)
  
client = ExchangeClient()

# print(client.send_crypto_case_c())
# print(client.send_crypto_case_d())
# print(client.send_crypto_case_e())
