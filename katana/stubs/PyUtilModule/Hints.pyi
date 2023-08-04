# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import FnAttribute as FnAttribute
import Utils as Utils
from typing import Set, Tuple

def AttrToHints(attr: FnAttribute.Attribute) -> Tuple[int, float, str, list, dict | None]: ...
def AttrToObject(attr: FnAttribute.Attribute) -> Tuple[int, float, str, list, dict | None]: ...
