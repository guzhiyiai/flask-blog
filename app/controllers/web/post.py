# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from app.models import Post, Comment
from app.extensions import db
from app.forms import PostForm, CommentsForm
from app.service.post import PostService
from app.service.comment import CommentService

from . import bp


@bp.route('/')
@bp.route('/page/<int:page>')
def index(page=1):
    if page < 1:
        page = 1
    page_obj = Post.query.order_by("-id").paginate(page, per_page=5)
    page_url = lambda page: url_for(".index", page=page)

    return render_template('index_web.html', page_obj=page_obj, page_url=page_url)
