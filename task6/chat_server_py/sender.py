
def broadcast(clients, message):
    for client in clients:
        try:
            client.send(message)
        except:
            print("Some errors!!")
