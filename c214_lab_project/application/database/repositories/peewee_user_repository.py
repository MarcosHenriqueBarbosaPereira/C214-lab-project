from peewee import DoesNotExist

from c214_lab_project.application.database.models.user_db import UserDB
from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.user_repository import UserRepository


class PeeweeUserRepository(UserRepository):
    def __init__(self) -> None:
        super(PeeweeUserRepository, self).__init__()

    def create(self, user: User) -> UserDB:
        created_user = UserDB.create(
            id=user.id,
            name=user.name,
            username=user.username,
            password=user.password,
        )

        return created_user

    def find_by_username(self, username: str) -> UserDB | None:
        try:
            found_user = (
                UserDB.select().where(UserDB.username == username).get()
            )
            return found_user
        except DoesNotExist:
            return None
