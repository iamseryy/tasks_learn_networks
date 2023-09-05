import threading
import sender

from datetime import datetime



def handle(nicknames, clients, client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            print(f'{datetime.now()} INFO: connected with {format(str(address))}, {format(nickname)} joined')
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


def receive(server):
    clients = []
    nicknames = []

    while True:
        # Accept Connection
        client, address = server.accept()

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print(f'{datetime.now()} INFO: connected with {format(str(address))}, {format(nickname)} joined')
        sender.broadcast(clients, "{} joined!".format(nickname).encode('utf-8'))

        client.send('Connected to server!'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(nicknames, clients, client,))
        thread.start()