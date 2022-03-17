from makerscamp.classes.db import *
from makerscamp.classes.user import User
from makerscamp import create_app

class TestUsers():
    """Testing for the Users class"""

    def test_create_user(self):
        """confirm a user is entered into the database"""

        # send user's information to DB ( no instance )
        username = "Joe Bloggs"
        User.create(username)

        # get all results from users table
        users_store = db_conn.exec("SELECT * FROM users")

        # visibility
        print(users_store)
        assert username in users_store

#    def test_find_user():
#        """a user can be retrieved from the database by username"""
#
#        # find a username within a database
#        name = "Joe Bloggs"
#
#        # return User object with username property
#        assert Users.find(name).username == username
#
#        
#
#    def test_find_by_id():
#        """a user can be retrieved from the database by pk_id"""
#
#    def test_find_all():
#        """all users can be retrieved from the database"""
#
#    def test_authenticate():
#        """a user can be authenticated""
