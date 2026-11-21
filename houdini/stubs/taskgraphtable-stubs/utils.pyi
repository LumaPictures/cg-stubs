# Houdini stubs generated from Houdini 22.0.466

from PySide6 import QtWidgets as QtWidgets
from collections.abc import Callable as Callable
from typing import Concatenate

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_S = TypeVar('_S')
def print_exceptions(f: Callable[_P, _R]) -> Callable[_P, _R]:
    """Wrapper to print any exceptions and then re-throw.

    Wrap the entire function in a try-catch and print the traceback if any, but
    also re-throw to allow proper exception handling where it exists. This is
    useful for the background thread methods, because those exceptions get
    swallowed by something.
    """
def synchronized(func: Callable[_P, _R]) -> Callable[_P, _R]: ...
def synchronized_method(method: Callable[Concatenate[_S, _P], _R]) -> Callable[Concatenate[_S, _P], _R]: ...
def clearLayout(layout: QtWidgets.QLayout) -> None: ...
