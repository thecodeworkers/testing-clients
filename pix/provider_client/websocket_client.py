
import grpc

from protos import websocket_pb2
from protos import websocket_pb2_grpc

class WebsocketClient():

  channel = grpc.insecure_channel('localhost:50052')
  stub = websocket_pb2_grpc.WebsocketsStub(channel)

  def activate_websocket(self):
    data = {
      'active': True
    }

    request = websocket_pb2.SendWebsocketRequest(**data)

    response = self.stub.activate_websocket(request)

    return response
    
  def deactivate_websocket(self):
    data = {
      'active': False
    }

    request = websocket_pb2.SendWebsocketRequest(**data)

    response = self.stub.activate_websocket(request)

    return response


client = WebsocketClient()

print(client.activate_websocket())
# print(client.deactivate_websocket())
