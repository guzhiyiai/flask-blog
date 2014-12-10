# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from app.models import Post, Comment
from app.extensions import db
from app.forms import PostForm, CommentsForm
from app.service.post import PostService
from app.service.comment import CommentService
from app.utils.auth import login_required

from . import bp


@bp.route('/')
@bp.route('/page/<int:page>')
def index():
    return render_template('admin/index.html')


@bp.route('/posts')
def show_posts():
    posts = PostService.get_posts()

    return render_template('admin/show_posts.html', posts=posts)


@bp.route('/posts/<int:id>')
def post(id):
    post = PostService.get_one(id)
    cs = CommentService.get_comments(id)

    return render_template('admin/post.html', post=post, cs=cs)


@bp.route('/posts/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm(request.form)
    if request.method == "GET":
        return render_template('admin/add_post.html', form=form)

    title = form.title.data
    content = form.content.data

    try:
        post = PostService.add_post(title, content)
        flash(u'文章存入成功')
    except:
        flash(u'文章存入失败，请与管理员联系')

    return render_template('admin/index.html')


@bp.route('/posts/<int:id>/delete')
def delete_post(id):
    try:
        PostService.delete_post(id)
        flash(u'文章删除成功')
    except:
        flash(u'文章删除失败，请与管理员联系')

    return render_template('admin/show_posts.html')


@bp.route('/posts/<int:id>/update', methods=['GET', 'POST'])
def update_post(id):
    post = PostService.get_one(id)

    form = PostForm(title=post.get('title'), content=post.get('content'))
    if request.method == "GET":
        return render_template('admin/update_post.html', form=form)

    title = request.form['title']
    content = request.form['content']

    try:
        post = PostService.update_post(id, {'title': title, 'content': content})
        flash(u'文章编辑成功')
    except:
        flash(u'文章编辑失败，请与管理员联系')

    return render_template('admin/show_posts.html')
