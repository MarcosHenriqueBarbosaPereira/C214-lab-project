from typing import Dict

from c214_lab_project.domain.entities.user import User


class UserMapper:
    @staticmethod
    def to_dict(user: User) -> Dict:

        return {
            "id": str(user.id),
            "name": user.name,
            "username": user.username,
            "password": user.password,
        }
