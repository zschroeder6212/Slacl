from flask import Flask
import static
from chat import Chat
import sqlite3
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

chat = Chat()

app.add_url_rule('/', view_func=static.index, methods=['GET'])
app.add_url_rule('/static/<path:path>', view_func=static.static_files, methods=['GET'])

socketio.on_event('send message', chat.send_message)
socketio.on_event('join', chat.join)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')
