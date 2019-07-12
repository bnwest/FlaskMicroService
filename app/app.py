"""
A Flask Micro Service app.
"""

import sys
import logging

import flask
import flask_restplus
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
