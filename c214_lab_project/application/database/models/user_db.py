from peewee import CharField

from c214_lab_project.application.database.models.base_model import BaseModel


class UserDB(BaseModel):
    name = CharField(max_length=250)
    username = CharField(max_length=200)
    password = CharField(max_length=200)
