# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
from typing import Set, Tuple

TOP_LEVEL_CONTAINER_NAME: str

def FlushCaches() -> None: ...
def GetProceduralArgs(assetId: str) -> PyFnAttribute.Attribute: ...
def ParseArgsFile(fileName: str) -> PyFnAttribute.Attribute: ...
