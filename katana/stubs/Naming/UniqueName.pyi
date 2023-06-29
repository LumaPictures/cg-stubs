# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import typing

def GetUniqueName(name: str, checkcallback: typing.Callable) -> str: ...