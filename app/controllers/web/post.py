# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from app.models import Post, Comment
from app.extensions import db
from app.service.post import PostService

from . import bp


@bp.route('/')
@bp.route('/page/<int:page>')
def index(page=1):

    page_obj = PostService.get_posts()
    page_url = lambda page: url_for(".index", page=page)

    return render_template('index_web.html', page_obj=page_obj, page_url=page_url)
