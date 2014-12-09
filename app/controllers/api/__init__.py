# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('api', __name__)


from . import comment
from . import post
