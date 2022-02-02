# -*- coding: utf-8 -*-
from Convert import Convert
from flask import Flask
from flask_restful import Api
import sys


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Convert, '/convert')

    try:
        port = int(sys.argv[1])
    except IndexError:
        port = 8080
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)
