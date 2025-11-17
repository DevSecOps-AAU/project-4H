
from src.users.queries import UserQueries


class UserServices:
    def __init__(self):
        self.user_queries = UserQueries()

    def login(self, username , passowrd):
        user, error =self.user_queries.login(username, passowrd)
        if not user:
            return error
        return user
    
    def register(self, username, email , passowrd):
        user, error =self.user_queries.login(username, email, passowrd)
        if not user:
            return error
        return user
