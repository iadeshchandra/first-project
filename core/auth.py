# Authentication Manager

class AuthenticationManager:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError('User already exists.')
        self.users[username] = password

    def authenticate(self, username, password):
        if username not in self.users:
            return False
        return self.users[username] == password

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]

    def list_users(self):
        return list(self.users.keys())
