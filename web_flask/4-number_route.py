#!/usr/bin/python3
""""""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def holberton():
    """"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """"""
    return 'C ' + text.replace("_", " ")
    
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonis(text='is cool'):
    """"""
    return 'Python ' + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """"""
    return '{} is a number'.format(n)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
