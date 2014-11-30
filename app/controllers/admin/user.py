# -*- coding: utf-8 -*-

from flask import Module
from flask import flash, redirect, render_template, request, url_for, session

from . import bp

from app.models import User
from app.extensions import db
from app.forms import SignupForm, SigninForm
from app.service.user import UserService


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'email' in session:
        return render_template('admin_index.html', form=form)

    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            username = form.username.data
            password = form.password.data
            email = form.email.data
            user = UserService.add_user(username, password, email)
            session['email'] = user.email

            return render_template('admin_index.html', form=form)

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'email' in session:
        return render_template('admin_index.html', form=form)

    if request.method == 'GET':
        return render_template('signin.html', form=form)

    session['email'] = form.email.data
    return render_template('admin_index.html', form=form)


@bp.route('/signout')
def signout():
    if 'email' not in session:
        return redirect(url_for('.signin'))
    session.pop('email', None)

    return redirect(url_for('.signin'))
