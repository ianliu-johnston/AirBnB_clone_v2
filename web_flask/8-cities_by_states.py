#!/usr/bin/python3
from flask import Flask
from flask import render_template
"""
Very Simple Flask hello world
"""


app = Flask(__name__)


@app.route('/states_list')
def hello_HBNB():

    """
    Just returns text
    """
    return ('Hello HBNB!')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
