from flask import Flask
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!!!</h1>'

@app.route('/google')
def google():
    return redirect('https://www.google.com/')

@app.route('/user/<name>')
def user(name):
    if any(not c.isalpha() for c in name):
        abort(404)
    return f'<h2>Hello {name}. Hope you are doing well!!'