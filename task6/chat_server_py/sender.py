

def broadcast(clients, message):
    for client in clients:
        client.send(message)

# def broadcast(clients, message):
#     for client in clients:
#         client.send(message)
