from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import Headquarters, CompanyModel
from sqlalchemy import text


class HeadquartersQueryModel(Headquarters):
    def join_tables_to_query(self, params, query):
        query = query.join(Headquarters, Headquarters.company_id == CompanyModel.id)

        return query

    def add_column_to_query(self, params, query):
        query = query.add_columns(Headquarters.id, Headquarters.city, Headquarters.state, CompanyModel.name)
        return query

    def filter_query(self, params, query):
        if company_name := params.get('company_name', None):
            query = query.filter(CompanyModel.name == company_name)
        if company_id := params.get('company_id', None):
            query = query.filter(CompanyModel.id == company_id)

        return query


class HeadquartersService(Service):
    pass


sede = Blueprint('sede', __name__, url_prefix='/')

sede_model_instance = HeadquartersQueryModel()
sede_service = HeadquartersService(sede_model_instance)
service_model = ServiceModelQuery(sede_model_instance)


@sede.route('sede/register', methods=['POST', 'PUT', 'DEL'])
def register():

    insert_validations = [
            'city IS not_empty, Informe o nome da cidade',
            'state IS not_empty, Informe o nome do  estado'

    ]
    update_validations = [
            'city IS not_empty, Informe o nome da cidade',
            'state IS not_empty, Informe o nome do estado ',
            'id IS not_empty, Informe o id '
    ]

    rest = Rest(sede_service, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Sede criada com sucesso')
    rest.set_response('DEL', 'Sede apagada com sucesso')
    rest.set_response('PUT', 'Sede atualizada com sucesso')

    return rest.response()


@sede.route('sede', methods=['GET'])
def get():
    params = service_model.get_params()

    return 'ab' , 200


#
