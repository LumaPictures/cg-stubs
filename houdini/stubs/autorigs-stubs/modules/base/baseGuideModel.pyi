# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Callable as Callable

from typing import TypeVar
from typing import TypeVar
_M = TypeVar('_M', bound='BaseGuideModel')
_V = TypeVar('_V')
def model_setter(arg: str) -> Callable[[Callable[[_M, _V], object]], Callable[[_M, _V], None]]: ...

class BaseGuideModel:
    unsavedchanges: bool
    def __init__(self) -> None: ...
    def hasUnsavedChanges(self) -> bool: ...
    def markSaved(self) -> None: ...
