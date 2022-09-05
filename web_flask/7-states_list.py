#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remSqlalchemy(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def statesList():
    """Displays a State list"""
    states=storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
