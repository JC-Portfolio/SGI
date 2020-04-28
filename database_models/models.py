from . import db

from core.core_model import Model
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.postgresql import UUID, JSON, BOOLEAN, ARRAY


def create_db(app):
    db.init_app(app)
    app.db = db


class CompanyModel(Model, db.Model):
    __tablename__ = 'company'

    name = db.Column(db.VARCHAR(100), nullable=False)


class Headquarters(Model, db.Model):
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey(CompanyModel.id), nullable=False)
    city = db.Column(db.VARCHAR(100), nullable=False)
    state = db.Column(db.VARCHAR(100), nullable=False)


class CinemaModel(db.Model, Model):
    __tablename__ = 'cinema'

    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey(CompanyModel.id), nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False)
    qt_salas = db.Column(db.Integer, nullable=False)
    headquarters = db.Column(UUID(as_uuid=True), db.ForeignKey(Headquarters.id), nullable=False)


class MovieModel(db.Model, Model):
    __tablename__ = 'movie'

    name = db.Column(db.VARCHAR(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.VARCHAR(55), nullable=False)
    half_price = db.Column(db.Integer, autoincrement=True)
    full_price = db.Column(db.Integer, autoincrement=True)


class MovieTheaterModel(db.Model, Model):
    __tablename__ = 'movie_theater'

    cinema_id = db.Column(UUID(as_uuid=True), db.ForeignKey(CinemaModel.id), nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False)
    qt_seats = db.Column(db.Integer, nullable=False)
    type_of = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(UUID(as_uuid=True), db.ForeignKey(MovieModel.id), nullable=False)


class ProfileModel(Model, db.Model):
    __tablename__ = 'profile'

    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey(CompanyModel.id), nullable=True)
    name = db.Column(db.VARCHAR(100), nullable=False)
    permission = db.Column(JSON, nullable=False)
    supreme = db.Column(BOOLEAN, nullable=False, default=False)


class UserModel(db.Model, Model):
    __tablename__ = 'user'

    profile_id = db.Column(UUID(as_uuid=True), db.ForeignKey(ProfileModel.id), nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=False)
    salt = db.Column(db.VARCHAR(32), nullable=False)
    password = db.Column(db.VARCHAR(32), nullable=False)
    password_recovery = db.Column(db.VARCHAR(32), nullable=True)
    password_history = db.Column(JSON, nullable=True)
    permission = db.Column(MutableList.as_mutable(ARRAY(db.String)), nullable=False)
    token = db.Column(MutableList.as_mutable(ARRAY(db.String)), nullable=True)
