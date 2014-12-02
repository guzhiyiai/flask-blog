# -*- coding: utf-8 -*-


class DefaultConfig(object):

    DEBUG = True
    TESTING = True

    CSRF_ENABLED = True
    SECRET_KEY = "gSf3Xd8y]w8vd0z"

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://root:abc123@localhost/my-blog"
    SQLALCHEMY_ECHO = True
