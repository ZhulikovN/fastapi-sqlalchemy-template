from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel, Field

from src.modules.author.domain.value_objects import Age, Biography, Name


@dataclass(frozen=True)
class NewAuthorCommand(BaseModel):
    name: Name
    age: Age
    biography: Optional[Biography]
