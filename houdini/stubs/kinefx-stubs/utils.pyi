import hou
from collections.abc import Iterable, Mapping
from typing import Protocol, overload

class _PlaybarAndNodeEventCallback(Protocol):
    @overload
    def __call__(self, event_type: hou.EnumValue[hou.playbarEvent], frame: float, /) -> object: ...
    @overload
    def __call__(self, *, event_type: hou.EnumValue[hou.nodeEventType], node: hou.OpNode, input_index: int) -> object: ...
    @overload
    def __call__(self, *, event_type: hou.EnumValue[hou.nodeEventType], node: hou.OpNode, parm_tuple: hou.ParmTuple | None) -> object: ...

def matrix4ToMatrix3(xform: hou.Matrix4) -> hou.Matrix3:
    """
    Convert a hou.Matrix4 object to a hou.Matrix3 object while preserving the scales.

    Methods such as ``hou.Matrix4().extractRotationMatrix3()`` will only return the rotation matrix and not the scale.
    This method provides a way to retain the original scales when converting from a hou.Matrix4 to a hou.Matrix3.

    :param xform: transformation matrix to convert
    :type xform: hou.Matrix4
    :return: rotation and scale transformation matrix
    :rtype: hou.Matrix3
    """
def getPointTransform(pt: hou.Point) -> hou.Matrix4:
    """
    Get a point's transformation matrix.

    :param pt: point to get the transformation matrix from
    :type pt: hou.Point
    :return: transformation matrix
    :rtype: hou.Matrix4
    .. note::
        If the point has no valid transform attribute, it returns only the translation matrix(translated identity matrix).
    """
def getRigidTransform(xform: hou.Matrix4) -> hou.Matrix4:
    """
    Make a transformation matrix rigid - effectively removing any non-uniform scales and setting its value to 1.

    :param xform: transformation matrix to make rigid
    :type xform: hou.Matrix4
    :return: transformation matrix
    :rtype: hou.Matrix4
    .. note::
        If it fails to extract the rotation, for example if scaling is zero on one axis, it returns only the translation matrix(translated identity matrix).
    """
def setPointTransform(pt: hou.Point, xform: hou.Matrix4) -> None:
    """
    Set a point's transform.

    :param pt: point to set the transform to
    :type pt: hou.Point
    :param xform: transformation matrix to set
    :type xform: hou.Matrix4
    """
def getPointParent(pt: hou.Point) -> hou.Point | None:
    """
    Get a point's parent.

    :param pt: point to get the parent of
    :type pt: hou.Point
    :return: parent point
    :rtype: hou.Point
    .. note::
        If the point has no parent, it returns None.
    """
def getPointChildren(pt: hou.Point) -> tuple[hou.Point, ...]:
    """
    Get a point's children.

    :param pt: point to get the children of
    :type pt: hou.Point
    :return: children points
    :rtype: tuple of hou.Point
    """
def findPointName(geo: hou.Geometry, name: str) -> hou.Point | None:
    """
    Get a point by name.

    :param geo: geometry to lookup the point in
    :type geo: hou.Geometry
    :param name: name to lookup the point by
    :type name: str
    :return: point
    :rtype: hou.Point
    .. note::
        If no point can be found, it returns None.
    """
def addNodeCallbacks(node: hou.OpNode, f: _PlaybarAndNodeEventCallback) -> None:
    """
    Add a callback to a node.

    :param node: node to add the callback to
    :type node: hou.Node
    :param f: callback function to add
    :type f: function
    .. note::
        The **event_types** used for the callback are hou.nodeEventType.InputDataChanged and hou.nodeEventType.ParmTupleChanged.
    """
def removeNodeCallbacks(node: hou.OpNode, f: _PlaybarAndNodeEventCallback) -> None:
    """
    Remove a callback from a node.

    :param node: node to add the callback to
    :type node: hou.Node
    :param f: callback function to add
    :type f: function
    """
def findValueInMultiparm(multiparm: hou.Parm, childparm_name: str, val: str) -> int:
    """ 
    Search for a string value on a multiparm instance and return the index of the found instance.
    
    :param multiparm: multiparm to search through
    :type multiparm: hou.Parm
    :param childparm_name: name of the multiparm instance parameter to compare with *val*
    :type childparm_name: str
    .. note::
        The childparm_name is assumed to have a '#' character that will be replaced during iteration
    :param val: value to search the index by
    :type val: str
    :return: index of the multiparm instance
    :rtype: int
    .. note::
        If no instance is found, it returns -1.
    """
def computeWorld(child_local: hou.Matrix4, parent_local: hou.Matrix4, parent_world: hou.Matrix4, compensate_mode: int = 0) -> hou.Matrix4:
    """
    Compute the world transformation matrix.

    :param child_local: local transformation matrix of the point the world transform will be computed for
    :type child_local: hou.Matrix4
    :param parent_local: local transformation matrix of the parent point
    :type parent_local: hou.Matrix4
    :param parent_world: world transformation matrix of the parent point
    :type parent_world: hou.Matrix4
    :param compensate_mode: scale inheritance mode to use when computing the world transform
    :type compensate_mode: int
    .. note::
        SCALE_INHERIT_DEFAULT (0) - simple inheritance:
        ``world = local * parent_world``

        SCALE_INHERIT_OFFSET_ONLY (1) - child doesn't scale with the parent local scales, but local translation is scaled:
        ``world = local_scale_rotates * invert(parent_local_scales) * local_translates * parent_world``

        SCALE_INHERIT_OFFSET_AND_SCALE (2) - local translation is scaled as before but parent local scaling is also reapplied by the child in local space:
        ``world = parent_local_scales * local_scale_rotates * invert(parent_local_scales) * T * parent_world``

        SCALE_INHERIT_SCALE_ONLY (3) - local translation is not scaled, but parent local scaling is reapplied by the child in local space:
        ``world = parent_local_scales * local * invert(parent_local_scales) * parent_world``

        SCALE_INHERIT_IGNORE (4) - child completely ignores any parent local scaling:
        ``world = local * invert(parent_local_scales) * parent_world``
    :return: world transformation matrix
    :rtype: hou.Matrix4
    """
def pointToLineDistance(origin: hou.Vector3, dir: hou.Vector3, point: hou.Vector3) -> float:
    """
    Get the distance from a point to a line.

    :param origin: line origin
    :type origin: hou.Vector3
    :param dir: the line to compute the distance to, passed in as a direction
    :type dir: hou.Vector3
    :param point: position of point to compute the distance from
    :type point: hou.Vector3
    :return: distance
    :rtype: float
    """
def closestPointToLine(geos: Iterable[hou.Geometry], o: hou.Vector3, d: hou.Vector3) -> tuple[hou.Point | None, float]:
    """
    Compute the closest point from a list of geometries to a line.

    :param geos: list of geometries
    :type geos: list of hou.Geometry
    :param o: line origin
    :type o: hou.Vector3
    :param d: the line to compute the distance to, passed in as a direction
    :type d: hou.Vector3
    :return: closest found point and distance from that point to the line
    :rtype: tuple of hou.Point and float
    .. note::
        If no point is found, return None.
    """
def setParmMatrix(node: hou.OpNode, prefix: str, m: hou.Matrix4) -> None:
    """
    Crack the matrix transforms and set them to the specified node parameters.

    :param node: node to set the parms on
    :type node: hou.Node
    :param prefix: node transform parameters prefix name
    :type prefix: string
    :param m: matrix to crack
    :type m: hou.Matrix4
    :Example:
        If your node has the following parameters: 'transform_t', 'transform_r', 'transform_s', the *prefix* would be 'transform'
    """
def mirrorTransform(m: hou.Matrix4, planeorigin: hou.Vector3, planenormal: hou.Vector3, flipaxes: int = 0) -> hou.Matrix4:
    """
    Mirror the transformation matrix around the specified plane.

    :param m: transformation matrix to mirror
    :type m: hou.Matrix4
    :param planeorigin: origin of the plane to mirror around
    :type planeorigin: hou.Vector3
    :param planenormal: normal of the plane to mirror around
    :type planenormal: hou.Vector3
    :param flipaxes: axis of the mirrored transformation matrix to flip
    :type flipaxes: int
    .. note::
        *flipaxes* should be passed in as a bit field. 1 for the x axis, 2 for the y axis, 4 for the z axis
    :return: mirrored transformation matrix
    :rtype: hou.Matrix4
    """
def attachControlGeo(pt: hou.Point, ctrlgeo: hou.Geometry, role: str = 'control') -> hou.PackedGeometry:
    """
    TODO: discuss whether we should get rid of this or not. We might need it though for the joint mirroring in the rigapi
    Attach a control geometry to a point.

    :param pt: point to attach the control geometry to
    :type pt: hou.Point
    :param ctrlgeo: control geometry to attach
    :type ctrlgeo: hou.Geometry or hou.PackedGeometry
    :param role: defines the function of the geometry to be attached: control: the given geometry is being used as control shape
    for easy selections of the given joint. Capture: It is being used as object to modify the capture values calculated by the
    byharmonic joint capture node.
    :return: attached control primitive
    :rtype: hou.PackedGeometry
    """
def getJointGeos(pt: hou.Point, role: str = 'control') -> list[hou.PackedGeometry]:
    """
    returns the current packed joint geometries that are attached to a given joint. 

    :param role: Defines which joint geometries are to be returned based on the geometry role.
        'control': The given joint geometry is to be used as a control element for the viewport
        'capture': The given joint geometry is to be used as an influence element to manipulate the biharmonic capture result
        '': Implies that all roles are to be mirrored. 
    :type role: string
    """
def initPointAttributes(geo: hou.Geometry, name_pattern: str = 'point_{}') -> hou.Geometry:
    """
    Initialize point attributes to turn geometry into a functional KineFX skeleton.

    Adds a transform, name, Cd, scaleinheritance and localtransform attributes if they are not present.

    :param geo: geometry to initialize the point attributes for
    :type geo: hou.Geometry
    :param name_pattern: name prefix to assign to each point
    :type name_pattern: string
    .. note::
        Each point's name will be suffixed with its point number
    :return: geometry with initialized point attributes
    :rtype: hou.Geometry
    """
def resolveMapping(geo: hou.Geometry, d: Mapping[str, hou._OptionValue]) -> int | None:
    """
    Get the point index from **geo** based on the passed in mapping point attribute.

    :param geo: source skeleton geometry you want the point index from
    :type geo: hou.Geometry
    :param d: the **mapping point attribute**
    :type d: dict
    .. note::
        The **mapping point attribute** can be initialized using the **kinefx::mappoints** node
    :return: mapped point index
    :rtype: int
    .. note::
        If it fails, it returns None.
    """
def mirrorJointGeo(pt: hou.Point, mirror_pt: hou.Point, planeorigin: hou.Vector3, planenormal: hou.Vector3, role: str = '') -> None:
    """
    Attach a mirrored copy an existing packed joint geometry from a given point to a mirrored point. Usually the joint geometry is been created with the
    attach joint geo sop node and is used for example as control element or as geometry that influences capture biharmonic capture weights.
    
    :param pt: point with joint geometries attachesa as packed prims 
    :type pt: hou.Point
    :param mirror_pt: the already mirrored hou.Point of pt, that the mirrored joint geometries will be attached to
    :type mirror_pt: hou.Point
    :param planeorigin: origin of the plane to mirror around
    :type planeorigin: hou.Vector3
    :param planenormal: normal of the plane to mirror around
    :type planenormal: hou.Vector3
    :param role: Defines which joint geometries are to be mirrored based on the geometry role. 
        'control': The given joint geometry is to be used as a control element for the viewport
        'capture': The given joint geometry is to be used as an influence element to manipulate the biharmonic capture result
        '': Implies that all roles are to be mirrored. 
    :type role: string
    """
