# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from app.models import Post, Comment
from app.extensions import db

from app.forms import PostForm, CommentsForm
from app.service.post import PostService
from app.service.comment import CommentService


from . import bp


@bp.route('/test')
def test():

    return render_template('web/test.html')

@bp.route('/')
def index():
    posts = PostService.get_posts()

    return render_template('web/index.html', posts=posts)


@bp.route('/posts/<int:id>', methods=['GET', 'POST'])
def post(id):
    form = CommentsForm(request.form)
    post = PostService.get_one(id)
    cs = CommentService.get_comments(id)

    if request.method == "GET":
        return render_template('web/post.html', form=form, post=post, cs=cs)

    post_id = int(id)
    name = form.name.data
    email = form.email.data
    comments = form.comments.data

    try:
        comment = CommentService.add_comment(
            post_id=post_id,
            name=name,
            email=email,
            comments=comments)
        flash('Add a comment successful!')
    except:
        flash('Failed to add a comment!')

    return render_template('web/post.html', form=form, post=post, cs=cs)
