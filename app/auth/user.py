from flask_login import UserMixin
import sqlite3
from sqlite3 import IntegrityError


class User(UserMixin):
    is_active = True
    is_anonymous = False

    def __init__(self, user_info, db):
        self.db = db
        self.user_info = user_info
        self.init_db()

    def is_authenticated(self):
        return self.id is not None

    def init_db(self):
        """Initialize database"""
        try:
            with sqlite3.connect(self.db) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Users VALUES (:id, :name, :email, :picture)", self.user_info)
                conn.commit()
        except IntegrityError:
            pass

    def get_user_info(self):
        return self.user_info

    def get_id(self):
        return str(self.user_info['id'])
