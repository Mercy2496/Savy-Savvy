#!/usr/bin/env python3
"""
...
"""
import sys
sys.path.extend(["../", "../../"])

from models import *
from os import getenv
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from api.V1.endpoints import endpoints


app = Flask(__name__)
app.register_blueprint(endpoints)

CORS(app)
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})



if __name__ == "__main__":
    host = getenv("API_HOST", "127.0.0.1")
    port = int(getenv("API_PORT", 5005)
)
    app.run(debug=True, host="127.0.0.1", port=port, threaded=True)