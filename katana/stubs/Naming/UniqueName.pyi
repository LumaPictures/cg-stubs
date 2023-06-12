from typing import Callable
# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


def GetUniqueName(name: str, checkcallback: Callable) -> str: ...