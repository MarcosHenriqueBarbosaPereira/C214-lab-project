from c214_lab_project.core.exceptions.user_exceptions import (
    DuplicatedUserUsernameException,
    NameIsEmptyException,
    PasswordIsTooShortException,
    UsernameIsEmptyException,
)
from c214_lab_project.domain.mappers.user_mapper import UserMapper
from c214_lab_project.domain.use_cases.user.create_user_use_case import (
    CreateUserUseCase,
)
from tests.common import CommonTestCase
from tests.factories.make_user import make_user
from tests.in_memory_repository.in_memory_user_repository import (
    InMemoryUserRepository,
)


class TestCreateUserUseCase(CommonTestCase):
    def setUp(self):
        self._repository = InMemoryUserRepository()
        self._sut = CreateUserUseCase(self._repository)

        return super(TestCreateUserUseCase, self).setUp()

    def test_should_be_able_to_create_a_user(self):
        user = make_user()

        result = self._sut.execute(UserMapper.to_dict(user))
        self.assertTrue(result.is_ok())
        self.assertIsInstance(result.ok_value, str)
        self.assertEqual(result.ok_value, user.id)

    def test_should_not_be_able_to_create_a_user_with_duplicated_username(self):
        user = make_user()
        self._repository.create(user)

        duplicated_user = make_user(username=user.username)

        result = self._sut.execute(UserMapper.to_dict(duplicated_user))
        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, DuplicatedUserUsernameException)

    def test_should_be_able_to_create_a_user_with_password_bigger_than_8_characters(
        self,
    ):
        user = make_user(password="12345678")

        result = self._sut.execute(UserMapper.to_dict(user))
        self.assertTrue(result.is_ok())
        self.assertEqual(result.ok_value, user.id)

    def test_should_not_be_able_to_create_a_user_with_password_smaller_than_8_characters(
        self,
    ):
        user = make_user(password="1234567")

        result = self._sut.execute(UserMapper.to_dict(user))
        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, PasswordIsTooShortException)

    def test_should_not_be_able_to_create_a_user_with_empty_username(self):
        user = make_user(username="")

        result = self._sut.execute(UserMapper.to_dict(user))
        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, UsernameIsEmptyException)

    def test_should_not_be_able_to_create_a_user_with_empty_name(self):
        user = make_user(name="")

        result = self._sut.execute(UserMapper.to_dict(user))
        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, NameIsEmptyException)
