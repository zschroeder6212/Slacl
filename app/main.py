from flask import Flask
import static
import chat
import sqlite3

app = Flask(__name__)

app.add_url_rule('/', view_func=static.index, methods=['GET'])
app.add_url_rule('/static/<path:path>', view_func=static.static_files, methods=['GET'])

app.add_url_rule('/api/chat/messages', view_func=chat.get_messages, methods=['POST'])
app.add_url_rule('/api/chat/send', view_func=chat.send_message, methods=['POST'])


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
    app.run(debug=True, host='0.0.0.0')
