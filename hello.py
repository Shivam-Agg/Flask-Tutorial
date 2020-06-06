from flask import Flask
from flask import redirect
from flask import abort
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    if any(not c.isalpha() for c in name):
        abort(404)
    return render_template('user.html', name = name)