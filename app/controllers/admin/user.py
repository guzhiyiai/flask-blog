# -*- coding: utf-8 -*-

from flask import render_template

from . import bp


@bp.route('/index')
def index():
    # return render_template('admin/index.html')
    return "hello world"
