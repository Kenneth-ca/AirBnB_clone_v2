#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    return 'HBNB'


@app.route('/c/<text>')
def hello_more(text):
    a_string = 'C ' + text
    return a_string.replace('_', ' ')


@app.route('/python/')
def hello_python():
    a_string = 'Python ' + 'is cool'
    return a_string.replace('_', ' ')


@app.route('/python/<text>')
def hello_python1(text):
    a_string = 'Python ' + text
    return a_string.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
