from peewee import CharField, FloatField, ForeignKeyField

from c214_lab_project.application.database.models.base_model import BaseModel
from c214_lab_project.application.database.models.user import User


class File(BaseModel):
    name = CharField(max_length=250)
    filesize = FloatField()
    filepath = CharField(max_length=1000)

    owner = ForeignKeyField(User, backref="files")
