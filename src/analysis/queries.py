
from datetime import datetime
from src.database.execute import DBClinet
from werkzeug.security import generate_password_hash, check_password_hash
from src.users.schema import users

class UserQueries:
    def __init__(self):
        self.db_client = DBClinet()

    def login(self, username, password):
        query = users.select().where(users.c.username == username)
        row = self.db_client.execute_one(query)
        if not row:
            return None, "no user have been found" 
        if not check_password_hash(row['password'], password):
            return None, "Invalid password"
        return row
    
    def register(self, username, email , password):
        hashed_password = generate_password_hash(password)
        query = users.insert().values(username = username, email=email, password=hashed_password)
        row = self.db_client.execute_one(query)
        if not row:
            return None, "user account creation issue"
        return row
