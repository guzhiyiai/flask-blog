# -*- coding: utf-8 -*-

from app.models import Post
from app.extensions import db


class PostService(object):
    @staticmethod
    def add_post(title, content=None):
        post = Post(content=content, title=title)
        db.session.add(post)
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def del_post(post):
        db.session.delete(post)
        db.session.commit()

    @staticmethod
    def update_post(id, title, content):
        post = Post.query.filter_by(id=id).update({"title": title, "content": content})
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def store_to_db():
        db.session.add()
        db.session.commit()
