# -*- coding: utf-8 -*-

from werkzeug import generate_password_hash, check_password_hash

from app.models import User
from app.extensions import db


class UserService(object):

    @staticmethod
    def add_user(username, password, email):
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()

        return user
