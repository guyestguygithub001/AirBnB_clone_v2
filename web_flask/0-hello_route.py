#!/usr/bin/python3
""" Starts Flash Web Applicatioet, """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints Message when / is called, """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Function, """
    app.run(host='0.0.0.0', port=5000)


