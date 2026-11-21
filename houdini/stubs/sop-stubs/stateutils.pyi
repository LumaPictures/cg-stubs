# Houdini stubs generated from Houdini 22.0.466

import hou
from enum import Enum

thePickerStateName: str

class SampleElement(Enum):
    Point = 0
    Prim = 1
    HeightField = 2
    Fog = 3
    SDF = 4

class HitRecord:
    position: hou.Vector3
    normal: hou.Vector3
    uvw: hou.Vector3
    hit_prim: int
    def __init__(self, position: hou.Vector3, normal: hou.Vector3, uvw: hou.Vector3, hit_prim: int) -> None: ...
    def isValidHit(self) -> bool: ...
    @staticmethod
    def fromIntersect(ui_event: hou.ViewerEvent, viewport: hou.GeometryViewport, geo: hou.Geometry, cache: hou.GeometryRayCache) -> HitRecord:
        """
        Returns a HitRecord instance    
        """

def sampleHeightField(ui_event: hou.ViewerEvent, viewport: hou.GeometryViewport, geo: hou.Geometry, cache: hou.GeometryRayCache, name: str = 'height') -> list[float]: ...

class InputCache:
    node: hou.SopNode
    input: hou.Geometry
    name: str
    type: SampleElement
    raycache: hou.GeometryRayCache
    def __init__(self, node: hou.SopNode, the_input: hou.Geometry, attrib: str, elem_type: SampleElement) -> None: ...
    def update(self) -> None: ...
    def __call__(self) -> hou.Geometry: ...
    def setNode(self, node: hou.SopNode) -> None: ...
    def attribName(self) -> str: ...
    def attribType(self) -> SampleElement: ...
    def sample(self, ui_event: hou.ViewerEvent, viewport: hou.GeometryViewport, drawable: hou.GeometryDrawable | hou.SimpleDrawable | None = None) -> list[float] | list[hou.AttribReturnType | hou.AttribDictReturnType]: ...
    def needsGeometryDrawable(self) -> bool: ...
    def validateInput(self) -> bool | None:
        """
        If the attribute we're trying to sample does not exist on the geometry
        then there's nothing to sample...    
        """

def enterPickerState(node: hou.OpNode, parm: str, attrib: str, geo_node: hou.SopNode, type: SampleElement = ...) -> None:
    '''
    Convenience function used to enter the picker state. This is used
    by pretty much all the COP nodes that have a picker state.
    Parms
    
    Node: should be kwargs["node"]
    
    Parm: The name of the parameter to set, eg. threshold. Name, not label !
    
    '''
def setAndConfigureState(state_name: str, viewer: hou.SceneViewer, args: dict[str, object]) -> None:
    """
    Wrapper that handles hou.OperationFailed    
    """
def exitState(viewer: hou.SceneViewer) -> bool: ...
def drawableFromInput(viewer: hou.SceneViewer, geo: hou.Geometry, type: hou.EnumValue[hou.drawableGeometryType] = ...) -> hou.GeometryDrawable: ...
def drawableColor(viewer: hou.SceneViewer, type: hou.EnumValue[hou.drawableGeometryType], hide: bool = False) -> hou.Vector4: ...
def drawableTypeFromSampleElement(type: SampleElement) -> hou.EnumValue[hou.drawableGeometryType]: ...
