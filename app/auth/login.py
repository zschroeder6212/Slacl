# AS simeple as possbile flask google oAuth 2.0
from flask import Flask, redirect, url_for
from authlib.integrations.flask_client import OAuth
import os
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import sqlite3
import json

from auth.user import User

class Login:
    def __init__(self, app, db, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET):
        self.db = db
        self.oauth = OAuth(app)
        self.oauth.register(
            name='google',
            client_id=GOOGLE_CLIENT_ID,
            client_secret=GOOGLE_CLIENT_SECRET,
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_params=None,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            api_base_url='https://www.googleapis.com/oauth2/v1/',
            userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
            client_kwargs={'scope': 'openid email profile'},
        )
        self.login_manager = LoginManager(app)
        self.login_manager.login_view = "login"

        self.init_db()

        @self.login_manager.user_loader
        def load_user(user_id):
            try:
                with sqlite3.connect(self.db) as conn:
                    conn.row_factory = sqlite3.Row
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Users WHERE id = :id", {'id': user_id})
                    return User(dict(cur.fetchall()[0]), self.db)
            except Exception:
                return None

        @self.login_manager.unauthorized_handler
        def unauthorized():
            return '', 401

    def init_db(self):
        """Initialize database"""
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Users (
                        id TEXT,
                        name TEXT,
                        email TEXT,
                        picture TEXT,
                        UNIQUE(id)
                    )""")
            conn.commit()

    def login(self):
        google = self.oauth.create_client('google')
        redirect_uri = url_for('authorize', _external=True)
        return google.authorize_redirect(redirect_uri)


    def authorize(self):
        google = self.oauth.create_client('google')
        token = google.authorize_access_token()
        resp = google.get('userinfo')
        user_info = resp.json()
        user = User(user_info, self.db)
        login_user(user)

        return redirect('/')

    @login_required
    def logout(self):
        logout_user()
        return redirect('/')
