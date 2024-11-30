from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.repositories.file_repository import FileRepository


class InMemoryFileRepository(FileRepository):
    def __init__(self) -> None:
        super(InMemoryFileRepository, self).__init__()

        self._items: list[File] = []

    def create(self, file: File):
        self._items.append(file)
