
from flask import flash, redirect, render_template, request, url_for, session

from . import bp

from app.models import Post
from app.extensions import db
from app.forms import PostForm

from flask_login import  current_user, LoginManager


login_manager = LoginManager()

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

    new_post = Post(form.title.data,form.content.data)
    db.session.add(new_post)
    db.session.commit()
    flash('New entry was successfully posted. Thanks.')

    posts = Post.query.order_by('-id').limit(10)
    return render_template('show_entries.html', posts=posts, form=form)
