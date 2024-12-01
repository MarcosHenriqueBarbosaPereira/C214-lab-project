from typing import Required, TypedDict, Union

from result import Err, Ok

from c214_lab_project.core.exceptions.user_exceptions import (
    DuplicatedUserUsernameException,
    NameIsEmptyException,
    PasswordIsTooShortException,
    UsernameIsEmptyException,
    WrongPasswordCredential,
    WrongUsernameCredential,
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


class LoginUserUseCase(UseCase):
    def __init__(self, repository: UserRepository) -> None:
        super(LoginUserUseCase, self).__init__()

        self._repository = repository

    def execute(
        self, username: str, password: str
    ) -> CreateUserUseCaseResponse:

        if username is None or username == "":
            return Err(UsernameIsEmptyException())

        user_on_database = self._repository.find_by_username(username)

        if user_on_database is None:
            Err(WrongUsernameCredential())
        elif user_on_database.password != password:
            Err(WrongPasswordCredential())

        return Ok(user_on_database)
