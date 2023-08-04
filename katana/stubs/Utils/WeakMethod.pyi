# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

class WeakMethodBound:
    def __init__(self, f) -> None: ...
    def __bool__(self) -> bool: ...
    def __call__(self, *args, **kwargs): ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class WeakMethodFree:
    def __init__(self, f) -> None: ...
    def __bool__(self) -> bool: ...
    def __call__(self, *args, **kwargs): ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class WeakMethodIsDeadError(TypeError): ...

def WeakMethod(f): ...
