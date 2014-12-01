# -*- coding: utf-8 -*-

from app.models import Comment
from app.extensions import db


class CommentService(object):

    @staticmethod
    def add_comment(name, email, comments, post_id):
        comment = Comment(post_id=post_id, name=name,
                          email=email, comments=comments)
        db.session.add(comment)
        db.session.commit()

        return comment.to_dict()
