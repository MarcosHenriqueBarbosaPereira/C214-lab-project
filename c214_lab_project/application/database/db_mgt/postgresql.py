from peewee import Database as PeeweeDatabaseClass
from peewee import PostgresqlDatabase

from c214_lab_project.application.database.db_mgt.base import Database


class _Postgresql(Database):
    DATABASE = PostgresqlDatabase(
        "nest-clean",
        user="docker",
        password="docker",
        host="localhost",
    )

    def __init__(self):
        self.connect()

    def connect(self):
        if not _Postgresql.DATABASE.is_closed():
            return

        _Postgresql.DATABASE.connect()

    def disconnect(self):
        if _Postgresql.DATABASE.is_closed():
            return

        _Postgresql.DATABASE.close()

    @property
    def db(self) -> PeeweeDatabaseClass:
        return _Postgresql.DATABASE


database_connection = _Postgresql()
