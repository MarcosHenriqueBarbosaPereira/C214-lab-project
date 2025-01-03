from uuid import uuid4


class BaseEntity[T]:
    def __init__(self, props: T) -> None:
        if not props.get("id", None):
            props["id"] = str(uuid4())

        self._props = props

    @property
    def id(self) -> str:
        return self._props["id"]

    @id.setter
    def id(self, new_id: str) -> None:
        self._props["id"] = new_id
