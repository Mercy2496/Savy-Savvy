#!/usr/bin/env python3
from flask import Blueprint

endpoints = Blueprint("endpoints", __name__, url_prefix="/api/v1")

from api.V1.endpoints.users import *
from api.V1.endpoints.status import *