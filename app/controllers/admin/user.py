# -*- coding: utf-8 -*-
from flask import Module
from flask import flash, redirect, render_template, request, url_for, session

from . import bp

from app.models import User
from app.extensions import db
from app.forms import SignupForm, SigninForm


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'email' in session:
        # return redirect(url_for('.welcome'))
        return render_template('admin_index.html', form=form)

    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.username.data, form.password.data, form.email.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            # return redirect(url_for('.index'))
            return render_template('admin_index.html', form=form)

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


# @bp.route('/welcome')
# def welcome():

#     if 'email' not in session:
#         return redirect(url_for('.signin'))

#     user = User.query.filter_by(email=session['email']).first()

#     if user is None:
#         return redirect(url_for('.signin'))
#     else:
#         return render_template('welcome.html')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'email' in session:
        return render_template('admin_index.html', form=form)

    if request.method == 'POST':
        if not form.validate():
            return render_template('signin.html', form=form)
        else:
            session['email'] = form.email.data
        # return redirect(url_for('.admin_index'))
        return render_template('admin_index.html', form=form)

    elif request.method == 'GET':
        return render_template('signin.html', form=form)


@bp.route('/signout')
def signout():

    if 'email' not in session:
        return redirect(url_for('.signin'))

    session.pop('email', None)
    # return redirect(url_for('.index'))
    return redirect(url_for('.signin'))
