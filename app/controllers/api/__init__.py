# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('api', __name__)


class APIError:

    OK = (200, 'OK')
    CREATE = (201, 'created_successfully')
    BAD_REQUEST = (400, 'bad_request')
    BAD_USER = (401, 'unauthorized')
    NO_ACCESS = (403, 'forbidden')
    NOT_FOUND = (404, 'not_found')

from . import post
