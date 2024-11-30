from abc import ABC, abstractmethod

from peewee import Database as PeeweeDatabaseClass


class Database(ABC):
    DATABASE: PeeweeDatabaseClass = None

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass
