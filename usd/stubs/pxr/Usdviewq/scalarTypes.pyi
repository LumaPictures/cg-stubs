# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete

_toStringFnCache: dict

def GetScalarTypeFromAttr(attr): ...
def ToClipboard(v, typeName: Incomplete | None = ...): ...
def ToString(v, valueType: Incomplete | None = ...): ...
