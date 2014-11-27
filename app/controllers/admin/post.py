# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from . import bp

from app.models import Post, Comment
from app.extensions import db
from app.forms import PostForm, CommentsForm
from app.service import PostService

@bp.route('/')
@bp.route('/page/<int:page>')
def index(page=1):
    if page < 1:
        page = 1
    page_obj = Post.query.order_by("-id").paginate(page, per_page=5)
    page_url = lambda page: url_for(".index", page=page)

    return render_template('index.html', page_obj=page_obj, page_url=page_url)


@bp.route('/post/<int:id>/entry', methods=['GET', 'POST'])
def entry(id):
    form = CommentsForm(request.form)
    page = Post.query.filter_by(id=id).first()
    # cs = Comment.query.all()
    cs = Comment.query.filter_by(post_id=id)

    if request.method == "GET":
        return render_template('entry.html', page=page, cs=cs, form=form)
    name = form.name.data
    email = form.email.data
    comments = form.comments.data

    c = Comment(
                 post_id = id,
                 name=name,
                 email=email,
                 comments=comments)
    try:
        c.store_to_db()
        flash('Comments added successfully!')
    except:
        flash('Failed to add a comment')

    return render_template('entry.html', page=page, cs=cs, form=form)


@bp.route('/add', methods=['GET', 'POST'])
def add_entry():
    form = PostForm(request.form)
    if request.method == "GET":
        return render_template('add_entry.html', form=form)

    title = form.title.data
    content = form.content.data

    try:
        post = PostService.add_post(title, content)
        flash(u'文章存入成功')
    except:
        flash(u'文章存入失败，请与管理员联系')

    return render_template('admin_index.html')

