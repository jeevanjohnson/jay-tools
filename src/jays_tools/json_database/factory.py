from pathlib import Path
from typing import Type, TypeVar

from pydantic import BaseModel

from .database import _JsonDatabase

# Dev Notes:
# factory = a function or class whos sole purpose is to create instances of a class, in this case, JsonDatabaseInit or JsonDatabaseOptional.

T = TypeVar("T", bound=BaseModel)

def JsonDatabase(
    path: str | Path,
    models: Type[T],
    backup_on_validation_error: bool = True,
) -> _JsonDatabase[T]:
    return _JsonDatabase(
        path=path,
        database_model=models,
        backup_on_validation_error=backup_on_validation_error,
    )