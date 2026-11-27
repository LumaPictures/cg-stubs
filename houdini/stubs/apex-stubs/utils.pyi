import _apex
import apex
import cProfile
import hou
import typing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from enum import StrEnum
from typing import Generic

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_K = TypeVar('_K')
_V = TypeVar('_V')
_PortRef: TypeAlias = int | tuple[int | str, str]
_PortMapping: TypeAlias = tuple[str, tuple[int | str, str]]
_PythonDictValue: TypeAlias = bool | int | float | str | hou.Vector2 | hou.Vector3 | hou.Vector4 | hou.Matrix3 | hou.Matrix4 | hou.Geometry | hou.Ramp | apex.Graph | apex.BoolArray | apex.IntArray | apex.FloatArray | apex.StringArray | apex.Vector2Array | apex.Vector3Array | apex.Vector4Array | apex.Matrix3Array | apex.Matrix4Array | apex.GeometryArray | apex.DictArray | dict[str, '_PythonDictValue | None']
ANIMATE_STATE_UNDO_TAG: str

class StateMessages(StrEnum):
    CONTROLS_NOT_IN_LAYER = 'Controls not added to active layer'
    INVALID_APEX_GEOMETRY = 'Geometry is not a valid APEX Scene'

def timing(f: Callable[_P, _R]) -> Callable[_P, _R]: ...

PROFILE_START: int | None
PROFILE_TIME: int | None
PROFILE_COUNT: int
PROFILE_DATA: dict[int, dict[str, float]]

def profile(f: Callable[_P, _R]) -> Callable[_P, _R]: ...
def profileTotal(f: Callable[_P, _R]) -> Callable[_P, _R]: ...
def profileMarker(name: str) -> None: ...

class BlockProfiler:
    profiler: cProfile.Profile | None
    limit: int
    def __init__(self, limit: int = 20) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

def profileBlock(f: Callable[_P, _R], n: int = 20) -> Callable[_P, _R]: ...
def loadGraph(file_path: str) -> apex.Graph: ...
def saveGraph(graph: apex.Graph, path: str) -> None: ...
def addAnimateStateUndo(undo: hou._UndoOperation, name: str, tag: str = ...) -> None: ...
def wirePorts(graph: apex.Graph, port_mapping: Iterable[tuple[_PortRef, _PortRef]], out_prefix: str = '', in_prefix: str = '') -> None: ...
def wireNewOutputMapping(graph: apex.Graph, output: int, output_mapping: Iterable[_PortMapping], prefix: str = '') -> None: ...
def wireNewInputMapping(graph: apex.Graph, parms: int, input_mapping: Iterable[_PortMapping], prefix: str = '') -> None: ...
def mergeGraph(graph: apex.Graph, other_graph: apex.Graph, prefix: str | None = None, offset: hou.Vector3 | None = None) -> list[int]: ...
def apexDictToPythonDict(apex_dict: apex.Dict) -> dict[str, _PythonDictValue | None]:
    """
    Helper Function that converts an apex.Dict to a python Dictionary
    """
def pythonDictToApexDict(dictionary: Mapping[str, _apex._ValueArg]) -> apex.Dict:
    """
    Helper Function that converts a python Dictionary to an apex.Dict
    """
def findControlNameFromPath(control_path: str) -> str:
    """
    Goes from a control path to a control name

    For example if the control path is /sceneaddcharacter5.char/Base.rig/leg_ikhandle_l
    The control name is leg_ikhandle_l. 
    """
def splitPathRef(ref: str) -> tuple[str | None, str]:
    '''
    Split a "<tool>:<path>" ref into (tool_prefix, path). Returns (None, ref)
    if there\'s no tool prefix.
    '''
def prependCharToControlPath(ctrl_ref: str, char_folder: str) -> str:
    '''
    Insert /<char_folder>/ at the start of a control path, preserving any
    "<tool>:" prefix. Idempotent if the path is already prefixed with the
    char folder.
    '''
def graphFromFile(file_name: str) -> apex.Graph: ...
def saveDrawableToGeometry(d: hou.SimpleDrawable | hou.GeometryDrawable | None, geo: hou.Geometry, prefix: str = '', suffix: str = '') -> None:
    """
    Saves a drawable's geometry to a geometry as a packed geometry with the
    name of the drawable
    """

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
    @typing.overload
    def getInverse(self, val: _V, default: None = ...) -> _K | None: ...
    @typing.overload
    def getInverse(self, val: _V, default: _K) -> _K: ...

def fname(f: Callable[_P, _R]) -> Callable[_P, _R]: ...
def fsignature(f: Callable[_P, _R]) -> Callable[_P, _R]: ...
def tb() -> None: ...
def traceCalls(base_paths: Sequence[str] = ...) -> None: ...
