from makerscamp.db import get_db
class Users():
    
    @classmethod
    def create(cls, username):
        with get_db.cursor() as cur:
            cur.execute('INSERT INTO users (username)' 'VALUES ?', (username))
            db.commit()
