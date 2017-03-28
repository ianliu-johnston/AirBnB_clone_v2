#!/usr/bin/python3
from flask import Flask
"""
Very Simple Flask hello world
"""


app = Flask(__name__)


@app.route('/')
def hello_HBNB():

    """
    Just returns text
    """
    return ('Hello HBNB!\n')


if __name__ == "__main__":
    app.run(port=5000)
