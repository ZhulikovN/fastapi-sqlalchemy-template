from typing import TypeVar

D = TypeVar("D", bound=object)  # Domain Entity Type
I = TypeVar("I", bound=object)  # noqa  # ID Type
P = TypeVar("P", bound=object)  # Persistence Entity Type
