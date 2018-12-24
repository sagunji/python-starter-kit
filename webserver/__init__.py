from __future__ import absolute_import
from flask import Flask, jsonify, request


def create_app():
    """Returns a flask app"""

    app = Flask(__name__, static_folder="static")
    return app


app = create_app()
app.config["PROPAGATE_EXCEPTIONS"] = True

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
