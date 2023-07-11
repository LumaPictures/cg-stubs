# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
from typing import Set, Tuple

def GetHintGroup(inputAttr: PyFnAttribute.Attribute) -> PyFnAttribute.GroupAttribute: ...
def ParseConditionalStateGrammar(inputExpr: str, prefix: str = ..., secondaryPrefix: str = ...) -> PyFnAttribute.GroupAttribute: ...
