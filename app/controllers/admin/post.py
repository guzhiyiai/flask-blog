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

    try:
        comment = CommentService.add_comment(id, name, email, comments)
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
        post = PostService.add_entry(title, content)
        flash(u'文章存入成功')
    except:
        flash(u'文章存入失败，请与管理员联系')

    return render_template('admin_index.html')


@bp.route('/<int:id>/del', methods=['GET', 'POST'])
def del_entry(id):
    entry = Post.query.filter_by(id=id).first()
    try:
        post = PostService.del_entry(entry)
        flash(u'文章删除成功')
    except:
        flash(u'文章删除失败，请与管理员联系')

    page_obj = Post.query.order_by("-id").paginate(2, per_page=5)
    page_url = lambda page: url_for(".index", page=page)

    return render_template('del_entry.html', page_obj=page_obj, page_url=page_url)


@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_entry(id):
    entry = Post.query.filter_by(id=id).first()
    form = PostForm(title=entry.title, content=entry.content)
    if request.method == "GET":
        return render_template('edit_entry.html', form=form)

    title = request.form['title']
    content = request.form['content']

    try:
        post = PostService.edit_entry(id, title, content)
        flash(u'文章删除成功')
    except:
        flash(u'文章删除失败，请与管理员联系')

    return render_template('admin_index.html')

