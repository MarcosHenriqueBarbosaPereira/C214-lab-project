from c214_lab_project.core.exceptions.file_exceptions import (
    BlockedFileByPermissionException,
    FileDoesNotExistsException,
)
from c214_lab_project.domain.mappers.file_mapper import FileMapper
from c214_lab_project.domain.use_cases.file.download_file_use_case import (
    DownloadFileUseCase,
)
from tests.common import CommonTestCase
from tests.factories.make_file import make_file
from tests.factories.make_shared_link import make_shared_link
from tests.in_memory_repository.in_memory_file_repository import (
    InMemoryFileRepository,
)
from tests.in_memory_repository.in_memory_r2_repository import (
    InMemoryR2Repository,
)
from tests.in_memory_repository.in_memory_shared_link_repository import (
    InMemorySharedLinkRepository,
)


class TestDownloadFileUseCase(CommonTestCase):
    def setUp(self):
        self._repository = InMemoryFileRepository()
        self._shared_link_repository = InMemorySharedLinkRepository()
        self._bucket = InMemoryR2Repository()

        self._sut = DownloadFileUseCase(
            self._repository, self._bucket, self._shared_link_repository
        )

        return super(TestDownloadFileUseCase, self).setUp()

    def test_should_be_able_to_download_a_file(self):
        file_owner = self.current_test_user
        file = make_file(owner=file_owner, _id="file-id")

        self._repository._items.append(file)

        result = self._sut.execute("file-id", self.current_test_user)
        self.assertTrue(result.is_ok())
        self.assertTrue(result.ok_value)

    def test_should_be_able_to_download_a_file(self):
        file_owner = self.current_test_user
        file = make_file(owner=file_owner, _id="file-id")

        self._repository._items.append(file)

        result = self._sut.execute(
            "file-id-not-uploaded", self.current_test_user
        )
        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, FileDoesNotExistsException)

    def test_should_not_be_able_to_download_file_from_another_owner_without_permissions(
        self,
    ):
        file = make_file(_id="file-id")

        self._repository._items.append(file)
        result = self._sut.execute("file-id", self.current_test_user)
        self.assertTrue(result.is_err())
        self.assertIsInstance(
            result.err_value, BlockedFileByPermissionException
        )

    def test_should_be_able_to_download_file_from_other_owner_with_permissions(
        self,
    ):
        file = make_file(_id="file-id")
        shared_link = make_shared_link(file=file, shared_by=file.owner)

        self._repository._items.append(file)
        self._shared_link_repository._items.append(shared_link)
        
        result = self._sut.execute("file-id", self.current_test_user)
        self.assertTrue(result.is_ok())
        self.assertTrue(
            result.ok_value,
        )
