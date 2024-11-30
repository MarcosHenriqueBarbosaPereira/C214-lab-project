from c214_lab_project.core.enums.shared_link_permissions import (
    ShareLinkPermission,
)
from c214_lab_project.core.exceptions.shared_link_exceptions import (
    NotAllowedToShareFileWithoutOwnershipException,
)
from c214_lab_project.domain.use_cases.shared_link.create_shared_link_use_case import (
    CreateSharedLinkUseCase,
)
from tests.common import CommonTestCase
from tests.factories.make_file import make_file
from tests.factories.make_user import make_user
from tests.in_memory_repository.in_memory_shared_link_repository import (
    InMemorySharedLinkRepository,
)


class TestCreateSharedLinkUseCase(CommonTestCase):
    def setUp(self):
        self._repository = InMemorySharedLinkRepository()
        self._sut = CreateSharedLinkUseCase(self._repository)

        return super(TestCreateSharedLinkUseCase, self).setUp()

    def test_should_be_able_to_share_a_file(self):
        shared_by = make_user()
        file = make_file(owner=shared_by)

        shared_link = {
            "file": file,
            "shared_by": shared_by,
            "permissions": ShareLinkPermission.FULL,
        }

        result = self._sut.execute(shared_link)
        self.assertTrue(result.is_ok())
        self.assertIsInstance(result.ok_value, str)

    def test_should_not_be_able_to_share_a_file_from_another_owner(self):
        shared_by = make_user()
        file = make_file()

        shared_link = {
            "file": file,
            "shared_by": shared_by,
            "permissions": ShareLinkPermission.FULL,
        }

        result = self._sut.execute(shared_link)
        self.assertTrue(result.is_err())
        self.assertIsInstance(
            result.err_value, NotAllowedToShareFileWithoutOwnershipException
        )
