import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Bundle, Environment
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_mail import Mail

from inkbusters.config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


css = Bundle(
    "css/base.css",
    "css/navbar.css",
    "css/footer.css",
    "css/index.css",
    "css/about.css",
    "css/contact.css",
    "css/gallery.css",
    "css/pricing.css",
    output="css/min/main.min.css",
    filters="cssmin",
)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init features
    db.init_app(app)
    migrate.init_app(app, db)
    app.debug = 0
    mail.init_app(app)
    admin = Admin(app)

    # assets
    assets = Environment(app)
    assets.register("main_css", css)

    # blueprints
    from inkbusters.main.routes import main

    app.register_blueprint(main)

    # # flask admin
    # from inkbusters.models import Questions

    # admin.add_view(ModelView(Questions, db.session))

    return app
