# -*- coding: utf-8 -*-


class DefaultConfig(object):

    DEBUG = True
    TESTING = True

    CSRF_ENABLED = True
    SECRET_KEY = "d\xff\xb3fP\x0e\xd0\xd2,'\xee\xd6\xc2\xca\x93ep\xfa\x12\xa0\x86\x08\x1e\xe8"

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://root:abc123@localhost/test3"
    SQLALCHEMY_ECHO = True
