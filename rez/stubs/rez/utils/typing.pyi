from typing import Any, Protocol

class SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool: ...
