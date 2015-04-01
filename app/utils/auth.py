from functools import wraps
from flask import session, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_uid' not in session:
            return redirect(url_for('.login'))
        return f(*args, **kwargs)
    return decorated_function


def login_admin(user_id):
    session.permanent = True
    session['admin_uid'] = user_id


def logout_admin():
    session.pop('admin_uid', None)


def current_user():
    pass

