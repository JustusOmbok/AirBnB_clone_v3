#!/usr/bin/python3
""" The master application file."""
from flask import Flask, Blueprint
from flask import jsonify
from os import getenv


app= Flask(__name__)
from api.v1.views import app_views
from models import storage


app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """Handles the 404 errors."""
    return jsonify({"error": "Not found"})

@app.teardown_appcontext
def teardown(exception):
    """The method that closes the session."""
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = getenv("HBNB_API_PORT", default="5000")
    app.run(debug=True, host=host, port=port, threaded=True)