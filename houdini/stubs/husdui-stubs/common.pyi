import hou
from collections.abc import Callable as Callable, Container
from husdui import constants as constants
from hutil.Qt import QtGui

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_T = TypeVar('_T')
theBypassDebug: bool

def debug_print(*args: object) -> None:
    """
    Print a debug message prepended by the calling function and line number.
    """
def error_print(*args: object) -> None:
    """
    Print an error message prepended by the calling function and linenumber.
    """

class debugPerfPaneEvent:
    def __init__(self, category: str, label: str) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

def debug_perfmon_function(category: str) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]:
    """
    Add perfmon instrumentation to a function.
    """
def debug_perfmon_class(category: str | None = None, exclude: Container[str] = ...) -> Callable[[type[_T]], type[_T]]:
    """
    Add perfmon instrumentation to all functions in a class.  Use `exclude` to specify function not to instrument.
    """

class NoValidStage(Exception): ...

def getNextOrdinalName(prefix: str, existing: Container[str] | None = None, start_index: int = 1) -> str: ...
def is_lopnodetype(node: object, typename: str) -> bool: ...
def getAttrIndexAndName(attr_name: str) -> tuple[str, int, str]: ...
def getAttrIndexAndBase(attr_name: str) -> tuple[int, str]: ...
def getAttrIndex(attr_name: str) -> int: ...
def getAttrBase(attr_name: str) -> str: ...
def toQColor(incolor: hou.Color | QtGui.QColor | list[float] | tuple[float, ...], alpha: float = 1.0) -> QtGui.QColor:
    """
    Very forgivingly convert to a QtGui.QColor.
    if `incolor` is a list or tuple of scalars then the they are clipped to
    fit [0.0, 1.0].  If the length is 4 then the fourth value is used as the
    alpha.  If the length is 3 then the `alpha` is used.
    if incolor is a hou.Color then call hou.qt.toQColor
    """

UNKNOWN_ICON: hou.qt.Icon
ATTR_ICONS: dict[tuple[str, bool], hou.qt.Icon]

def attrIcon(attr_name: str, overridden: bool = False) -> hou.qt.Icon: ...
