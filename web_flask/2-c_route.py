#!/usr/bin/python3
"""
simple implementation of routing pathes using flask
"""


from flask import Flask

hbnb = Flask(__name__)


@hbnb.route("/", strict_slashes=False)
def home_page():
    """
    returning simple welcome msg for home page
    """
    return "Hello HBNB!"


@hbnb.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """
    returning simple welcome msg for hbnb page
    """
    return "HBNB"


@hbnb.route(f"/c/<text>", strict_slashes=False)
def c_page(text):
    """
    returning simple welcome msg for files in c directory
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
