# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils as Utils
from typing import Set, Tuple

class UndoContextGuard:
    def __init__(self, name, logWarnings: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, excType, excValue, tb): ...

class UndoGrouping:
    def __init__(self, name) -> None: ...
    def __del__(self) -> None: ...
