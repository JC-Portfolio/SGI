from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import MovieModel
from sqlalchemy import text


class MovieModelQueryModel(MovieModel):
    def join_tables_to_query(self, params, query):
        # smt = text()
        #
        # query = query.from_statement()

        return query

    def add_column_to_query(self, params, query):
        pass


class MovieService(Service):
    pass


movie = Blueprint('movie', __name__, url_prefix='/')

movie_model_instance = MovieModelQueryModel
movie_service = MovieService(movie_model_instance)
service_model = ServiceModelQuery(movie_service)


@movie.route('movie/register', methods=['POST', 'PUT', 'DEL'])
def register_company():

    insert_validations = [
            'name IS not_empty, Informe o nome',

    ]
    update_validations = [
            'name IS not_empty, Informe o nome',
            'id IS not_empty, Informe o id '
    ]

    rest = Rest(movie_model_instance, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Empresa criada com sucesso')
    rest.set_response('DEL', 'Empresa apagada com sucesso')
    rest.set_response('PUT', 'Empresa atualizada com sucesso')

    return rest.response()


@movie.route('movie', methods=['GET'])
def get_company():
    params = service_model.get_params()

    return 'ab' , 200


#
