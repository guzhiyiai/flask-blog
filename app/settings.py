# -*- coding: utf-8 -*-


class Config(object):

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):

    ENV = 'development'
    DEBUG = True

    # session
    CSRF_ENABLED = True
    SECRET_KEY = "asgSfsf3Xd8ffy]fw8vfd0zbvssqwertsd4sdwe"

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://root:abc123@localhost/my-blog"
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):

    ENV = 'testing'
    TESTING = True


class ProductionConfig(Config):

    ENV = 'production'
    # SQLALCHEMY_DATABASE_URI =


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
