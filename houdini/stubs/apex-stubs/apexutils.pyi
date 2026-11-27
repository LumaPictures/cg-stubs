import apex
import hou
import typing
from _typeshed import SupportsKeysAndGetItem
from collections.abc import Callable as Callable, Mapping
from typing import Generic, Literal, Protocol
from typing_extensions import NotRequired, TypedDict

from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
_V = TypeVar('_V')
class _AttribSpec(TypedDict):
    required: NotRequired[bool]
    default: str | tuple[float, float, float] | hou._OptionDict

class _AttribOps(TypedDict):
    type: hou.EnumValue[hou.attribType]
    find: Callable[[hou.Geometry, str], hou.Attrib | None]
    create: Callable[[hou.Geometry, str, hou._AttribValueArg[hou._OptionValue]], hou.Attrib]

class _Labeled(Protocol):
    @property
    def label(self) -> str: ...

class _CharacterElement(Protocol):
    @property
    def character(self) -> _Labeled: ...
    @property
    def label(self) -> str: ...

class _Manipulator(Protocol):
    @property
    def rig(self) -> _CharacterElement: ...
    @property
    def label(self) -> str: ...

CHARACTER_EXTENSION: str
RIG_EXTENSION: str
CTRL_EXTENSION: str
CTRL_GRAPH_EXTENSION: str
TAGS_ATTR: str
geospec: dict[str, dict[str, _AttribSpec]]
ATTRIB_OPS: dict[str, _AttribOps]
NUMERIC_DEFAULTS: dict[str, int | float | str | hou.Vector2 | hou.Vector3 | hou.Vector4 | hou.Matrix3 | hou.Matrix4 | apex.Dict]
GRAPH_TYPE: str
VECTOR3_TYPE: str
INT_TYPE: str
FLOAT_TYPE: str
STRING_TYPE: str
VECTOR2_TYPE: str
VECTOR4_TYPE: str
MATRIX3_TYPE: str
MATRIX4_TYPE: str
GEOMETRY_TYPE: str
DICT_TYPE: str
BOOL_TYPE: str
NODEID_TYPE: str
PORTID_TYPE: str
FLOATRAMP_TYPE: str
COLORRAMP_TYPE: str
ARRAY_INDICATOR: str
DICTARRAY_TYPE: str

def findMissingAttributes(geo: hou.Geometry) -> dict[str, dict[str, _AttribSpec]]: ...
def initMissingAttributes(geo: hou.Geometry) -> None: ...
def isCharacterNode(node: hou.SopNode, geo_input: int = False) -> bool: ...
def isCharacterGeo(geo: hou.Geometry) -> bool: ...
def nameFromPrimpath(path: str) -> str: ...
def pathFromPrimpath(path: str) -> str: ...
def assemblePrimPath(folder: str, filename: str) -> str: ...
def updatePrimFilename(primpath: str, filename: str) -> str: ...
def extractCharGeo(element_geo: hou.Geometry, primpath: str, verb: hou.SopVerb | None = None, single_element: bool = False, unpack: bool = True) -> hou.Geometry | None:
    """this will be based on the packed folder api. This here is pure improvisation until we have that"""
def extendCharGeo(geo: hou.Geometry, elements: Mapping[str, hou.Geometry], parentpath: str = '/', verb: hou.SopVerb | None = None) -> hou.Geometry: ...
def removeCharGeo(geo: hou.Geometry, primpath: str, verb: hou.SopVerb | None = None) -> hou.Geometry | None: ...
def findCharElements(element_geo: hou.Geometry, group: str = '*.rig') -> list[str] | list[int]:
    """this is currently just a placeholder to find the prims on one level and needs to be replaced by the packed folder api
    :param element_geo: _description_
    :param group: _description_
    """
def findOutputNode(geometry: hou.Geometry, portName: str) -> str | None: ...
def getGraphInputs(graph: apex.Graph, input_type: str = 'Geometry') -> list[str]: ...
def make_name(name: str, module: _CharacterElement | None = None, manip: _Manipulator | None = None) -> str | None: ...
@typing.overload
def assembleTags(name: str | None = ..., character_name: str | None = ..., rig_name: str | None = ..., manipulator_name: str | None = ..., *, asstring: Literal[True], portname: str | None = ...) -> str: ...
@typing.overload
def assembleTags(name: str | None, character_name: str | None, rig_name: str | None, manipulator_name: str | None, asstring: Literal[True], portname: str | None = ...) -> str: ...
@typing.overload
def assembleTags(name: str | None = ..., character_name: str | None = ..., rig_name: str | None = ..., manipulator_name: str | None = ..., asstring: Literal[False] = ..., portname: str | None = ...) -> list[str]: ...
@typing.overload
def assembleTags(name: str | None = ..., character_name: str | None = ..., rig_name: str | None = ..., manipulator_name: str | None = ..., asstring: bool = ..., portname: str | None = ...) -> list[str] | str: ...

class BijectiveMap(dict[_K, _V], Generic[_K, _V]):
    """
    Invertible map. meaning that the inverted dictionary of the given main dict is always automatically maintained. 
    This map does not allow duplicate entries on the inverse side and will always remove the old assignment before setting a new assignment
    """
    inverse: BijectiveMap[_V, _K]
    def __init__(self, inverse: BijectiveMap[_V, _K] | None = None) -> None:
        """
        this is a doc test
        """
    def __setitem__(self, key: _K, value: _V) -> None: ...
    def __delitem__(self, key: _K) -> None: ...
    def getFirstInverse(self, val: _V) -> _K | None: ...
    def getLastInverse(self, val: _V) -> _K | None: ...
    def update(self, val: SupportsKeysAndGetItem[_K, _V]) -> None: ...
    def removeItem(self, key: _K) -> None: ...
