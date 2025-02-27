#!/usr/bin/python3
"""
starts Flask web application,
"""
from models import storage
from flask import Flask, render_template
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """displays states, cities listed in alphabetical order,"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes storage on teardown,"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

