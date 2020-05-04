from flask import request
from datetime import datetime
from core.util import response


class Service:

    def __init__(self, model=None):
        self.model = model
        self._data = None

    #TODO CRIAR PROPRIEDADE PARA _DATA
    def data(self, index=None):
        data = self._data if self._data else request.json

        if index:
            return data.get(index, None)
        return data

    def insert(self):
        data = self._data

        self.model.insert(data)
        return response("Registro criado com sucesso", 200)

    def list(self):

        sql_objects = self.model.get_list()
        list_dict = [new_dict.to_dict() for new_dict in sql_objects]

        return {f"{self.model.__tablename__}": list_dict}, 200

    def update(self):

        self._data['updated_at'] = datetime.now()

        obj = self.model.update(self._data)
        if obj:
            return response("Cadastro atualizado com sucesso", http_status=200)

        return response("Cadastro não encontrado", http_status=404)

    def delete(self):
        for ids in self._data['ids']:
            self.model.delete(ids)

        return response("Registro apagado com sucesso", http_status=200)