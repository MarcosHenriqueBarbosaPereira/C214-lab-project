from abc import ABC, abstractmethod

from c214_lab_project.domain.entities.file import File


class FileRepository(ABC):
    @abstractmethod
    def create(self, file: File) -> None:
        pass

    @abstractmethod
    def find_by_id(self, file_id: str) -> File | None:
        pass
