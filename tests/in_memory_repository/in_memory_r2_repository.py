from pathlib import Path
from uuid import uuid4

from c214_lab_project.domain.repositories.r2_repository import (
    FileObjectId,
    R2Repository,
)


class InMemoryR2Repository(R2Repository):
    def upload(self, filepath: Path) -> FileObjectId:
        return str(uuid4())
