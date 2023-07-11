# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

_DeprecatedFunctions: set

def deprecated(*args): ...
