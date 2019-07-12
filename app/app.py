"""
A Flask Micro Service app.
"""

import sys
import logging

import flask

# flask_restplus.Model marshals and defines the structure
# of the data returned by the flask app's response
import flask_restplus

# marshmallow.Schema validates the structure and type of JSON data
# passed to the API during a request
import marshmallow

LOGGER = logging.getLogger(__name__)

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Dockerized: Hello World.'


@app.route('/get_versions')
def get_versions():
    versions = {
        'python': sys.version,
        'python-info': sys.version_info,
        'flask': flask.__version__,
        'flask_restplus': flask_restplus.__version__,
        'marshmallow': marshmallow.__version__,
        # numpy
        # tensorflow
        # etc.
    }
    return flask.jsonify(versions)


if __name__ == '__main__':
    LOGGER.info('Starting flask app up ...')
    app.run(debug=True,host='0.0.0.0')
