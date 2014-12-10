# -*- coding: utf-8 -*-

from app.models import Post
from app.extensions import db


class PostService(object):

    @staticmethod
    def get_posts():
        posts = Post.query.order_by("id").all()
        return [post.to_dict() for post in posts]

    @staticmethod
    def get_one(id):
        post = Post.query.filter_by(id=id).first()
        return post and post.to_dict()

    @staticmethod
    def add_post(title, content=None):
        post = Post(content=content, title=title)
        db.session.add(post)
        db.session.commit()
        return post.to_dict()

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()

    @staticmethod
    def update_post(id, info_dict):
        post = Post.query.get(id)
        for k, v in info_dict.items():
            if v is not None:
                setattr(post, k, v)
        db.session.add(post)
        db.session.commit()

        return post.to_dict()
