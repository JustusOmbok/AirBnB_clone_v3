#!/usr/bin/python3
"""Gives the amenities view."""
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/amenities', methods=['GET', 'POST'])
def amenities():
    """ Performs rest api funcs on amenities."""
    if request.method == 'GET':
        amenities = [amenity.to_dict()
                     for amenity in storage.all(Amenity).values()]
        return jsonify(amenities), 200

    if request.method == 'POST':
        if not request.is_json:
            return "Not a JSON", 400
        data = request.get_json()
        if 'name' not in data:
            return "Missing name", 400
        new_amenity = Amenity(**data)
        new_amenity.save()
        return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'])
def amenity(amenity_id):
    """Performs rest api funcs using amenity id."""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(amenity.to_dict()), 200
    elif request.method == 'PUT':
        if not request.is_json:
            return "Not a JSON", 400
        data = request.get_json()
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(amenity, key, value)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
    elif request.method == 'DELETE':
        amenity.delete()
        storage.save()
        return jsonify({}), 200
