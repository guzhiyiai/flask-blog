# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_script import Server
from flask_script import prompt_bool

from app.application import create_app
from app.extensions import db
from app import models

app = create_app()

# flask_script -> add application of command line parameters
manager = Manager(app)


@manager.command
def createall():
    "Creates database tables"
    db.create_all()


@manager.command
def dropall():
    "Drops all database tables"
    if prompt_bool("Are you sure ? You will lose all your data!"):
        db.drop_all()

manager.add_command("runserver", Server(host='0.0.0.0', port=5555))


if __name__ == '__main__':
    manager.run()
