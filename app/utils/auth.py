from functools import wraps
from flask import session, redirect, url_for

from app.service.user import UserService

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_uid' not in session:
            return redirect(url_for('.login'))
        return f(*args, **kwargs)
    return decorated_function


def token_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        user_id = session['admin_uid']
        if user_id:
            token = UserService.generate_auth_token(user_id)
            user = UserService.verify_auth_token(token)
        return method(*args, **kwargs)
    return wrapper


def login_admin(user_id):
    session.permanent = True
    session['admin_uid'] = user_id


def logout_admin():
    session.pop('admin_uid', None)


def current_user():
    pass


