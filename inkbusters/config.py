import os
import json

try:
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)
except IOError:
    pass

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or config.get("SECRET_KEY")

    # sql alchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "inkbusters.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get("DEBUG_MODE") or config.get("DEBUG_MODE")

    # email
    MAIL_SERVER = os.environ.get("MAIL_SERVER") or config.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or config.get("MAIL_PORT"))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or config.get("MAIL_USE_TLS")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or config.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or config.get("MAIL_PASSWORD")
