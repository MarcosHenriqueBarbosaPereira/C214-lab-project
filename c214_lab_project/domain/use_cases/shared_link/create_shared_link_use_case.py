from typing import Required, TypedDict, Union

from result import Err, Ok

from c214_lab_project.core.enums.shared_link_permissions import (
    ShareLinkPermission,
)
from c214_lab_project.core.exceptions.shared_link_exceptions import (
    DuplicateShareLinkException,
    NotAllowedToShareFileWithoutOwnershipException,
)
from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.entities.shared_link import SharedLink
from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.shared_link_repository import (
    SharedLinkRepository,
)
from c214_lab_project.domain.use_cases import UseCase


class SharedLinkRequest(TypedDict):
    permissions: Required[ShareLinkPermission]
    file: Required[File]
    file_owner: Required[User]


type CreateSharedLinkUseCaseResponse = Union[
    Ok[str] | Err[NotAllowedToShareFileWithoutOwnershipException]
]


class CreateSharedLinkUseCase(UseCase):
    def __init__(self, repository: SharedLinkRepository) -> None:
        super(CreateSharedLinkUseCase, self).__init__()

        self._repository = repository

    def execute(
        self, data: SharedLinkRequest
    ) -> CreateSharedLinkUseCaseResponse:
        shared_link = SharedLink(data)

        if shared_link.shared_by.id != shared_link.file.owner.id:
            return Err(NotAllowedToShareFileWithoutOwnershipException())

        shared_links_on_database = self._repository.find_by_file(
            shared_link.file.id
        )

        has_shared_links = len(shared_links_on_database) > 0
        if has_shared_links:
            is_duplicated_share_link = False
            for share_link in shared_links_on_database:
                if share_link.permissions == shared_link.permissions:
                    is_duplicated_share_link = True

            if is_duplicated_share_link:
                return Err(DuplicateShareLinkException())

        self._repository.create(shared_link)
        return Ok(shared_link.id)
