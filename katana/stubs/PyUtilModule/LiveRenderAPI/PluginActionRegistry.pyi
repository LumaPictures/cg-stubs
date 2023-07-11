# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

__actionClasses: list

def GetRegisteredActionClasses() -> list: ...
def RegisterActionClass(actionClass: type): ...
