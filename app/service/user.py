# -*- coding: utf-8 -*-

from werkzeug import generate_password_hash, check_password_hash

from app.models import User
from app.extensions import db


class UserService(object):

    # def __init__(self, username, password, email):
    #     self.username = username
    #     self.email = email
    #     self.set_password(password)

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

    @staticmethod
    def add_user(username, password, email):
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()

        return user
