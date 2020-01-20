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
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "inkbusters.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get("DEBUG_MODE") or config.get("DEBUG_MODE")
