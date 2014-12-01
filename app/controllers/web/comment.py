# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from app.models import Post, Comment
from app.extensions import db
from app.forms import PostForm, CommentsForm
from app.service.post import PostService
from app.service.comment import CommentService

from . import bp


@bp.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    form = CommentsForm(request.form)
    page = Post.query.filter_by(id=id).first()
    cs = Comment.query.filter_by(post_id=id).all()

    if request.method == "GET":
        return render_template('comment.html', page=page, cs=cs, form=form)

    post_id = int(id)
    name = form.name.data
    email = form.email.data
    comments = form.comments.data

    try:
        comment = CommentService.add_comment(post_id=post_id, name=name, email=email, comments=comments)
        flash('Add a comment successful!')
    except:
        flash('Failed to add a comment!')

    page = 1
    page_obj = Post.query.order_by("id").paginate(page, per_page=5)
    page_url = lambda page: url_for(".index", page=page)

    return render_template('index_web.html', page_obj=page_obj, page_url=page_url)


