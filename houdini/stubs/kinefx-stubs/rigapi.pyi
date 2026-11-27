import hou
import typing
from collections.abc import Callable as Callable, Mapping, MutableSequence, Sequence
from kinefx import poseparms as poseparms
from kinefx.stateutils import buildAttribGroupString as buildAttribGroupString
from typing import ClassVar, Literal, TypedDict

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_AxisName: TypeAlias = Literal['NEGX', 'NEGY', 'NEGZ', 'X', 'Y', 'Z']
_AxisArg: TypeAlias = hou.Vector3 | int | _AxisName
_PositionArg: TypeAlias = hou.Point | hou.Matrix4 | hou.Vector3
_PointsArg: TypeAlias = Sequence[hou.Point] | str | hou.Selection
_AttribValue: TypeAlias = hou.AttribReturnType | hou._OptionDict | tuple[hou._OptionDict, ...]
_GroupRenameTokens = TypedDict('_GroupRenameTokens', {'from': str, 'to': str})

class RigContext:
    """
    Hold a current node and a geometry to write to.
    Wrap the geometry into a GeoSkeleton wrapper which allows access to the points directly by name.

    :param geo: skeleton geometry to initialize the GeoSkeleton from
    :type geo: hou.Geometry
    :param node: node to read the geometry from its inputs using **inputRig** or **inputRigAtFrame** methods
    :type node: hou.Node
    """
    def __init__(self, geo: hou.Geometry, node: hou.SopNode | None = None) -> None:
        """
        Constructor method
        """
    @property
    def rig(self) -> GeoSkeleton:
        """ 
        :return: a read and write GeoSkeleton
        :rtype: rigapi.GeoSkeleton
        """
    def inputRig(self, i: int) -> GeoSkeleton | None:
        """ 
        Get a read-only GeoSkeleton at the current frame for the given input.

        :param i: input index of the current node to read the geometry from
        :type i: int
        :return: a read only GeoSkeleton
        :rtype: rigapi.GeoSkeleton
        """
    def inputRigAtFrame(self, i: int, frame: float) -> GeoSkeleton | None:
        """
        Get a read-only GeoSkeleton at the given frame for the given input.

        :param i: input index of the current node to read the geometry from
        :type i: int
        :param i: frame to evaluate the goemtry at
        :type i: int
        :return: a read only GeoSkeleton
        :rtype: rigapi.GeoSkeleton
        """

class GeoSkeleton:
    """ 
    Wrap a geometry and allow access to a KinefxPoint by a python name accessor.
    
    :param geo: skeleton geometry to initialize the GeoSkeleton from
    :type geo: hou.Geometry
    :param readonly: geometry flag that describes whether it can be written to or not 
    :type readonly: bool
    """
    def __init__(self, geo: hou.Geometry, readonly: bool = False) -> None:
        """ 
        Constructor method
        """
    @property
    def geo(self) -> hou.Geometry:
        """ 
        :return: skeleton geometry
        :rtype: hou.Geometry
        """
    def __getattr__(self, item: str) -> KinefxPoint | None:
        """ 
        Get a point by name as if it was a property of the class.
        Syntax:
        ``GeoSkeleton.point_name`` will perform the lookup
        
        :param item: name of the point
        :type item: str
        :return: point
        :rtype: rigapi.KinefxPoint
        .. note::
            If no point was found, return None.
        """
    def __getitem__(self, item: str) -> KinefxPoint | None:
        """ 
        Get a point by name using the arraylookup operator[].
        Syntax:
        ``GeoSkeleton[point_nam]`` will perform the lookup
        
        :param item: name of the point
        :type item: str
        :return: point
        :rtype: rigapi.KinefxPoint
        .. note::
            If no point was found, return None.
        """
    def createPoint(self, name: str = '', transform: hou.Matrix4 | None = None, islocaltransform: bool = False, parent: hou.Point | None = None) -> KinefxPoint | None:
        """ 
        Creates a point and returns a KinefxPoint wrapper.
        
        :param name: name of the point
        :type name: str
        :param transform: transformation matrix
        :type transform: hou.Matrix4
        :param islocaltransform: interpret the **transform** argument as localtransform or regular transform
        :type islocaltransform: bool
        :param parent: parent point 
        :type parent: hou.Point
        :return: point
        :rtype: rigapi.KinefxPoint
        .. note::
            If geometry is readonly, returns None.
        """
    def points(self) -> list['KinefxPoint']:
        """ 
        Get all the points from the geometry as KinefxPoints.
        
        :return: list of all the point in the geometry
        :rtype: list of rigapi.KinefxPoint
        """
    def splitEdge(self, p0: KinefxPoint | str, p1: KinefxPoint | str, num: int = 1, reparent_first: bool = True, reparent_splits: bool = True, reparent_p1: bool = True, xform1: hou.Matrix4 | None = None, fmt: str | Sequence[str] = '%s_split%d', ret_weights: MutableSequence[float] | None = None) -> list['KinefxPoint']:
        """ 
        Create **num** of split joints interpolating the transform from **p0** to **p1**.
        Provide options to reparent the split joints under **p0**.

        :param p0: start point or point name
        :type p0: KinefxPoint or str
        :param p1: end point or point name
        :type p1: KinefxPoint or str
        :param num: number of split joints to create
        :type num: int
        :param reparent_first: parent the first split joint to **p0**
        :type reparent_first: bool
        :param reparent_splits: parent the rest of the split joints(starting from the 2nd) to **p0**
        :type reparent_splits: bool
        :param reparent_p1: parent **p1** to **p0**
        :type reparent_p1: bool
        :param xform1: custom transform to interpolate to; replace **p1** xform with this if provided
        :type xform1: hou.Matrix4
        :param fmt: split joints name or name format(using python string formatting %s %d)
        :type fmt: str
        :param ret_weights:
        :type ret_weights:
        :return: list of created split joints
        :rtype: list of rigapi.KinefxPoint
        .. note::
            If **num** is 0 or lower, returns empty list.
        """

class KinefxPoint:
    """ 
    Wrap a hou.Point and grant access to methods for parenting and transforming it with a given read/write permission.

    :param pt: point to turn into a KinefxPoint
    :type pt: hou.Point
    :param readonly: KinefxPoint flag that describes whether it can be written to or not 
    :type readonly: bool
    """
    def __init__(self, pt: hou.Point, readonly: bool = False) -> None:
        """ 
        Constructor method
        """
    @property
    def geo(self) -> hou.Geometry:
        ''' 
        Access the geometry of the point.

        :return: geometry of the point
        "rtype: hou.Geometry
        '''
    @property
    def pt(self) -> hou.Point:
        ''' 
        Access the hou.Point of the point.

        :return: point
        "rtype: hou.Point
        '''
    @property
    def name(self) -> str:
        ''' 
        Get the name of the point from the attribute.

        :return: point name
        "rtype: str
        '''
    @name.setter
    def name(self, name: str) -> None:
        """ 
        Set the name attribute of the point.
        Name will be sanitized to avoid duplicates.

        :param name: name to set
        :type name: str
        """
    @property
    def number(self) -> int:
        ''' 
        Returns the point number.

        :return: point number
        "rtype: int
        '''
    @property
    def transform(self) -> hou.Matrix4:
        ''' 
        Returns the transform of the point.

        :return: point transform
        "rtype: hou.Matrix4
        '''
    @transform.setter
    def transform(self, m: hou.Matrix4) -> None:
        """ 
        Sets the transform of the point.

        :param m: transformation matrix to set
        :type m: hou.Matrix4
        """
    @property
    def color(self) -> hou.Vector3:
        """ 
        Returns the color of the point from the attribute.

        :return: point color
        :rtype: hou.Vector3
        """
    @color.setter
    def color(self, v: hou.Vector3 | Sequence[float]) -> None:
        """ 
        Set the color attribute of the point.

        :param v: color to set
        :type v: hou.Vector3 or tuple of 3 float
        """
    @property
    def localtransform(self) -> hou.Matrix4:
        """ 
        Returns the localtransform of the point.

        :return: point local transformation matrix
        :rtype: hou.Matrix4
        """
    @property
    def parent(self) -> KinefxPoint | None:
        """ 
        Returns the parent of the point.

        :return: point parent
        :rtype: rigapi.KinefxPoint
        .. note::
            If no parent was found, returns None.
        """
    @parent.setter
    def parent(self, parent: hou.Point | KinefxPoint | None) -> None:
        """ 
        Sets the parent of the point.

        :param parent: point parent to set
        :type parent: hou.Point or rigapi.KinefxPoint
        """
    @property
    def children(self) -> list['KinefxPoint']:
        """ 
        Returns the children of the point.

        :return: list of children points
        :rtype: list of rigapi.KinefxPoint
        .. note::
            if no children were found, returns an empty list.
        """
    def destroy(self) -> None:
        """ 
        Deletes the point from the geometry.
        """
    def blendtransform(self, xform: hou.Matrix4 | KinefxPoint, bias: float, components: int = 7) -> hou.Matrix4:
        """ 
        Returns a blended transform between this point and another point or transform.
        It doesn't modify the current transform.

        :param xform: point transformation matrix or a KinefxPoint
        :type xform: hou.Matrix4 or rigapi.KinefxPoint
        :param bias: blend bias
        :type bias: float
        :param components: transformation components to blend
        :type components: int
        .. note::
            *components* should be passed in as a bit field. 1 for translation, 2 for rotaion, 4 for scaling and any combination
            between these
        :return: blended transformation matrix
        :rtype: hou.Matrix4
        """

class AxesType(type):
    """
    Helper to access to XYZ axes vectors.
    Class should NOT be used - use the **Axes** class instead.
    """
    axes_names: list[_AxisName]
    axes_vals: list[hou.Vector3]
    axes_dict: dict[_AxisName, hou.Vector3]
    def __getattr__(self, item: str) -> hou.Vector3:
        """
        Get an axis vector as if it was a property of the class.

        :param item: name of the axis to get as defined in the **axes_names** list
        :type item: str
        :return: axis vector
        :rtype: hou.Vector3
        """
    def __getitem__(self, item: int | _AxisName) -> hou.Vector3:
        """
        Get an axis vector by using the arraylookup operator[].

        :param item: index of the axis to get or the name of the axis as defined in the **axes_names** list
        :type item: int or str
        :return: axis vector
        :rtype: hou.Vector3
        """
    def vectorToAxisIndex(self, v: hou.Vector3) -> int:
        """
        Get the axis index that corresponds to the passed in **v**.

        :param v: axis vector
        :type v: hou.Vector3
        :return: axis index
        :rtype: int
        """
    def vectorToAxisString(self, v: hou.Vector3) -> _AxisName:
        """
        Get the axis name that corresponds to the passed in **v**.

        :param v: axis vector
        :type v: hou.Vector3
        :return: axis name
        :rtype: str
        """
    def axisStringToIndex(self, s: _AxisName) -> int:
        """
        Get the axis index that corresponds to the passed in axis name.

        :param s: axis name
        :type s: str
        :return: axis index
        :rtype: int
        """
    def axisStringToVector(self, s: _AxisName) -> hou.Vector3:
        """
        Get the axis vector that corresponds to the passed in axis name.

        :param s: axis name
        :type s: str
        :return: axis vector
        :rtype: hou.Vector3
        """
    def axisIndexToString(self, idx: int) -> _AxisName:
        """
        Get the axis name that corresponds to the passed in axis index.

        :param idx: axis index
        :type idx: int
        :return: axis name
        :rtype: str
        """
    def axisIndexToVector(self, idx: int) -> hou.Vector3:
        """
        Get the axis vector that corresponds to the passed in axis index.

        :param idx: axis index
        :type idx: int
        :return: axis vector
        :rtype: hou.Vector3
        """

class Axes:
    """
    Wrapper around the **AxesType** class.
    Provides access to calls such as: ``Axes.X or Axes[3]`` that will return the vector corresponding to the specified axis.
    """
    NEGX: ClassVar[hou.Vector3]
    NEGY: ClassVar[hou.Vector3]
    NEGZ: ClassVar[hou.Vector3]
    X: ClassVar[hou.Vector3]
    Y: ClassVar[hou.Vector3]
    Z: ClassVar[hou.Vector3]

def findPublicOrPrivatePointAttr(geo: hou.Geometry, name: str) -> hou.Attrib | None:
    """
    Return a public or private point attribute by name.

    :param geo: geometry to query
    :type pt: hou.Geometry
    :param name: name of the point attribute
    :type pt: str
    :return: point attribute or None
    :rtype: hou.Attribute
    """
def findInputLocalTransformAttr(geo: hou.Geometry) -> hou.Attrib | None:
    '''
    Return a public or private "__inputlocaltransform" attribute.
    :param geo: geometry to query
    :type pt: hou.Geometry
    :return: point attribute or None
    :rtype: hou.Attribute
    '''
def findEffectiveLocalTransformAttr(geo: hou.Geometry) -> hou.Attrib | None:
    '''
    Return a public or private "__effectivelocaltransform" attribute.
    :param geo: geometry to query
    :type pt: hou.Geometry
    :return: point attribute or None
    :rtype: hou.Attribute
    '''
def attribValue(pt: hou.Point | None, name: str, default_value: _T) -> _AttribValue | _T:
    """
    Get a point attribute value.
    Return **default_value** if no point or attribute by the specified **name** could be found.

    :param pt: point to get the attribute from
    :type pt: hou.Point
    :param name: attribute name
    :type name: str
    :param default_value: default value to return if the query fails
    :type default_value: any
    :return: attribute value
    :rtype: any
    """
def attribMatrix4(pt: hou.Point | None, name: str) -> hou.Matrix4:
    """
    Get a point's hou.Matrix4 attribute value.
    Returns an identity matrix if no point or attribute by the specified **name** could be found.

    :param pt: point to get the attribute from
    :type pt: hou.Point
    :param name: attribute name
    :type name: str
    :return: attribute value
    :rtype: hou.Matrix4
    """
def attribMatrix3(pt: hou.Point | None, name: str) -> hou.Matrix3:
    """
    Get a point's hou.Matrix3 attribute value.
    Returns an identity matrix if no point or attribute by the specified **name** could be found.

    :param pt: point to get the attribute from
    :type pt: hou.Point
    :param name: attribute name
    :type name: str
    :return: attribute value
    :rtype: hou.Matrix3
    """
def getPointTransform(pt: hou.Point | None) -> hou.Matrix4:
    """
    Get a point's transformation matrix.

    :param pt: point to get the transform for
    :type pt: hou.Point
    :return: point transformation matrix
    :rtype: hou.Matrix4
    .. note::
        If no point was found, returns the identity matrix.
    """
def getPointTransformAtFrame(pt: hou.Point, frame: float) -> hou.Matrix4:
    """
    Get a point's transformation matrix at the specified **frame**.

    :param pt: point to get the transform for
    :type pt: hou.Point
    :param frame: frame to get the transform at
    :type frame: int
    :return: point transformation matrix
    :rtype: hou.Matrix4
    .. note::
        If the point does not belong to any SOP node geometry, returns the point's current transform.
    """
def getPointTransformsAtFrame(pts: Sequence[hou.Point], frame: float) -> tuple[hou.Matrix4, ...]:
    """
    Get the transformation matrices for a list of points at the specified **frame**.

    :param pts: points to get the transform for
    :type pts: list of hou.Point
    :param frame: frame to get the transform at
    :type frame: int
    :return: tuple of point transformation matrices
    :rtype: tuple of hou.Matrix4
    .. note::
        If the points do not belong to any SOP node geometry, returns a tuple of their current transforms.
    """
def setPointTransform(pt: hou.Point, xform: hou.Matrix4 | tuple[float, ...], create_missing_attribs: bool = False) -> None:
    """
    Set a point's transformation matrix.

    :param pt: point to set the transform to
    :type pt: hou.Point
    :param xform: transformation matrix to set
    :type xform: hou.Matrix4
    """
def getParentTransform(pt: hou.Point | None) -> hou.Matrix4:
    """
    Get a point parent's transformation matrix.

    :param pt: point to get the parent from
    :type pt: hou.Point
    :return: transformation matrix of the parent point
    :rtype: hou.Matrix4
    .. note::
        If the point was not found or if it has no parent, returns the identity matrix.
    """
def buildFrameFromAxes(z: _AxisArg, y: _AxisArg) -> hou.Matrix3:
    """
    Get a transformation matrix from two axes.

    :param z: axis vector or axis index or name as defined in **AxesType**
    :type z: hou.Vector3 or int or str
    :param y: axis vector or axis index or name as defined in **AxesType**
    :type y:  hou.Vector3 or int or str
    :return: transformation matrix built by the two axes
    :rtype: hou.Matrix3
    .. note::
        If the passed in axes are equal, returns the identity matrix.
    """
def buildRotateAxisToAxis(axis_from: hou.Vector3, axis_to: hou.Vector3) -> hou.Matrix4:
    """
    Returns a transformation matrix rotating the **axis_from** onto the given **axis_to**.

    :param axis_from: axis to rotate from
    :type axis_from: hou.Vector3
    :param axis_to: axis to rotate to
    :type axis_to: hou.Vector3
    :return: rotation matrix
    :rtype: hou.Matrix4
    """
def lookat(f: _PositionArg, la: _PositionArg, lu: _PositionArg, lookat_axis: _AxisArg = 'Z', lookup_axis: _AxisArg = 'Y', lookup_is_relative: bool = True, rigid: bool = True) -> hou.Matrix4:
    """
    Compute a lookat transformation matrix that rotates the source **f** to point down its **lookat_axis** to the lookat target **la**
    and its **lookup_axis** to the up target **lu**.

    :param f: source point or source transformation matrix to compute the lookat for
    :type f: hou.Point or hou.Matrix4
    :param la: lookat target position
    :type la: hou.Point or hou.Matrix4 or a hou.Vector3
    :param lu: up target position
    :type lu: hou.Point or hou.Matrix4 or a hou.Vector3
    :param lookat_axis: axis of source **f** that should be oriented to point at the lookat target position
    :type lookat_axis: hou.Vector3 or int or str
    :param lookup_axis: up axis of source **f** that should be oriented to point at the up target position
    :type lookup_axis: hou.Vector3 or int or str
    :param lookup_is_relative: compute the up target position relative to the source **f** or not
    :type lookup_is_relative: bool
    :param rigid: make the lookat transformation matrix rigid - effectively removing any non-uniform scales and setting its value to 1
    :type rigid: bool
    :return: lookat transformation matrix
    :rtype: hou.Matrix4
    """
def closestAxisToVector(m: hou.Point | hou.Matrix4 | hou.Matrix3, v: hou.Vector3) -> hou.Vector3 | None:
    """
    Get the axis of matrix **m** that has the closest orientation to vector **v**.

    :param m: transformation matrix to get the axis from
    :type m: hou.Matrix4
    :param v: vector to compare against the matrix axes
    :type v: hou.Vector3
    :return: closest axis of the transformation matrix
    :rtype: hou.Vector3
    """
def computePointLocalTransform(pt: hou.Point) -> hou.Matrix4:
    """
    Compute a point's local transformation matrix.

    :param pt: point to compute the local transformation for
    :type pt: hou.Point
    :return: local transformation matrix
    :rtype: hou.Matrix4
    .. note::
        If the point has a 'scaleinheritance' attribute, its value will be used when computing the local transform.
    """
def computePointWorldTransform(pt: hou.Point) -> hou.Matrix4:
    """
    Compute a point's world transformation matrix.

    :param pt: point to compute the world transformation for
    :type pt: hou.Point
    :return: world transformation matrix
    :rtype: hou.Matrix4
    .. note::
        If the point has a 'scaleinheritance' attribute, its value will be used when computing the world transform.
    """
def getPointParentPrim(pt: hou.Point | None) -> tuple[hou.Prim, int] | tuple[None, None]:
    """
    Get the primitive that the parent of **pt** belongs to.

    :param pt: point to get the parent primitive from
    :type pt: hou.Point
    :return: primitive that the parent of **pt** belongs to and the index of the parent point in the list of points of the primitive
    :rtype: hou.Prim, int
    .. note::
        If the point was not found, returns None, None.
    """
def getPointParent(pt: hou.Point | None) -> hou.Point | None:
    """
    Get the parent point of **pt**.

    :param pt: point to get the parent of
    :type pt: hou.Point
    :return: parent point
    :rtype: hou.Point
    .. note::
        If the point was not found or if it has no parent, returns None.
    """
def getPointChildren(pt: hou.Point | None) -> tuple[hou.Point, ...] | list[hou.Point]:
    """
    Get the children points of **pt**.

    :param pt: point to get the children of
    :type pt: hou.Point
    :return: list of children points
    :rtype: list of hou.Point
    .. note::
        If the point was not found or if it has no children, returns an empty list.
    """
def getPointDescendants(pt: hou.Point | None) -> list[hou.Point]:
    """
    Get the descendant points of **pt**.

    :param pt: point to get the descendants of
    :type pt: hou.Point
    :return: list of descendant points
    :rtype: list of hou.Point
    .. note::
        If the point was not found or if it has no children, returns an empty list.
    """
def getPointAncestors(pt: hou.Point | None) -> list[hou.Point]:
    """
    Get the ancestor points of **pt**.

    :param pt: point to get the ancestors of
    :type pt: hou.Point
    :return: list of ancestor points
    :rtype: list of hou.Point
    .. note::
        If the point was not found or if it has no parent, returns an empty list.
    """
def getNearestCommonAncestor(pts: Sequence[hou.Point], inclusive: bool = False) -> hou.Point | None:
    """
    Get the nearest common ancestor of the pts given in lst.

    :param pts: List of points to get the common ancestor of
    :type pt: List[hou.Point]
    :param inclusive: If true, one of input points can be the common ancestor
    :type inclusive: bool
    :return: the nearest common ancestor of all the points in pts
    :rtype: hou.Point
    .. note::
        If there is no common ancestor, returns None.
    """
def findRoots(geo: hou.Geometry) -> tuple[hou.Point, ...]:
    """
    Get the root points of **geo**.

    :param geo: geometry to get the root points from
    :type geo: hou.Geometry
    :return: tuple of root points
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
def setPointParent(pt: hou.Point | None, newparent: hou.Point | None = None, preventcycles: bool = True) -> bool:
    """
    Set a point's parent.

    :param pt: point to set the new parent to
    :type pt: hou.Point
    :param newparent: new parent to set
    :type newparent: hou.Point
    :param preventcycles: setting **preventcycles** to ``True`` will make the method return ``False`` if the specified **newparent**
    creates a cycle in the skeleton hierarchy
    :type preventcycles: bool
    :return: whether the operation succeeded or not
    :rtype: bool
    """
def rerootHierarchy(root: hou.Point) -> None:
    """
    Set a new point as the skeleton hierarchy root.

    :param root: new point to act as the root
    :type root: hou.Point
    """
@typing.overload
def createPoint(geo: None = ..., name: str = ..., transform: hou.Matrix4 | None = ..., islocaltransform: bool = ..., parent: hou.Point | None = ..., scaleinheritance: int | None = ...) -> None: ...
@typing.overload
def createPoint(geo: hou.Geometry, name: str = ..., transform: hou.Matrix4 | None = ..., islocaltransform: bool = ..., parent: hou.Point | None = ..., scaleinheritance: int | None = ...) -> hou.Point: ...
def deletePoints(geo: hou.Geometry, points: _PointsArg, reparent: bool = True, increment_data_ids: bool = True, invert: bool = False) -> None:
    """ 
    Deletes the specified **points** from the **geo**.
    
    :param geo: geometry to delete the points from
    :type geo: hou.Geometry
    :param points: point list or tuple, point group as a string or a point selection to delete
    :type points: list or tuple of hou.Point or str or hou.Selection
    :param reparent: reparent the hierarchy after the deletion
    :type reparent: bool
    :param increment_data_ids: increment the data ids for the geometry
    :type increment_data_ids: bool
    :param invert: delete all the points in the geometry EXCEPT the ones in **points**
    :type invert: bool
    """
def splitEdge(edge: hou.Prim | hou.Edge, bias: float = 0.5) -> hou.Point:
    """ 
    Create a new point by splitting the given **edge** and initialize the Kinefx-specific attributes on it.
    The position of the newly created point will be interpolated based on the **bias**.
    
    :param edge: edge to split
    :type edge: hou.Prim
    :param bias: interpolate the new point's position based on **bias**
    :type bias: float
    :return: new point
    :rtype: hou.Point
    """
def reverseLink(prim: hou.Prim) -> None:
    """ 
    Reverse the order of **prim**(reverse the order of its vertices).

    :param prim: primitive to reverse
    :type prim: hou.Prim
    """
def mirrorPoints(geo: hou.Geometry, points: _PointsArg, planeorigin: hou.Vector3 = ..., planenormal: hou.Vector3 = ..., flipaxes: int = 0) -> None:
    """ 
    Mirror the **points** around the specified plane.

    :param geo: geometry that the points belong to
    :type geo: hou.Geometry
    :param points: point list or tuple, point group as a string or a point selection to delete
    :type points: list or tuple of hou.Point or str or hou.Selection
    :param planeorigin: origin of the plane to mirror around
    :type planeorigin: hou.Vector3
    :param planenormal: normal of the plane to mirror around
    :type planenormal: hou.Vector3
    :param flipaxes: axis of the mirrored points transformation matrices to flip
    :type flipaxes: int
    """
def createMirroredPoints(pts: Sequence[hou.Point], mirrorattrib: str | None = 'mirrorpt', refattrib: str | None = None, findtokens: Sequence[str] | None = None, replacetokens: Sequence[str] | None = None, planeorigin: hou.Vector3 = ..., planenormal: hou.Vector3 = ..., flipaxes: int = 0, token_position: Literal[0, 1, 2] = 1, attributes_to_mirror: str = '*', groups_to_mirror: str = '*', group_rename_tokens: _GroupRenameTokens = {'from': '*', 'to': '*'}, update_existing: bool = False) -> list[hou.Point]:
    """ 
    Create a set of new points by mirroring the **pts** and store the mirror data in a dictionary point attribute.
    Options for mirroring the point attributes and groups.

    :param pts: point list or tuple to create mirrors of
    :type pts: list or tuple of hou.Point
    :param mirrorattrib: name of the mirror point dictionary attribute in which to store the mirror data
    :type mirrorattrib: str
    :param refattrib: name of the attribute that will be used as reference to match the point to its mirror
    :type refattrib: str
    :param findtokens: a space separated sequence of tokens to replace with the corresponding tokens in the sequence **replacetokens**
    :type findtokens: str
    :param replacetokens: a space separated sequence of tokens to use as replacements for the tokens in the sequence **findtokens**
    :type replacetokens: str
    :param planeorigin: origin of the plane to mirror around
    :type planeorigin: hou.Vector3
    :param planenormal: normal of the plane to mirror around
    :type planenormal: hou.Vector3
    :param flipaxes: axis of the mirrored points transformation matrices to flip
    :type flipaxes: int
    :param token_position: where in the point name to look for the tokens in **findtokens** and replace them with **replacetokens**
    Accepted values are as follows: 0-left, 1-middle, 2-right
    :type token_position: int
    :param attributes_to_mirror: a list of point attributes to transform when the mirrored points are created;
    note that the attributes will be transformed consistently with the mirroring operation based on their type:
    ``normal``, ``vectors``, ``point``, ``hpoint``, ``quaternion`` and ``matrix`` types will be mirrored, other types 
    will get copied over
    :type attributes_to_mirror: str
    :param groups_to_mirror: any point groups listed will be copied over as part of the mirroring operation
    :type groups_to_mirror: str
    :param group_rename_tokens: a dictionary of patterns to search for in the group names;
    the **from** pattern will be replaced with the **to** pattern
    :type group_rename_tokens: dict with key 'from': str and key 'to':str
    :return: list of mirrored points
    :rtype: list of hou.Point
    .. note::
        If **refattrib** is None, the reference attribute will be set to ``ptnum``.
    """
@typing.overload
def extractPoseParms(pt: hou.Point, refpt: hou.Point, parent_local: hou.Matrix4 | None = ..., scale_inheritance: int = ..., refattrib: str = ..., mode: Literal['pre', 'post'] = ...) -> dict[str, hou.Vector3]: ...
@typing.overload
def extractPoseParms(pt: hou.Matrix4, refpt: hou.Point | hou.Matrix4, parent_local: hou.Matrix4, scale_inheritance: int = ..., refattrib: str = ..., mode: Literal['pre', 'post'] = ...) -> dict[str, hou.Vector3]: ...
def combinePoseParms(pt: hou.Point, parm_dict: Mapping[str, hou.Vector3] | None = None, dtattrib: str = 'dt', drattrib: str = 'dr', dsattrib: str = 'ds') -> hou.Matrix4:
    """ 
    Compute the local transformation matrix of **pt** from the passed in **parm_dict** dictionary or **dtattrib**, **drattrib**, 
    **dsattrib** point attributes.

    :param pt: point to compute the local transformation matrix for
    :type pt: hou.Point
    :param parm_dict: dictionary that holds the individual transformation components: `translate`, `rotate`, `scale`
    :type parm_dict: dict
    :param dtattrib: name of the hou.Vector3 translation point attribute
    :type dtattrib: str
    :param drattrib: name of the hou.Vector3 rotation point attribute
    :type drattrib: str
    :param dsattrib: name of the hou.Vector3 scale point attribute
    :type dsattrib: str
    :return: local transformation matrix of **pt** computed from the passed in transformation components
    :rtype: hou.Matrix4
    .. note::
        **dtattrib**, **drattrib** and **dsattrib** will be used to get the transformation components 
        if **parm_dict** is not specified.
    """

parm_formats: dict[str, Callable[[str, int], str]]

def setPoseParmsFromGeo(pp: poseparms.PoseParms, geo: hou.Geometry, ref_geo: hou.Geometry | None = None, parmname: str = 'transformations', threshold: float = 0.001, refattrib: str = 'localtransform', mode: Literal['pre', 'post', 'override'] = 'pre') -> None:
    """ 
    Set parameters on a ``PoseParms`` multiparm instance from a **ref_geo**.
    Basically read a bunch of point world transforms from **ref_geo** and convert them to a set of individual local transform
    components.

    :param pp: ``PoseParms`` multiparm instance to set
    :type pp: poseparms.PoseParms
    :param geo: geometry which points are modified by the multiparm instance
    :type geo: hou.Geometry
    :param ref_geo: geo from where to read the transforms that will be set on the multiparm
    :type ref_geo: hou.Geometry
    :param parmname: name of the multiparm instance
    :type parmname: str
    :param threshold: set the parameter only if its absolute value is higher than the threshold 
    :type threshold: float
    :param refattrib: name of the hou.Matrix4 point attribute to extract from **ref_geo** and convert to individual 
    transformation components
    :type refattrib: str
    :param mode: mode to apply the extracted transformation onto the points(same as the rigpose 'mode' parm); 
    available modes are: 'pre'(pre-multiplication), post'(post-multiplication), 'override'
    :type mode: str
    """
def sanitizeName(pnt: hou.Point) -> bool:
    """
    Sanitize one name at a time.
    Example: original list [test, test] -> after sanitization [test, test1].

    :param pnt: point which name to sanitize
    :type pnt: hou.Point
    :return: whether the name has been sanitized or not
    :rtype: bool
    """
def sanitizeNames(geo: hou.Geometry, store_original: str = '') -> list[int]:
    """ 
    Sanitize all names in **geo**.

    :param geo: geometry which point names to sanitize
    :type geo: hou.Geometry
    :param store_original: name of the point attribute to store the original point in
    :type store_original: str
    :return: list of points that have had their names sanitized
    :rtype: list of hou.Point
    .. note::
        If **store_original** point attribute does not exist, it will be created.
    """
@typing.overload
def lerp(v1: hou.Vector3 | Sequence[float], v2: hou.Vector3 | Sequence[float], bias: float, clamp: Literal[True] = ...) -> hou.Vector3: ...
@typing.overload
def lerp(v1: hou.Vector3, v2: hou.Vector3, bias: float, clamp: bool = ...) -> hou.Vector3: ...
def slerpEulerAngles(r1: hou.Vector3 | Sequence[float], r2: hou.Vector3 | Sequence[float], bias: float) -> hou.Vector3:
    """ 
    Perform a spherical linear interpolation between **r1** and **r2**.

    :param r1: Euler rotation to interpolate from
    :type r1: hou.Vector3
    :param r2: Euler rotation to interpolate to
    :type r2: hou.Vector3
    :param bias: interpolation bias
    :type bias: float
    :return: interpolated rotation
    :rtype: hou.Vector3
    """
def blendTransforms(xform1: hou.Matrix4, xform2: hou.Matrix4, bias: float, components: int = 7) -> hou.Matrix4:
    """ 
    Perform a linear interpolation, between the specified transformation components, between ** xform1** and **xform2**.

    :param xform1: transformation matrix to blend from
    :type xform1: hou.Matrix4
    :param xform2: transformation matrix to blend to
    :type xform2: hou.Matrix4
    :param bias: blend bias
    :type bias: float
    :param components: transformation components to blend
    :type components: int
    :return: blended transformation matrix
    :rtype: hou.Matrix4
    .. note::
        *components* should be passed in as a bit field. 1 for translation, 2 for rotaion, 4 for scaling and any combination
        between these
    """
