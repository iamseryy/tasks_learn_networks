import json
import socket
from datetime import datetime


def start(host, port):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((host, port))
    srv.listen()

    return srv


def handshake(server, clients):
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

        return user, client


def handle(clients, client):
    while True:
        try:
            message = json.loads(client.recv(1024))
            user = message["user"]
            print(f'{datetime.now()} INFO: message from {message["user"]} - {message["message"]}')
            broadcast(clients.find_chat_friends(client), f"{user}: {message['message']}".encode('utf-8'))
        except:
            user = clients.find_user(client)
            clients.remove_by_user(user)
            client.close()
            if clients:
                print(f'{datetime.now()} INFO: {user} left the chat')
                broadcast(clients.find_all().values(), f'{user} left the chat'.encode('utf-8'))

            break


def broadcast(clients, message):
    for client in clients:
        try:
            client.send(message)
        except:
            print("Some errors!!")
