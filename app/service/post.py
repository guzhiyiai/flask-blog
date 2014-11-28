# -*- coding: utf-8 -*-

from app.models import Post
from app.extensions import db


class PostService(object):
    @staticmethod
    def add_entry(title, content=None):
        post = Post(content=content, title=title)
        db.session.add(post)
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def del_entry(entry):
        db.session.delete(entry)
        db.session.commit()

    @staticmethod
    def edit_entry(id, title, content):
        print "xxxnnnnn"
        post = Post.query.filter_by(id=id)
        post.title = title
        post.content = content
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def store_to_db():
        db.session.add()
        db.session.commit()
