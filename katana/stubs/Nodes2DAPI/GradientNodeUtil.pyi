# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO as PyXmlIO
import Utils as Utils
from _typeshed import Incomplete

LinearGradLayerXML: str
SuperGradLayerXML: str

def AddLinearGradLayer(layerParam, name: Incomplete | None = ...): ...
def AddSuperGradLayer(node, x: float = ..., y: float = ..., r: float = ..., g: float = ..., b: float = ..., a: float = ...): ...
def GetUniqueLinearGradLayerName(layerParam): ...
def GetUniqueSuperGradLayerName(node): ...
def SetGradLayerName(layerParam, name): ...