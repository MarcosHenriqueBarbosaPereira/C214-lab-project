from typing import Required, TypedDict

from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.file_repository import FileRepository
from c214_lab_project.domain.use_cases import UseCase


class FileRequest(TypedDict):
    name: Required[str]
    filesize: Required[float]
    link: Required[str]
    owner: Required[User]


class UploadFileUseCase(UseCase):
    def __init__(self, repository: FileRepository) -> None:
        super(UploadFileUseCase, self).__init__()

        self._repository = repository

    def execute(self, data: FileRequest):
        file = File(data)
        self._repository.create()

        return file.id
