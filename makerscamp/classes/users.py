from makerscamp.db import *
from werkzeug.security import check_password_hash  #generate_password_hash

db_conn = DB


class User():

    @classmethod
    def create(cls, username, password):
        #with create_app().app_context():
        db_conn.exec(
            f"INSERT INTO users (username, password) VALUES ('{username}, {password}')")

    @classmethod
    def find(cls, username):
        user = db_conn.exec(
            f"SELECT username FROM users WHERE username = ('{username}')")
        if user:
         return User(user['username'], user['password'], user['id'])
        else:
         return None
    
    @classmethod
    def find_by_id(cls, user_id):
        user = db_conn.exec(f"SELECT id FROM users WHERE id = ('{user_id}')")
        if user:
         return User(user['username'], user['password'], user['id'])
        else:
         return None



    def __init__(self, username, password, id):
        self.username = username
        self.password = password
        self.id = id

    def authenticate(self, password):
        return check_password_hash(self.password, password)


