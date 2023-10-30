#!/usr/bin/python3
"""Give the status of the api to be okay."""

from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Returns the status in json."""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def get_stats():
    """Returns the total number of each object."""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return stats
