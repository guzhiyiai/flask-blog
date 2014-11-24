# -*- coding: utf-8 -*-
from flask import Module
from flask import flash, redirect, render_template, request, url_for, session
from flask_login import login_user, login_required, logout_user
from flask.ext.login import LoginManager

from . import bp

from app.models import User
from app.extensions import db
from app.forms import SignupForm, SigninForm

# from app.myapp import bcrypt


# account = Module(__name__)

# login_manager = LoginManager()

# login_manager.login_view = 'account.login'
# login_manager.login_message = u'你需要登录后才能进行下一步操作'


@bp.route('/home')
def home():
  return render_template('home.html')

@bp.route('/about')
def about():
  return render_template('about.html')

@bp.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.'

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if 'email' in session:
        return redirect(url_for('.welcome'))

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.username.data, form.password.data, form.email.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            print "test"
            return render_template('layout.html')
            return redirect(url_for('.welcome'))

    elif request.method == 'GET':
         return render_template('signup.html', form=form)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'email' in session:
        return redirect(url_for('.welcome'))

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signin.html', form=form)
        else:
            session['email'] = form.email.data
        return redirect(url_for('.welcome'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)

@bp.route('/welcome')
def welcome():

    if 'email' not in session:
        return redirect(url_for('.signin'))

    user = User.query.filter_by(email = session['email']).first()

    if user is None:
        return redirect(url_for('.signin'))
    else:
        return render_template('welcome.html')

@bp.route('/signout')
def signout():

    if 'email' not in session:
        return redirect(url_for('.signin'))

    session.pop('email', None)
    return redirect(url_for('.home'))


# @login_manager.user_loader
# def load_user(userid):
#     return User.get(userid)


# @bp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User(
#             username=form.username.data,
#             password=form.password.data,
#             email=form.email.data
#         )
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     form = LoginForm(request.form)
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             user = User.query.filter_by(name=request.form['username']).first()
#             if user is not None:
#                 login_user(user)
#                 flash('You were logged in.')
#                 return redirect(url_for('index'))
#             else:
#                 error = 'Invalid username or password.'
#     return render_template('login.html', form=form, error=error)

# @bp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You were logged out.')
#     return redirect(url_for('home.welcome'))


