# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, session

from . import bp

from app.models import Post, Comment
from app.extensions import db
from app.forms import PostForm, CommentsForm
from app.service import PostService


@bp.route('/')
@bp.route('/page/<int:page>')
def page(page=1):

    if page < 1:
        page = 1

    topwz = Post.query.order_by('-id').limit(10)
    topcs = Comment.query.order_by('-id').limit(10)
    page_obj = Post.query.order_by("-id").paginate(page, per_page=5)
    page_url = lambda page: url_for(".page", page=page)

    return render_template('page.html', page_obj=page_obj,
                           page_url=page_url, topwz=topwz, topcs=topcs)


@bp.route('/post/<int:id>/entry', methods=['GET', 'POST'])
def entry(id):
    form = CommentsForm(request.form)
    topwz = Post.query.order_by("-id").limit(10)
    topcs = Comment.query.order_by('-id').limit(10)
    page = Post.query.filter_by(id=id).first()
    cs = Comment.query.filter_by(id=id)

    if request.method == 'POST':

        name = form.name.data
        email = form.email.data
        comments = form.comments.data

        c = Comment(
            name=name,
            email=email,
            comments=comments)
        try:
            c.PostService.store_to_db()
            flash(u'评论成功')
        except:
            flash(u'失败')

        return render_template('entry.html', page=page, topwz=topwz, form=form, cs=cs, topcs=topcs)

    return render_template('entry.html', page=page, topwz=topwz, form=form, cs=cs, topcs=topcs)


@bp.route('/', methods=['GET', 'POST'])
def show_entries():
    error = None
    form = PostForm(request.form)

    posts = Post.query.order_by('-id').limit(10)

    return render_template('show_entries.html', posts=posts, form=form, error=error)


@bp.route('/add', methods=['GET', 'POST'])
def add_entry():

    if request.method == 'GET':
        return render_template("add_entries.html")

    form = PostForm(request.form)

    post = PostService.add_post(form.title.data, form.content.data)

    flash('New entry was successfully posted. Thanks.')

    posts = Post.query.order_by('-id').limit(10)
    return render_template('show_entries.html', posts=posts, form=form)
