from abc import ABC, abstractmethod
from pathlib import Path

type FileObjectId = str


class R2Repository(ABC):
    @abstractmethod
    def upload(self, filepath: Path) -> FileObjectId:
        pass
