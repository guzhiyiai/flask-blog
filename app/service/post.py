# -*- coding: utf-8 -*-

from app.extensions import db

class PostService(object):

    @staticmethod
    def store_to_db():
        db.session.add()
        db.session.commit()
