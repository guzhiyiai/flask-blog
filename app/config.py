# -*- coding: utf-8 -*-

# configuration mysql
_DBUSER = "root"
_DBPASS = "abc123"
_DBHOST = "localhost"
_DBNAME = "test1"


class DefaultConfig(object):


    USERNAME = 'admin'
    PASSWORD = 'admin'

    CSRF_ENABLED = True
    SECRET_KEY = 'good-for-you'

    DEBUG = True
    TESTING = True
    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (_DBUSER, _DBPASS, _DBHOST, _DBNAME)
    SQLALCHEMY_ECHO = True
