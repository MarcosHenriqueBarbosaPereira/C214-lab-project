from abc import ABC, abstractmethod

from c214_lab_project.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User): ...
