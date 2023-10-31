#!/usr/bin/python3
"""Performs Restful api tasks with states."""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def states():
    """Gives the default functins on all the states."""
    if request.method == 'GET':
        states = [state.to_dict()
                  for state in storage.all(State).values()]
        return jsonify(states), 200
    elif request.method == 'POST':
        if not request.is_json:
            return "Not a JSON", 400
        data = request.get_json()
        if 'name' not in data:
            return "Missing name", 400
        new_state = State(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def state(state_id):
    """Gives the default functions on a specific state."""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(state.to_dict()), 200
    elif request.method == 'PUT':
        if not request.is_json:
            return "Not a JSON", 400
        data = request.get_json()
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200
    elif request.method == 'DELETE':
        state.delete()
        storage.save()
        return jsonify({}), 200
