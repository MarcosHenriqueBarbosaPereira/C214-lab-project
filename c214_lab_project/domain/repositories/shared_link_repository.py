from abc import ABC, abstractmethod

from c214_lab_project.domain.entities.shared_link import SharedLink


class SharedLinkRepository(ABC):
    @abstractmethod
    def create(self, shared_link: SharedLink) -> None:
        pass

    @abstractmethod
    def find_by_file(self, shared_file_id: str) -> list[SharedLink]:
        pass
