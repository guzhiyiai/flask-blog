# -*- coding: utf-8 -*-

from datetime import datetime

# from flaskext.login import AnonymousUser

from app.extensions import db


# class Anonymous(AnonymousUser):
    # name = u"Guest"


class UserRole:

    USER = 0
    ADMIN = 1
    EDITOR = 2


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    role    = db.Column(db.Integer, index=True, default=UserRole.USER, nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
                id = self.id,
                username = self.username,
                email = self.email,
                role = self.role
            )


class PostStatus:

    SHOWN = 0
    HIDDEN = 1
    DELETED = 2


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)
    status = db.Column(db.Integer, default=PostStatus.HIDDEN, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # user_id     = db.Column(db.Integer, index=True)

    def to_dict(self):
        return dict(
            id = self.id,
            title = self.title,
            content = self.content,
            status = self.status,
            created_at = self.created_at,
            updated_at = self.updated_at
        )


class CommentStatus:

    APPROVED = 0
    MODERATED = 1
    TRASHED = 2


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    status = db.Column(db.Integer, index=True, default=CommentStatus.MODERATED, nullable=False)
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    post_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id         = self.id,
            content    = self.content,
            created_at = self.created_at,
            post_id    = self.post_id,
            show       = self.show
        )
