# -*- coding: utf-8 -*-


class Config(object):

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):

    ENV = 'development'
    DEBUG = True

    # session
    CSRF_ENABLED = True
    SECRET_KEY = "gSf3Xd8y]w8vd0z"

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://root:abc123@localhost/my-blog"
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):

    ENV = 'testing'
    TESTING = True


class ProductionConfig(Config):

    ENV = 'production'


class StagingConfig(Config):

    ENV = 'staging'
