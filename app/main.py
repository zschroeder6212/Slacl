from flask import Flask
import static
from flask_socketio import SocketIO
from api.chat import Chat
from api.events import Events
from api.profile import get_user_details
from auth.login import Login
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
socketio = SocketIO(app)

chat = Chat('slacl.db')
events = Events('slacl.db')
login = Login(app, 'slacl.db', os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET"))

app.add_url_rule('/', view_func=static.index, methods=['GET'])
app.add_url_rule('/static/<path:path>', view_func=static.static_files, methods=['GET'])

app.add_url_rule('/api/events/create_event', view_func=events.create_event, methods=['POST'])
app.add_url_rule('/api/events/get_events_by_area/<area_id>/<order>', view_func=events.get_events_by_area, methods=['GET'])
app.add_url_rule('/api/events/get_event_details/<event_id>', view_func=events.get_event_details, methods=['GET'])
app.add_url_rule('/api/events/star/<event_id>', view_func=events.star_event, methods=['GET'])

app.add_url_rule('/api/profile/details', view_func=get_user_details, methods=['GET'])

app.add_url_rule('/auth/login', view_func=login.login, methods=['GET'])
app.add_url_rule('/auth/authorize', view_func=login.authorize, methods=['GET'])
app.add_url_rule('/auth/logout', view_func=login.logout, methods=['GET'])

socketio.on_event('send message', chat.send_message)
socketio.on_event('join', chat.join)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')
