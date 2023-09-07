import socket
import receiver

from datetime import datetime
from properties import HOST
from properties import PORT



# import json
#
# m ={"id": 2, "name": "abc"}
# jsonObj = json.dumps(m)
# print(m)
# print(jsonObj)
#
# y = json.loads(jsonObj)
# print(y)
# print(y["name"])




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f'{datetime.now()} INFO: Server started')
#receiver.receive(server)
receiver.handshake(server)