from collections.abc import MutableMapping
from typing import Any, Self

from bookish import util

class ParserError(Exception): ...

class ParserContext(util.Context):
    def __init__(
        self,
        m: MutableMapping[str, Any] | None = ...,
        parent: "ParserContext | None" = ...,
        namespace: dict[str, Any] | None = ...,
        debug: bool = ...,
    ) -> None: ...
    @property
    def namespace(self) -> dict[str, Any]: ...
    @property
    def debug(self) -> bool | None: ...
    @property
    def cache(self) -> dict[Any, Any]: ...
    def set_debug(self, v: bool) -> Self: ...

def condition_string(c: str, add_eot: bool = ...) -> str: ...
