import sqlite3
from flask import request, escape
import time
from flask_socketio import emit, join_room


def get_all_messages(event_id):
    with sqlite3.connect("slacl.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Chat WHERE event_id = :event_id", {'event_id': event_id})

        messages = {}
        messages['messages'] = []
        for row in cur.fetchall():
            messages['messages'].append(dict(row))

        return messages


# 'join' websocket event handler
def join(data):
    join_room(data['event_id'])
    emit("push message", get_all_messages(data['event_id']))


# 'send message' websocket event handler
def send_message(data):
    message = {
        'messages': [{
            'body': escape(data['body']),
            'time': int(time.time()),
            'user_id': request.remote_addr,  # using IP until I setup proper auth
            'event_id': escape(data['event_id'])
        }]
    }

    print(message)
    with sqlite3.connect("slacl.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Chat VALUES (:body, :time, :user_id, :event_id)", message['messages'][0])
        conn.commit()
    emit("push message", message, room=data['event_id'])
