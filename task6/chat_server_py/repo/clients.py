class Clients:

    def add(self, user, client):
        self._clients[user] = client

    def contains(self, user):
        return user in self._clients

    def remove(self, user):
        if self.contains(user):
            del self._clients[user]
        else:
            return False

    def find_all(self):
        return self._clients

    @staticmethod
    def _init_dict():
        clients = {}
        return clients

    _clients = _init_dict()
