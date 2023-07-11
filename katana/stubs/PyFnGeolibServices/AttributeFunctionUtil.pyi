# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
from typing import Set, Tuple

def GetRegisteredFunctionNames(omitInternal: bool = ...) -> list: ...
def Run(name: str, args: PyFnAttribute.Attribute) -> PyFnAttribute.Attribute: ...
