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


@app.route('/hbnb')
def HBNB():

    """
    Returns the route /hbnb
    """
    return ('HBNB\n')


@app.route('/c/<value>')
def c_is(value):

    """
    Returns the route /c/<value>
    where <value> is any URI that the user requests
    """
    return ("C {:s}\n".format(value.replace("_", " ")))


@app.route('/python/')
@app.route('/python')
@app.route('/python/<text>')
def python_is(text="is cool"):

    """
    Returns the route /python/<text>
    where <value> is any URI that the user requests
    """
    return ("Python {:s}\n".format(text.replace("_", " ")))

if __name__ == "__main__":
    app.run(port=5000)
