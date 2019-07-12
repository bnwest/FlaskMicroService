"""
A Flask Micro Service app.
"""

import sys

from flask import Flask, jsonify
from flask import __version__ as flask_version

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Dockerized: Hello World.'


@app.route('/get_versions')
def get_versions():
    versions = {
        'python': sys.version,
        'python-info': sys.version_info,
        'flask': flask_version,
        # numpy
        # tensorflow
        # etc.
    }
    return jsonify(versions)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
