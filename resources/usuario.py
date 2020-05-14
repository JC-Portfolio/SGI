from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import UserModel


class UserModelQuery(UserModel):
    pass


class UserService(Service):
    pass


user = Blueprint('user', __name__, url_prefix='/')
user_model_instance = UserModelQuery()
user_service = UserService(user_model_instance)
model_service = ServiceModelQuery(user_model_instance)


@user.route('user/register', methods=['POST', 'PUT', 'DEL'])
def register_users():

    insert_validations = [
            'name IS not_empty, Informar o nome'
        ]
    update_validations = [
            'name IS not_empty, Informar o nome'
        ]

    rest = Rest(user_service, insert_validations, update_validations)

    rest.call_rest_method()

