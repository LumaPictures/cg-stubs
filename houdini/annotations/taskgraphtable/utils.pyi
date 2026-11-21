from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

from PySide6 import QtWidgets

_P = ParamSpec("_P")
_R = TypeVar("_R")
_S = TypeVar("_S")

def print_exceptions(f: Callable[_P, _R]) -> Callable[_P, _R]: ...
def synchronized(func: Callable[_P, _R]) -> Callable[_P, _R]: ...
def synchronized_method(
    method: Callable[Concatenate[_S, _P], _R],
) -> Callable[Concatenate[_S, _P], _R]: ...
def clearLayout(layout: QtWidgets.QLayout) -> None: ...
