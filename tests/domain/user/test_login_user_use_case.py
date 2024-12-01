from c214_lab_project.core.exceptions.user_exceptions import (
    UsernameIsEmptyException,
)
from c214_lab_project.domain.mappers.user_mapper import UserMapper
from c214_lab_project.domain.use_cases.user.create_user_use_case import (
    CreateUserUseCase,
)
from c214_lab_project.domain.use_cases.user.login_user_use_case import (
    LoginUserUseCase,
)
from tests.common import CommonTestCase
from tests.factories.make_user import make_user
from tests.in_memory_repository.in_memory_user_repository import (
    InMemoryUserRepository,
)


class TestLoginUserUseCase(CommonTestCase):
    def setUp(self):
        self._repository = InMemoryUserRepository()
        self._sut = LoginUserUseCase(self._repository)
        self._create_user_use_case = CreateUserUseCase(self._repository)
        self._user = make_user()
        self._create_user_use_case.execute(UserMapper.to_dict(self._user))

        return super(TestLoginUserUseCase, self).setUp()

    def test_should_be_able_to_login(self):
        result = self._sut.execute(
            username=self._user.username, password=self._user.password
        )

        self.assertTrue(result.is_ok())

    def test_should_not_be_able_to_login_empty_username(self):
        result = self._sut.execute(username="", password="123")

        self.assertTrue(result.is_err())
        self.assertIsInstance(result.err_value, UsernameIsEmptyException)
