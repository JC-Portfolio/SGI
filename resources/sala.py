from flask import Blueprint
from core.rest import Rest
from core.service import Service, ServiceModelQuery
from database_models.models import MovieTheaterModel, CinemaModel, MovieModel


class MovieTheaterQueryModel(MovieTheaterModel):
    def join_tables_to_query(self, params, query):
        query = query.join(MovieTheaterModel, MovieTheaterModel.id == CinemaModel.id)
        query = query.join(MovieTheaterModel, MovieTheaterModel.movie_id == MovieModel.id)

        return query

    def add_column_to_query(self, params, query):

        query = query.add_columns(MovieTheaterModel.id, MovieTheaterModel.qt_seats,
                                  MovieTheaterModel.movie_id,
                                  MovieTheaterModel.type_of,
                                  MovieTheaterModel.name,
                                  )

        return query

    def filter_query(self, params, query):
        return query


class MovieTheaterService(Service):
    pass


sala = Blueprint('sala', __name__, url_prefix='/')

sala_model_instance = MovieTheaterQueryModel()
sala_service = MovieTheaterService(sala_model_instance)
service_model = ServiceModelQuery(sala_model_instance)


@sala.route('sala/register', methods=['POST', 'PUT', 'DEL'])
def register():

    insert_validations = [
            'name IS not_empty AND less_or_equal_than_str:55, Informe o nome',
            'qt_seats IS not_empty AND less_or_equal_than:70, Informe a quantidade de cadeiras',
            'type IS not_empty AND less_or_equal_than_str:10, Informe o tipo de sala',
            'id_cinema IS not_empty, Informe o id do cinema'

    ]
    update_validations = [
            'name IS not_empty AND less_or_equal_than_str:55, Informe o nome',
            'qt_seats IS not_empty AND less_or_equal_than:70, Informe a quantidade de cadeiras',
            'type IS not_empty AND less_or_equal_than_str:10, Informe o tipo de sala',
            'film_id IS not_empty, Informe o id do filme',

    ]

    rest = Rest(sala_service, insert_validations, update_validations)

    rest.call_rest_method()
    rest.set_response('POST', 'Sala criada com sucesso')
    rest.set_response('DEL', 'Sala apagada com sucesso')
    rest.set_response('PUT', 'Sala atualizada com sucesso')

    return rest.response()


@sala.route('sala', methods=['GET'])
def get():
    params = service_model.get_params()

    return 'ab' , 200


#
