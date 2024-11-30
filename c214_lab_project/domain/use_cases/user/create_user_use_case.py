from typing import Required, TypedDict

from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.user_repository import UserRepository
from c214_lab_project.domain.use_cases import UseCase


class UserRequest(TypedDict):
    name: Required[str]
    username: Required[str]
    password: Required[str]


class CreateUserUseCase(UseCase):
    def __init__(self, repository: UserRepository) -> None:
        super(CreateUserUseCase, self).__init__()

        self._repository = repository

    def execute(self, data: UserRequest):
        user = User(data)
        self._repository.create(user)

        return user.id
