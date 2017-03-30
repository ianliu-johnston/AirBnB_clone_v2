#!/usr/bin/python3
from flask import Flask, Response
from flask import render_template
from models import storage
"""
Very Simple Flask hello world
"""


app = Flask(__name__)


@app.route('/states/')
@app.route('/states')
@app.route('/states/<state_id>')
def state_info(state_id="(nil)"):
    """
    Inserts all Cities in each State from the database to the DOM
    """
    storall = storage.all("State").values()
    state = "Not found!" if state_id != "(nil)" else state_id
    for states in storall:
        if states.id == state_id:
            state = states
    return (Response(render_template(
        '9-states.html',
        states=storall,
        state_id=state))
        )


@app.teardown_appcontext
def teardown(exception):
    """
    Tears down the db connection
    """
    storage.close()


@app.after_request
def add_headers(response):
    """
    Sets a custom http header
    """
    response.headers['Server'] = "apache/2.4.7"
    return (response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
