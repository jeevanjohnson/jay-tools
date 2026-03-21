from pathlib import Path
from typing import Type, TypeVar

from pydantic import BaseModel

from .database import _JsonDatabase

# Dev Notes:
# factory = a function or class whose sole purpose is to create instances of a class, in this case, `_JsonDatabase` parametrized with the provided Pydantic model.

T = TypeVar("T", bound=BaseModel)

def JsonDatabase(
    path: str | Path,
    models: Type[T],
    backup_on_validation_error: bool = True,
    encoding: str = "utf-8",
    errors: str = "strict",
    read_fallback_encodings: tuple[str, ...] = (),
    ensure_ascii: bool = False,
) -> _JsonDatabase[T]:
    return _JsonDatabase(
        path=path,
        database_model=models,
        backup_on_validation_error=backup_on_validation_error,
        encoding=encoding,
        errors=errors,
        read_fallback_encodings=read_fallback_encodings,
        ensure_ascii=ensure_ascii,
    )