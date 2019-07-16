"""
A Flask Micro Service app
with versions in routes,
via flask and flask_restplus.
"""

import sys

import flask
import flask_restplus
import marshmallow

###############################################################################
###############################################################################
# flask
###############################################################################
###############################################################################

app = flask.Flask(__name__)

@app.route('/url_map')
def url_map():
    routes= {}
    map = app.url_map
    for rule in map._rules:
        routes[rule.endpoint] = rule.rule
    return flask.jsonify(routes)

###############################################################################
# route: /get, no version
# usage: curl -i -X GET http://localhost:5000/get
###############################################################################

@app.route('/get')
def get1():
    payload = flask.request.json
    versions = {
        'flask.request.path': flask.request.path,
        'flask.request.full_path': flask.request.full_path,
        'flask.request.url': flask.request.url,
        'flask.request.base_url': flask.request.base_url,
        'flask.request.url_root': flask.request.url_root,
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

# app.add_url_rule(rule='/get', endpoint='get1', view_func=get1)

###############################################################################
# route: /v1/get, hardcoded version 1
# usage: curl -i -X GET http://localhost:5000/v1/get
###############################################################################

@app.route('/v1/get')
def get2():
    payload = flask.request.json
    versions = {
        'flask.request.url': flask.request.url,
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
# route: /vN/get, variable version N where N > 1
# usage: curl -i -X GET http://localhost:5000/v2/get
###############################################################################

@app.route('/v<int:version_id>/get')
def get3(version_id):
    payload = flask.request.json
    versions = {
        'flask.request.url': flask.request.url,
        'app': version_id,
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
###############################################################################
# flask_restplus
###############################################################################
###############################################################################

api = flask_restplus.Api(
    title = 'Subsystem-Service',
    version = '1.0',
    description = 'A set of services for the Subsytem',
    endpoint = 'frp', # does not do a damn thing
)

###############################################################################
# route: /frp/get, flask_restplus, no version
# usage: curl -i -X GET http://localhost:5000/frp/get
###############################################################################

@api.route('/frp/get')
class Get4(flask_restplus.Resource):
    """
    Usage:
        curl -i --request GET http://localhost:5000/frp/get
    """
    def get(self):
        payload = flask.request.json
        versions = {
            'flask.request.url': flask.request.url,
            'api': api.version,
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
###############################################################################
# flask_restplus namespace
###############################################################################
###############################################################################

ns2 = flask_restplus.Namespace(
    name='Subsystem-Service-v2',
    description='A set of service for the Subsytem v2.',
    path='/v2',
)

###############################################################################
# route: /v2/frp/get, flask_restplus, version in namespace
# usage: curl -i -X GET http://localhost:5000/v2/frp/get
###############################################################################

@ns2.route('/frp/get')
class Get5(flask_restplus.Resource):
    def get(self):
        payload = flask.request.json
        versions = {
            'flask.request.url': flask.request.url,
            'api': api.version,
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
# main
###############################################################################

api.add_namespace(ns2)

api.init_app(app)

"""
$ curl -X GET http://localhost:5000/url_map
{
  "Subsystem-Service-v2_get5": "/v2/frp/get", 
  "doc": "/", 
  "get1": "/get", 
  "get2": "/v1/get", 
  "get3": "/v<int:version_id>/get", 
  "get4": "/frp/get", 
  "restplus_doc.static": "/swaggerui/<path:filename>", 
  "root": "/", 
  "specs": "/swagger.json", 
  "static": "/static/<path:filename>", 
  "url_map": "/url_map"
}
"""

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
