# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

def exportConfiguration() -> dict[str, str]: ...
def get(key: str) -> str: ...
def has(key: str) -> bool: ...
def set(key: str, value: str) -> None: ...
