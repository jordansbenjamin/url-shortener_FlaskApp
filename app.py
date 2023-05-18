from flask import Flask

app = Flask(__name__)

# Homepage/base url route
@app.route('/')
def home():
    return 'Hello Flask!'

# Name of route and function does not need to match
@app.route('/about')
def about():
    return 'This is a url shortener'