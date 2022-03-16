from makerscamp.db import *
from flask.cli import with_appcontext
from makerscamp import create_app

db_conn = DB
class User():
    
    @classmethod
    def create(cls, username):
        #with create_app().app_context():
        db_conn.exec(f"INSERT INTO users (username) VALUES ('{username}')")
