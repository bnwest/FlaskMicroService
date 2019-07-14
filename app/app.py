"""
A Flask Micro Service app.
"""

import sys
import logging
from datetime import datetime

import flask

# flask_restplus.Model marshals and defines the structure
# of the data returned by the flask app's response
import flask_restplus

# marshmallow.Schema validates the structure and type of JSON data
# passed to the API during a request
import marshmallow


app = flask.Flask(__name__)

# flask signals:
# https://flask.palletsprojects.com/en/1.0.x/api/#core-signals-list

###############################################################################
# /endpoint
###############################################################################

@app.route('/')
def hello_world():
    app.logger.info('HELLO WORLD.')
    return flask.jsonify('\nFlask Dockerized:\n\nHello World.\n')

###############################################################################
# /get_versions endpoint
###############################################################################

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

###############################################################################
# /echo endpoint
###############################################################################

class EchoGetRequestSchema(marshmallow.Schema):
    """
    Data required for the /echo endpoint
    """
    answer = marshmallow.fields.Int(required=True)
    # marshmallow.fields.{Dict, List, Tuple, String, UUID, Number, Integer, Decimal, Boolean, Float, DateTime, Time, Date, Url}

    @marshmallow.validates('answer')
    def validate_lead_time(self, answer):
        """ Answer must be 42. """
        if answer is not 42:
            raise marshmallow.ValidationError('Answer must 42. Deep Thought has degreed.')


@app.route('/echo')
def echo():
    """
    Usage:
        curl -i --request GET http://localhost:5000/echo --header "Content-Type: application/json" --data '{ "answer": 42 }'
    """
    # flask.request.json's name is a LIE; it is a python dictionary.
    payload = flask.request.json
    app.logger.info('echo called with payload:\n%s', payload)

    # validate the incoming request JSON payload via marshmallow
    kwargs = EchoGetRequestSchema().load(payload)
    app.logger.info('marshmallow load returns:\n%s', kwargs)

    # karmaic return
    return flask.jsonify(payload)

###############################################################################
# /echo_plus endpoint
###############################################################################

api = flask_restplus.Api(app)

echo_plus_model = api.model('Echo Get Response Model', {
    'answer':  flask_restplus.fields.Integer(required=True, description='The answer to all questions.'),
    "utc":     flask_restplus.fields.DateTime(attribute=lambda x: datetime.utcnow()),
    "utc_alt": flask_restplus.fields.String(attribute=lambda x: str(datetime.utcnow())), # str() is not required
    # flask_restplus.fields.{FormattedString, Url, Date, DateTime, Fixed, Float, Integer, String}
})

@api.route('/echo_plus')
class EchoPlus(flask_restplus.Resource):
    """
    Usage:
        curl -i --request GET http://localhost:5000/echo_plus --header "Content-Type: application/json" --data '{ "answer": 42 }'
    """

    @api.marshal_with(echo_plus_model)
    def get(self):
        payload = flask.request.json
        app.logger.info('echo_plus called with payload:\n%s', payload)

        # validate the incoming request JSON payload via marshmallow
        kwargs = EchoGetRequestSchema().load(payload)
        app.logger.info('marshmallow load returns:\n%s', kwargs)

        # karmaic-ish return
        payload['ignore_fools_errand'] = True # gets ignored when marshalled by model
        # create/marshal a response via a flask_restplus model (see @api.marshal_with() decorator),
        # which ignores and adds as it sees fit
        return payload

###############################################################################
# main
###############################################################################

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
