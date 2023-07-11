# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.AbstractTransform as AbstractTransform
import PyFnAttribute as FnAttribute
from Nodes3DAPI.AbstractTransform import AT as AT
from typing import Set, Tuple

_MAX_ATTR_CACHE_SIZE: int
_attrCache: dict

def GetJackGeometryAttr(scale: float = ...): ...
def GetPointerGeometryAttr(scale: float = ...): ...
