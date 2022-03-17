from makerscamp.db import *

db_conn = DB

class Message():

    def __init__(self, pk_id, user_id, channel_id, message):
        self.pk_id = pk_id
        self.user_id = user_id
        self.channel_id = channel_id
        self.message = message

    @classmethod
    def create(cls, id, user_id, channel_id, message):
        """send from html form, through route, to sql"""
        db_conn.exec(
            f"INSERT INTO messages (user_id, channel_id, message) VALUES ('{user_id}', '{channel_id}', '{message}')")
