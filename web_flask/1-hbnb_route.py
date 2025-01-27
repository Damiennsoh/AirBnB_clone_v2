#!/usr/bin/python3
"""
A simple flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """This route returns hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """This route return HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
