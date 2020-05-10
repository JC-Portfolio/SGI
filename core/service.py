from flask import request
from datetime import datetime
from core.util import response
from functools import wraps
from core.insert_validations import InsertValidations


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

    def list(self):

        sql_objects = self.model.get_list()
        list_dict = [new_dict.to_dict() for new_dict in sql_objects]

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
