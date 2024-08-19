#!/usr/bin/python3
"""This script starts the Flask web application"""
from flask import Flask

app = Flask(__name__)

def replace_underscore_with_space(text):
    """Helper function to replace underscores with spaces in a string"""
    return text.replace('_', ' ')

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
    return f'C {replace_underscore_with_space(text)}'

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays "Python" followed by a text"""
    return f'Python {replace_underscore_with_space(text)}'

@app.route('/number/<int:n>/', strict_slashes=False)
def number(n):
    """Displays "n is a number" only if n is an integer"""
    return f'{n} is a number'

if __name__ == '__main__':
    """Ensures that the module is not executable when imported"""
    app.run(host='0.0.0.0', port=5000)
