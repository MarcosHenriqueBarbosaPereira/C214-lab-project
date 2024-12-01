from pathlib import Path
from typing import Required, TypedDict

from result import Err, Ok

from c214_lab_project.core.exceptions.file_exceptions import (
    FileIsTooLargeException,
)
from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.file_repository import FileRepository
from c214_lab_project.domain.repositories.r2_repository import R2Repository
from c214_lab_project.domain.use_cases import UseCase


class FileRequest(TypedDict):
    name: Required[str]
    filesize: Required[float]
    filepath: Required[Path]
    owner: Required[User]


MAX_FILESIZE = 1073741824  # 1GiB IN BYTES


class UploadFileUseCase(UseCase):
    def __init__(
        self, repository: FileRepository, r2_repository: R2Repository
    ) -> None:
        super(UploadFileUseCase, self).__init__()

        self._repository = repository
        self._bucket = r2_repository

    def execute(
        self, data: FileRequest
    ) -> Ok[str] | Err[FileIsTooLargeException]:
        file = File(data)

        if file.size >= MAX_FILESIZE:
            return Err(FileIsTooLargeException())

        self._bucket.upload(file.filepath, file.id)
        self._repository.create(file)

        return Ok(file.id)
