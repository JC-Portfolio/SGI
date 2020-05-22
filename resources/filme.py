from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import MovieModel, CinemaModel
from sqlalchemy import text


class MovieModelQueryModel(MovieModel):
    def join_tables_to_query(self, params, query):
        query = query.join(MovieModel.id == CinemaModel.id)

        return query

    def add_column_to_query(self, params, query):
        query = query.add_columns(MovieModel.id,
                                  MovieModel.name,
                                  MovieModel.gender,
                                  MovieModel.full_price,
                                  MovieModel.half_price,
                                  MovieModel.duration
                                  )
        return query

    def filter_query(self, params, query):
        if name := params.get('name', None) is not None:
            query = query.filter(MovieModel.name == name)
        if duration := params.get('duration', None) is not None:
            query = query.filter(MovieModel.duration == duration)
        if gender := params.get('gender', None) is not None:
            query = query.filter(MovieModel.gender == gender)
        if cinema_id := params.get('cinema_id', None) is not None:
            query = query.filter(CinemaModel.id == cinema_id)

        return query


class MovieService(Service):
    pass


movie = Blueprint('movie', __name__, url_prefix='/')

movie_model_instance = MovieModelQueryModel
movie_service = MovieService(movie_model_instance)
service_model = ServiceModelQuery(movie_service)


@movie.route('movie/register', methods=['POST', 'PUT', 'DEL'])
def register():

    insert_validations = [
            'name IS not_empty AND more_than:0, Informe o nome',
            'duration IS not_empty AND more_or_equal_than:30, Informe a duração do filme',
            'gender IS not_empty AND less_or_equal_than:10, Informe um nome válido'

    ]
    update_validations = [
            'name IS not_empty AND more_than:0, Informe o nome',
            'duration IS not_empty AND more_or_equal_than:30, Informe a duração do filme',
            'gender IS not_empty AND less_or_equal_than:10, Informe um nome válido',
            'id IS not_empty, Informe o ID'

    ]
    rest = Rest(movie_model_instance, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Empresa criada com sucesso')
    rest.set_response('DEL', 'Empresa apagada com sucesso')
    rest.set_response('PUT', 'Empresa atualizada com sucesso')

    return rest.response()


@movie.route('movie', methods=['GET'])
def get():
    params = service_model.get_params()

    return 'ab' , 200


#
