from c214_lab_project.domain.entities.shared_link import SharedLink
from c214_lab_project.domain.repositories.shared_link_repository import (
    SharedLinkRepository,
)


class InMemorySharedLinkRepository(SharedLinkRepository):
    def __init__(self) -> None:
        super(InMemorySharedLinkRepository, self).__init__()

        self._items: list[SharedLink] = []

    def create(self, shared_link: SharedLink):
        self._items.append(shared_link)
