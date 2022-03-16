from tkinter.tix import Select
#from makerscamp.db import DB
#from makerscamp.classes.user import User

class Auth:
  def test():
    return "test"

  def authenticate(username, password):
    #if user in database
    #if password == password in database
    return true
    #else false

    user = User.find(username)
    DB.exec(f"SELECT * FROM users WHERE usernam={user.username}")
