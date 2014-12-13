# -*- coding: utf-8 -*-

from flask import Flask

from app.settings import DefaultConfig
from app.controllers.admin import bp as admin_web_bp
from app.controllers.web import bp as web_bp
from app.controllers.api import bp as api_bp
from app.extensions import db


DEFAULT_APP_NAME = 'app'


def create_app(config=None):
    app = Flask(DEFAULT_APP_NAME)

    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)
    configure_logging(app)

    app.debug_logger.debug(' * Runing in -----* ')

    return app


def configure_app(app, config):
    if not config:
        config = DefaultConfig

    app.config.from_object(config)


def configure_extensions(app):
    db.app = app
    db.init_app(app)


def configure_logging(app):

    import logging
    from logging import StreamHandler

    class DebugHandler(StreamHandler):
        def emit(x, record):
            StreamHandler.emit(x, record) if app.debug else None

    logger = logging.getLogger('app')
    logger.addHandler(DebugHandler())
    logger.setLevel(logging.DEBUG)

    app.debug_logger = logger


def configure_blueprints(app):
    app.register_blueprint(admin_web_bp, url_prefix='/admin')
    app.register_blueprint(web_bp, url_prefix='')
    app.register_blueprint(api_bp, url_prefix='/api/v1')
