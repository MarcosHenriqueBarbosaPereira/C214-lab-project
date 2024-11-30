from typing import Required, TypedDict, Union

from result import Err, Ok

from c214_lab_project.core.exceptions.user_exceptions import (
    DuplicatedUserUsernameException,
    NameIsEmptyException,
    PasswordIsTooShortException,
    UsernameIsEmptyException,
)
from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.user_repository import UserRepository
from c214_lab_project.domain.use_cases import UseCase

type CreateUserUseCaseResponse = Union[
    Ok[str], Err[DuplicatedUserUsernameException]
]


class UserRequest(TypedDict):
    name: Required[str]
    username: Required[str]
    password: Required[str]


class CreateUserUseCase(UseCase):
    def __init__(self, repository: UserRepository) -> None:
        super(CreateUserUseCase, self).__init__()

        self._repository = repository

    def execute(self, data: UserRequest) -> CreateUserUseCaseResponse:
        user = User(data)

        if not user.name or user.name == "":
            return Err(NameIsEmptyException())

        if not user.username or user.username == "":
            return Err(UsernameIsEmptyException())

        user_on_database = self._repository.find_by_username(user.username)

        if user_on_database:
            return Err(DuplicatedUserUsernameException())

        if len(user.password) < 8:
            return Err(PasswordIsTooShortException())

        self._repository.create(user)

        return Ok(user.id)
