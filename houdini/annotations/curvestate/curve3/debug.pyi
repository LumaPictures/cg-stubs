from typing import Protocol, TypedDict, Unpack

class _TextSink(Protocol):
    def write(self, s: str, /) -> object: ...
    def flush(self) -> object: ...

class _PrintKwargs(TypedDict, total=False):
    sep: str | None
    end: str | None
    file: _TextSink | None
    flush: bool

def debug_print(*args: object, unit: str = ..., **kwargs: Unpack[_PrintKwargs]) -> None: ...
