from flask import current_app
from inkbusters import db


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"{id}-{title}"
