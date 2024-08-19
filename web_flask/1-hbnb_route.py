#!/usr/bin/python3
"""This script starts the Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting for the root URL"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """Returns a string for the /hbnb URL"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
