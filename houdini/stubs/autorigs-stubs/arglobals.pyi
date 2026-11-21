# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Callable as Callable
from typing import Concatenate

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_S = TypeVar('_S')
_P = ParamSpec('_P')
unsavedchanges: bool

def mark_unsaved(setter: Callable[Concatenate[_S, _P], object]) -> Callable[Concatenate[_S, _P], None]:
    """decorator for any setters that should mark autorigs as unsaved"""
def mark_saved() -> None:
    """Mark autorigs has saved"""
def mark_dirty() -> None:
    """Mark autorigs has dirty"""
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
