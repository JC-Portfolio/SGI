from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import Headquarters
from sqlalchemy import text


class HeadquartersQueryModel(Headquarters):
    def join_tables_to_query(self, params, query):
        # smt = text()
        #
        # query = query.from_statement()

        return query

    def add_column_to_query(self, params, query):
        pass


class HeadquartersService(Service):
    pass


sede = Blueprint('sede', __name__, url_prefix='/')

sede_model_instance = HeadquartersQueryModel()
sede_service = HeadquartersService(sede_model_instance)
service_model = ServiceModelQuery(sede_model_instance)


@sede.route('sede/register', methods=['POST', 'PUT', 'DEL'])
def register_company():

    insert_validations = [
            'name IS not_empty, Informe o nome',

    ]
    update_validations = [
            'name IS not_empty, Informe o nome',
            'id IS not_empty, Informe o id '
    ]

    rest = Rest(sede_service, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Empresa criada com sucesso')
    rest.set_response('DEL', 'Empresa apagada com sucesso')
    rest.set_response('PUT', 'Empresa atualizada com sucesso')

    return rest.response()


@sede.route('sede', methods=['GET'])
def get_company():
    params = service_model.get_params()

    return 'ab' , 200


#
