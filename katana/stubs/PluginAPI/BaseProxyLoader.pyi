# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
from typing import Set, Tuple

class BaseProxyLoader:
    @classmethod
    def createProxyAttr(cls, proxyFile: str, time: int, args: PyFnAttribute.GroupAttribute) -> PyFnAttribute.GroupAttribute: ...
    @classmethod
    def getFileExtensions(cls): ...
