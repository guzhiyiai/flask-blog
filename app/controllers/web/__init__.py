# -*- coding: utf-8 -*-


from flask import Blueprint

bp = Blueprint('web', __name__)


from . import post
