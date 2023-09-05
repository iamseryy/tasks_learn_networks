class Users:
    def add(self, user):
        self._users.append(user)

    def contains(self, user):
        return user in self._users

    _users = []