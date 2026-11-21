# Houdini stubs generated from Houdini 22.0.466

from typing import Protocol, TypedDict, Unpack

class _TextSink(Protocol):
    def write(self, s: str, /) -> object: ...
    def flush(self) -> object: ...

class _PrintKwargs(TypedDict, total=False):
    sep: str | None
    end: str | None
    file: _TextSink | None
    flush: bool

def debug_enabled(unit: str) -> bool:
    """Return True when constants-based debug enables this unit."""
def log(unit: str, message: str) -> None: ...
def debug_print(*args: object, unit: str = 'raw', **kwargs: Unpack[_PrintKwargs]) -> None:
    """Drop-in replacement for print gated by curve3 debug flags."""
