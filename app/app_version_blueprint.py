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
###############################################################################
# flask blueprint
###############################################################################
###############################################################################

v1 = flask.Blueprint(
    name='v1',
    import_name=__name__,
    url_prefix='/v1'
)

###############################################################################
# route: /get, version in blueprint
# usage: curl -i -X GET http://localhost:5000/v1/get
###############################################################################

@v1.route('/get')
def get1():
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
###############################################################################
# flask_restplus
###############################################################################
###############################################################################

subsys = flask.Blueprint(
    name='Subsystem',
    import_name=__name__,
    url_prefix='/subsys'
)

api = flask_restplus.Api(
    subsys, # flask.Blueprint
    title = 'Subsystem Service',
    version = '1.0',
    description = 'A set of services for the Subsytem',
    endpoint = 'bp-frp', # does not do a damn thing
)

ns2 = flask_restplus.Namespace(
    name='Subsystem Service v2',
    description='A set of services for the Subsytem v2.',
    path='/v2',
)

###############################################################################
# route: /get, version in namespace
# usage: curl -i -X GET http://localhost:5000/subsys/v2/get
###############################################################################

@ns2.route('/get')
class Get2(flask_restplus.Resource):
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

# Calling Api.init_app() is not required here because registering the blueprint
# with the app takes care of setting up the routing for the application.
# api.init_app(app)

app.register_blueprint(v1)
app.register_blueprint(subsys)

"""
$ curl -X GET http://localhost:5000/url_map
{
  "Subsystem.Subsystem Service v2_get2": "/subsys/v2/get", 
  "Subsystem.doc": "/subsys/", 
  "Subsystem.root": "/subsys/", 
  "Subsystem.specs": "/subsys/swagger.json", 
  "restplus_doc.static": "/swaggerui/<path:filename>", 
  "static": "/static/<path:filename>", 
  "url_map": "/url_map", 
  "v1.get1": "/v1/get"
}
"""

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
