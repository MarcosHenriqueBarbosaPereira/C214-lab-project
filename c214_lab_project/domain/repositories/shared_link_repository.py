from abc import ABC, abstractmethod

from c214_lab_project.domain.entities.shared_link import SharedLink


class SharedLinkRepository(ABC):
    @abstractmethod
    def create(self, shared_link: SharedLink): ...
