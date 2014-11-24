# -*- coding: utf-8 -*-

from flask import Flask
# from flask.ext.bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
# from flask_login import LoginManager

from app.config import DefaultConfig
from app.controllers.admin import bp as admin_web_bp
from app.extensions import db


DEFAULT_APP_NAME = 'app'


def create_app(config=None):
    app = Flask(DEFAULT_APP_NAME)
    # bcrypt = Bcrypt(app)
    Bootstrap(app)

    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # from app.models import User
    # login_manager.login_view = "users.login"

    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)

    return app

def configure_app(app, config):
    if not config:
        config = DefaultConfig
        print "ccc"
    app.config.from_object(config)

def configure_extensions(app):
    db.app = app
    db.init_app(app)

def configure_blueprints(app):
    app.register_blueprint(admin_web_bp, url_prefix='/admin')
