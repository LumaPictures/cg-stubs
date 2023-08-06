# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnAttribute
import Utils as Utils
from typing import Set, Tuple

def AttrToHints(attr: PyFnAttribute.Attribute) -> Tuple[int, float, str, list, dict | None]: ...
def AttrToObject(attr: PyFnAttribute.Attribute) -> Tuple[int, float, str, list, dict | None]: ...
