#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
a_dict = storage.all('State').values()


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


@app.route('/number/<int:n>')
def hello_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html', my_dict=a_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
