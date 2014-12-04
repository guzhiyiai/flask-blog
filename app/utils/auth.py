from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
	    return redirect(url_for('.signin'))
	return f(*args, **kwargs)
    return decorated_function
