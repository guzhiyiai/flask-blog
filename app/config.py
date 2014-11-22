# -*- coding: utf-8 -*-

# configuration mysql
_DBUSER = "root"
_DBPASS = "abc123"
_DBHOST = "localhost"
_DBNAME = "myblog"

class DefaultConfig(object):

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (_DBUSER, _DBPASS, _DBHOST, _DBNAME)
    SQLALCHEMY_ECHO = True
