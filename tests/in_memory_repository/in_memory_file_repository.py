from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.repositories.file_repository import FileRepository


class InMemoryFileRepository(FileRepository):
    def __init__(self) -> None:
        super(InMemoryFileRepository, self).__init__()

        self._items: list[File] = []

    def create(self, file: File):
        self._items.append(file)

    def find_by_id(self, file_id: str) -> File | None:
        for file in self._items:
            if file.id == file_id:
                return file
