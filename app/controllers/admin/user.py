# -*- coding: utf-8 -*-

from flask import Module
from flask import flash, redirect, render_template, request, url_for, session, jsonify

from app.models import User
from app.forms import SignupForm
from app.service.user import UserService
from app.extensions import db
from app.external_service import send_email
from app.utils.auth import login_required, login_admin, logout_admin, token_required

from . import bp


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'admin_uid' in session:
        return render_template('admin/index.html', form=form)

    if request.method == 'GET':
        return render_template('admin/signup.html', form=form)

    username = form.username.data
    password = form.password.data
    email = form.email.data

    user = UserService.add_user(username, password, email)

    token = UserService.generate_email_token(user['email'])

    confirm_url = url_for('admin.confirm_email', token=token, external=True)
    html = render_template('admin/email.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    sender = 'bababa'
    send_email(subject, sender, user['email'], html)

    return render_template('admin/signin.html', form=form)


@bp.route('/confirm/<token>', methods=['GET'])
def confirm_email(token):
    try:
        email = UserService.verify_email_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')

    user = UserService.get_by_email(email['email'])
    if user['confirmed']:
        flash('Account already confirmed. Please login.', 'success')
    else:
        UserService.update_confirmed_user(email['email'])
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('admin.signin'))


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('admin/signin.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = UserService.get_by_email(email)

    if user is not None and UserService.check_password(user['id'], password):
        login_admin(user['id'])
        return redirect(url_for('admin.show_posts'))

    return render_template('admin/signin.html')


@bp.route('/signout', methods=['GET', 'POST'])
def signout():
    logout_admin()
    return redirect(url_for('admin.signin'))


@bp.route('/api/token')
@login_required
def get_auth_token():
    user_id = session['admin_uid']
    token = UserService.generate_auth_token(user_id)
    session['token'] = token
    return jsonify({'token': token.decode('ascii')})


@bp.route('/api/resource')
@token_required
def get_resource():
    return jsonify({'resource': "hello, world!"})


@bp.route('/users/<int:user_id>', methods=['GET', 'POST'])
def get_my_profile(user_id):
    user = UserService.get(user_id)
    if not user:
        pass
    # return jsonify({ 'resource': "hello, world!" })
    return render_template('admin/user.html', user=user)
