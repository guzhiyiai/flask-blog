# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, SubmitField
from wtforms import validators

from app.models import User


class SignupForm(Form):
    username = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign Up")


class SigninForm(Form):
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")


class PostForm(Form):
    title = TextField('title', [validators.Required("title")])
    content = TextAreaField('content', [validators.Required("content")])
    submit = SubmitField('Post')


class CommentsForm(Form):
    name = TextField(u"name(必填)", [validators.Required("name")])
    email = TextField(u"email(必填)", [validators.Required("email")])
    comments = TextAreaField(u"comment", [validators.Required("comment")])
    submit = SubmitField(u"Comment")


