from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import ProfileModel, CompanyModel
from sqlalchemy import or_


class ProfileQueryModel(ProfileModel):
    def join_tables_to_query(self, params, query):
        query = query.join(ProfileModel, ProfileModel.company_id == CompanyModel.id)

        return query

    def add_column_to_query(self, params, query):
        query = query.add_columns(ProfileModel.id, ProfileModel.name, CompanyModel.name.label('empresa'))
        return query

    def filter_query(self, params, query):
        if profile_id := params.get('profile_id', None):
            query = query.filter(ProfileModel.id == profile_id)
        if company_id := params.get('company_id', None):
            query = query.filter(CompanyModel.id == company_id)

        return query


class ProfileService(Service):
    pass


profile = Blueprint('profile', __name__, url_prefix='/')

profile_model_instance = ProfileQueryModel()
profile_service = ProfileService(profile_model_instance)
service_model = ServiceModelQuery(profile_model_instance)


@profile.route('profile/register', methods=['POST', 'PUT', 'DEL'])
def register():

    insert_validations = [
            'name IS not_empty, Informe o nome',
            'company_id IS not_empty, Informe o id da empresa'

    ]
    update_validations = [
            'name IS not_empty, Informe o nome',
            'id IS not_empty, Informe o id',
            'company_id IS not_empty, Informe o id da empresa'
    ]

    rest = Rest(profile_model_instance, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Perfil criado com sucesso')
    rest.set_response('DEL', 'Perfil apagado com sucesso')
    rest.set_response('PUT', 'Perfil atualizado com sucesso')

    return rest.response()


@profile.route('company', methods=['GET'])
def get():
    params = service_model.get_params()

    return 'ab' , 200


#
