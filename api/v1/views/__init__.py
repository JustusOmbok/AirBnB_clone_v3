#!/usr/bin/python3
"""The file imports blueprint from flask."""

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *

app_views = Blueprint('app_views', __name__, url_prifix='/api/v1')
