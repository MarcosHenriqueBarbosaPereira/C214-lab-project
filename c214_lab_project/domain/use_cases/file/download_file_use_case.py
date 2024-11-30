from result import Err, Ok

from c214_lab_project.core.exceptions.file_exceptions import (
    BlockedFileByPermissionException,
    FileDoesNotExistsException,
)
from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.file_repository import FileRepository
from c214_lab_project.domain.repositories.r2_repository import R2Repository
from c214_lab_project.domain.repositories.shared_link_repository import (
    SharedLinkRepository,
)
from c214_lab_project.domain.use_cases import UseCase


class DownloadFileUseCase(UseCase):
    def __init__(
        self,
        repository: FileRepository,
        r2_repository: R2Repository,
        shared_link_repository: SharedLinkRepository,
    ) -> None:
        super(DownloadFileUseCase, self).__init__()

        self._repository = repository
        self._bucket = r2_repository
        self._shared_link_repository = shared_link_repository

    def execute(
        self, file_id: str, current_user: User
    ) -> Ok[bool] | Err[FileDoesNotExistsException]:
        file_on_db = self._repository.find_by_id(file_id)
        if file_on_db is None:
            return Err(FileDoesNotExistsException())

        if file_on_db.owner.id != current_user.id:
            shared_links = self._shared_link_repository.find_by_file(file_id)
            is_permitted_to_download_file = len(shared_links) > 0
            if not is_permitted_to_download_file:
                return Err(BlockedFileByPermissionException())

        download_result = self._bucket.download(file_on_db.id)
        return Ok(download_result)
