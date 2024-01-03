from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/soccerbase')
def soccerbase():
    return {'Player': 'Country'}