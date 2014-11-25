# -*- coding: utf-8 -*-


class DefaultConfig(object):

    DEBUG = True
    TESTING = True

    USERNAME = 'admin'
    PASSWORD = 'admin'

    CSRF_ENABLED = True
    SECRET_KEY = 'good-for-you'

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (
        'root', 'abc123', 'localhost', 'test1')
    SQLALCHEMY_ECHO = True
