from typing import Required, TypedDict

from c214_lab_project.domain.entities.base.entity import BaseEntity


class UserProps(TypedDict):
    id: Required[str]
    name: Required[str]
    username: Required[str]
    password: Required[str]


class User(BaseEntity[UserProps]):
    def __init__(self, props: UserProps) -> None:
        super(User, self).__init__(props)

    @property
    def name(self) -> str:
        return self._props["name"]

    @property
    def username(self) -> str:
        return self._props["username"]

    @property
    def password(self) -> str:
        return self._props["password"]
