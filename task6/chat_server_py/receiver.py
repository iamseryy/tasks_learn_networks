import threading
import sender

from datetime import datetime

from repo import clients


def handle(nicknames, clients, client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            sender.broadcast(clients, message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            sender.broadcast(clients, '{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
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
    while True:
        client, address = server.accept()
        print(f'{datetime.now()} INFO: Connected with {format(str(address))}')
        client.send('To connect to the chat you need to register. What is your nickname?'.encode('utf-8'))
        user = client.recv(1024).decode('utf-8')
        print(f'{datetime.now()} INFO: {user} joined')
        client.send('You have joined the chat'.encode('utf-8'))
        sender.broadcast(clients.find_all.values(), "{} joined!".format(user).encode('utf-8'))
        clients.add(user, client)

