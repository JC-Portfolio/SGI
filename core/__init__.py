from env import APP_NAME
from flask import Flask
import database_models
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api
from database_models import create_db


def create_app():
    app = Flask(APP_NAME)
    create_db(app)

    Api.init_app(app)
    JWTManager.init_app(app)
    Migrate(app, app.db)

    app.__dict__()

    return app