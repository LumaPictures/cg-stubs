from _typeshed import Incomplete
from pxr import Usd as Usd, UsdGeom as UsdGeom, UsdShade as UsdShade
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup

class ComputedPropertyNames(ConstantsGroup):
    """Names of all available computed properties."""
    WORLD_BBOX: str
    LOCAL_WORLD_XFORM: str
    RESOLVED_PREVIEW_MATERIAL: str
    RESOLVED_FULL_MATERIAL: str

def _GetCustomAttributes(currentPrim, rootDataModel): ...

class CustomAttribute:
    _currentPrim: Incomplete
    _rootDataModel: Incomplete
    def __init__(self, currentPrim, rootDataModel) -> None: ...
    def IsVisible(self): ...
    def GetName(self): ...
    def Get(self, frame): ...
    def GetTypeName(self): ...
    def GetPrimPath(self): ...

class BoundingBoxAttribute(CustomAttribute):
    def __init__(self, currentPrim, rootDataModel) -> None: ...
    def GetName(self): ...
    def Get(self, frame): ...

class LocalToWorldXformAttribute(CustomAttribute):
    def __init__(self, currentPrim, rootDataModel) -> None: ...
    def GetName(self): ...
    def Get(self, frame): ...

class ResolvedBoundMaterial(CustomAttribute):
    _purpose: Incomplete
    def __init__(self, currentPrim, rootDataModel, purpose) -> None: ...
    def GetName(self): ...
    def Get(self, frame): ...

class ResolvedFullMaterial(ResolvedBoundMaterial):
    def __init__(self, currentPrim, rootDataModel) -> None: ...

class ResolvedPreviewMaterial(ResolvedBoundMaterial):
    def __init__(self, currentPrim, rootDataModel) -> None: ...

class ComputedPropertyFactory:
    """Creates computed properties."""
    _rootDataModel: Incomplete
    def __init__(self, rootDataModel) -> None: ...
    def getComputedProperty(self, prim, propName):
        """Create a new computed property from a prim and property name."""
