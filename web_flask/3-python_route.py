#!/usr/bin/python3
"""This script starts the Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a string 'Hello HBNB!'
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a string 'HBNB'
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns 'C' followed by the value of the text variable with underscores replaced by spaces.
    """
    return f'C {text.replace("_", " ")}'

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python' followed by the text, with underscores replaced by spaces.
    """
    return f'Python {text.replace("_", " ")}'

if __name__ == '__main__':
    """
    Ensures that the module is not executed when imported.
    """
    app.run(host='0.0.0.0', port=5000)
