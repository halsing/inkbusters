from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Adres e-mail"},
    )

    title = StringField(
        "Title",
        validators=[DataRequired()],
        render_kw={"placeholder": "Tytuł wiadomości"},
    )

    content = TextAreaField(
        "Content",
        validators=[DataRequired()],
        render_kw={"placeholder": "Treść wiadomości"},
    )
    submit = SubmitField("Wyślij")
