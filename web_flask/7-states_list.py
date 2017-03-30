#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
"""
Very Simple Flask hello world
"""


app = Flask(__name__)


@app.route('/states_list')
def state_list():
    """
    Inserts all States from the database to the DOM
    """
    storall = storage.all("State").values()
    return (render_template('7-states_list.html', states=storall))


@app.teardown_appcontext
def teardown(exception):
    """
    Tears down the db connection
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
