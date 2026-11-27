from collections.abc import Sequence
from typing import TypeAlias, TypeVar, overload

import _apex
import hou
import typing

# What a node's `parms` dict attribute can be set from.  Lists and tuples of numbers become
# vectors or matrices by their length (a tuple of numbers otherwise), of strings a tuple of
# strings; anything else (a hou.Vector3, a dict, a list of bools, ...) and non-string keys are
# silently dropped.  The argument must be a dict: other mappings are rejected.
_ParmValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | list[int]
    | list[float]
    | list[str]
    | tuple[float, ...]
    | tuple[str, ...]
)
# A dict is invariant in its values, so a dict of any of those (`dict[str, float]`) is taken
# through a TypeVar.
_ParmT = TypeVar("_ParmT", bound=_ParmValue)
from typing import Any, overload

@typing.overload
def addNode(arg0: hou.Geometry, arg1: str, arg2: str) -> hou.Point: ...
@typing.overload
def addNode(arg0: hou.Geometry, arg1: str, arg2: str, arg3: hou.Vector3) -> hou.Point: ...
def aliasToPortname(arg0: hou.Point, arg1: str) -> str:
    """aliasToPortname(arg0: object, arg1: str) -> str"""
def computeRefCounts(py_geo: hou.Geometry, refcountattrib: str, groupname: str, promote: bool = ...) -> None:
    """computeRefCounts(py_geo: object, refcountattrib: str, groupname: str, promote: bool = True) -> None"""
# The first variant returns the new wire, or None when the points are in different geometries;
# a None target disconnects the input.  The wire is a polygon, but comes back as a plain hou.Prim
# (no Face/Polygon methods).
@typing.overload
def connectInput(
    arg0: hou.Point, arg1: str, arg2: hou.Point | None, arg3: str
) -> hou.Prim | None: ...
@typing.overload
def connectInput(
    arg0: hou.Geometry, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str
) -> None: ...
@typing.overload
def connectInput(
    arg0: hou.Point, arg1: str, arg2: str, arg3: hou.Point | None, arg4: str, arg5: str
) -> None: ...
@typing.overload
def connectInput(
    arg0: hou.Point, arg1: str, arg2: str, arg3: hou.Point | None, arg4: str, arg5: str, arg6: int
) -> None: ...
def deleteNode(arg0: hou.Geometry, arg1: str) -> bool:
    """deleteNode(arg0: object, arg1: str) -> bool"""
@typing.overload
def disconnectInput(arg0: hou.Point, arg1: str) -> None: ...
@typing.overload
def disconnectInput(arg0: hou.Geometry, arg1: str, arg2: str) -> None: ...
def findInput(arg0: hou.Point, arg1: str) -> hou.Vertex | None:
    """findInput(arg0: object, arg1: str) -> object"""
def findNode(arg0: hou.Geometry, arg1: str) -> hou.Point | None:
    """findNode(arg0: object, arg1: str) -> object"""
def findNodeByPath(arg0: hou.Geometry, arg1: str) -> None:
    """findNodeByPath(arg0: object, arg1: str) -> None"""
def findOutput(arg0: hou.Point, arg1: str) -> hou.Vertex | None:
    """findOutput(arg0: object, arg1: str) -> object"""
def findPortVertex(arg0: hou.Geometry, arg1: str) -> hou.Vertex | None:
    """findPortVertex(arg0: object, arg1: str) -> object"""
def findRoots(arg0: hou.Geometry) -> list[hou.Point]:
    """findRoots(arg0: object) -> list[object]"""
def getAlias(arg0: hou.Geometry, arg1: str, arg2: str) -> str:
    """getAlias(arg0: object, arg1: str, arg2: str) -> str"""
def getAllConnectedNodes(arg0: hou.Geometry, arg1: str) -> list[str]:
    """getAllConnectedNodes(arg0: object, arg1: str) -> list[str]"""
def getAncestors(arg0: hou.Point) -> list[hou.Point]:
    """getAncestors(arg0: object) -> list[object]"""
@typing.overload
def getDescendants(arg0: hou.Point) -> list[hou.Point]: ...
@typing.overload
def getDescendants(arg0: hou.Geometry, arg1: str) -> list[str]: ...
def getGroupHoles(arg0: hou.Geometry, arg1: str) -> list[int]:
    """getGroupHoles(arg0: object, arg1: str) -> list[int]"""
def getInputAncestors(arg0: hou.Point, arg1: str) -> list[hou.Point]:
    """getInputAncestors(*args, **kwargs)
    Overloaded function.

    1. getInputAncestors(arg0: object, arg1: str) -> list[object]

    2. getInputAncestors(arg0: object, arg1: str) -> list[object]
    """
def getInputPts(arg0: hou.Point) -> list[int]:
    """getInputPts(arg0: object) -> list[int]"""
def getOutputDescendants(arg0: hou.Point, arg1: str) -> list[hou.Point]:
    """getOutputDescendants(arg0: object, arg1: str) -> list[object]"""
@typing.overload
def getOutputNodeNames(arg0: hou.Point) -> list[str]: ...
@typing.overload
def getOutputNodeNames(arg0: hou.Geometry, arg1: str) -> list[str]: ...
def getOutputPts(py_pt: hou.Point, outputname: str = ...) -> list[int]:
    """getOutputPts(py_pt: object, outputname: str = '') -> list[int]"""
def getOutputsConnectedToInput(arg0: hou.Point, arg1: str) -> list[hou.Vertex]:
    """getOutputsConnectedToInput(arg0: object, arg1: str) -> object"""
def getSortedIndices(py_geo: hou.Geometry, scope_attrib: str = ...) -> list[list[int]]:
    """getSortedIndices(py_geo: object, scope_attrib: str = '') -> list[list[int]]"""
def getUniqueNodeName(arg0: hou.Geometry, arg1: str) -> str:
    """getUniqueNodeName(arg0: object, arg1: str) -> str"""
def isInputVertex(arg0: hou.Vertex) -> bool:
    """isInputVertex(arg0: object) -> bool"""
def isOutputPt(arg0: hou.Point) -> bool:
    """isOutputPt(arg0: object) -> bool"""
def isOutputVertex(arg0: hou.Vertex) -> bool:
    """isOutputVertex(arg0: object) -> bool"""
def isParmPt(arg0: hou.Point) -> bool:
    """isParmPt(arg0: object) -> bool"""
def isSubnetPt(arg0: hou.Point) -> bool:
    """isSubnetPt(arg0: object) -> bool"""
def isValidNodeGroup(arg0: hou.Geometry, arg1: str) -> bool:
    """isValidNodeGroup(arg0: object, arg1: str) -> bool"""
def layoutInputsAndOutputs(arg0: hou.Geometry) -> None:
    """layoutInputsAndOutputs(arg0: object) -> None"""
def layoutNodes(arg0: hou.Geometry, arg1: str, arg2: hou.Vector2, arg3: hou.Vector2) -> None:
    """layoutNodes(arg0: object, arg1: str, arg2: object, arg3: object) -> None"""
def makeNamesUnique(arg0: hou.Geometry) -> None:
    """makeNamesUnique(arg0: object) -> None"""
def mergeGraph(arg0: hou.Geometry, arg1: hou.Geometry) -> None:
    """mergeGraph(arg0: object, arg1: object) -> None"""
def mergeNodes(arg0: hou.Geometry, arg1: hou.Geometry, arg2: str) -> None:
    """mergeNodes(arg0: object, arg1: object, arg2: str) -> None"""
def moveNode(arg0: hou.Geometry, arg1: str, arg2: hou.Vector3) -> None:
    """moveNode(arg0: object, arg1: str, arg2: object) -> None"""
def packSubnet(arg0: hou.Geometry, arg1: str, arg2: str) -> hou.Point | None:
    """packSubnet(arg0: object, arg1: str, arg2: str) -> object"""
def pruneForOutputs(arg0: hou.Geometry, arg1: str) -> None:
    """pruneForOutputs(arg0: object, arg1: str) -> None"""
@typing.overload
def rewireOutputConnections(arg0: hou.Point, arg1: str, arg2: hou.Point, arg3: str) -> None: ...
@typing.overload
def rewireOutputConnections(
    arg0: hou.Geometry, arg1: str, arg2: str, arg3: str, arg4: str
) -> None: ...
def setAlias(arg0: hou.Geometry, arg1: str, arg2: str, arg3: str) -> None:
    """setAlias(arg0: object, arg1: str, arg2: str, arg3: str) -> None"""
def setName(arg0: hou.Geometry, arg1: str, arg2: str) -> None:
    """setName(arg0: object, arg1: str, arg2: str) -> None"""
@typing.overload
def setParms(arg0: hou.Point, arg1: dict[str, _ParmT]) -> None: ...
@typing.overload
def setParms(arg0: hou.Geometry, arg1: str, arg2: dict[str, _ParmT]) -> None: ...
def setTags(arg0: hou.Geometry, arg1: str, arg2: Sequence[str] | _apex.StringArray) -> None:
    """setTags(arg0: object, arg1: str, arg2: list[str]) -> None"""
def sort(py_geo: hou.Geometry, scope_attrib: str = ...) -> None:
    """sort(py_geo: object, scope_attrib: str = '') -> None"""
@typing.overload
def unpackSubnet(py_geo: hou.Geometry, nodename: str, keep_subnet_bindings: bool = ...) -> None: ...
@typing.overload
def unpackSubnet(py_pt: hou.Point, keep_subnet_bindings: bool = ...) -> None: ...
def unpackSubnets(py_geo: hou.Geometry, keep_subnet_bindings: bool = ..., depth: int = ...) -> None:
    """unpackSubnets(py_geo: object, keep_subnet_bindings: bool = True, depth: int = -1) -> None"""
