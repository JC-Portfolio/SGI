from flask import request, jsonify
from datetime import datetime
from functools import wraps
from core.util import sanitize_obj, sql_to_dict
from core.insert_validations import InsertValidations
from core.api_exceptions import ApiException


class ServiceDecorators:
    @classmethod
    def _validation(cls, json=None, validations=None):
        def decorate(func):
            @wraps(func)
            def make_validation(*args, **kwargs):
                insert = InsertValidations(json)
                for x in validations:
                    extract_args = x.split(',')
                    insert.add(*extract_args)
                insert.is_valid()
                return func(*args, **kwargs)

            return make_validation

        return decorate

    @classmethod
    def _profile_type(cls):
        pass


class Service(ServiceDecorators):

    def __init__(self, model):
        self.model = model
        self._data = None

    def data(self, index=None):
        self._data = self._data if self._data else request.json

        if index:
            return self._data.get(index, None)
        return self._data

    def make_insert(self, validations):
        @ServiceDecorators._validation(self._data, validations)
        def insert(self):
            self.model.insert(self._data)

        insert(self)

    def list(self, *args):

        sql_objects = self.model.get_list()
        list_dict = [new_dict.sql_to_dict() for new_dict in sql_objects]

        return {f"{self.model.__tablename__}": list_dict}, 200

    def make_update(self, validations):
        @ServiceDecorators._validation(self._data, validations)
        def update(self):

            self._data['updated_at'] = datetime.now()

            self.model.update(self._data)

        update(self)

    #TODO implementar profile type
    def delete(self, *args):
        for ids in self._data['ids']:
            self.model.delete(ids)


class ServiceModelQuery:
    def __init__(self, model):
        self.model = model

    @classmethod
    def get_params(cls):
        args = request.args
        json_args = request.json

        return {"params": args[key] for key in args.keys(), *json_args}

    def find_all(self, params):
        query = self.model.query
        query = query.filter_query(params, query)
        query = query.join_tables_to_query(params, query)
        query = query.add_column_to_query(params, query)
        page = params.get('page', None)
        per_page = params.get('per_page', None)
        max_per = params.get('max_per_page', None)
        query = query.paginate(page, per_page, error_out=True, max_per_page=max_per)
        remove_fields = ['created_by', 'removed_at', 'removed_by', 'updated_at', 'updated_by']

        response_obj = {"documents": sanitize_obj(query.items, remove_fields),
                        "paginate": {
                             "page": {"current": query.page, "total": query.pages},
                             "size": query.per_page}
                        }

        return response_obj

    def find_by_id(self, params):
        uuid = params.get('id', None)

        if uuid is None:
            raise ApiException('Você deve informar o registro')

        query = self.model.query
        query = query.join_tables_to_query(params, query)
        query = query.add_column_to_query(params, query)
        query = query.filter_by(id=uuid).first()

        remove_fields = ['created_by', 'removed_at', 'removed_by', 'updated_at', 'updated_by']
        dict_obj = [sql_to_dict(query)]

        response_obj = {'documents': sanitize_obj(dict_obj, remove_fields)}

        return response_obj



