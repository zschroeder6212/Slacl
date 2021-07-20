import sqlite3
from uuid import uuid4
from flask import request, escape
import time


class Events:
    def __init__(self, db):
        """Init"""
        self.db = db
        self.init_db()

    def init_db(self):
        """Initialize database"""
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Events (
                                title TEXT,
                                body TEXT,
                                stars INTEGER,
                                time INTEGER,
                                user_id TEXT,
                                event_id TEXT,
                                area_id TEXT
                            )""")
            conn.commit()

    def get_event_details(self, event_id):
        """Get event details"""
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM Events WHERE event_id = :event_id", {'event_id': event_id})

            return dict(cur.fetchall()[0])

    def get_events_by_area(self, area_id, order):
        """Get list of events"""
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            """gonna need better filtering"""
            if order == 'new':
                cur.execute("SELECT event_id FROM Events WHERE area_id = :area_id ORDER BY time DESC", {'area_id': area_id})
            elif order == 'hot':
                cur.execute("SELECT event_id FROM Events WHERE area_id = :area_id ORDER BY stars DESC", {'area_id': area_id})

            events = {}
            events['events'] = []
            for row in cur.fetchall():
                events['events'].append(row['event_id'])

            return events

    def create_event(self):
        """Create event"""
        event = {
            'title': escape(request.json.get('title')),
            'body': escape(request.json.get('body')),
            'stars': 0,
            'time': int(time.time()),
            'user_id': request.json.get('user_id'),
            'event_id': uuid4().hex,
            'area_id': request.json.get('area_id')
        }

        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Events VALUES (:title, :body, :stars, :time, :user_id, :event_id, :area_id)", event)
            conn.commit()

        return ('', 200)
    
    def star_event(self, event_id):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE Events SET stars = stars + 1 WHERE event_id = :event_id", {'event_id': event_id})
            conn.commit()
        return '', 200
