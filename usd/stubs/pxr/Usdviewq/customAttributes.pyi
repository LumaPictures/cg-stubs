# mypy: disable_error_code = misc
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
import pxr.UsdShade as UsdShade
import pxr.UsdUtils.constantsGroup
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from typing import ClassVar

class BoundingBoxAttribute(CustomAttribute):
    def __init__(self, currentPrim, rootDataModel): ...
    def Get(self, frame): ...
    def GetName(self): ...

class ComputedPropertyFactory:
    def __init__(self, rootDataModel): ...
    def getComputedProperty(self, prim, propName): ...

class ComputedPropertyNames(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    LOCAL_WORLD_XFORM: ClassVar[str] = ...
    RESOLVED_FULL_MATERIAL: ClassVar[str] = ...
    RESOLVED_PREVIEW_MATERIAL: ClassVar[str] = ...
    WORLD_BBOX: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class CustomAttribute:
    def __init__(self, currentPrim, rootDataModel): ...
    def Get(self, frame): ...
    def GetName(self): ...
    def GetPrimPath(self): ...
    def GetTypeName(self): ...
    def IsVisible(self): ...

class LocalToWorldXformAttribute(CustomAttribute):
    def __init__(self, currentPrim, rootDataModel): ...
    def Get(self, frame): ...
    def GetName(self): ...

class ResolvedBoundMaterial(CustomAttribute):
    def __init__(self, currentPrim, rootDataModel, purpose): ...
    def Get(self, frame): ...
    def GetName(self): ...

class ResolvedFullMaterial(ResolvedBoundMaterial):
    def __init__(self, currentPrim, rootDataModel): ...

class ResolvedPreviewMaterial(ResolvedBoundMaterial):
    def __init__(self, currentPrim, rootDataModel): ...

def _GetCustomAttributes(currentPrim, rootDataModel): ...