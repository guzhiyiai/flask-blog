# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('admin', __name__)


from . import user
from . import post
