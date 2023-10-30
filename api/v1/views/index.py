#!/usr/bin/python3
"""Give the status of the api to be okay."""

from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Returns the status in json."""
    return jsonify({"status": "OK"})