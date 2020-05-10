from core.service import Service
from flask import jsonify
from flask import request
from flask import Blueprint
from database_models.models import UserModel
from core.rest import Rest


class UserService(Service):
    def update_validations(self):
        pass

    def insert_validations(self):
        pass


user = Blueprint('user', __name__, url_prefix='/user')
user_service = UserService(UserModel)


@user.route('/register', methods=['POST', 'PUT', 'DEL'])
def register_user():
    data = user_service.data()
    method = request.method

    insert_validations = [
            'name IS not_empty, Informar o nome'
        ]
    update_validations = [
            'name IS not_empty, Informar o nome'
        ]

    rest = Rest(user_service, insert_validations, update_validations)

    rest.call_rest_method()

    # if method == 'POST':
    #
    #     validations = [
    #         'name IS not_empty, Informar o nome'
    #     ]
    #     user_service.make_insert(data, validations)
    #
    #     return {'metodo': 'POST'}
    #
    # if method == 'PUT':
    #     validations = [
    #         'name IS not_empty, Informar o nome'
    #     ]
    #
    #     user_service.make_update(validations)
    #
    #     return 'update'
    #
    # if method == 'DEL':
    #     user_service.delete()
    #
    #     return 'delete'
    #
    #


def testando_escopo():
    validações = 'a'

    print(locals())

#
# testando_escopo()
#
