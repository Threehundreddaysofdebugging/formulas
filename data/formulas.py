import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Formula(SqlAlchemyBase):
    __tablename__ = 'formula'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    section = sqlalchemy.Column(sqlalchemy.String)
    definition = sqlalchemy.Column(sqlalchemy.String)
