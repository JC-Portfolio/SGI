from core.service import Service
from flask import Blueprint
from database_models.models import UserModel
from core.rest import Rest


class UserService(Service):
    pass


user = Blueprint('user', __name__, url_prefix='/user')
user_service = UserService(UserModel())


@user.route('/register', methods=['POST', 'PUT', 'DEL'])
def register_users():

    insert_validations = [
            'name IS not_empty, Informar o nome'
        ]
    update_validations = [
            'name IS not_empty, Informar o nome'
        ]

    rest = Rest(user_service, insert_validations, update_validations)

    rest.call_rest_method()

#
