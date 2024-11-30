import uuid

from peewee import Model, UUIDField

from c214_lab_project.application.database.db_mgt.postgresql import (
    database_connection,
)


class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        database = database_connection.DATABASE
