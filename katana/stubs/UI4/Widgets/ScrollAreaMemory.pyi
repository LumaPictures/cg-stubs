# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

class ScrollAreaMemory:
    def __init__(self, target) -> None: ...
    def __del__(self) -> None: ...
