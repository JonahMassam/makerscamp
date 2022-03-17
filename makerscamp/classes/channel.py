from makerscamp.classes.db import DB

class Channel:
  
  @classmethod
  def create(cls, name):
    DB.exec(f"INSERT IN channels (name) VALUES ('{name}') ")

  @classmethod
  def find(name):
    channel = DB.exec(
      f"SELECT * FROM channels WHERE name = '{name}'"
    )
    if channel:
      return Channel(channel[0][0], channel[0][1])

  @classmethod
  def find_by_id(id):
    channel = DB.exec(
      f"SELECT * FROM channels WHERE name = '{id}'"
    )
    if channel:
      return Channel(channel[0][0], channel[0][1])
    

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

  def get_messages():
    pass