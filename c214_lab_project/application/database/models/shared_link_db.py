from peewee import CharField, ForeignKeyField

from c214_lab_project.application.database.models.base_model import BaseModel
from c214_lab_project.application.database.models.file_db import FileDB
from c214_lab_project.application.database.models.user_db import UserDB


class SharedLinkDB(BaseModel):
    permission = CharField()

    file = ForeignKeyField(FileDB, backref="shared_links")
    shared_by = ForeignKeyField(UserDB, backref="shared_links")
