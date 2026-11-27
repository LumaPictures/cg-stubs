from typing import Never
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import ClassVar, Generic, NoReturn, TypeAlias, TypeVar, overload

import hou
import typing

_T = TypeVar("_T")
_V = TypeVar("_V")

# An APEX value (a Dict entry, a port's data, a graph output) as python gets it.  Values of the
# types python has no conversion for (AnimChannel, AnimStack, DynamicPath, ApexNodeID, ...) come
# back as None, as do missing ones.
_Value: TypeAlias = (
    bool
    | int
    | float
    | str
    | hou.Vector2
    | hou.Vector3
    | hou.Vector4
    | hou.Matrix3
    | hou.Matrix4
    | hou.Geometry
    | hou.Ramp
    | Dict
    | Graph
    | BoolArray
    | IntArray
    | FloatArray
    | StringArray
    | Vector2Array
    | Vector3Array
    | Vector4Array
    | Matrix3Array
    | Matrix4Array
    | GeometryArray
    | DictArray
)
# What Dict.asDict() turns those into: arrays become lists, Dicts dicts.
_PlainValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | hou.Vector2
    | hou.Vector3
    | hou.Vector4
    | hou.Matrix3
    | hou.Matrix4
    | hou.Geometry
    | hou.Ramp
    | Graph
    | dict[str, "_PlainValue | None"]
    | list[bool]
    | list[int]
    | list[float]
    | list[str]
    | list[hou.Vector2]
    | list[hou.Vector3]
    | list[hou.Vector4]
    | list[hou.Matrix3]
    | list[hou.Matrix4]
    | list[hou.Geometry]
    | list[dict[str, "_PlainValue | None"]]
)
# What an APEX value can be set from.  A list or tuple of one element type becomes the array of
# that type (an empty one a BoolArray, ints mixed with floats a FloatArray), and a dict a Dict;
# other sequences and mappings are rejected.  bytes become a String.
_ValueArg: TypeAlias = (
    bool
    | int
    | float
    | str
    | bytes
    | hou.Vector2
    | hou.Vector3
    | hou.Vector4
    | hou.Matrix3
    | hou.Matrix4
    | hou.Geometry
    | hou.Ramp
    | Dict
    | Graph
    | BoolArray
    | IntArray
    | FloatArray
    | StringArray
    | Vector2Array
    | Vector3Array
    | Vector4Array
    | Matrix3Array
    | Matrix4Array
    | GeometryArray
    | DictArray
    | Sequence[bool]
    | Sequence[int]
    | Sequence[float]
    | Sequence[str]
    | Sequence[bytes]
    | Sequence[hou.Vector2]
    | Sequence[hou.Vector3]
    | Sequence[hou.Vector4]
    | Sequence[hou.Matrix3]
    | Sequence[hou.Matrix4]
    | Sequence[hou.Geometry]
    | Sequence[Dict | Mapping[str, "_ValueArg"]]
    | Mapping[str, "_ValueArg"]
)
from . import graphops as graphops
from typing import Any, Callable, ClassVar, Iterable, Iterator, overload

class AnimationCatalog:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def clipGeometry(self, arg0: str, arg1: hou.Geometry) -> bool:
        """clipGeometry(self: _apex.AnimationCatalog, arg0: str, arg1: object) -> bool"""
    def duplicateClip(self, arg0: str) -> str:
        """duplicateClip(self: _apex.AnimationCatalog, arg0: str) -> str"""
    def exportFolders(self, arg0: Sequence[str] | StringArray, arg1: str) -> None:
        """exportFolders(self: _apex.AnimationCatalog, arg0: UT_Array[str], arg1: str) -> None"""
    def hasUnsavedChanges(self) -> bool:
        """hasUnsavedChanges(self: _apex.AnimationCatalog) -> bool"""
    def importFrom(self, arg0: str) -> bool:
        """importFrom(self: _apex.AnimationCatalog, arg0: str) -> bool"""
    def itemIds(self) -> list[str]:
        """itemIds(self: _apex.AnimationCatalog) -> UT_Array[str]"""
    def lastLoadTime(self) -> int:
        """lastLoadTime(self: _apex.AnimationCatalog) -> int"""
    def preview(self, arg0: str) -> str:
        """preview(self: _apex.AnimationCatalog, arg0: str) -> str"""
    def reload(self) -> None:
        """reload(self: _apex.AnimationCatalog) -> None"""
    def setPreview(self, arg0: str, arg1: str) -> bool:
        """setPreview(self: _apex.AnimationCatalog, arg0: str, arg1: str) -> bool"""

class BoolArray:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.BoolArray) -> None

        2. __init__(self: _apex.BoolArray, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[bool]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.BoolArray) -> None

        2. __init__(self: _apex.BoolArray, arg0: list[object]) -> None
        """
    def append(self, arg0: bool) -> None:
        """append(self: _apex.BoolArray, arg0: object) -> None"""
    def asList(self) -> list[bool]:
        """asList(self: _apex.BoolArray) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.BoolArray) -> None"""
    def pop(self, arg0: int) -> bool:
        """pop(self: _apex.BoolArray, arg0: int) -> object"""
    def remove(self, arg0: bool) -> None:
        """remove(self: _apex.BoolArray, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.BoolArray, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.BoolArray) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> bool:
        """__getitem__(self: _apex.BoolArray, arg0: int) -> object"""
    def __iter__(self) -> Iterator[bool]:
        """__iter__(self: _apex.BoolArray) -> Iterator[bool]"""
    def __len__(self) -> int:
        """__len__(self: _apex.BoolArray) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: bool) -> None:
        """__setitem__(self: _apex.BoolArray, arg0: int, arg1: bool) -> None"""

class ChannelPrimMapping:
    def __init__(self) -> None:
        """__init__(self: _apex.ChannelPrimMapping) -> None"""
    def items(self) -> ItemsView[list[int]]:
        """items(self: _apex.ChannelPrimMapping) -> _apex.ItemsView"""
    def keys(self) -> KeysView:
        """keys(self: _apex.ChannelPrimMapping) -> _apex.KeysView"""
    def values(self) -> ValuesView[list[int]]:
        """values(self: _apex.ChannelPrimMapping) -> _apex.ValuesView"""
    def __bool__(self) -> bool:
        """__bool__(self: _apex.ChannelPrimMapping) -> bool

        Check whether the map is nonempty
        """
    @overload
    def __contains__(self, other: str) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apex.ChannelPrimMapping, arg0: str) -> bool

        2. __contains__(self: _apex.ChannelPrimMapping, arg0: object) -> bool
        """
    @overload
    def __contains__(self, other: object) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apex.ChannelPrimMapping, arg0: str) -> bool

        2. __contains__(self: _apex.ChannelPrimMapping, arg0: object) -> bool
        """
    def __delitem__(self, other: str) -> None:
        """__delitem__(self: _apex.ChannelPrimMapping, arg0: str) -> None"""
    def __getitem__(self, index: str) -> list[int]:
        """__getitem__(self: _apex.ChannelPrimMapping, arg0: str) -> list[int]"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apex.ChannelPrimMapping) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(self: _apex.ChannelPrimMapping) -> int"""
    def __setitem__(self, index: str, object: Sequence[int] | IntArray) -> None:
        """__setitem__(self: _apex.ChannelPrimMapping, arg0: str, arg1: list[int]) -> None"""

class CompatibilityMap:
    class CompatibilityResolver:
        def __init__(self, *, no_constructor: Never) -> None: ...
        def errors(self) -> str:
            """errors(self: _apex.CompatibilityMap.CompatibilityResolver) -> str"""
        @overload
        def inputIndex(self, arg0: int) -> int:
            """inputIndex(*args, **kwargs)
            Overloaded function.

            1. inputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> int

            2. inputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> int
            """
        @overload
        def inputIndex(self, arg0: str) -> int:
            """inputIndex(*args, **kwargs)
            Overloaded function.

            1. inputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> int

            2. inputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> int
            """
        @overload
        def inputName(self, arg0: int) -> str:
            """inputName(*args, **kwargs)
            Overloaded function.

            1. inputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> str

            2. inputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> str
            """
        @overload
        def inputName(self, arg0: str) -> str:
            """inputName(*args, **kwargs)
            Overloaded function.

            1. inputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> str

            2. inputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> str
            """
        def isValid(self) -> bool:
            """isValid(self: _apex.CompatibilityMap.CompatibilityResolver) -> bool"""
        def newName(self) -> str:
            """newName(self: _apex.CompatibilityMap.CompatibilityResolver) -> str"""
        def newSignature(self) -> Signature:
            """newSignature(self: _apex.CompatibilityMap.CompatibilityResolver) -> _apex.Signature"""
        def numInputs(self) -> int:
            """numInputs(self: _apex.CompatibilityMap.CompatibilityResolver) -> int"""
        def numOutputs(self) -> int:
            """numOutputs(self: _apex.CompatibilityMap.CompatibilityResolver) -> int"""
        def oldName(self) -> str:
            """oldName(self: _apex.CompatibilityMap.CompatibilityResolver) -> str"""
        def oldSignature(self) -> Signature:
            """oldSignature(self: _apex.CompatibilityMap.CompatibilityResolver) -> _apex.Signature"""
        @overload
        def outputIndex(self, arg0: int) -> int:
            """outputIndex(*args, **kwargs)
            Overloaded function.

            1. outputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> int

            2. outputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> int
            """
        @overload
        def outputIndex(self, arg0: str) -> int:
            """outputIndex(*args, **kwargs)
            Overloaded function.

            1. outputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> int

            2. outputIndex(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> int
            """
        @overload
        def outputName(self, arg0: int) -> str:
            """outputName(*args, **kwargs)
            Overloaded function.

            1. outputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> str

            2. outputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> str
            """
        @overload
        def outputName(self, arg0: str) -> str:
            """outputName(*args, **kwargs)
            Overloaded function.

            1. outputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: int) -> str

            2. outputName(self: _apex.CompatibilityMap.CompatibilityResolver, arg0: str) -> str
            """
        def __bool__(self) -> bool:
            """__bool__(self: _apex.CompatibilityMap.CompatibilityResolver) -> bool"""
    def __init__(self, *, no_constructor: Never) -> None: ...
    def findName(self, name: str, version: str = ...) -> str:
        """findName(self: _apex.CompatibilityMap, name: str, version: str = None) -> str"""
    def getKeys(self, version: str = ...) -> list[str]:
        """getKeys(self: _apex.CompatibilityMap, version: str = None) -> UT_Array[str]"""

class Dict:
    __iter__: ClassVar[None] = ...  # read-only
    @typing.overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Dict) -> None

        2. __init__(self: _apex.Dict, arg0: dict) -> None

        3. __init__(self: _apex.Dict, arg0: _apex.Dict) -> None
        """
    @typing.overload
    def __init__(self, arg0: Mapping[str, _ValueArg]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Dict) -> None

        2. __init__(self: _apex.Dict, arg0: dict) -> None

        3. __init__(self: _apex.Dict, arg0: _apex.Dict) -> None
        """
    @typing.overload
    def __init__(self, arg0: Dict) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Dict) -> None

        2. __init__(self: _apex.Dict, arg0: dict) -> None

        3. __init__(self: _apex.Dict, arg0: _apex.Dict) -> None
        """
    def asDict(self) -> dict[str, _PlainValue | None]:
        """asDict(self: _apex.Dict) -> object"""
    def bumpDataID(self, arg0: str) -> None:
        """bumpDataID(self: _apex.Dict, arg0: str) -> None"""
    def clear(self) -> None:
        """clear(self: _apex.Dict) -> None"""
    def contains(self, arg0: str) -> bool:
        """contains(self: _apex.Dict, arg0: str) -> bool"""
    def dataID(self) -> int:
        """dataID(self: _apex.Dict) -> int"""
    def empty(self) -> bool:
        """empty(self: _apex.Dict) -> bool"""
    def freeze(self) -> Dict:
        """freeze(self: _apex.Dict) -> _apex.Dict"""
    @overload
    def get(self, arg0: str) -> _Value | None:
        """get(*args, **kwargs)
        Overloaded function.

        1. get(self: _apex.Dict, arg0: str) -> object

        2. get(self: _apex.Dict, arg0: str, arg1: object) -> object
        """
    @overload
    def get(self, arg0: str, arg1: _T) -> _Value | _T | None:
        """get(*args, **kwargs)
        Overloaded function.

        1. get(self: _apex.Dict, arg0: str) -> object

        2. get(self: _apex.Dict, arg0: str, arg1: object) -> object
        """
    def getDataID(self, arg0: str) -> int:
        """getDataID(self: _apex.Dict, arg0: str) -> int"""
    def getDataType(self, arg0: str) -> str:
        """getDataType(self: _apex.Dict, arg0: str) -> str"""
    def getValue(self, arg0: str) -> _Value | None:
        """getValue(self: _apex.Dict, arg0: str) -> object"""
    def items(self, sorted: bool = ...) -> list[tuple[str, _Value | None]]:
        """items(self: _apex.Dict, sorted: bool = False) -> list[tuple[str, object]]"""
    def keys(self, sorted: bool = ...) -> list[str]:
        """keys(self: _apex.Dict, sorted: bool = False) -> list[str]"""
    def pop(self, arg0: str) -> _Value | None:
        """pop(self: _apex.Dict, arg0: str) -> object"""
    def set(self, arg0: str, arg1: _ValueArg) -> None:
        """set(self: _apex.Dict, arg0: str, arg1: object) -> None"""
    @typing.overload
    def update(self, arg0: Dict) -> None:
        """update(*args, **kwargs)
        Overloaded function.

        1. update(self: _apex.Dict, arg0: _apex.Dict) -> None

        2. update(self: _apex.Dict, arg0: _apex.Dict, arg1: bool, arg2: bool) -> None

        3. update(self: _apex.Dict, arg0: _apex.Dict, arg1: list[tuple[str, str]], arg2: bool, arg3: bool) -> None

        4. update(self: _apex.Dict, arg0: _apex.Dict, arg1: str, arg2: str, arg3: bool, arg4: bool) -> None

        5. update(self: _apex.Dict, arg0: dict, arg1: bool, arg2: bool) -> None
        """
    @typing.overload
    def update(self, arg0: Dict, arg1: bool, arg2: bool) -> None:
        """update(*args, **kwargs)
        Overloaded function.

        1. update(self: _apex.Dict, arg0: _apex.Dict) -> None

        2. update(self: _apex.Dict, arg0: _apex.Dict, arg1: bool, arg2: bool) -> None

        3. update(self: _apex.Dict, arg0: _apex.Dict, arg1: list[tuple[str, str]], arg2: bool, arg3: bool) -> None

        4. update(self: _apex.Dict, arg0: _apex.Dict, arg1: str, arg2: str, arg3: bool, arg4: bool) -> None

        5. update(self: _apex.Dict, arg0: dict, arg1: bool, arg2: bool) -> None
        """
    @typing.overload
    def update(self, arg0: Dict, arg1: Sequence[tuple[str, str]], arg2: bool, arg3: bool) -> None:
        """update(*args, **kwargs)
        Overloaded function.

        1. update(self: _apex.Dict, arg0: _apex.Dict) -> None

        2. update(self: _apex.Dict, arg0: _apex.Dict, arg1: bool, arg2: bool) -> None

        3. update(self: _apex.Dict, arg0: _apex.Dict, arg1: list[tuple[str, str]], arg2: bool, arg3: bool) -> None

        4. update(self: _apex.Dict, arg0: _apex.Dict, arg1: str, arg2: str, arg3: bool, arg4: bool) -> None

        5. update(self: _apex.Dict, arg0: dict, arg1: bool, arg2: bool) -> None
        """
    @typing.overload
    def update(self, arg0: Dict, arg1: str, arg2: str, arg3: bool, arg4: bool) -> None:
        """update(*args, **kwargs)
        Overloaded function.

        1. update(self: _apex.Dict, arg0: _apex.Dict) -> None

        2. update(self: _apex.Dict, arg0: _apex.Dict, arg1: bool, arg2: bool) -> None

        3. update(self: _apex.Dict, arg0: _apex.Dict, arg1: list[tuple[str, str]], arg2: bool, arg3: bool) -> None

        4. update(self: _apex.Dict, arg0: _apex.Dict, arg1: str, arg2: str, arg3: bool, arg4: bool) -> None

        5. update(self: _apex.Dict, arg0: dict, arg1: bool, arg2: bool) -> None
        """
    @typing.overload
    def update(self, arg0: Mapping[str, _ValueArg], arg1: bool, arg2: bool) -> None:
        """update(*args, **kwargs)
        Overloaded function.

        1. update(self: _apex.Dict, arg0: _apex.Dict) -> None

        2. update(self: _apex.Dict, arg0: _apex.Dict, arg1: bool, arg2: bool) -> None

        3. update(self: _apex.Dict, arg0: _apex.Dict, arg1: list[tuple[str, str]], arg2: bool, arg3: bool) -> None

        4. update(self: _apex.Dict, arg0: _apex.Dict, arg1: str, arg2: str, arg3: bool, arg4: bool) -> None

        5. update(self: _apex.Dict, arg0: dict, arg1: bool, arg2: bool) -> None
        """
    def updateFromDetail(self, arg0: hou.Geometry, arg1: str) -> None:
        """updateFromDetail(self: _apex.Dict, arg0: object, arg1: str) -> None"""
    def values(self) -> list[_Value | None]:
        """values(self: _apex.Dict) -> list[object]"""
    def writeToDetail(self, geo: hou.Geometry, name: str, include_geometry: bool = ...) -> None:
        """writeToDetail(self: _apex.Dict, geo: object, name: str, include_geometry: bool = False) -> None"""
    def __contains__(self, other: str) -> bool:
        """__contains__(self: _apex.Dict, arg0: str) -> bool"""
    def __getitem__(self, index: str) -> _Value | None:
        """__getitem__(self: _apex.Dict, arg0: str) -> object"""
    def __len__(self) -> int:
        """__len__(self: _apex.Dict) -> int"""
    def __setitem__(self, index: str, object: _ValueArg) -> None:
        """__setitem__(self: _apex.Dict, arg0: str, arg1: object) -> None"""

class DictArray:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.DictArray) -> None

        2. __init__(self: _apex.DictArray, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[Dict | Mapping[str, _ValueArg]]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.DictArray) -> None

        2. __init__(self: _apex.DictArray, arg0: list[object]) -> None
        """
    def append(self, arg0: Dict) -> None:
        """append(self: _apex.DictArray, arg0: object) -> None"""
    def asList(self) -> list[dict[str, _PlainValue | None]]:
        """asList(self: _apex.DictArray) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.DictArray) -> None"""
    def pop(self, arg0: int) -> Dict:
        """pop(self: _apex.DictArray, arg0: int) -> object"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.DictArray, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.DictArray) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> Dict:
        """__getitem__(self: _apex.DictArray, arg0: int) -> object"""
    def __iter__(self) -> Iterator[Dict]:
        """__iter__(self: _apex.DictArray) -> Iterator[apex::APEX_COWHandle<apex::APEX_ParmDict>]"""
    def __len__(self) -> int:
        """__len__(self: _apex.DictArray) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: Dict) -> None:
        """__setitem__(self: _apex.DictArray, arg0: int, arg1: apex::APEX_COWHandle<apex::APEX_ParmDict>) -> None"""

class FloatArray:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.FloatArray) -> None

        2. __init__(self: _apex.FloatArray, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[float]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.FloatArray) -> None

        2. __init__(self: _apex.FloatArray, arg0: list[object]) -> None
        """
    def append(self, arg0: float) -> None:
        """append(self: _apex.FloatArray, arg0: object) -> None"""
    def asList(self) -> list[float]:
        """asList(self: _apex.FloatArray) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.FloatArray) -> None"""
    def pop(self, arg0: int) -> float:
        """pop(self: _apex.FloatArray, arg0: int) -> object"""
    def remove(self, arg0: float) -> None:
        """remove(self: _apex.FloatArray, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.FloatArray, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.FloatArray) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> float:
        """__getitem__(self: _apex.FloatArray, arg0: int) -> object"""
    def __iter__(self) -> Iterator[float]:
        """__iter__(self: _apex.FloatArray) -> Iterator[float]"""
    def __len__(self) -> int:
        """__len__(self: _apex.FloatArray) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: float) -> None:
        """__setitem__(self: _apex.FloatArray, arg0: int, arg1: float) -> None"""

class GeometryArray:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.GeometryArray) -> None

        2. __init__(self: _apex.GeometryArray, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[hou.Geometry]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.GeometryArray) -> None

        2. __init__(self: _apex.GeometryArray, arg0: list[object]) -> None
        """
    def append(self, arg0: hou.Geometry) -> None:
        """append(self: _apex.GeometryArray, arg0: object) -> None"""
    def asList(self) -> list[hou.Geometry]:
        """asList(self: _apex.GeometryArray) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.GeometryArray) -> None"""
    def pop(self, arg0: int) -> hou.Geometry:
        """pop(self: _apex.GeometryArray, arg0: int) -> object"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.GeometryArray, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.GeometryArray) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> hou.Geometry:
        """__getitem__(self: _apex.GeometryArray, arg0: int) -> object"""
    def __iter__(self) -> Iterator[hou.Geometry]:
        """__iter__(self: _apex.GeometryArray) -> Iterator[Geometry]"""
    def __len__(self) -> int:
        """__len__(self: _apex.GeometryArray) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: hou.Geometry) -> None:
        """__setitem__(self: _apex.GeometryArray, arg0: int, arg1: Geometry) -> None"""

class Graph:
    class connectorType:
        __members__: ClassVar[dict[str, Graph.connectorType]] = ...  # read-only
        Input: ClassVar[Graph.connectorType] = ...
        Output: ClassVar[Graph.connectorType] = ...
        __entries: ClassVar[dict[str, tuple[Graph.connectorType, str | None]]] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: _apex.Graph.connectorType, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: _apex.Graph.connectorType) -> int"""
        def __int__(self) -> int:
            """__int__(self: _apex.Graph.connectorType) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...
    Input: ClassVar[Graph.connectorType] = ...
    Output: ClassVar[Graph.connectorType] = ...
    @typing.overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Graph) -> None

        2. __init__(self: _apex.Graph, arg0: str) -> None

        3. __init__(self: _apex.Graph, arg0: object) -> None
        """
    @typing.overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Graph) -> None

        2. __init__(self: _apex.Graph, arg0: str) -> None

        3. __init__(self: _apex.Graph, arg0: object) -> None
        """
    @typing.overload
    def __init__(self, arg0: hou.Geometry) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Graph) -> None

        2. __init__(self: _apex.Graph, arg0: str) -> None

        3. __init__(self: _apex.Graph, arg0: object) -> None
        """
    def addGraphInput(self, nodeid: int, portname: str, force_unique: bool = ...) -> int:
        """addGraphInput(self: _apex.Graph, nodeid: int, portname: str, force_unique: bool = False) -> int"""
    def addGraphOutput(self, nodeid: int, portname: str, force_unique: bool = ...) -> int:
        """addGraphOutput(self: _apex.Graph, nodeid: int, portname: str, force_unique: bool = False) -> int"""
    def addNode(self, arg0: str, arg1: str) -> int:
        """addNode(self: _apex.Graph, arg0: str, arg1: str) -> int"""
    def addNodeToSubnet(self, arg0: int, arg1: str, arg2: str) -> int:
        """addNodeToSubnet(self: _apex.Graph, arg0: int, arg1: str, arg2: str) -> int"""
    def addSubPort(self, portid: int, portname: str, force_unique: bool = ...) -> int:
        """addSubPort(self: _apex.Graph, portid: int, portname: str, force_unique: bool = False) -> int"""
    def addSubnet(self, name: str, contents: Graph, parent: int = ...) -> int:
        """addSubnet(self: _apex.Graph, name: str, contents: _apex.Graph, parent: int = -1) -> int"""
    def addSubnetInput(self, arg0: int, arg1: str) -> int:
        """addSubnetInput(self: _apex.Graph, arg0: int, arg1: str) -> int"""
    def addSubnetOutput(self, arg0: int, arg1: str) -> int:
        """addSubnetOutput(self: _apex.Graph, arg0: int, arg1: str) -> int"""
    def addTemplate(self, arg0: str, arg1: Graph) -> int:
        """addTemplate(self: _apex.Graph, arg0: str, arg1: _apex.Graph) -> int"""
    @overload
    def addWire(self, arg0: int, arg1: int) -> int:
        """addWire(*args, **kwargs)
        Overloaded function.

        1. addWire(self: _apex.Graph, arg0: int, arg1: int) -> int

        2. addWire(self: _apex.Graph, arg0: int, arg1: str, arg2: int, arg3: str) -> int
        """
    @overload
    def addWire(self, arg0: int, arg1: str, arg2: int, arg3: str) -> int:
        """addWire(*args, **kwargs)
        Overloaded function.

        1. addWire(self: _apex.Graph, arg0: int, arg1: int) -> int

        2. addWire(self: _apex.Graph, arg0: int, arg1: str, arg2: int, arg3: str) -> int
        """
    def addWirePath(self, src_portid: int, dst_portid: int, name: str = ...) -> list[int]:
        """addWirePath(self: _apex.Graph, src_portid: int, dst_portid: int, name: str = '') -> list[int]"""
    def allNodes(self) -> Iterator[int]:
        """allNodes(self: _apex.Graph) -> Iterator[int]"""
    def allPorts(self) -> Iterator[int]:
        """allPorts(self: _apex.Graph) -> Iterator[int]"""
    def ancestors(self, nodeid: Sequence[int] | IntArray, traverse_subnets: bool = ..., inclusive: bool = ..., halting_pattern: str = ..., get_halting_nodes: bool = ...) -> list[int]:
        """ancestors(self: _apex.Graph, nodeid: list[int], traverse_subnets: bool = False, inclusive: bool = False, halting_pattern: str = '', get_halting_nodes: bool = False) -> list[int]"""
    def buildParmDependencies(self) -> None:
        """buildParmDependencies(self: _apex.Graph) -> None"""
    def buildParmSubgraph(self, arg0: str) -> list[int]:
        """buildParmSubgraph(self: _apex.Graph, arg0: str) -> list[int]"""
    def callbackName(self, arg0: int) -> str:
        """callbackName(self: _apex.Graph, arg0: int) -> str"""
    def compileProgram(self) -> None:
        """compileProgram(self: _apex.Graph) -> None"""
    def connectedPorts(self, portid: int, include_subports: bool = ..., traverse_subnets: bool = ..., traverse_spares: bool = ...) -> list[int]:
        """connectedPorts(self: _apex.Graph, portid: int, include_subports: bool = True, traverse_subnets: bool = False, traverse_spares: bool = False) -> list[int]"""
    def convertSubgraphToSubnet(self, arg0: int) -> int:
        """convertSubgraphToSubnet(self: _apex.Graph, arg0: int) -> int"""
    def dataId(self) -> int:
        """dataId(self: _apex.Graph) -> int"""
    def descendants(self, nodeid: Sequence[int] | IntArray, traverse_subnets: bool = ..., inclusive: bool = ..., halting_pattern: str = ..., get_halting_nodes: bool = ...) -> list[int]:
        """descendants(self: _apex.Graph, nodeid: list[int], traverse_subnets: bool = False, inclusive: bool = False, halting_pattern: str = '', get_halting_nodes: bool = False) -> list[int]"""
    def errors(self) -> list[str]:
        """errors(self: _apex.Graph) -> list[str]"""
    def evaluateNodes(self, arg0: Sequence[int] | IntArray) -> None:
        """evaluateNodes(self: _apex.Graph, arg0: list[int]) -> None"""
    def evaluateOutput(self, arg0: str) -> _Value | None:
        """evaluateOutput(self: _apex.Graph, arg0: str) -> object"""
    @typing.overload
    def evaluateOutputs(self, arg0: str) -> Dict:
        """evaluateOutputs(*args, **kwargs)
        Overloaded function.

        1. evaluateOutputs(self: _apex.Graph, arg0: str) -> _apex.Dict

        2. evaluateOutputs(self: _apex.Graph, arg0: list[int]) -> list
        """
    @typing.overload
    def evaluateOutputs(self, arg0: Sequence[int] | IntArray) -> list[_Value | None]:
        """evaluateOutputs(*args, **kwargs)
        Overloaded function.

        1. evaluateOutputs(self: _apex.Graph, arg0: str) -> _apex.Dict

        2. evaluateOutputs(self: _apex.Graph, arg0: list[int]) -> list
        """
    @staticmethod
    def executeMulti(arg0: Sequence[Graph]) -> None:
        """executeMulti(arg0: list[_apex.Graph]) -> None"""
    def executeProgram(self) -> None:
        """executeProgram(self: _apex.Graph) -> None"""
    def executionErrors(self) -> list[str]:
        """executionErrors(self: _apex.Graph) -> list[str]"""
    def findAllDominatedPorts(self, include_subgraphs: bool = ...) -> dict[int, list[int]]:
        """findAllDominatedPorts(self: _apex.Graph, include_subgraphs: bool = False) -> dict[int, list[int]]"""
    def findAndRemoveWire(self, arg0: int, arg1: int, arg2: bool) -> None:
        """findAndRemoveWire(self: _apex.Graph, arg0: int, arg1: int, arg2: bool) -> None"""
    def findDominatedPort(self, portid: int, include_subgraphs: bool = ...) -> int:
        """findDominatedPort(self: _apex.Graph, portid: int, include_subgraphs: bool = False) -> int"""
    def findDominatedPorts(self, include_subgraphs: bool = ...) -> dict[int, int]:
        """findDominatedPorts(self: _apex.Graph, include_subgraphs: bool = False) -> dict[int, int]"""
    def findGraphInputPort(self, arg0: str) -> int:
        """findGraphInputPort(self: _apex.Graph, arg0: str) -> int"""
    def findGraphOutputPort(self, arg0: str) -> int:
        """findGraphOutputPort(self: _apex.Graph, arg0: str) -> int"""
    def findOrAddPort(self, arg0: int, arg1: str) -> int:
        """findOrAddPort(self: _apex.Graph, arg0: int, arg1: str) -> int"""
    def findPorts(self, arg0: int, arg1: Sequence[str] | StringArray) -> list[int]:
        """findPorts(self: _apex.Graph, arg0: int, arg1: list[str]) -> list[int]"""
    def findWire(self, arg0: int, arg1: int) -> int:
        """findWire(self: _apex.Graph, arg0: int, arg1: int) -> int"""
    def findWirePath(self, src_portid: int, dst_portid: int, allow_partial: bool = ...) -> list[int]:
        """findWirePath(self: _apex.Graph, src_portid: int, dst_portid: int, allow_partial: bool = False) -> list[int]"""
    def freeze(self) -> Graph:
        """freeze(self: _apex.Graph) -> _apex.Graph"""
    def getConnectedNodes(self, portid: int, include_subports: bool = ..., traverse_subnets: bool = ..., traverse_spares: bool = ...) -> list[int]:
        """getConnectedNodes(self: _apex.Graph, portid: int, include_subports: bool = True, traverse_subnets: bool = False, traverse_spares: bool = False) -> list[int]"""
    def getDefaultParameters(self, include_compiled: bool = ...) -> Dict:
        """getDefaultParameters(self: _apex.Graph, include_compiled: bool = False) -> _apex.Dict"""
    def getDirtyNodes(self) -> list[int]:
        """getDirtyNodes(self: _apex.Graph) -> list[int]"""
    def getDirtyParameters(self) -> list[str]:
        """getDirtyParameters(self: _apex.Graph) -> list[str]"""
    def getInputPorts(self, arg0: int) -> list[int]:
        """getInputPorts(self: _apex.Graph, arg0: int) -> list[int]"""
    def getNodeOutputData(self, arg0: str, arg1: str) -> _Value | None:
        """getNodeOutputData(self: _apex.Graph, arg0: str, arg1: str) -> object"""
    def getNodeParmDependencies(self, arg0: int) -> list[int]:
        """getNodeParmDependencies(self: _apex.Graph, arg0: int) -> list[int]"""
    def getNodeParms(self, arg0: int) -> Dict:
        """getNodeParms(self: _apex.Graph, arg0: int) -> _apex.Dict"""
    def getNodeProperties(self, arg0: int) -> Dict:
        """getNodeProperties(self: _apex.Graph, arg0: int) -> _apex.Dict"""
    def getNodesDependingOnParm(self, arg0: int) -> list[int]:
        """getNodesDependingOnParm(self: _apex.Graph, arg0: int) -> list[int]"""
    def getOutputData(self, arg0: str) -> _Value | None:
        """getOutputData(self: _apex.Graph, arg0: str) -> object"""
    def getOutputPorts(self, arg0: int) -> list[int]:
        """getOutputPorts(self: _apex.Graph, arg0: int) -> list[int]"""
    def getParmDict(self) -> Dict:
        """getParmDict(self: _apex.Graph) -> _apex.Dict"""
    def getPort(self, arg0: int, arg1: str) -> int:
        """getPort(self: _apex.Graph, arg0: int, arg1: str) -> int"""
    def getPortData(self, arg0: int, arg1: bool) -> _Value | None:
        """getPortData(self: _apex.Graph, arg0: int, arg1: bool) -> object"""
    def getPromotedPort(self, arg0: int, arg1: bool) -> int:
        """getPromotedPort(self: _apex.Graph, arg0: int, arg1: bool) -> int"""
    def inputPorts(self) -> list[int]:
        """inputPorts(self: _apex.Graph) -> list[int]"""
    def isGraphAsset(self, arg0: int) -> bool:
        """isGraphAsset(self: _apex.Graph, arg0: int) -> bool"""
    def isPortInPlace(self, arg0: int) -> bool:
        """isPortInPlace(self: _apex.Graph, arg0: int) -> bool"""
    def isPortPromoted(self, arg0: int, arg1: bool) -> bool:
        """isPortPromoted(self: _apex.Graph, arg0: int, arg1: bool) -> bool"""
    def isValidForGeometry(self, arg0: hou.Geometry) -> bool:
        """isValidForGeometry(self: _apex.Graph, arg0: object) -> bool"""
    def isValidNodeID(self, arg0: int) -> bool:
        """isValidNodeID(self: _apex.Graph, arg0: int) -> bool"""
    def isValidPortID(self, arg0: int) -> bool:
        """isValidPortID(self: _apex.Graph, arg0: int) -> bool"""
    def layout(self) -> None:
        """layout(self: _apex.Graph) -> None"""
    def linkPort(self, arg0: int) -> int:
        """linkPort(self: _apex.Graph, arg0: int) -> int"""
    def loadFromGeometry(self, py_geo: hou.Geometry, essential_only: bool = ...) -> bool:
        """loadFromGeometry(self: _apex.Graph, py_geo: object, essential_only: bool = False) -> bool"""
    def matchFirstNode(self, pattern: str, breadth_first: bool = ...) -> int:
        """matchFirstNode(self: _apex.Graph, pattern: str, breadth_first: bool = False) -> int"""
    def matchGraphInputs(self, pattern: str) -> list[int]:
        """matchGraphInputs(self: _apex.Graph, pattern: str) -> list[int]"""
    def matchGraphOutputs(self, pattern: str) -> list[int]:
        """matchGraphOutputs(self: _apex.Graph, pattern: str) -> list[int]"""
    def matchNodes(self, pattern: str, breadth_first: bool = ...) -> list[int]:
        """matchNodes(self: _apex.Graph, pattern: str, breadth_first: bool = False) -> list[int]"""
    def matchPorts(self, pattern: str, breadth_first: bool = ...) -> list[int]:
        """matchPorts(self: _apex.Graph, pattern: str, breadth_first: bool = False) -> list[int]"""
    def merge(self, arg0: Graph) -> list[int]:
        """merge(self: _apex.Graph, arg0: _apex.Graph) -> list[int]"""
    def name(self) -> str:
        """name(self: _apex.Graph) -> str"""
    def needsRecompile(self) -> bool:
        """needsRecompile(self: _apex.Graph) -> bool"""
    def nodeColor(self, arg0: int) -> hou.Vector3:
        """nodeColor(self: _apex.Graph, arg0: int) -> Vector3"""
    def nodeInvocationIndex(self, arg0: int) -> int:
        """nodeInvocationIndex(self: _apex.Graph, arg0: int) -> int"""
    def nodeName(self, arg0: int) -> str:
        """nodeName(self: _apex.Graph, arg0: int) -> str"""
    def nodeParent(self, arg0: int) -> int:
        """nodeParent(self: _apex.Graph, arg0: int) -> int"""
    def nodePath(self, arg0: int) -> str:
        """nodePath(self: _apex.Graph, arg0: int) -> str"""
    def nodePosition(self, arg0: int) -> hou.Vector3:
        """nodePosition(self: _apex.Graph, arg0: int) -> Vector3"""
    def nodeScopeBegin(self, nodeid: int, inclusive: bool = ...) -> int:
        """nodeScopeBegin(self: _apex.Graph, nodeid: int, inclusive: bool = True) -> int"""
    def nodeScopeEnd(self, nodeid: int, inclusive: bool = ...) -> int:
        """nodeScopeEnd(self: _apex.Graph, nodeid: int, inclusive: bool = True) -> int"""
    def nodeScopeNodes(self, nodeid: int, inclusive: bool = ...) -> list[int]:
        """nodeScopeNodes(self: _apex.Graph, nodeid: int, inclusive: bool = True) -> list[int]"""
    def nodeTags(self, arg0: int) -> StringArray:
        """nodeTags(self: _apex.Graph, arg0: int) -> _apex.StringArray"""
    def outerPort(self, arg0: int) -> int:
        """outerPort(self: _apex.Graph, arg0: int) -> int"""
    def outerPortIndex(self, arg0: int) -> int:
        """outerPortIndex(self: _apex.Graph, arg0: int) -> int"""
    def outputPorts(self) -> list[int]:
        """outputPorts(self: _apex.Graph) -> list[int]"""
    def packSubGraph(self, arg0: str, arg1: Sequence[int] | IntArray) -> int:
        """packSubGraph(self: _apex.Graph, arg0: str, arg1: list[int]) -> int"""
    def parameters(self) -> Dict:
        """parameters(self: _apex.Graph) -> _apex.Dict"""
    def portAcceptsSubPorts(self, arg0: int) -> bool:
        """portAcceptsSubPorts(self: _apex.Graph, arg0: int) -> bool"""
    def portAlias(self, arg0: int) -> str:
        """portAlias(self: _apex.Graph, arg0: int) -> str"""
    def portKind(self, arg0: int) -> Graph.connectorType:
        """portKind(self: _apex.Graph, arg0: int) -> UNI_PortKind"""
    def portName(self, arg0: int) -> str:
        """portName(self: _apex.Graph, arg0: int) -> str"""
    def portNode(self, arg0: int) -> int:
        """portNode(self: _apex.Graph, arg0: int) -> int"""
    def portParm(self, arg0: int) -> _Value | None:
        """portParm(self: _apex.Graph, arg0: int) -> object"""
    def portPath(self, arg0: int) -> str:
        """portPath(self: _apex.Graph, arg0: int) -> str"""
    def portPaths(self) -> list[str]:
        """portPaths(self: _apex.Graph) -> list[str]"""
    def portTypeIsArray(self, arg0: int) -> bool:
        """portTypeIsArray(self: _apex.Graph, arg0: int) -> bool"""
    def portTypeName(self, arg0: int) -> str:
        """portTypeName(self: _apex.Graph, arg0: int) -> str"""
    def portWires(self, arg0: int) -> list[int]:
        """portWires(self: _apex.Graph, arg0: int) -> list[int]"""
    def previewDirtyNodes(self) -> list[int]:
        """previewDirtyNodes(self: _apex.Graph) -> list[int]"""
    def promoteDominantArgs(self) -> list[str]:
        """promoteDominantArgs(self: _apex.Graph) -> list[str]"""
    def promoteInput(self, arg0: int, arg1: int, arg2: str) -> int:
        """promoteInput(self: _apex.Graph, arg0: int, arg1: int, arg2: str) -> int"""
    def promoteOutput(self, arg0: int, arg1: int, arg2: str) -> int:
        """promoteOutput(self: _apex.Graph, arg0: int, arg1: int, arg2: str) -> int"""
    def properties(self) -> Dict:
        """properties(self: _apex.Graph) -> _apex.Dict"""
    def removeNode(self, arg0: str) -> None:
        """removeNode(self: _apex.Graph, arg0: str) -> None"""
    def removeNodes(self, arg0: Sequence[int] | IntArray) -> None:
        """removeNodes(self: _apex.Graph, arg0: list[int]) -> None"""
    def removeWire(self, arg0: int, arg1: bool) -> None:
        """removeWire(self: _apex.Graph, arg0: int, arg1: bool) -> None"""
    def removeWires(self, arg0: Sequence[int] | IntArray, arg1: bool) -> None:
        """removeWires(self: _apex.Graph, arg0: list[int], arg1: bool) -> None"""
    def resolveTypes(self) -> bool:
        """resolveTypes(self: _apex.Graph) -> bool"""
    @overload
    def saveToGeometry(self, py_geo: hou.Geometry, output_node_data: bool = ..., output_debug: bool = ..., preserve_generics: bool = ...) -> None:
        """saveToGeometry(*args, **kwargs)
        Overloaded function.

        1. saveToGeometry(self: _apex.Graph, py_geo: object, output_node_data: bool = False, output_debug: bool = False, preserve_generics: bool = False) -> None

        2. saveToGeometry(self: _apex.Graph, arg0: object, arg1: list[int]) -> None
        """
    @overload
    def saveToGeometry(self, arg0: hou.Geometry, arg1: Sequence[int] | IntArray) -> None:
        """saveToGeometry(*args, **kwargs)
        Overloaded function.

        1. saveToGeometry(self: _apex.Graph, py_geo: object, output_node_data: bool = False, output_debug: bool = False, preserve_generics: bool = False) -> None

        2. saveToGeometry(self: _apex.Graph, arg0: object, arg1: list[int]) -> None
        """
    def setAbortingOnError(self, arg0: bool) -> None:
        """setAbortingOnError(self: _apex.Graph, arg0: bool) -> None"""
    def setDebug(self, arg0: bool) -> None:
        """setDebug(self: _apex.Graph, arg0: bool) -> None"""
    def setDefaultParms(self, parms: Dict, clear: bool = ...) -> None:
        """setDefaultParms(self: _apex.Graph, parms: _apex.Dict, clear: bool = True) -> None"""
    def setName(self, arg0: str) -> None:
        """setName(self: _apex.Graph, arg0: str) -> None"""
    def setNodeColor(self, arg0: int, arg1: hou.Vector3 | hou.Color) -> None:
        """setNodeColor(*args, **kwargs)
        Overloaded function.

        1. setNodeColor(self: _apex.Graph, arg0: int, arg1: object) -> None

        2. setNodeColor(self: _apex.Graph, arg0: int, arg1: Vector3) -> None
        """
    def setNodeName(self, arg0: int, arg1: str) -> None:
        """setNodeName(self: _apex.Graph, arg0: int, arg1: str) -> None"""
    def setNodeParm(self, arg0: int, arg1: str, arg2: _ValueArg) -> None:
        """setNodeParm(self: _apex.Graph, arg0: int, arg1: str, arg2: object) -> None"""
    def setNodeParms(self, nodeid: int, dict: Dict, merge: bool = ...) -> None:
        """setNodeParms(self: _apex.Graph, nodeid: int, dict: _apex.Dict, merge: bool = False) -> None"""
    def setNodePosition(self, arg0: int, arg1: hou.Vector3) -> None:
        """setNodePosition(self: _apex.Graph, arg0: int, arg1: Vector3) -> None"""
    def setNodeProperties(self, arg0: int, arg1: Dict) -> None:
        """setNodeProperties(self: _apex.Graph, arg0: int, arg1: _apex.Dict) -> None"""
    def setNodeTag(self, arg0: int, arg1: str) -> None:
        """setNodeTag(self: _apex.Graph, arg0: int, arg1: str) -> None"""
    def setNodeTags(self, arg0: int, arg1: StringArray, arg2: bool) -> None:
        """setNodeTags(self: _apex.Graph, arg0: int, arg1: _apex.StringArray, arg2: bool) -> None"""
    def setParametersDirty(self, arg0: Sequence[str] | StringArray) -> None:
        """setParametersDirty(self: _apex.Graph, arg0: list[str]) -> None"""
    def setParm(self, key: str, py_obj: _ValueArg, set_default: bool = ...) -> None:
        """setParm(self: _apex.Graph, key: str, py_obj: object, set_default: bool = True) -> None"""
    @overload
    def setParms(self, arg0: Mapping[str, _ValueArg]) -> None:
        """setParms(*args, **kwargs)
        Overloaded function.

        1. setParms(self: _apex.Graph, arg0: dict) -> None

        2. setParms(self: _apex.Graph, parms: _apex.Dict, clear: bool = True) -> None
        """
    @overload
    def setParms(self, parms: Dict, clear: bool = ...) -> None:
        """setParms(*args, **kwargs)
        Overloaded function.

        1. setParms(self: _apex.Graph, arg0: dict) -> None

        2. setParms(self: _apex.Graph, parms: _apex.Dict, clear: bool = True) -> None
        """
    def setPortName(self, arg0: int, arg1: str) -> None:
        """setPortName(self: _apex.Graph, arg0: int, arg1: str) -> None"""
    def setProperties(self, arg0: Dict) -> None:
        """setProperties(self: _apex.Graph, arg0: _apex.Dict) -> None"""
    def setStrictCompile(self, arg0: bool) -> None:
        """setStrictCompile(self: _apex.Graph, arg0: bool) -> None"""
    def signature(self) -> Signature:
        """signature(self: _apex.Graph) -> apex::APEX_Signature"""
    def sort(self, update_position: bool = ..., use_compile_sort: bool = ...) -> None:
        """sort(self: _apex.Graph, update_position: bool = False, use_compile_sort: bool = False) -> None"""
    def sourcePort(self, portid: int, traverse_subnets: bool = ..., traverse_spares: bool = ...) -> int:
        """sourcePort(self: _apex.Graph, portid: int, traverse_subnets: bool = True, traverse_spares: bool = True) -> int"""
    def split(self, nodeids: Sequence[int] | IntArray, excluded_inputs: Sequence[int] | IntArray, prefix: str, split_ancestors: bool = ..., inclusive: bool = ...) -> Graph:
        """split(self: _apex.Graph, nodeids: list[int], excluded_inputs: list[int], prefix: str, split_ancestors: bool = True, inclusive: bool = True) -> _apex.Graph"""
    def stat(self) -> dict[str, int]:
        """stat(self: _apex.Graph) -> dict[str, int]"""
    def subGraphForOutput(self, arg0: str) -> list[int]:
        """subGraphForOutput(self: _apex.Graph, arg0: str) -> list[int]"""
    def subPortIndex(self, arg0: int) -> int:
        """subPortIndex(self: _apex.Graph, arg0: int) -> int"""
    def subPorts(self, arg0: int) -> list[int]:
        """subPorts(self: _apex.Graph, arg0: int) -> list[int]"""
    def unpackSubGraph(self, arg0: int) -> list[int]:
        """unpackSubGraph(self: _apex.Graph, arg0: int) -> list[int]"""
    def warnings(self) -> list[str]:
        """warnings(self: _apex.Graph) -> list[str]"""
    def wirePorts(self, arg0: int) -> tuple[int, int]:
        """wirePorts(self: _apex.Graph, arg0: int) -> tuple[int, int]"""
    @overload
    def writeToGeometry(self, py_geo: hou.Geometry, output_node_data: bool = ..., output_debug: bool = ..., preserve_generics: bool = ...) -> None:
        """writeToGeometry(*args, **kwargs)
        Overloaded function.

        1. writeToGeometry(self: _apex.Graph, py_geo: object, output_node_data: bool = False, output_debug: bool = False, preserve_generics: bool = False) -> object

        2. writeToGeometry(self: _apex.Graph, arg0: object, arg1: list[int]) -> object
        """
    @overload
    def writeToGeometry(self, arg0: hou.Geometry, arg1: Sequence[int] | IntArray) -> None:
        """writeToGeometry(*args, **kwargs)
        Overloaded function.

        1. writeToGeometry(self: _apex.Graph, py_geo: object, output_node_data: bool = False, output_debug: bool = False, preserve_generics: bool = False) -> object

        2. writeToGeometry(self: _apex.Graph, arg0: object, arg1: list[int]) -> object
        """
    def __copy__(self) -> Graph:
        """__copy__(self: _apex.Graph) -> _apex.Graph"""

class GraphDebugger:
    def __init__(self) -> None:
        """__init__(self: _apex.GraphDebugger) -> None"""
    def isValid(self) -> bool:
        """isValid(self: _apex.GraphDebugger) -> bool"""
    def next(self) -> bool:
        """next(self: _apex.GraphDebugger) -> bool"""
    def outputPattern(self) -> str:
        """outputPattern(self: _apex.GraphDebugger) -> str"""
    def resume(self) -> bool:
        """resume(self: _apex.GraphDebugger) -> bool"""
    def run(self, parms: Dict = ...) -> None:
        """run(self: _apex.GraphDebugger, parms: _apex.Dict = <apex.Dict {}>) -> None"""
    def setGraph(self, arg0: Graph) -> bool:
        """setGraph(self: _apex.GraphDebugger, arg0: _apex.Graph) -> bool"""
    def setOutputPattern(self, arg0: str) -> None:
        """setOutputPattern(self: _apex.GraphDebugger, arg0: str) -> None"""
    def setPostNodeExecuteCallback(self, arg0: Callable[[str, Dict], object]) -> None:
        """setPostNodeExecuteCallback(self: _apex.GraphDebugger, arg0: Callable[[str, _apex.Dict], None]) -> None"""
    def setPostProgramExecuteCallback(self, arg0: Callable[[Dict], object]) -> None:
        """setPostProgramExecuteCallback(self: _apex.GraphDebugger, arg0: Callable[[_apex.Dict], None]) -> None"""
    def setPreNodeExecuteCallback(self, arg0: Callable[[str, Dict], bool]) -> None:
        """setPreNodeExecuteCallback(self: _apex.GraphDebugger, arg0: Callable[[str, _apex.Dict], bool]) -> None"""
    def setPreProgramExecuteCallback(self, arg0: Callable[[Dict], object]) -> None:
        """setPreProgramExecuteCallback(self: _apex.GraphDebugger, arg0: Callable[[_apex.Dict], None]) -> None"""
    def __bool__(self) -> bool:
        """__bool__(self: _apex.GraphDebugger) -> bool"""

class GraphExecutor:
    def __init__(self) -> None:
        """__init__(self: _apex.GraphExecutor) -> None"""
    def addGraph(self, arg0: Graph) -> None:
        """addGraph(self: _apex.GraphExecutor, arg0: _apex.Graph) -> None"""
    def clear(self) -> None:
        """clear(self: _apex.GraphExecutor) -> None"""
    def compile(self) -> None:
        """compile(self: _apex.GraphExecutor) -> None"""
    def execute(self, arg0: float) -> None:
        """execute(self: _apex.GraphExecutor, arg0: float) -> None"""
    def getGraph(self, arg0: int) -> Graph:
        """getGraph(self: _apex.GraphExecutor, arg0: int) -> _apex.Graph"""

class IntArray:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.IntArray) -> None

        2. __init__(self: _apex.IntArray, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[int]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.IntArray) -> None

        2. __init__(self: _apex.IntArray, arg0: list[object]) -> None
        """
    def append(self, arg0: int) -> None:
        """append(self: _apex.IntArray, arg0: object) -> None"""
    def asList(self) -> list[int]:
        """asList(self: _apex.IntArray) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.IntArray) -> None"""
    def pop(self, arg0: int) -> int:
        """pop(self: _apex.IntArray, arg0: int) -> object"""
    def remove(self, arg0: int) -> None:
        """remove(self: _apex.IntArray, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.IntArray, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.IntArray) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> int:
        """__getitem__(self: _apex.IntArray, arg0: int) -> object"""
    def __iter__(self) -> Iterator[int]:
        """__iter__(self: _apex.IntArray) -> Iterator[int]"""
    def __len__(self) -> int:
        """__len__(self: _apex.IntArray) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: int) -> None:
        """__setitem__(self: _apex.IntArray, arg0: int, arg1: int) -> None"""

class ItemsView(Generic[_V]):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> Iterator[tuple[str, _V]]:
        """__iter__(self: _apex.ItemsView) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _apex.ItemsView) -> int"""

class KeysView:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __contains__(self, other: object) -> bool:
        """__contains__(self: _apex.KeysView, arg0: object) -> bool"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apex.KeysView) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _apex.KeysView) -> int"""

class Matrix3Array:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Matrix3Array) -> None

        2. __init__(self: _apex.Matrix3Array, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[hou.Matrix3]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Matrix3Array) -> None

        2. __init__(self: _apex.Matrix3Array, arg0: list[object]) -> None
        """
    def append(self, arg0: hou.Matrix3) -> None:
        """append(self: _apex.Matrix3Array, arg0: object) -> None"""
    def asList(self) -> list[hou.Matrix3]:
        """asList(self: _apex.Matrix3Array) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.Matrix3Array) -> None"""
    def pop(self, arg0: int) -> hou.Matrix3:
        """pop(self: _apex.Matrix3Array, arg0: int) -> object"""
    def remove(self, arg0: hou.Matrix3) -> None:
        """remove(self: _apex.Matrix3Array, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.Matrix3Array, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.Matrix3Array) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> hou.Matrix3:
        """__getitem__(self: _apex.Matrix3Array, arg0: int) -> object"""
    def __iter__(self) -> Iterator[hou.Matrix3]:
        """__iter__(self: _apex.Matrix3Array) -> Iterator[Matrix3]"""
    def __len__(self) -> int:
        """__len__(self: _apex.Matrix3Array) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: hou.Matrix3) -> None:
        """__setitem__(self: _apex.Matrix3Array, arg0: int, arg1: Matrix3) -> None"""

class Matrix4Array:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Matrix4Array) -> None

        2. __init__(self: _apex.Matrix4Array, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[hou.Matrix4]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Matrix4Array) -> None

        2. __init__(self: _apex.Matrix4Array, arg0: list[object]) -> None
        """
    def append(self, arg0: hou.Matrix4) -> None:
        """append(self: _apex.Matrix4Array, arg0: object) -> None"""
    def asList(self) -> list[hou.Matrix4]:
        """asList(self: _apex.Matrix4Array) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.Matrix4Array) -> None"""
    def pop(self, arg0: int) -> hou.Matrix4:
        """pop(self: _apex.Matrix4Array, arg0: int) -> object"""
    def remove(self, arg0: hou.Matrix4) -> None:
        """remove(self: _apex.Matrix4Array, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.Matrix4Array, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.Matrix4Array) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> hou.Matrix4:
        """__getitem__(self: _apex.Matrix4Array, arg0: int) -> object"""
    def __iter__(self) -> Iterator[hou.Matrix4]:
        """__iter__(self: _apex.Matrix4Array) -> Iterator[Matrix4]"""
    def __len__(self) -> int:
        """__len__(self: _apex.Matrix4Array) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: hou.Matrix4) -> None:
        """__setitem__(self: _apex.Matrix4Array, arg0: int, arg1: Matrix4) -> None"""

class OverloadSet:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def getCallbacks(self, filter: Signature | None = ...) -> list[str]:
        """getCallbacks(self: _apex.OverloadSet, filter: _apex.Signature = None) -> list[str]"""
    def getSignature(self, filter: Signature | None = ...) -> Signature:
        """getSignature(self: _apex.OverloadSet, filter: _apex.Signature = None) -> _apex.Signature"""

class Parm:
    name: str
    type_name: str
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Parm, arg0: str) -> None

        2. __init__(self: _apex.Parm, arg0: str, arg1: str) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Parm, arg0: str) -> None

        2. __init__(self: _apex.Parm, arg0: str, arg1: str) -> None
        """
    def freeze(self) -> Parm:
        """freeze(self: _apex.Parm) -> _apex.Parm"""
    def isInplace(self) -> bool:
        """isInplace(self: _apex.Parm) -> bool"""
    def isValid(self) -> bool:
        """isValid(self: _apex.Parm) -> bool"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _apex.Parm, arg0: _apex.Parm) -> bool"""

class Registry:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Registry) -> None

        2. __init__(self: _apex.Registry, arg0: bool) -> None
        """
    @overload
    def __init__(self, arg0: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Registry) -> None

        2. __init__(self: _apex.Registry, arg0: bool) -> None
        """
    def callbackDefinitions(self, include_ancestors: bool = ...) -> list[str]:
        """callbackDefinitions(self: _apex.Registry, include_ancestors: bool = False) -> list[str]"""
    def clearSubgraphs(self, except_geo_loaded: bool = ...) -> None:
        """clearSubgraphs(self: _apex.Registry, except_geo_loaded: bool = False) -> None"""
    def findMatchingNames(self, pattern: str, version: str = ..., include_ancestors: bool = ...) -> list[str]:
        """findMatchingNames(self: _apex.Registry, pattern: str, version: str = '', include_ancestors: bool = False) -> UT_Array[str]"""
    def getCallbackScopeConnection(self, function_name: str, include_ancestors: bool = ...) -> str:
        """getCallbackScopeConnection(self: _apex.Registry, function_name: str, include_ancestors: bool = False) -> str"""
    def getCompatibilityMap(self) -> CompatibilityMap:
        """getCompatibilityMap(self: _apex.Registry) -> _apex.CompatibilityMap"""
    def getCompatibilityResolver(self, name: str, version: str, include_ancestors: bool = ...) -> CompatibilityMap.CompatibilityResolver | None:
        """getCompatibilityResolver(self: _apex.Registry, name: str, version: str, include_ancestors: bool = False) -> _apex.CompatibilityMap.CompatibilityResolver"""
    def getDataId(self) -> int:
        """getDataId(self: _apex.Registry) -> int"""
    def getIsHidden(self, name: str, include_ancestors: bool = ...) -> bool:
        """getIsHidden(self: _apex.Registry, name: str, include_ancestors: bool = False) -> bool"""
    def getMinProductVersion(self, name: str, include_ancestors: bool = ...) -> str:
        """getMinProductVersion(self: _apex.Registry, name: str, include_ancestors: bool = False) -> str"""
    def getNamesInPrecedenceOrder(self, name: str, include_ancestors: bool = ...) -> list[str]:
        """getNamesInPrecedenceOrder(self: _apex.Registry, name: str, include_ancestors: bool = False) -> list[str]"""
    def getOverloadSet(self, name: str, include_ancestors: bool = ...) -> OverloadSet | None:
        """getOverloadSet(self: _apex.Registry, name: str, include_ancestors: bool = False) -> _apex.OverloadSet"""
    def getParmDefaults(self, name: str, include_ancestors: bool = ...) -> Dict:
        """getParmDefaults(self: _apex.Registry, name: str, include_ancestors: bool = False) -> _apex.Dict"""
    def getSignature(self, name: str, include_ancestors: bool = ...) -> Signature:
        """getSignature(self: _apex.Registry, name: str, include_ancestors: bool = False) -> _apex.Signature"""
    def getSubGraph(self, subgraph_name: str, include_ancestors: bool = ...) -> Graph:
        """getSubGraph(self: _apex.Registry, subgraph_name: str, include_ancestors: bool = False) -> _apex.Graph"""
    def getSubGraphGeo(self, subgraph_name: str, include_ancestors: bool = ...) -> hou.Geometry:
        """getSubGraphGeo(self: _apex.Registry, subgraph_name: str, include_ancestors: bool = False) -> object"""
    def getSubGraphPath(self, subgraph_name: str, include_ancestors: bool = ...) -> str:
        """getSubGraphPath(self: _apex.Registry, subgraph_name: str, include_ancestors: bool = False) -> str"""
    def latestCallbackName(self, function_name: str, include_ancestors: bool = ...) -> str:
        """latestCallbackName(self: _apex.Registry, function_name: str, include_ancestors: bool = False) -> str"""
    def loadSubGraphLibrary(self, arg0: hou.Geometry) -> bool:
        """loadSubGraphLibrary(self: _apex.Registry, arg0: object) -> bool"""
    def reloadSubgraphs(self) -> None:
        """reloadSubgraphs(self: _apex.Registry) -> None"""
    def subGraphNames(self, version: str = ..., include_ancestors: bool = ...) -> list[str]:
        """subGraphNames(self: _apex.Registry, version: str = None, include_ancestors: bool = False) -> UT_Array[str]"""
    def subGraphs(self, include_ancestors: bool = ...) -> dict[str, Graph]:
        """subGraphs(self: _apex.Registry, include_ancestors: bool = False) -> dict[str, _apex.Graph]"""

class RegistryList:
    @typing.overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.RegistryList) -> None

        2. __init__(self: _apex.RegistryList, arg0: _apex.RegistryList) -> None

        Copy constructor

        3. __init__(self: _apex.RegistryList, arg0: Iterable) -> None
        """
    @typing.overload
    def __init__(self, arg0: RegistryList) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.RegistryList) -> None

        2. __init__(self: _apex.RegistryList, arg0: _apex.RegistryList) -> None

        Copy constructor

        3. __init__(self: _apex.RegistryList, arg0: Iterable) -> None
        """
    @typing.overload
    def __init__(self, arg0: Iterable[Registry]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.RegistryList) -> None

        2. __init__(self: _apex.RegistryList, arg0: _apex.RegistryList) -> None

        Copy constructor

        3. __init__(self: _apex.RegistryList, arg0: Iterable) -> None
        """
    def append(self, x: Registry) -> None:
        """append(self: _apex.RegistryList, x: apex::APEX_Registry) -> None

        Add an item to the end of the list
        """
    def clear(self) -> None:
        """clear(self: _apex.RegistryList) -> None

        Clear the contents
        """
    def count(self, x: Registry) -> int:
        """count(self: _apex.RegistryList, x: apex::APEX_Registry) -> int

        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: RegistryList) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _apex.RegistryList, L: _apex.RegistryList) -> None

        Extend the list by appending all the items in the given list

        2. extend(self: _apex.RegistryList, L: Iterable) -> None

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: Iterable[Registry]) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _apex.RegistryList, L: _apex.RegistryList) -> None

        Extend the list by appending all the items in the given list

        2. extend(self: _apex.RegistryList, L: Iterable) -> None

        Extend the list by appending all the items in the given list
        """
    def insert(self, i: int, x: Registry) -> None:
        """insert(self: _apex.RegistryList, i: int, x: apex::APEX_Registry) -> None

        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Registry:
        """pop(*args, **kwargs)
        Overloaded function.

        1. pop(self: _apex.RegistryList) -> apex::APEX_Registry

        Remove and return the last item

        2. pop(self: _apex.RegistryList, i: int) -> apex::APEX_Registry

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Registry:
        """pop(*args, **kwargs)
        Overloaded function.

        1. pop(self: _apex.RegistryList) -> apex::APEX_Registry

        Remove and return the last item

        2. pop(self: _apex.RegistryList, i: int) -> apex::APEX_Registry

        Remove and return the item at index ``i``
        """
    def remove(self, x: Registry) -> None:
        """remove(self: _apex.RegistryList, x: apex::APEX_Registry) -> None

        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    def __bool__(self) -> bool:
        """__bool__(self: _apex.RegistryList) -> bool

        Check whether the list is nonempty
        """
    def __contains__(self, other: Registry) -> bool:
        """__contains__(self: _apex.RegistryList, x: apex::APEX_Registry) -> bool

        Return true the container contains ``x``
        """
    @overload
    def __delitem__(self, other: int) -> None:
        """__delitem__(*args, **kwargs)
        Overloaded function.

        1. __delitem__(self: _apex.RegistryList, arg0: int) -> None

        Delete the list elements at index ``i``

        2. __delitem__(self: _apex.RegistryList, arg0: slice) -> None

        Delete list elements using a slice object
        """
    @overload
    def __delitem__(self, other: slice) -> None:
        """__delitem__(*args, **kwargs)
        Overloaded function.

        1. __delitem__(self: _apex.RegistryList, arg0: int) -> None

        Delete the list elements at index ``i``

        2. __delitem__(self: _apex.RegistryList, arg0: slice) -> None

        Delete list elements using a slice object
        """
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _apex.RegistryList, arg0: _apex.RegistryList) -> bool"""
    @typing.overload
    def __getitem__(self, index: int) -> Registry:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _apex.RegistryList, s: slice) -> _apex.RegistryList

        Retrieve list elements using a slice object

        2. __getitem__(self: _apex.RegistryList, arg0: int) -> apex::APEX_Registry
        """
    @typing.overload
    def __getitem__(self, index: slice) -> RegistryList:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _apex.RegistryList, s: slice) -> _apex.RegistryList

        Retrieve list elements using a slice object

        2. __getitem__(self: _apex.RegistryList, arg0: int) -> apex::APEX_Registry
        """
    def __iter__(self) -> Iterator[Registry]:
        """__iter__(self: _apex.RegistryList) -> Iterator[apex::APEX_Registry]"""
    def __len__(self) -> int:
        """__len__(self: _apex.RegistryList) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: _apex.RegistryList, arg0: _apex.RegistryList) -> bool"""
    @typing.overload
    def __setitem__(self, index: int, object: Registry) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _apex.RegistryList, arg0: int, arg1: apex::APEX_Registry) -> None

        2. __setitem__(self: _apex.RegistryList, arg0: slice, arg1: _apex.RegistryList) -> None

        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, index: slice, object: RegistryList) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _apex.RegistryList, arg0: int, arg1: apex::APEX_Registry) -> None

        2. __setitem__(self: _apex.RegistryList, arg0: slice, arg1: _apex.RegistryList) -> None

        Assign list elements using a slice object
        """

class Signature:
    def __init__(self) -> None:
        """__init__(self: _apex.Signature) -> None"""
    def addInput(self, parm: Parm, index: int = ...) -> Parm:
        """addInput(self: _apex.Signature, parm: _apex.Parm, index: int = -1) -> _apex.Parm"""
    def addOutput(self, parm: Parm, index: int = ...) -> Parm:
        """addOutput(self: _apex.Signature, parm: _apex.Parm, index: int = -1) -> _apex.Parm"""
    def asDict(self) -> dict[str, list[Parm]]:
        """asDict(self: _apex.Signature) -> dict[str, list[_apex.Parm]]"""
    def findInput(self, arg0: str) -> tuple[int, Parm | None]:
        """findInput(self: _apex.Signature, arg0: str) -> tuple[int, object]"""
    def findInputIndex(self, arg0: str) -> int:
        """findInputIndex(self: _apex.Signature, arg0: str) -> int"""
    def findOutput(self, arg0: str) -> tuple[int, Parm | None]:
        """findOutput(self: _apex.Signature, arg0: str) -> tuple[int, object]"""
    def findOutputIndex(self, arg0: str) -> int:
        """findOutputIndex(self: _apex.Signature, arg0: str) -> int"""
    def freeze(self) -> Signature:
        """freeze(self: _apex.Signature) -> _apex.Signature"""
    def inputs(self) -> list[Parm]:
        """inputs(self: _apex.Signature) -> list[_apex.Parm]"""
    def isEmpty(self) -> bool:
        """isEmpty(self: _apex.Signature) -> bool"""
    def isGeneric(self) -> bool:
        """isGeneric(self: _apex.Signature) -> bool"""
    def outputs(self) -> list[Parm]:
        """outputs(self: _apex.Signature) -> list[_apex.Parm]"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _apex.Signature, arg0: _apex.Signature) -> bool"""

class StringArray:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.StringArray) -> None

        2. __init__(self: _apex.StringArray, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[str]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.StringArray) -> None

        2. __init__(self: _apex.StringArray, arg0: list[object]) -> None
        """
    def append(self, arg0: str) -> None:
        """append(self: _apex.StringArray, arg0: object) -> None"""
    def asList(self) -> list[str]:
        """asList(self: _apex.StringArray) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.StringArray) -> None"""
    def pop(self, arg0: int) -> str:
        """pop(self: _apex.StringArray, arg0: int) -> object"""
    def remove(self, arg0: str) -> None:
        """remove(self: _apex.StringArray, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.StringArray, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.StringArray) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> str:
        """__getitem__(self: _apex.StringArray, arg0: int) -> object"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apex.StringArray) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(self: _apex.StringArray) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: str) -> None:
        """__setitem__(self: _apex.StringArray, arg0: int, arg1: str) -> None"""

class Tags:
    def __init__(self) -> None:
        """__init__(self: _apex.Tags) -> None"""
    def items(self) -> ItemsView[str]:
        """items(self: _apex.Tags) -> _apex.ItemsView"""
    def keys(self) -> KeysView:
        """keys(self: _apex.Tags) -> _apex.KeysView"""
    def values(self) -> ValuesView[str]:
        """values(self: _apex.Tags) -> _apex.ValuesView"""
    def __bool__(self) -> bool:
        """__bool__(self: _apex.Tags) -> bool

        Check whether the map is nonempty
        """
    @overload
    def __contains__(self, other: str) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apex.Tags, arg0: str) -> bool

        2. __contains__(self: _apex.Tags, arg0: object) -> bool
        """
    @overload
    def __contains__(self, other: object) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apex.Tags, arg0: str) -> bool

        2. __contains__(self: _apex.Tags, arg0: object) -> bool
        """
    def __delitem__(self, other: str) -> None:
        """__delitem__(self: _apex.Tags, arg0: str) -> None"""
    def __getitem__(self, index: str) -> str:
        """__getitem__(self: _apex.Tags, arg0: str) -> str"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apex.Tags) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(self: _apex.Tags) -> int"""
    def __setitem__(self, index: str, object: str) -> None:
        """__setitem__(self: _apex.Tags, arg0: str, arg1: str) -> None"""

class ValuesView(Generic[_V]):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> Iterator[_V]:
        """__iter__(self: _apex.ValuesView) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _apex.ValuesView) -> int"""

class Vector2Array:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Vector2Array) -> None

        2. __init__(self: _apex.Vector2Array, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[hou.Vector2]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Vector2Array) -> None

        2. __init__(self: _apex.Vector2Array, arg0: list[object]) -> None
        """
    def append(self, arg0: hou.Vector2) -> None:
        """append(self: _apex.Vector2Array, arg0: object) -> None"""
    def asList(self) -> list[hou.Vector2]:
        """asList(self: _apex.Vector2Array) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.Vector2Array) -> None"""
    def pop(self, arg0: int) -> hou.Vector2:
        """pop(self: _apex.Vector2Array, arg0: int) -> object"""
    def remove(self, arg0: hou.Vector2) -> None:
        """remove(self: _apex.Vector2Array, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.Vector2Array, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.Vector2Array) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> hou.Vector2:
        """__getitem__(self: _apex.Vector2Array, arg0: int) -> object"""
    def __iter__(self) -> Iterator[hou.Vector2]:
        """__iter__(self: _apex.Vector2Array) -> Iterator[Vector2]"""
    def __len__(self) -> int:
        """__len__(self: _apex.Vector2Array) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: hou.Vector2) -> None:
        """__setitem__(self: _apex.Vector2Array, arg0: int, arg1: Vector2) -> None"""

class Vector3Array:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Vector3Array) -> None

        2. __init__(self: _apex.Vector3Array, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[hou.Vector3]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Vector3Array) -> None

        2. __init__(self: _apex.Vector3Array, arg0: list[object]) -> None
        """
    def append(self, arg0: hou.Vector3) -> None:
        """append(self: _apex.Vector3Array, arg0: object) -> None"""
    def asList(self) -> list[hou.Vector3]:
        """asList(self: _apex.Vector3Array) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.Vector3Array) -> None"""
    def pop(self, arg0: int) -> hou.Vector3:
        """pop(self: _apex.Vector3Array, arg0: int) -> object"""
    def remove(self, arg0: hou.Vector3) -> None:
        """remove(self: _apex.Vector3Array, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.Vector3Array, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.Vector3Array) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> hou.Vector3:
        """__getitem__(self: _apex.Vector3Array, arg0: int) -> object"""
    def __iter__(self) -> Iterator[hou.Vector3]:
        """__iter__(self: _apex.Vector3Array) -> Iterator[Vector3]"""
    def __len__(self) -> int:
        """__len__(self: _apex.Vector3Array) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: hou.Vector3) -> None:
        """__setitem__(self: _apex.Vector3Array, arg0: int, arg1: Vector3) -> None"""

class Vector4Array:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Vector4Array) -> None

        2. __init__(self: _apex.Vector4Array, arg0: list[object]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[hou.Vector4]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apex.Vector4Array) -> None

        2. __init__(self: _apex.Vector4Array, arg0: list[object]) -> None
        """
    def append(self, arg0: hou.Vector4) -> None:
        """append(self: _apex.Vector4Array, arg0: object) -> None"""
    def asList(self) -> list[hou.Vector4]:
        """asList(self: _apex.Vector4Array) -> object"""
    def clear(self) -> None:
        """clear(self: _apex.Vector4Array) -> None"""
    def pop(self, arg0: int) -> hou.Vector4:
        """pop(self: _apex.Vector4Array, arg0: int) -> object"""
    def remove(self, arg0: hou.Vector4) -> None:
        """remove(self: _apex.Vector4Array, arg0: object) -> None"""
    def setSize(self, arg0: int) -> None:
        """setSize(self: _apex.Vector4Array, arg0: int) -> None"""
    def size(self) -> int:
        """size(self: _apex.Vector4Array) -> int"""
    def __buffer__(self, flags: int, /) -> NoReturn:
        """Return a buffer object that exposes the underlying memory of the object."""
    def __getitem__(self, index: int) -> hou.Vector4:
        """__getitem__(self: _apex.Vector4Array, arg0: int) -> object"""
    def __iter__(self) -> Iterator[hou.Vector4]:
        """__iter__(self: _apex.Vector4Array) -> Iterator[Vector4]"""
    def __len__(self) -> int:
        """__len__(self: _apex.Vector4Array) -> int"""
    def __release_buffer__(self, buffer: memoryview, /) -> None:
        """Release the buffer object that exposes the underlying memory of the object."""
    def __setitem__(self, index: int, object: hou.Vector4) -> None:
        """__setitem__(self: _apex.Vector4Array, arg0: int, arg1: Vector4) -> None"""

def brushRegistry() -> Registry:
    """brushRegistry() -> _apex.Registry"""
def callbackRegistry() -> Registry:
    """callbackRegistry() -> _apex.Registry"""
def catalog(arg0: str) -> AnimationCatalog | None:
    """catalog(arg0: str) -> object"""
def clearCatalog(arg0: str) -> None:
    """clearCatalog(arg0: str) -> None"""
def componentRegistry() -> Registry:
    """componentRegistry() -> _apex.Registry"""
def constraintRegistry() -> Registry:
    """constraintRegistry() -> _apex.Registry"""
def controlRegistry() -> Registry:
    """controlRegistry() -> _apex.Registry"""
def controlTag() -> str:
    """controlTag() -> str"""
@overload
def createClipScene(arg0: hou.Geometry, arg1: hou.Geometry, arg2: str, arg3: dict[str, list[str]]) -> None:
    """createClipScene(*args, **kwargs)
    Overloaded function.

    1. createClipScene(arg0: object, arg1: object, arg2: str, arg3: dict) -> None

    2. createClipScene(arg0: object, arg1: object, arg2: str) -> None
    """
@overload
def createClipScene(arg0: hou.Geometry, arg1: hou.Geometry, arg2: str) -> None:
    """createClipScene(*args, **kwargs)
    Overloaded function.

    1. createClipScene(arg0: object, arg1: object, arg2: str, arg3: dict) -> None

    2. createClipScene(arg0: object, arg1: object, arg2: str) -> None
    """
def findFirstSkeletonJoint(arg0: hou.Geometry, arg1: str) -> int:
    """findFirstSkeletonJoint(arg0: object, arg1: str) -> int"""
def findSkeletonJoints(arg0: hou.Geometry, arg1: str) -> list[int]:
    """findSkeletonJoints(arg0: object, arg1: str) -> list[int]"""
def getRegistries() -> RegistryList:
    """getRegistries() -> _apex.RegistryList"""
def mergeAnimation(arg0: hou.Geometry, arg1: hou.Geometry, arg2: bool) -> None:
    """mergeAnimation(arg0: object, arg1: object, arg2: bool) -> None"""
def mergeSceneDelta(geo: hou.Geometry, delta: hou.Geometry, inherit_layers: bool = ...) -> None:
    """mergeSceneDelta(geo: object, delta: object, inherit_layers: bool = False) -> None"""
def packFolderMerge(arg0: hou.Geometry, arg1: hou.Geometry, arg2: str) -> None:
    """packFolderMerge(arg0: object, arg1: object, arg2: str) -> None"""
def packToFolders(py_geo: hou.Geometry, src: Dict, properties: Dict | None = ...) -> None:
    """packToFolders(py_geo: object, src: _apex.Dict, properties: object = None) -> None"""
def processRigForViewerState(arg0: Graph) -> None:
    """processRigForViewerState(arg0: _apex.Graph) -> None"""
def rootControlTag() -> str:
    """rootControlTag() -> str"""
def splitNameAndVersion(arg0: str) -> tuple[str, str]:
    """splitNameAndVersion(arg0: str) -> tuple[str, str]"""
def tagRigControls(graph: Graph, input_node_filter: str = ...) -> None:
    """tagRigControls(graph: _apex.Graph, input_node_filter: str = '*') -> None"""
def trimClip(arg0: hou.Geometry, arg1: str, arg2: float, arg3: float) -> None:
    """trimClip(arg0: object, arg1: str, arg2: float, arg3: float) -> None"""
