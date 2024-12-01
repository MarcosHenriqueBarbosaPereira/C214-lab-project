from uuid import uuid4

from peewee import DoesNotExist

from c214_lab_project.application.database.models.file_db import FileDB
from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.repositories.file_repository import FileRepository


class PeeweeFileRepository(FileRepository):
    def __init__(self) -> None:
        super(PeeweeFileRepository, self).__init__()

    def create(self, file: File) -> FileDB:
        created_file = FileDB.create(
            id=file.id,
            name=file.name,
            filesize=file.size,
            filepath=file.filepath,
            owner=file.owner.id,
        )
        return created_file

    def find_by_id(self, file_id: str) -> FileDB | None:
        try:
            found_file = FileDB.select().where(FileDB.id == file_id).get()
            return found_file
        except DoesNotExist:
            return None
