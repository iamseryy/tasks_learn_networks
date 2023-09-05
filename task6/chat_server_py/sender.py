

def broadcast(clients, message):
    for client in clients:
        client.send(message)
