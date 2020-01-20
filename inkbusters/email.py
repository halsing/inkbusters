from flask_mail import Message
from flask import render_template
from flask import current_app

from inkbusters import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def email_page(data):
    """
    Prepare email to send 
    """
    subject = f"Inkbusters form contact: {data['title']}"
    sender = current_app.config["MAIL_USERNAME"]
    recipients= ['adrian.borowski.tattoo@gmail.com']
    text_body=render_template('email/email_contact.txt', data=data)
    html_body=render_template('email/email_contact.html', data=data)

    send_email(
        subject=subject,
        sender=sender,
        recipients=recipients,
        text_body=text_body,
        html_body=html_body
    )
