from uuid import uuid4

from peewee import DoesNotExist

from c214_lab_project.application.database.models.shared_link_db import (
    SharedLinkDB,
)
from c214_lab_project.domain.entities.shared_link import SharedLink
from c214_lab_project.domain.repositories.shared_link_repository import (
    SharedLinkRepository,
)


class PeeweeSharedLinkRepository(SharedLinkRepository):
    def __init__(self) -> None:
        super(PeeweeSharedLinkRepository, self).__init__()

    def create(self, shared_link: SharedLink) -> SharedLinkDB:
        created_shared_link = SharedLinkDB.create(
            id=shared_link.id,
            permissions=shared_link.permissions,
            file=shared_link.file.id,
            shared_by=shared_link.shared_by.id,
        )
        return created_shared_link

    def find_by_file(self, shared_file_id: str) -> list[SharedLinkDB] | None:
        try:
            found_links = (
                SharedLinkDB.select()
                .where(SharedLinkDB.file == shared_file_id)
                .get()
            )
            return found_links
        except DoesNotExist:
            return []
