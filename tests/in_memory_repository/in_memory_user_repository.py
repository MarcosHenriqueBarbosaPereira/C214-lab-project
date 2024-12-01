from c214_lab_project.domain.entities.user import User
from c214_lab_project.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        super(InMemoryUserRepository, self).__init__()

        self._items: list[User] = []

    def create(self, user: User):
        self._items.append(user)

    def find_by_username(self, username: str) -> User:
        for user in self._items:
            if user.username == username:
                return user
        return None
