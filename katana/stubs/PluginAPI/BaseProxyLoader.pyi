# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import FnAttribute

class BaseProxyLoader:
    @classmethod
    def createProxyAttr(cls, proxyFile: str, time: int, args: FnAttribute.GroupAttribute) -> FnAttribute.GroupAttribute: ...
    @classmethod
    def getFileExtensions(cls): ...