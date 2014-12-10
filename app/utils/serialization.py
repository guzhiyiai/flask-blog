# -*- coding: utf-8 -*-

from flask import jsonify


# API response
def jsonify_with_data(err, **kwargs):
    """Return a json message(200/201)
    """
    resp = {'data': kwargs, 'message': err[1], 'code': err[0]}
    return jsonify(resp), err[0]


def jsonify_with_error(err, errors=None):
    resp = {'message': err[1], 'code': err[0]}
    return jsonify(resp), err[0]
