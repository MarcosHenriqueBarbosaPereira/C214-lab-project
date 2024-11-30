from faker import Faker

from c214_lab_project.domain.entities.file import File, User
from tests.factories.make_user import make_user
from tests.utils.convert_uuid_into_str import convert_uuid_into_str

fake = Faker()


def make_file(
    name: str = None,
    filesize: str = None,
    link: str = None,
    owner: User = None,
    *,
    _id: str = None,
) -> File:
    if _id is None:
        _id = fake.uuid4(convert_uuid_into_str)

    if owner is None:
        owner = make_user()

    if link is None:
        link = fake.url()

    if filesize is None:
        filesize = fake.random_int()

    if name is None:
        name = fake.file_name()

    return File(
        {
            "id": _id,
            "name": name,
            "filesize": filesize,
            "link": link,
            "owner": owner,
        }
    )
