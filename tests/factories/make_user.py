from faker import Faker

from c214_lab_project.domain.entities.user import User
from tests.utils.convert_uuid_into_str import convert_uuid_into_str

fake = Faker()


def make_user(
    name: str = None,
    username: str = None,
    password: str = None,
    *,
    _id: str = None,
) -> User:
    if _id is None:
        _id = fake.uuid4(convert_uuid_into_str)

    if password is None:
        password = fake.password()

    if username is None:
        username = fake.user_name()

    if name is None:
        name = fake.name()

    return User(
        {"id": _id, "name": name, "username": username, "password": password}
    )
