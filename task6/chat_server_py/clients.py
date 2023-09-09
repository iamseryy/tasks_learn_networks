class Clients:

    def __init__(self):
        self._clients = {}

    def add(self, user, client):
        self._clients[user] = client

    def contains(self, user):
        return user in self._clients

    def remove_by_user(self, user):
        if self.contains(user):
            del self._clients[user]
        else:
            return False

    def remove_by_client(self, client):
        user = [key for key, value in self._clients if value == client]
        if self.contains(user[0]):
            del self._clients[user[0]]
        else:
            return False

    def find_user(self, client):
        return [key for key in self._clients if self._clients[key] == client][0]

    def find_all(self):
        return self._clients

    def find_chat_friends(self, client):
        return [item for item in self._clients.values() if item != client]

