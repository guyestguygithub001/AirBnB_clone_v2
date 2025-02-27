#!/usr/bin/python3
""" Starts Flask Web Application for C is FUN,"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints Message when / is called, """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints Message when /hbnb is called, """
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by its value of <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    """ Given Function,"""
    app.run(host='0.0.0.0', port=5000)

