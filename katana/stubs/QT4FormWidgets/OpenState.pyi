# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

_openWidgets: dict

def QueryOpenState(key): ...
def RegisterOpenState(key, isOpen): ...
