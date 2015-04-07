# -*- coding: utf-8 -*-

from flask import Module
from flask import flash, redirect, render_template, request, url_for, session, jsonify

from . import bp

from app.utils.auth import login_required, login_admin, logout_admin, token_required
from app.models import User
from app.extensions import db
from app.forms import SignupForm
from app.service.user import UserService



@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'admin_uid' in session:
        return render_template('admin/index.html', form=form)

    if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            email = form.email.data
            user = UserService.add_user(username, password, email)

            return render_template('admin/signin.html', form=form)

    elif request.method == 'GET':
        return render_template('admin/login.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('admin/login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = UserService.get_by_email(email)

    if user is not None and UserService.check_password(user['id'], password):
        login_admin(user['id'])
        return redirect(url_for('admin.show_posts'))

    return render_template('admin/login.html')


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_admin(user['id'])
    return redirect(url_for('admin.login'))


@bp.route('/api/token')
@login_required
def get_auth_token():
    user_id = session['admin_uid']
    token = UserService.generate_auth_token(user_id)
    session['token'] = token
    return jsonify({ 'token': token.decode('ascii') })


@bp.route('/api/resource')
@token_required
def get_resource():
    return jsonify({ 'resource': "hello, world!" })

