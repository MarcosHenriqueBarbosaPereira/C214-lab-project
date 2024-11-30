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

    def find_by_file(self, shared_file_id: str) -> list[SharedLink]:
        shared_links = []
        for shared_link in self._items:
            if shared_link.file.id == shared_file_id:
                shared_links.append(shared_link)
        return shared_links
