import json
import socket

from properties import HOST
from properties import PORT


def receive(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write(user, client):
    while True:
        message = input('')
        if not message:
            continue

        client.send(json.dumps({"user": user, "message": message}).encode('utf-8'))


def handshake():
    while True:
        try:
            user = input("Choose your nickname: ")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, PORT))
            client.send(user.encode('utf-8'))
            message = client.recv(1024).decode('utf-8')

            if message == 'nickname exists':
                client.close()
                print('Nickname already exists, choose another one')
                continue

            print(message)

            return user, client

            break
        except:
            print("An error occured!")
            client.close()

            return None, None
