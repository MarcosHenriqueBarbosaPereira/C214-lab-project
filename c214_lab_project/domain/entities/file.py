from pathlib import Path
from typing import Required, TypedDict

from c214_lab_project.domain.entities.base.entity import BaseEntity
from c214_lab_project.domain.entities.user import User


class FileProps(TypedDict):
    id: Required[str]
    name: Required[str]
    filesize: Required[float]
    filepath: Required[Path]
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
    def filepath(self):
        return self._props["filepath"]

    @property
    def owner(self):
        return self._props["owner"]
