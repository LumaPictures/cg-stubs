from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

_S = TypeVar("_S")
_P = ParamSpec("_P")

unsavedchanges: bool

def mark_unsaved(setter: Callable[Concatenate[_S, _P], object]) -> Callable[Concatenate[_S, _P], None]: ...
def mark_saved() -> None: ...
def mark_dirty() -> None: ...
def hasUnsavedChanges() -> bool: ...

class Dialogs:
    SAVE: int
    SAVE_ALL: int
    DISCARD: int
    DISCARD_ALL: int

    @staticmethod
    def multiSaveDialog(msg: str) -> int: ...
    @staticmethod
    def singleSaveDialog(msg: str) -> int: ...
