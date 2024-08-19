#!/usr/bin/python3
"""This script starts the Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns C followed by the value of the text variable"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

if __name__ == '__main__':
    """Ensures that the module is not executable when imported"""
    app.run(host='0.0.0.0', port=5000)
