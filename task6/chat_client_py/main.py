import socket
import threading


# # Choosing Nickname
# nickname = input("Choose your nickname: ")
#
# # Connecting To Server
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 55555))


# Listening to Server and Sending Nickname
# def receive():
#     while True:
#         try:
#             # Receive Message From Server
#             # If 'NICK' Send Nickname
#             message = client.recv(1024).decode('utf-8')
#             if message == 'NICK':
#                 client.send(nickname.encode('utf-8'))
#             else:
#                 print(message)
#         except:
#             # Close Connection When Error
#             print("An error occured!")
#             client.close()
#             break


def receive(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


def write(user, client):
    while True:
        message = '{}: {}'.format(user, input(''))
        client.send(message.encode('utf-8'))


# Starting Threads For Listening And Writing
# receive_thread = threading.Thread(target=receive)
# receive_thread.start()
#
# write_thread = threading.Thread(target=write)
# write_thread.start()


def handshake():
    while True:
        try:
            user = input("Choose your nickname: ")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 55555))
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


print('Client chat started')

user, client = handshake()

if client and user:
    threading.Thread(target=receive, args=(client,)).start()
    threading.Thread(target=write, args=(user,client,)).start()

else:
    print('Error')
