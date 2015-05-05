# -*- coding: utf-8 -*-

from datetime import datetime

from werkzeug import generate_password_hash, check_password_hash

from app.extensions import db


class Permission:
    READ = 0x04
    WRITE = 0x02
    ACCESS = 0x01


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    user_id = db.Column(db.Integer)


class UserRole:

    USER = 0
    ADMIN = 1
    EDITOR = 2

    roles = {
        'User': (Permission.READ |
                 Permission.WRITE |
                 Permission.ACCESS, True),
        'Anonymous': (Permission.READ, False),
        'Administrator': (0xff, False)
    }


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(100), unique=True)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    role = db.Column(db.Integer, index=True,
                     default=UserRole.USER, nullable=False)

    location = db.Column(db.String(64))
    description = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            confirmed=self.confirmed,
            role=self.role)


class PostStatus:

    SHOWN = 0
    PENDING = 1
    DELETED = 2


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)
    status = db.Column(db.Integer, default=PostStatus.PENDING, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            content=self.content,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at
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
    status = db.Column(db.Integer, index=True,
                       default=CommentStatus.MODERATED, nullable=False)
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)


    def to_dict(self):
        return dict(
            id=self.id,
            content=self.content,
            created_at=self.created_at,
            post_id=self.post_id,
            show=self.show
        )
