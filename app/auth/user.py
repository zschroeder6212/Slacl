from flask_login import UserMixin
import sqlite3
from sqlite3 import IntegrityError

class User(UserMixin):
    is_authenticated = True
    is_active = True
    is_anonymous = False
    def __init__(self, user_info, db):
        self.db = db
        self.user_info = user_info
        self.id = user_info['id']
        self.name = user_info['name']
        self.email = user_info['email']
        self.picture = user_info['picture']
        self.init_db()

    def init_db(self):
        """Initialize database"""
        try:
            with sqlite3.connect(self.db) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Users VALUES (:id, :name, :email, :picture)", self.user_info)
                conn.commit()
        except IntegrityError:
            pass

    def get_id(self):
        return str(self.id)
