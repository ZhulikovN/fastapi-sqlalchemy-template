# pylint: ambiguous variable name

from typing import TypeVar  # noqa

D = TypeVar("D", bound=object)  # Domain Entity Type
I = TypeVar("I", bound=object)  # noqa  # ID Type
P = TypeVar("P", bound=object)  # Persistence Entity Type
