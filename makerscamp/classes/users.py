from makerscamp.db import *

db_conn = DB
class User():
    
    @classmethod
    def create(cls, username):
        #with create_app().app_context():
        db_conn.exec(f"INSERT INTO users (username) VALUES ('{username}')")

    def __init__(self, username):
        self.username = username
