from core.service import Service
from flask import jsonify
from flask import request
from flask import Blueprint
from database_models.models import UserModel


class UserService(Service):

    def update_validations(self):
        pass

    def insert_validations(self):
        pass

#TODO TALVEZ IMPLEMENTAR SINGLETON


user = Blueprint('user', __name__, url_prefix='/user')
user_service = UserService(UserModel)


@user.route('/register', methods=['POST', 'PUT'])
def register_user():
    data = request.json

    if request.method == 'POST':

        validations = [
            'name IS not_empty, Informar o nome'
        ]
        user_service.make_insert(data, validations)

        return {'metodo': 'POST'}

    return {'metodo': 'UPDATE'}




