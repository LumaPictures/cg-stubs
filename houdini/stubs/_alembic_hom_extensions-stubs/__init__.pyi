# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
from typing import Literal, Never, TypeAlias, Unpack

# An archive is a file path, or a sequence of paths to layer.
_Archive: TypeAlias = str | Sequence[str]
_Matrix4: TypeAlias = tuple[
    float, float, float, float,
    float, float, float, float,
    float, float, float, float,
    float, float, float, float,
]
_BoundingBox: TypeAlias = tuple[float, float, float, float, float, float]
_Value: TypeAlias = int | float | str | tuple[int, ...] | tuple[float, ...]
_Scope: TypeAlias = Literal["varying", "vertex", "facevarying", "uniform", "constant", "unknown"]
# (object name, object type, children)
_SceneNode: TypeAlias = tuple[str, str, tuple["_SceneNode", ...]]
from typing import Any

def alembicArbGeometry(abcPath: _Archive, objectPath: str, name: str, sampleTime: float) -> tuple[list[_Value], bool, _Scope] | None:
    """(value, isConstant, scope) = alembicArbGeometry(abcPath, objectPath, name, sampleTime)

    Returns None or a tuple (value, isConstant, scope).  The tuple
    contains the value for the attribute, it's scope ('varying',
    'vertex', 'facevarying', 'uniform', 'constant' or 'unknown') and
    a boolean flag indicating whether the attribute is constant over
    time or not."""
def alembicBoundingBox(abcPath: _Archive, objectPath: str, sampleTime: float) -> tuple[_BoundingBox, bool] | None:
    """(value, isConstant) = alembicBoundingBox(abcPath, objectPath, sampleTime)

    Returns None or a tuple (value,isConstant). The tuple contains the
    boundingBox for the object, and a boolean flag indicating whether
    boundingBox is constant over the animation.
    The boundingBox returned is a tuple with six elements.
    """
def alembicClearArchiveCache(abcPath: _Archive) -> None:
    """alembicClearArchiveCache(abcPath)

    Clear the internal cache of Alembic files."""
def alembicGetArchiveMaxCacheSize() -> int:
    """alembicGetArchiveMaxCacheSize()

    Return the Alembic files cache size."""
def alembicGetCameraDict(abcPath: _Archive, objectPath: str, sampleTime: float) -> dict[str, float]:
    """alembicGetCameraDict(abcPath, objectPath, sampleTime)

    Returns a dictionary of camera parameters for the given object."""
def alembicGetCameraResolution(abcPath: _Archive, objectPath: str, sampleTime: float) -> tuple[float, float] | None:
    """alembicGetCameraResolution(abcPath, objectPath, sampleTime)

    Returns None or a Tuple containing two floats.
    The first value is resolution x of the Houdini Camera.
    The second value is resolution y of the Houdini Camera.
    Some camera (ex. Maya Camera) does not have a resolution,
    in this case, None is returned.
    """
def alembicGetChildrenHash(abcPath: _Archive, objectPath: str) -> str | None:
    """alembicGetChildrenHash(abcPath, objectPath)

    Returns the aggregated child objects hash if it exists.
    """
def alembicGetLocalXform(abcPath: _Archive, objectPath: str, sampleTime: float) -> tuple[_Matrix4, int] | None:
    """(xform, isConstant) = alembicGetLocalXform(abcPath, objectPath, sampleTime)

    Returns a tuple (xform, isConstant) containing the transform and a
    flag indicating whether the transform is animated or constant. The
    transform is a 16-tuple of floats.

    This is deprecated in favour of getLocalXform()"""
def alembicGetObjectPathListForMenu(abcPath: _Archive) -> list[str]:
    """alembicGetObjectPathListForMenu(abcPath)

    Returns a tuple of strings in the form expected for menu callbacks.
    That is, each object is duplicated as a token/label pair."""
def alembicGetSceneHierarchy(abcPath: _Archive, objectPath: str) -> _SceneNode | None:
    """alembicGetSceneHierarchy(abcPath, objectPath)

    Returns a tree of tuples.  Each tuple is constructed as:
    \tnode[0] := object_name
    \tnode[1] := object_type
    \tnode[2] := (children)
    Where (children) is a tuple containing the child nodes.
    Object types include (but may contain other types):
      - cxform    A constant transform node
      - xform     An animated transform node
      - camera    A camera node
      - polymesh  A Polygon Mesh shape node
      - subdmesh  A Subdivision Surface Mesh shape node
      - faceset   A Face Set shape node
      - curves    A Curves shape node
      - points    A Points shape node
      - nupatch   A NuPatch shape node
      - unknown   An unknown node"""
def alembicHasUserProperties(abcPath: _Archive, objectPath: str) -> bool | None:
    """alembicHasUserProperties(abcPath, objectPath)

    Returns None if the object has no user properties. Otherwise,
    returns whether the userProperties are constant over time or not.
    """
def alembicSetArchiveMaxCacheSize(size: int) -> None:
    """alembicSetArchiveMaxCacheSize(size)

    Set the maximum number of Alembic files cached at one time."""
def alembicTimeRange(*args: Unpack[tuple[_Archive, Unpack[tuple[str, ...]]]], **kwargs: Never) -> tuple[float, float] | None:
    """(start_time, end_time) = alembicTimeRange(abcPath, [objectPath=None])

    Returns None or a tuple (start_time, end_time). The tuple contains
    the global start and end times for the alembic archive, using the fps
    information in the archive. If an object path is provided, it computes
    the start and end times for the object.
    Returns None if the archive is constant.
    """
def alembicUserProperty(abcPath: _Archive, objectPath: str, name: str, sampleTime: float) -> tuple[list[_Value], bool] | None:
    """(value, isConstant) = alembicUserProperty(abcPath, objectPath, name, sampleTime)

    Returns None or a tuple (value,isConstant).  The tuple contains the
    value for the attribute, and a boolean flag indicating whether the
    attribute is constant over time or not.
    """
def alembicUserPropertyMetadata(abcPath: _Archive, objectPath: str, sampleTime: float) -> str | None:
    """alembicUserPropertyMetadata(abcPath, objectPath, sampleTime)

    Returns None or a JSON dictionary containing a map of user property 
    names --> user property metadata.
    """
def alembicUserPropertyValues(*args: Unpack[tuple[_Archive, str, float]], **kwargs: Never) -> str | None:
    """alembicUserPropertyDictionary(abcPath, objectPath, sampleTime)

    Returns None or a JSON dictionary containing a map of user property 
    names --> user property values.
    """
def alembicUserPropertyValuesAndMetadata(abcPath: _Archive, objectPath: str, sampleTime: float) -> tuple[str, str] | None:
    """alembicUserPropertyValuesAndMetadata(abcPath, objectPath, sampleTime)

    Returns None or a Tuple containing two JSON dictionaries. The first 
    dictionary contains a map of user properties to values. The second
    dictionary contains a map of user properties to metadata used to
    interpret the first dictionary.
    """
def alembicVisibility(*args: Unpack[tuple[_Archive, str, float, Unpack[tuple[int, ...]]]], **kwargs: Never) -> tuple[int, bool] | None:
    """(value, isConstant) = alembicVisibility(abcPath, objectPath, sampleTime, [check_ancestor=False])

    Returns None or a tuple (value,isConstant).  The tuple contains the
    visibility for the object, and a boolean flag indicating whether
    visibility is constant over the animation.  The visibility returned
    is an integer where 0 := hidden, 1 := visible, and -1 is deferred
    (dependent on parent visibility).
    """
def getLocalXform(abcPath: _Archive, objectPath: str, sampleTime: float) -> tuple[_Matrix4, int, int] | None:
    """(xform, isConstant, inherit) = getLocalXform(abcPath, objectPath, sampleTime)

    Returns a tuple (xform, isConstant, inherits) containing the transform
    and flags indicating whether the transform is animated/constant,
    along with whether the node inherits it's parent transform (or is
    disconnected from the transform hierarchy)."""
def getWorldXform(abcPath: _Archive, objectPath: str, sampleTime: float) -> tuple[_Matrix4, int, int] | None:
    """(xform, isConstant, inherit) = getWorldXform(abcPath, objectPath, sampleTime)

    Returns a tuple (xform, isConstant, inherits) containing the object to
    world transform flags indicating whether the transform is animated
    or constant, along with whether the node inherit it's parent
    transform (or is disconnected from the transform hierarchy)."""
