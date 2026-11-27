from _apex import *
from _apexscene import *
from collections.abc import Callable as Callable

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
ParmDict = Dict

def extends_class(cls: type[object]) -> Callable[[Callable[_P, _R]], None]: ...
