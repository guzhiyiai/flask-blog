# -*- coding: utf-8 -*-

from flask import current_app

from app.models import Comment
from app.extensions import db
from app.utils.cache import get_counter
from app.utils.cache import inc_counter
from app.utils.cache import set_counter

POST_COMMENTS_COUNT = {
        'key': 'posts:{post_id}:comments_count'
    }


class CommentService(object):

    @staticmethod
    def add_comment(name, email, comments, post_id):
        comment = Comment(post_id=post_id, name=name,
                          email=email, comments=comments)
        db.session.add(comment)
        db.session.commit()

        CommentService.inc_comments_count(post_id)

        return comment.to_dict()

    @staticmethod
    def get_comments(id):
        comment_list = Comment.query.filter_by(post_id=id).all()

        return comment_list

    @staticmethod
    def get_comments_count(post_id):

        comments_count = get_counter(POST_COMMENTS_COUNT, post_id=post_id)

        if comments_count is not None:
            comments_count = Comment.query.filter_by(post_id=post_id).count()
        return comments_count


    @staticmethod
    def set_comments_count(post_id):
        comments_count = Comment.query.filter_by(post_id=post_id).count()
        set_counter(POST_COMMENTS_COUNT, post_id=post_id)
        return comments_count

    @staticmethod
    def inc_comments_count(post_id):
        comments_count = get_counter(POST_COMMENTS_COUNT, post_id=post_id)
        if comments_count is None:
            CommentService.set_comments_count(post_id)
        else:
            inc_counter(POST_COMMENTS_COUNT, post_id=post_id)
