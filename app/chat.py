import sqlite3
import json
from flask import request, Response, escape
import time


# path /api/chat/messages
def get_messages():
    with sqlite3.connect("slacl.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Chat WHERE event_id = :event_id AND time > :after", {'event_id': request.form['event_id'], 'after': request.form['after']})
        
        response = {}
        response['messages'] = []
        for row in cur.fetchall():
            response['messages'].append(dict(row))

        return Response(json.dumps(response), mimetype='application/json')


# path /api/chat/send
def send_message():
    with sqlite3.connect("slacl.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Chat VALUES (:body, :time, :user_id, :event_id)",
                    {
                        'body': request.form['body'],
                        'time': int(time.time()),
                        'user_id': request.remote_addr,  # using IP until I setup proper auth
                        'event_id': request.form['event_id']
                    })
        conn.commit()
    return "OK"
