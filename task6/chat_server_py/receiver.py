import json
import threading
import sender

from datetime import datetime

from repo.clients import Clients


def handle(clients, client):
    while True:
        try:
            message = json.loads(client.recv(1024))
            user = message["user"]
            print(f'{datetime.now()} INFO: message from {message["user"]} - {message["message"]}')
            sender.broadcast([item for item in clients if item != client], f"{user}: {message['message']}".encode('utf-8'))
#            sender.broadcast([item for item in clients if item != client], message)
        except:
            # Removing And Closing Clients
            # index = clients.index(client)
            # clients.remove(client)
            # client.close()
            # nickname = nicknames[index]
            # sender.broadcast(clients, f'{nicknames} left!'.format(nickname).encode('utf-8'))
            # nicknames.remove(nickname)
            break

# Receiving / Listening Function //Handshake
def receive(server):
    clients = []
    nicknames = []

    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        sender.broadcast(clients, "{} joined!".format(nickname).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(nicknames, clients, client,))
        thread.start()

def handshake(server):
    clients = Clients()
    while True:
        client, address = server.accept()
        user = client.recv(1024).decode('utf-8')

        print(f'{datetime.now()} INFO: Connected with {format(str(address))}; user: {user}')

        if clients.contains(user):
            client.send('nickname exists'.encode('utf-8'))
            print(f'{datetime.now()} INFO: Nickname: {user} exists, connection closed')
            client.close()
            continue

        print(f'{datetime.now()} INFO: {user} joined')
        client.send('You have joined the chat'.encode('utf-8'))
        sender.broadcast(clients.find_all().values(), f"{user} joined!".encode('utf-8'))
        clients.add(user, client)

        thread = threading.Thread(target=handle, args=(clients.find_all().values(), client,))
        thread.start()