import hou
from collections.abc import Mapping, Sequence
from typing import Protocol

class _GroupParmInfo(Protocol):
    @property
    def groupparmname(self) -> str: ...
    @property
    def grouptypeparmname(self) -> str: ...
    @property
    def grouptypevalues(self) -> Mapping[hou.EnumValue[hou.geometryType], int]: ...

def interactiveAlign(pane: hou.SceneViewer | None = None, quick_mode: bool = True) -> None:
    """ Queries the user for a source component and a target component, and
        transforms the geometry to align the source with the target.  How
        this transform occurs depends on what level the operation is done.
        At the object level, the transform is done in the source object's
        transform, and at the SOP level a transform SOP is appended.

        Set quick_mode to False to allow selecting more than one source and
        target component at once.
    """
def interactiveObjectAlign(pane: hou.SceneViewer | None = None, quick_mode: bool = True) -> None:
    """ The object level implementation of interactiveAlign().
    """
def interactiveSopAlign(pane: hou.SceneViewer | None = None, quick_mode: bool = True) -> None:
    """ The SOP level implementation of interactiveAlign().
    """
def showError(msg: str) -> None: ...
def getObject(node: hou.Node) -> hou.ObjNode: ...

class CoordFrame:
    origin: hou.Vector3
    x: hou.Vector3
    y: hou.Vector3
    z: hou.Vector3
    def __init__(self, origin: hou.Vector3 = ..., x: hou.Vector3 = ..., y: hou.Vector3 = ..., z: hou.Vector3 = ..., normalize: bool = False) -> None: ...
    def transform(self, xform: hou.Matrix4) -> None: ...
    def transformed(self, xform: hou.Matrix4) -> CoordFrame: ...
    def flippedAboutUp(self, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> CoordFrame | None: ...
    def flippedAboutX(self) -> CoordFrame: ...
    def flippedAboutY(self) -> CoordFrame: ...
    def flippedAboutZ(self) -> CoordFrame: ...
    def spaceChangeTransform(self, dst_frame: CoordFrame) -> hou.Matrix4: ...

def alignObject(src_obj: hou.ObjNode, src_frame: CoordFrame, dst_obj: hou.ObjNode, dst_frame: CoordFrame) -> None:
    """ Changes the pivot space on src_obj to the equivalent of src_frame, and
        transforms src_obj to align src_frame with dst_frame on dst_obj.
    """
def setObjParmPivotTransform(obj: hou.ObjNode, new_pivot_xform: hou.Matrix4) -> None:
    """ Sets the pivot transform parameters so that the net pivot transform is
        new_pivot_xform and updates the object pre-transform so that the net
        world transform of the object remains unchanged.
    """
def initNewSopFromGeometrySelection(newnode: hou.SopNode, container: hou.Node, geoselection: hou.GeometrySelection, groupparminfo: _GroupParmInfo) -> None:
    """ Set up the connections and group parameters of a new SOP from a
        hou.GeometrySelection.
    """
def initNewSopFromSelection(newnode: hou.SopNode, container: hou.Node, inputnode: hou.SopNode, selection: hou.Selection | None, geometry: hou.Geometry | None, groupparminfo: _GroupParmInfo, inheritselectabletemplateflags: bool) -> None:
    """ Set up the connections and group parameters of a new SOP from an
        input node and optional hou.Selection.  If selection is None the
        group type is assumed to be primitives and the empty group string
        is used to affect all the geometry.
    """
def setGroupParmsOnSop(node: hou.OpNode, groupparmname: str, selectionstring: str, grouptypeparmname: str, grouptypevalue: int) -> None: ...
def initSopParmTransform(node: hou.OpNode, src_frame: CoordFrame, dst_frame: CoordFrame) -> None:
    """ Initializes the standard transform parms on the given SOP node so that
        the transform aligns src_frame with dst_frame with the pivot transform
        aligned to src_frame.
    """
def buildSrcSpaceCoordFrames(src_node: hou.SopNode, src_sel: hou.Selection, src_comp_index: int, dst_node: hou.SopNode, dst_sel: hou.Selection, dst_comp_index: int, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> tuple[CoordFrame | None, CoordFrame]:
    """ Returns a tuple of CoordFrame objects representing the local coordinate
        frames of the two specified components in the source and destination
        selections.
    """
def buildSelCoordFrame(geometry: hou.Geometry, sel: hou.Selection, comp_index: int, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> CoordFrame: ...
def findPrimXAlignDir(prim: hou.Prim, target_up_vector: hou.Vector3) -> hou.Vector3: ...
def findPointXAlignDir(point: hou.Point, target_up_vector: hou.Vector3) -> hou.Vector3: ...
def buildPrimCoordFrame(geometry: hou.Geometry, prim: hou.Prim, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> CoordFrame: ...
def buildPointCoordFrame(geometry: hou.Geometry, point: hou.Point, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> CoordFrame: ...
def buildEdgeCoordFrame(geometry: hou.Geometry, edge: hou.Edge, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> CoordFrame: ...
def buildVertexCoordFrame(geometry: hou.Geometry, vertex: hou.Vertex, to_normal: hou.EnumValue[hou.handleOrientToNormalAxis], target_up_vector: hou.Vector3) -> CoordFrame: ...
def primBaryCenter(prim: hou.Prim) -> hou.Vector3: ...
def buildCoordFrameYX(origin: hou.Vector3, yvec: hou.Vector3, xvec: hou.Vector3) -> CoordFrame: ...
def buildCoordFrameXY(origin: hou.Vector3, xvec: hou.Vector3, yvec: hou.Vector3) -> CoordFrame: ...
def buildCoordFrameZX(origin: hou.Vector3, zvec: hou.Vector3, xvec: hou.Vector3) -> CoordFrame: ...
def buildCoordFrameXZ(origin: hou.Vector3, xvec: hou.Vector3, zvec: hou.Vector3) -> CoordFrame: ...
def targetUpVector(scene_viewer: hou.SceneViewer) -> hou.Vector3: ...
def marshalGeometrySelectionToSingletonTupleList(geo_sel: hou.GeometrySelection) -> list[tuple[hou.SopNode, hou.Selection, int]]:
    """ Utility function for marshalling a hou.GeometrySelection potentially
        consisting of multiple nodes and hou.Selection instances with multiple
        components into a list of (node, selection, index) tuples.
    """
def buildConnectedSelectionFromSelComponent(selection: hou.Selection, component_index: int, geometry: hou.Geometry) -> hou.Selection | None:
    """ Convenience function wrapping the various selections for which we can
        build a connected selection per component.
    """
def buildConnectedSelectionFromPrims(seed_prims: Sequence[hou.Prim]) -> hou.Selection | None:
    """ Utility function for creating a hou.Selection() containing all the
        primitives connected to a list of seed primitives.
    """
def buildConnectedSelectionFromEdges(seed_edges: Sequence[hou.Edge]) -> hou.Selection | None:
    """ Utility function for creating a hou.Selection() containing all the
        primitives connected to a list of seed edges.
    """
def buildConnectedSelectionFromPoints(seed_points: Sequence[hou.Point]) -> hou.Selection | None:
    """ Utility function for creating a hou.Selection() containing all the
        points connected to a list of seed points.
    """
