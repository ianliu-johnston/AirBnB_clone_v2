#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_HBNB():
    return (' Hello HBNB!')
