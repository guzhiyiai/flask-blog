# -*- coding: utf-8 -*-

from datetime import datetime

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from itsdangerous import URLSafeTimedSerializer as UrlSerializer
from werkzeug import generate_password_hash, check_password_hash

from app.models import User
from app.extensions import db

from app.settings import DevelopmentConfig


class UserService(object):

    @staticmethod
    def add_user(username, password, email):
        salted_password = generate_password_hash(password)
        user = User(username=username, password=salted_password, email=email, confirmed=False)
        db.session.add(user)
        db.session.commit()

        return user.to_dict()

    @staticmethod
    def update_confirmed_user(email):
        user = User.query.filter_by(email=email).first()
        user.confirmed = True
        user.confirmed_on = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    @staticmethod
    def check_password(user_id, password):
        user = User.query.get(user_id)
        return check_password_hash(user.password, password)

    @staticmethod
    def get_by_email(email):
        user = User.query.filter_by(email=email).first()
        return user and user.to_dict()

    @staticmethod
    def get(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user and user.to_dict()

    @staticmethod
    def generate_auth_token(user_id, expiration=600):
        s = Serializer(DevelopmentConfig.SECRET_KEY, expires_in=expiration)
        return s.dumps({'user_id': user_id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(DevelopmentConfig.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None     # valid token, but expired
        except BadSignature:
            return None     # invalid token
        user = User.query.get(data['user_id'])
        return user

    @staticmethod
    def generate_email_token(email):
        s = UrlSerializer(DevelopmentConfig.SECRET_KEY)
        return s.dumps({'email': email})

    @staticmethod
    def verify_email_token(token, expiration=3600):
        s = UrlSerializer(DevelopmentConfig.SECRET_KEY)
        try:
            email = s.loads(token, max_age=expiration)
        except:
            return False
        return email
