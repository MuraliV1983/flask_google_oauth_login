from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
from flask_session import Session
import os
import json

app = Flask(__name__)
app.secret_key = "RANDOM_SECRET_KEY"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Load Google OAuth credentials from client_secret.json
with open("client_secret.json", "r") as f:
    client_secrets = json.load(f)["web"]

# Google OAuth config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=client_secrets["client_id"],
    client_secret=client_secrets["client_secret"],
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['profile'] = user_info
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    user = session.get('profile')
    if user:
        return render_template("welcome.html", user=user)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
