from flask import Flask
import static
import chat
import sqlite3
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

app.add_url_rule('/', view_func=static.index, methods=['GET'])
app.add_url_rule('/static/<path:path>', view_func=static.static_files, methods=['GET'])

socketio.on_event('send message', chat.send_message)
socketio.on_event('join', chat.join)


def init_db():
    with sqlite3.connect("slacl.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Chat (
                            body TEXT,
                            time INTEGER,
                            user_id TEXT,
                            event_id TEXT
                        )""")
        conn.commit()


init_db()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')
