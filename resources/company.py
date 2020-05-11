from flask import Blueprint
from core.rest import Rest
from core.service import Service
from database_models.models import CompanyModel


class CompanyService(Service):
    pass

#TODO IMPLEMENTAR CLASSE DE QUERYS
#TODO ARRUMAR ROTAS


company = Blueprint('company', __name__, url_prefix='/')
company_service = CompanyService(CompanyModel())


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


@company.route('company', method=['GET'])
def get_company():

    return company_service.list()


#
