from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import CinemaModel
from sqlalchemy import text


class CinemaQueryModel(CinemaModel):
    def join_tables_to_query(self, params, query):
        # smt = text()
        #
        # query = query.from_statement()

        return query

    def add_column_to_query(self, params, query):
        pass


class CinemaService(Service):
    pass


cinema = Blueprint('company', __name__, url_prefix='/')

cinema_model_instance = CinemaQueryModel()
cinema_service = CinemaService(cinema_model_instance)
service_model = ServiceModelQuery(cinema_model_instance)


@cinema.route('cinema/register', methods=['POST', 'PUT', 'DEL'])
def register_company():

    insert_validations = [
            'name IS not_empty, Informe o nome',

    ]
    update_validations = [
            'name IS not_empty, Informe o nome',
            'id IS not_empty, Informe o id '
    ]

    rest = Rest(cinema, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Empresa criada com sucesso')
    rest.set_response('DEL', 'Empresa apagada com sucesso')
    rest.set_response('PUT', 'Empresa atualizada com sucesso')

    return rest.response()


@cinema.route('cinema', methods=['GET'])
def get_company():
    params = service_model.get_params()

    return 'ab' , 200


#
