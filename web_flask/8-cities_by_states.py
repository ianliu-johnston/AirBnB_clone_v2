#!/usr/bin/python3
from flask import Flask, Response
from flask import render_template
from models import storage
"""
Very Simple Flask hello world
"""


app = Flask(__name__)


@app.route('/cities_by_state')
def cities_by_state():
    """
    Inserts all States from the database to the DOM
    """
    storall = storage.all("State").values()
    return (Response(render_template('8-cities_by_states.html', states=storall)))


@app.teardown_appcontext
def teardown(exception):
    """
    Tears down the db connection
    """
    storage.close()

@app.after_request
def add_headers(response):
    response.headers['Server'] = "apache/2.4.7"
    return (response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
