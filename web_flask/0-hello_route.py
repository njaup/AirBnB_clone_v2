#!/usr/bin/python3
"""This script initializes a Flask web server application"""
from flask import Flask

web_app = Flask(__name__)

@web_app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a greeting message
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    Executes the Flask web server if this module is run as the main program
    """
   web_app.run(host='0.0.0.0', port=5000)
