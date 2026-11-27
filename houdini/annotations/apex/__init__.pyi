from collections.abc import Callable
from typing import ParamSpec, TypeVar

_P = ParamSpec("_P")
_R = TypeVar("_R")

def extends_class(cls: type[object]) -> Callable[[Callable[_P, _R]], None]: ...
