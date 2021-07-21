import sqlite3
from flask import escape
import time
from flask_socketio import emit, join_room


class Chat:
    def __init__(self, db):
        self.db = db
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Chat (
                                body TEXT,
                                time INTEGER,
                                user_id TEXT,
                                event_id TEXT
                            )""")
            conn.commit()

    def get_all_messages(self, event_id):
        """Get a list of messages by ID"""
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM Chat WHERE event_id = :event_id", {'event_id': event_id})

            messages = {}
            messages['messages'] = []
            for row in cur.fetchall():
                messages['messages'].append(dict(row))

            return messages

    def join(self, data):
        """Join event handler. Called when the user joins a room"""
        join_room(data['event_id'])
        emit("init messages", self.get_all_messages(data['event_id']))

    def send_message(self, data):
        """Send a message to room"""
        message = {
            'body': escape(data['body']),
            'time': int(time.time()),
            'user_id': data['user_id'],  # using IP until I setup proper auth
            'event_id': data['event_id']
        }

        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Chat VALUES (:body, :time, :user_id, :event_id)", message)
            conn.commit()
        emit("push message", message, room=data['event_id'])
