from typing import Any, Protocol


class SWidget(Protocol):

    def get_context(self) -> Any:
        ...

    def serialize(self) -> Any:
        ...

    def load(self, value: Any) -> None:
        ...

    def get_default_serialized_data(self) -> Any:
        ...


    @property
    def widget_type(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def label(self) -> str:
        ...

    @property
    def col(self) -> int:
        ...

