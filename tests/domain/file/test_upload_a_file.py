from c214_lab_project.core.exceptions.file_exceptions import (
    FileIsTooLargeException,
)
from c214_lab_project.domain.mappers.file_mapper import FileMapper
from c214_lab_project.domain.use_cases.file.upload_file_use_case import (
    UploadFileUseCase,
)
from tests.common import CommonTestCase
from tests.factories.make_file import make_file
from tests.in_memory_repository.in_memory_file_repository import (
    InMemoryFileRepository,
)
from tests.in_memory_repository.in_memory_r2_repository import (
    InMemoryR2Repository,
)


class TestUploadAFileUseCase(CommonTestCase):
    def setUp(self):
        self._repository = InMemoryFileRepository()
        self._bucket = InMemoryR2Repository()

        self._sut = UploadFileUseCase(self._repository, self._bucket)

        return super(TestUploadAFileUseCase, self).setUp()

    def test_should_be_able_to_upload_a_file(self):
        file_owner = self.current_test_user

        file = {
            "owner": file_owner,
            "filesize": 0,
            "filepath": __file__,
            "name": __file__,
        }

        result = self._sut.execute(file)
        self.assertTrue(result.is_ok())
        self.assertIsInstance(result.ok_value, str)

    def test_should_not_be_able_to_upload_large_file(self):
        file = make_file(filesize=1073741824)

        result = self._sut.execute(FileMapper.to_dict(file))
        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, FileIsTooLargeException)
