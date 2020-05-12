from abc import ABCMeta, abstractmethod
from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

from database_models import db


class Model:

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    status = Column(Boolean, nullable=True, default=True)
    created_by = Column(UUID(as_uuid=True), nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.utcnow)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    updated_at = Column(DateTime, nullable=True)
    removed_by = Column(UUID(as_uuid=True), nullable=True)
    removed_at = Column(DateTime, nullable=True)

    #TODO IMPLMENTAR FUNÇÃO PARA CREATED_BY - PEGAR ID
    def insert(self, json_obj):
        from core.util import create_uuid
        json_obj['id'] = create_uuid() if 'id' not in json_obj.keys() else json_obj['id']

        for keys in json_obj.keys():
            self.__setattr__(keys, json_obj[keys])

        db.session.add(self)
        db.session.commit()

    def get_list(self):
        return self.query.all()

    def sql_to_dict(self):
        sql_columns = self.__table__.columns.keys()

        sql_dict = {key: self.__getattribute__(key) for key in sql_columns}

        return sql_dict

    def update(self, data):
        id_param = data.get('id', None)

        if id_param:
            sql_obj = self.query.filter_by(id=id_param).first()

            for key in data.keys():
                sql_obj.__setattr__(key, data[key])

            db.session.commit()

    def delete(self, uuid):
        sql_obj = self.query.filter_by(id=uuid).first()

        if sql_obj:
            db.session.delete(sql_obj)
            db.session.commit()


class ModelQueryAbstract(metaclass=ABCMeta):
    pass


class ModelQuery:
    pass
