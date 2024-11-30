from typing import Required, TypedDict

from c214_lab_project.domain.entities.base.entity import BaseEntity
from c214_lab_project.domain.entities.user import User


class FileProps(TypedDict):
    id: Required[str]
    name: Required[str]
    filesize: Required[float]
    link: Required[str]
    owner: Required[User]


class File(BaseEntity[FileProps]):
    def __init__(self, props: FileProps) -> None:
        super(File, self).__init__(props)

    @property
    def name(self):
        return self._props["name"]

    @property
    def size(self):
        return self._props["filesize"]

    @property
    def shared_link(self):
        return self._props["share_link"]

    @property
    def link(self):
        return self._props["link"]

    @property
    def owner(self):
        return self._props["owner"]
