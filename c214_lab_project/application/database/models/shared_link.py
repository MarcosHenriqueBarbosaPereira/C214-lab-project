from peewee import CharField, ForeignKeyField

from c214_lab_project.application.database.models.base_model import BaseModel
from c214_lab_project.application.database.models.file import File
from c214_lab_project.application.database.models.user import User


class SharedLink(BaseModel):
    permission = CharField()

    file = ForeignKeyField(File, backref="shared_links")
    shared_by = ForeignKeyField(User, backref="shared_links")
