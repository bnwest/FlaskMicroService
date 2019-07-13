"""
A Flask Micro Service app.
"""

import sys
import logging
import json

import flask

# flask_restplus.Model marshals and defines the structure
# of the data returned by the flask app's response
import flask_restplus

# marshmallow.Schema validates the structure and type of JSON data
# passed to the API during a request
import marshmallow


app = flask.Flask(__name__)
# api = flask_restplus.Api(app)


@app.route('/')
def hello_world():
    app.logger.info('HELLO WORLD.')
    return flask.jsonify('\nFlask Dockerized:\n\nHello World.\n')


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


@app.route('/echo')
def echo():
    """
    Usage:
        curl -i -X GET http://localhost:5000/echo -H "Content-Type: application/json" -d '{ "answer": 42 }'
    """
    # flask.request.json's name is a LIE; it is a python dictionary.
    payload = flask.request.json
    app.logger.info('echo called with payload:\n%s', flask.request.json)

    # karmaic return
    return flask.jsonify(payload)


if __name__ == '__main__':
    # app.logger.info('Starting flask app up ...') # no op since app is not running?
    app.run(debug=True,host='0.0.0.0')
