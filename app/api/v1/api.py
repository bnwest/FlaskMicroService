from flask_restplus import Namespace

ns = Namespace('v1', description='Predict Construction Time')


def build_namespaces():
    from api.v1.predict_construction_time import app
    return ns