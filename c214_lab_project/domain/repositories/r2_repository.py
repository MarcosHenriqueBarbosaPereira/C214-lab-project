from abc import ABC, abstractmethod
from pathlib import Path

type FileObjectId = str


class R2Repository(ABC):
    @abstractmethod
    def upload(self, filepath: Path, file_id: str) -> FileObjectId:
        pass

    @abstractmethod
    def download(self, file_object_id: str) -> bool:
        pass
