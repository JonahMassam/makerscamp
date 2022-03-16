from makerscamp.db import *
from makerscamp.classes.users import Users

class TestUsers():
    """Testing for the Users class"""

    def test_create_user(self):
        """confirm a user is entered into the database"""

        # create a db
        db = get_db()
        cur = db.cursor()

        # send user's information to DB ( no instance )
        username = "Joe Bloggs"
        Users.create(username)

        # get all results from users table
        cur.execute("SELECT * FROM users")
        users_array = cur.fetchall()

        # visibility
        print(users_array)
        assert username in users_array

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
#        """a user can be retrieved from the database"""
#
#    def test_find_all():
#        """all users can be retrieved from the database"""
#
#    def test_authenticate():
#        """a user can be authenticated""
