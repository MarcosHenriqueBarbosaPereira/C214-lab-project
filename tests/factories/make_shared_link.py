from faker import Faker

from c214_lab_project.core.enums.shared_link_permissions import (
    ShareLinkPermission,
)
from c214_lab_project.domain.entities.file import File
from c214_lab_project.domain.entities.shared_link import SharedLink
from c214_lab_project.domain.entities.user import User
from tests.factories.make_file import make_file
from tests.factories.make_user import make_user
from tests.utils.convert_uuid_into_str import convert_uuid_into_str

fake = Faker()


def make_shared_link(
    link: str = None,
    permissions: ShareLinkPermission = None,
    shared_by: User = None,
    file: File = None,
    *,
    _id: str = None,
) -> SharedLink:
    if _id is None:
        _id = fake.uuid4(convert_uuid_into_str)

    if link is None:
        link = fake.url()

    if permissions is None:
        permissions = ShareLinkPermission.READ_ONLY

    if shared_by is None:
        shared_by = make_user()

    if file is None:
        file = make_file(owner=shared_by)

    return SharedLink(
        {
            "id": _id,
            "link": link,
            "permissions": permissions,
            "shared_by": shared_by,
            "file": file,
        }
    )
