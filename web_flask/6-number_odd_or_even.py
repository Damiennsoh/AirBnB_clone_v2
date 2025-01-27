#!/usr/bin/python3
"""
A simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """This route returns hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """This route return HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Returns 'C' followed by the text provided"""
    text = text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Returns the text provided"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """Returns the number only if it is an integer"""
    return "{} is number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_page(n):
    """
    Returns an html page with the number provided
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
     Determines whether the number provided
     is even on odd
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
