# -*- coding: utf-8 -*-


from flask_mail import Message


from app.extensions import mail


from app.settings import config

def send_email(subject, sender, recipients, html):

    msg = Message(
        subject=subject,
        sender= sender,
        recipients= [recipients]
    )

    msg.html = html

    mail.send(msg)