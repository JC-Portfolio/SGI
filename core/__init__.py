from env import APP_NAME, DATABASE_URI
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api
from database_models import create_db
from database_models import models
from resources.user import user
from resources.company import company
from .api_exceptions import InvalidRegister, api_handle


def create_app():
    app = Flask(APP_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    create_db(app)

    api = Api(app)
    jwt = JWTManager(app)

    Migrate(app, app.db)

    app.register_blueprint(user)
    app.register_blueprint(company)
    app.register_error_handler(InvalidRegister, api_handle)

    return app