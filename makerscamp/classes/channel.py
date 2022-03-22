from makerscamp.classes.db import DB

class Channel:
  
  @classmethod
  def create(cls, name):
    DB.exec(f"INSERT INTO channels (name) VALUES ('{DB.sanitize(name)}') ")

  @classmethod
  def find(cls, name):
    channel = DB.exec(
      f"SELECT * FROM channels WHERE name = '{DB.sanitize(name)}'"
    )
    if channel:
      return Channel(channel[0][0], channel[0][1])

  @classmethod
  def find_by_id(cls, id):
    channel = DB.exec(
      f"SELECT * FROM channels WHERE name = '{id}'"
    )
    if channel:
      return Channel(channel[0][0], channel[0][1])

  @classmethod
  def get_messages(cls, id):
    return DB.exec(f"SELECT * FROM messages WHERE channel_id={id}")

  @classmethod
  def all(cls):
    return [ Channel(ch[0], ch[1]) for ch in DB.exec("SELECT * FROM channels")]

  def __init__(self, id, name):
      self.id = id
      self.name = name

  def get_users(self):
    users = DB.exec(
      f"SELECT * FROM user_channels WHERE channel_id = {self.id}"
    )
    return users

  def add_user(self, user_id):
    DB.exec(
      f"INSERT INTO user_channels (user_id, channel_id) VALUES ({user_id}, {self.id})"
    )

  def add_message():
    pass
