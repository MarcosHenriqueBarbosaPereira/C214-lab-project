from abc import ABC, abstractmethod

from c214_lab_project.domain.entities.file import File


class FileRepository(ABC):
    @abstractmethod
    def upload(self, file: File): ...
