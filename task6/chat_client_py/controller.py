import threading

from client import handshake, receive, write


def start():
    print('Client chat started')

    user, client = handshake()

    if client and user:
        threading.Thread(target=receive, args=(client,)).start()
        threading.Thread(target=write, args=(user, client,)).start()

    else:
        print('Error')
