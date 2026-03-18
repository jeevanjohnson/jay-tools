from typing import Literal, Type, TypeVar, overload
from pathlib import Path
from .database import JsonDatabaseInit
from .database import JsonDatabaseOptional

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

@overload
def JsonDatabase(
    path: str | Path, 
    models: Type[T], 
    auto_init: Literal[True], 
    backup_on_validation_error: bool = True,
) -> JsonDatabaseInit[T]: ...

@overload
def JsonDatabase(
    path: str | Path, 
    models: Type[T], 
    auto_init: Literal[False], 
    backup_on_validation_error: bool = True,
) -> JsonDatabaseOptional[T]: ...

@overload
def JsonDatabase(
    path: str | Path, 
    models: Type[T],
    *, # This forces the caller to use keyword arguments for the following parameters.
    backup_on_validation_error: bool = True,
) -> JsonDatabaseOptional[T]: ...

@overload
def JsonDatabase(
    path: str | Path, 
    models: Type[T],
) -> JsonDatabaseOptional[T]: ...

def JsonDatabase(
    path: str | Path,
    models: Type[T],
    auto_init: bool = False,
    backup_on_validation_error: bool = True,
) -> JsonDatabaseInit[T] | JsonDatabaseOptional[T]:
    if auto_init:
        return JsonDatabaseInit(
            path=path,
            database_model=models,
            backup_on_validation_error=backup_on_validation_error,
        )
    else:
        return JsonDatabaseOptional(
            path=path,
            database_model=models,
            backup_on_validation_error=backup_on_validation_error,
        )