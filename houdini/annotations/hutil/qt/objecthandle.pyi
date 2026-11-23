from collections.abc import Callable
from typing import Generic, ParamSpec, TypeVar

from PySide6 import QtCore

_T = TypeVar("_T", bound=QtCore.QObject)
_P = ParamSpec("_P")

class QtObjectHandle(Generic[_T]):
    def __init__(self, object_type: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def __call__(self) -> _T: ...
