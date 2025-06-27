# 🔐 Flask Google OAuth2 Login

A simple and secure **Flask app** that enables users to log in using their **Google account** via OAuth2.  
No password storage, no custom authentication — just clean Google login.

## 🚀 Features

- 🔐 Login with Google (OAuth 2.0)
- 👤 User profile fetched using Google's `userinfo` endpoint
- 📦 Flask + Authlib + Flask-Session integration
- 🌐 Easily extendable to your own apps

## 📁 Project Structure

flask_google_oauth_login/
├── app.py # Main Flask app
├── requirements.txt # Dependencies
├── .gitignore # Prevents committing secrets
├── templates/
│ ├── home.html # Homepage with login button
│ └── welcome.html # Displays user info after login
└── client_secret.json # NOT included – add your own

bash
Copy
Edit

## 🛠️ Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/MuraliV1983/flask_google_oauth_login.git
   cd flask_google_oauth_login
Install dependencies:

bash
Copy
Edit
py -m pip install -r requirements.txt
Create your OAuth2 credentials:

Go to Google Cloud Console

Create a project

Enable "OAuth Consent Screen"

Create OAuth2 credentials → OAuth client ID

Download client_secret.json and place it in your root folder

Run the app:

bash
Copy
Edit
py app.py
Visit http://localhost:5000 and try logging in!

🧠 Credits
Developed with ❤️ by Murali Dharan
Feel free to ⭐️ the repo or contribute ideas!

⚠️ Note
Never commit your client_secret.json!
Keep secrets in .env or use python-dotenv for better security.
