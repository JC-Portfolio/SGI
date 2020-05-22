from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import CompanyModel
from sqlalchemy import text


class CompanyQueryModel(CompanyModel):
    def join_tables_to_query(self, params, query):
        return query

    def add_column_to_query(self, params, query):
        query = query.add_columns(CompanyModel.id, CompanyModel.name)
        return query

    def filter_query(self, params, query):
        if company_name := params.get('company_name', None) is not None:
            query = query.filter(CompanyModel.name == company_name)

        return query


class CompanyService(Service):
    pass


company = Blueprint('company', __name__, url_prefix='/')

company_model_instance = CompanyQueryModel()
company_service = CompanyService(company_model_instance)
service_model = ServiceModelQuery(CompanyQueryModel)


@company.route('company/register', methods=['POST', 'PUT', 'DEL'])
def register_company():

    insert_validations = [
            'name IS not_empty, Informe o nome',

    ]
    update_validations = [
            'name IS not_empty, Informe o nome',
            'id IS not_empty, Informe o id '
    ]

    rest = Rest(company_service, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Empresa criada com sucesso')
    rest.set_response('DEL', 'Empresa apagada com sucesso')
    rest.set_response('PUT', 'Empresa atualizada com sucesso')

    return rest.response()


@company.route('company', methods=['GET'])
def get():
    params = service_model.get_params()

    return 'ab' , 200


#
