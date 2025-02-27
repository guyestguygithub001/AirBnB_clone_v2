#!/usr/bin/python3
"""
starts Flask web application,
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays HTML page with states listed in alphabetical order,"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """closes storage on teardown,"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

