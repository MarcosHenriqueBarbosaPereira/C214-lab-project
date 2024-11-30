from typing import Required, TypedDict

from c214_lab_project.core.enums.shared_link_permissions import (
    ShareLinkPermission,
)
from c214_lab_project.domain.entities.base.entity import BaseEntity
from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.entities.user import User


class SharedLinkProps(TypedDict):
    id: Required[str]
    permissions: Required[ShareLinkPermission]
    file: Required[File]
    shared_by: Required[User]


class SharedLink(BaseEntity[SharedLinkProps]):
    def __init__(self, props: SharedLinkProps) -> None:
        super(SharedLink, self).__init__(props)

    @property
    def file(self):
        return self._props["file"]

    @property
    def permissions(self):
        return self._props["permissions"]

    @property
    def shared_by(self):
        return self._props["shared_by"]
