# -*- coding: utf-8 -*-

import os
import socket

from flask_script import Manager
from flask_script import Server
from flask_script import prompt_bool

from app.settings import DevelopmentConfig
from app.settings import StagingConfig
from app.settings import ProductionConfig

from app.application import create_app
from app.extensions import db
from app import models


# create app with env
config_map = {
    'dev': DevelopmentConfig,
    'stag': StagingConfig,
    'prod': ProductionConfig
}

# set env via hostnave/environment variable
hostname = socket.gethostname()
flask_env = 'prod'
if 'stag' in hostname:
    flask_env = 'stag'
elif hostname.endswith('local'):
    flask_env = 'dev'
flask_env = os.environ.get('FLASK_ENV', flask_env)


app = create_app(config_map[flask_env])

# flask_script -> add application of command line parameters
manager = Manager(app)


@manager.command
def initdb():
    "Creates database tables"
    if prompt_bool("Are you sure? You will init your database"):
        db.create_all()


@manager.command
def dropdb():
    "Drops all database tables"
    if prompt_bool("Are you sure ? You will lose all your data!"):
        db.drop_all()

manager.add_command("runserver", Server(host='0.0.0.0', port=5555))


if __name__ == '__main__':
    manager.run()
