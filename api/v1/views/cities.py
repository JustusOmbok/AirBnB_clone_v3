#!/usr/bin/python3
"""Gives the cities view."""

from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/state/<state_id>/cities', methods=['GET', 'POST'])
def cities_by_state(state_id):
    """Performs functions on cities by state."""
    state = storage.get(State, state_id)
    if state is None:
        abort(400)

    if request.method == 'GET':
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities), 200

    if request.method == 'POST':
        if not request.is_json:
            return "Not a JSON", 400
        data = request.get_json()
        if 'name' not in data:
            return "Missing name", 400
        new_city = City(**data)
        new_city.state_id = state_id
        new_city.save()
        return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'])
def city(city_id):
    """Performs Rest api funcs on a single city."""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(city.to_dict()), 200
    elif request.method == 'PUT':
        if not request.is_json:
            return "Not a JSON", 400
        data = request.get_json()
        for key, value in data.items():
            if key not in ['id', 'state_id', 'created_at', 'updated_at']:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    elif request.method == 'DELETE':
        city.delete()
        storage.save()
        return jsonify({}), 200
