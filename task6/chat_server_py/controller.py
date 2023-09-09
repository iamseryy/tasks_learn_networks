import threading
import server
from clients import Clients
from properties import HOST
from properties import PORT
from datetime import datetime


def start():
    print(f'{datetime.now()} INFO: Server started')
    srv = server.start(HOST, PORT)

    clients = Clients()
    while True:
        user, client = server.handshake(srv, clients)
        clients.add(user, client)

        server.broadcast(clients.find_chat_friends(client), f"{user} joined!".encode('utf-8'))

        thread = threading.Thread(target=server.handle, args=(clients, client,))
        thread.start()
