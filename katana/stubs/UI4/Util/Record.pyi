# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

class Record:
    def __init__(self: int, index: str, title: str, text: int, level: int, timestamp: str | None, iconName) -> None: ...
    def getIconName(self) -> str | None: ...
    def getIndex(self) -> int: ...
    def getLevel(self) -> int: ...
    def getText(self) -> str: ...
    def getTimestamp(self) -> int: ...
    def getTitle(self) -> str: ...
