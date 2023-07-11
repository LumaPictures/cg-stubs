# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import typing
from typing import Set, Tuple

def GetUniqueName(name: str, checkcallback: typing.Callable) -> str: ...
