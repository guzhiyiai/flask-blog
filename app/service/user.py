# -*- coding: utf-8 -*-

from app.models import User
from app.extensions import db

class UserService(object):
    @staticmethod
    def add_user(username, password, email):
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()

        return user
