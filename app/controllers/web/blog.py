
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from app.forms import MessageForm
from app.models import Post
from app.extensions import db


# use decorators to link the function to a url
@bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = Post(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('base'))
    else:
        posts = db.session.query(Post).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)


@bp.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
