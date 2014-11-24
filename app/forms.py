# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from app.models import User


class PostForm(Form):
    title = TextField('title', [validators.Required("title")])
    content = TextAreaField('content', [validators.Required("content")])
    submit = SubmitField('Post')


class SignupForm(Form):
    username = TextField("User name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True


class SigninForm(Form):
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False


# class LoginForm(Form):
#     username = TextField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])


# class RegisterForm(Form):
#     username = TextField(
#         'username',
#         validators=[DataRequired(), Length(min=3, max=25)]
#     )
#     email = TextField(
#         'email',
#         validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
#     )
#     password = PasswordField(
#         'password',
#         validators=[DataRequired(), Length(min=6, max=25)]
#     )
#     confirm = PasswordField(
#         'Repeat password',
#         validators=[
#             DataRequired(), EqualTo('password', message='Passwords must match.')
#         ]
#     )


# class ConmmentForm(Form):
#     title = TextField('Title', validators=[DataRequired()])
#     description = TextField(
#         'Description', validators=[DataRequired()])
