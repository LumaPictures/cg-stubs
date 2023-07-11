# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyResolutionTableFn as ResolutionTable
from typing import Set, Tuple

_XMLDocument: str
_XMLFormatElement: str

def GetTempResolutionTablePath() -> str: ...
def SaveResolutionTables(): ...
