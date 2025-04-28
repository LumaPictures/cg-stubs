from typing import Any, Protocol

class SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool: ...

class SupportsWrite(Protocol):
    def write(self, /, __s: str) -> object: ...
