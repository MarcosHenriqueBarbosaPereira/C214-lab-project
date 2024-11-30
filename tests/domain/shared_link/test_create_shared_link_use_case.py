from c214_lab_project.core.enums.shared_link_permissions import (
    ShareLinkPermission,
)
from c214_lab_project.core.exceptions.shared_link_exceptions import (
    DuplicateShareLinkException,
    NotAllowedToShareFileWithoutOwnershipException,
)
from c214_lab_project.domain.mappers.shared_link_mapper import SharedLinkMapper
from c214_lab_project.domain.use_cases.shared_link.create_shared_link_use_case import (
    CreateSharedLinkUseCase,
)
from tests.common import CommonTestCase
from tests.factories.make_file import make_file
from tests.factories.make_shared_link import make_shared_link
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

    def test_should_be_able_to_create_shared_link_with_different_permissions_to_same_file(
        self,
    ):
        shared_by = make_user()
        file = make_file(owner=shared_by)

        shared_link_full_access = make_shared_link(
            file=file, permissions=ShareLinkPermission.FULL, shared_by=shared_by
        )
        shared_link_read_only = make_shared_link(
            file=file,
            permissions=ShareLinkPermission.READ_ONLY,
            shared_by=shared_by,
        )

        self._repository._items.append(shared_link_full_access)
        result = self._sut.execute(
            SharedLinkMapper.to_dict(shared_link_read_only)
        )

        self.assertTrue(result.is_ok())
        self.assertEqual(result.ok_value, shared_link_read_only.id)

    def test_should_not_be_able_to_create_shared_link_with_same_permissions_to_same_file(
        self,
    ):
        shared_by = make_user()
        file = make_file(owner=shared_by)

        shared_link_full_access = make_shared_link(
            file=file, permissions=ShareLinkPermission.FULL, shared_by=shared_by
        )
        shared_link_full_access_2 = make_shared_link(
            file=file, permissions=ShareLinkPermission.FULL, shared_by=shared_by
        )

        self._repository._items.append(shared_link_full_access)
        result = self._sut.execute(
            SharedLinkMapper.to_dict(shared_link_full_access_2)
        )

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, DuplicateShareLinkException)
