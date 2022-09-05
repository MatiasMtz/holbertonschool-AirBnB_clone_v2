#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remSqlalchemy(self):
    storage.close()


@app.route('/states', strict_slashes=False)
def statesList():
    """Displays a State list"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def stateByID(id):
    """shows an specific state"""
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
