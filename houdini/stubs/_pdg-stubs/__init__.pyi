from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from types import ModuleType
from typing import Any, ClassVar, Generic, Literal, Never, NoReturn, NotRequired, ParamSpec, Protocol, TypeAlias, TypedDict, TypeVar, overload, type_check_only

from _typeshed import SupportsRichComparison

import _pdg
import hou
from _pdgutils import PDGNPollingClient
from pdg.dependency import PyDependency
from pdg.node import PyNode
from pdg.scheduler import PyScheduler
from pdg.workitem import PyWorkItem
import typing

_T = TypeVar("_T")
_P = ParamSpec("_P")
_R = TypeVar("_R")
_R_co = TypeVar("_R_co", covariant=True)
_NodeT = TypeVar("_NodeT", bound="Node")

# Values a pdg.Dictionary can hold.  Short numeric arrays parsed from a JSON string come back as
# float tuples (UT_Options vector types).
_DictValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | Dictionary
    | list[int]
    | list[float]
    | list[str]
    | list[Dictionary]
    | tuple[float, ...]
)
# What Dictionary.asDictionary() turns those into by default (recursive=True): nested
# Dictionaries become dicts too.
_PlainDictValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | dict[str, "_PlainDictValue"]
    | list[int]
    | list[float]
    | list[str]
    | list[dict[str, "_PlainDictValue"]]
    | tuple[float, ...]
)
# What a pdg.Dictionary takes from a python dict (which must be a dict, not another mapping):
# bytes become a list of ints, bools in a sequence ints; None, mixed sequences, sets and other
# objects are rejected (or, with skip_invalid=True, left out).
_DictArg: TypeAlias = (
    bool
    | int
    | float
    | str
    | Sequence[int]
    | Sequence[float]
    | Sequence[str]
    | Mapping[str, "_DictArg"]
    | Sequence[Mapping[str, "_DictArg"]]
)
_Attribute: TypeAlias = (
    AttributeDictionary
    | AttributeFile
    | AttributeFloat
    | AttributeGeometry
    | AttributeInt
    | AttributePyObject
    | AttributeString
)
_PortValue: TypeAlias = int | float | str | tuple[int, ...] | tuple[float, ...] | tuple[str, ...]
_EnvValue: TypeAlias = int | float | str
_DebugLevel: TypeAlias = (
    debugLevelCache
    | debugLevelExpression
    | debugLevelNode
    | debugLevelScheduler
    | debugLevelService
    | debugLevelTransfer
    | debugLevelTypeRegistration
    | debugLevelWorkItem
)
_EventCallback: TypeAlias = Callable[[Event], object] | Callable[[PyEventHandler, Event], object]
_DependencyGraph: TypeAlias = tuple[
    dict[WorkItem, list[WorkItem]], dict[WorkItem, list[WorkItem]], list[WorkItem]
]

# What pdg's python setValue/setParameter unpack: a value, or an iterable of values for the
# port's indices.
_ParmValue: TypeAlias = int | float | str | Iterable[int | float | str]

# What the sharedserver jobs report (pdgjob.pdgcmd, pdg.feedback). setSharedServerInfo stores any
# dict of simple values as given; these are the keys SideFX's code sets and reads.
class _SharedServerInfo(TypedDict):
    name: str
    pid: int
    host: str
    port: int
    proto_type: NotRequired[str]

# WorkItem.savePythonDict(): the fields that aren't set on the work item are None.
class _WorkItemBasicDict(TypedDict):
    node: Node | PyNode
    name: str
    label: str | None
    type: workItemType
    index: int
    priority: int
    batch_parent: BatchWorkItem | None
    batch_index: int | None
    state: workItemState
    cache_state: workItemCacheState | None
    dependency_state: workItemState
    failed_dependencies: ConstWorkItemList
    partition_items: ConstWorkItemList | None
    frame: float | None

class _WorkItemCookDict(TypedDict):
    type: workItemCookType
    scheduler: SchedulerBase | None
    status: str | None
    log: str | None
    progress: float | None
    python_module: str | None
    main_thread: bool | None
    service_name: str | None
    service_client: str | None
    command: str | None

class _WorkItemStatsDict(TypedDict):
    queue_time: float
    schedule_time: float
    start_time: float
    end_time: float
    cook_time: float

class _WorkItemFilesDict(TypedDict):
    inputs: list[File] | None
    outputs: list[File]
    expected_outputs: list[File]
    transfer_outputs: bool

class _WorkItemPythonDict(TypedDict):
    basic: _WorkItemBasicDict
    cook: _WorkItemCookDict
    stats: _WorkItemStatsDict
    files: _WorkItemFilesDict
import _pdg
import types
import typing
from typing import Any, Callable, ClassVar, Iterable, Iterator, overload

class ActiveItemBlock:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __enter__(self) -> WorkItem:
        """__enter__(self: _pdg.ActiveItemBlock) -> PDG_WorkItem"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdg.ActiveItemBlock, arg0: object, arg1: object, arg2: object) -> bool"""

class AddDependencyResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> Dependency: ...

class AddNodeResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> Node: ...

class AddParameterResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> Port: ...

class AddSchedulerResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> Scheduler: ...

class AttribError(Exception): ...

class AttributeConfig:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def attributeOrigins(self) -> dict[str, int]: ...
    @property
    def defaultOrigin(self) -> int: ...

class AttributeDictionary(AttributeDictionaryBase):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def clear(self) -> None:
        """clear(self: _pdg.AttributeDictionary) -> None

        Clears the contents of the attribute
        """
    @overload
    def description(self, pretty_print: bool = ...) -> str:
        """description(*args, **kwargs)
        Overloaded function.

        1. description(self: _pdg.AttributeDictionary, pretty_print: bool = False) -> object

        Returns a string description of all values in the dict array

        2. description(self: _pdg.AttributeDictionary, index: int = 0, pretty_print: bool = False) -> object

        Returns a string description of the dict array value at the specified index
        """
    @overload
    def description(self, index: int = ..., pretty_print: bool = ...) -> str:
        """description(*args, **kwargs)
        Overloaded function.

        1. description(self: _pdg.AttributeDictionary, pretty_print: bool = False) -> object

        Returns a string description of all values in the dict array

        2. description(self: _pdg.AttributeDictionary, index: int = 0, pretty_print: bool = False) -> object

        Returns a string description of the dict array value at the specified index
        """
    def importAttributes(self, pattern: AttributePattern, work_item: WorkItem, index: int = ..., overwrite: attribOverwrite = ...) -> None:
        """importAttributes(self: _pdg.AttributeDictionary, pattern: PDG_AttributePattern, work_item: PDG_WorkItem, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Imports matching attributes from the specified work item into dictionary key/values in this attribute
        """
    def mergeValue(self, dict: Dictionary, index: int = ...) -> None:
        """mergeValue(self: _pdg.AttributeDictionary, dict: UT_OptionsHolder, index: int = 0) -> None

        Merges the key/value pairs from the dictionary into this attribute at the specified index
        """
    def queryF(self, query: str, index: int = ...) -> float:
        """queryF(self: _pdg.AttributeDictionary, query: str, index: int = 0) -> float

        Queries a floating point value by recursively indexing into the dictionary values in the attribute
        """
    def queryS(self, query: str, index: int = ...) -> str:
        """queryS(self: _pdg.AttributeDictionary, query: str, index: int = 0) -> str

        Queries a string value by recursively indexing into the dictionary values in the attribute
        """
    def reduce(self, merge_op: attribMergeType, stride: int = ...) -> None:
        """reduce(self: _pdg.AttributeDictionary, merge_op: _pdg.attribMergeType, stride: int = 1) -> None

        Applies a merge operation to the data to reduce it to a single value
        """
    @overload
    def setValue(self, value: Dictionary, index: int = ...) -> None:
        """setValue(*args, **kwargs)
        Overloaded function.

        1. setValue(self: _pdg.AttributeDictionary, value: UT_OptionsHolder, index: int = 0) -> None

        Sets the value of the attribute at the specific index

        2. setValue(self: _pdg.AttributeDictionary, repr: str, index: int = 0) -> None

        Sets the value of the attribute at the specified index to a string representation of a Python dictionary
        """
    @overload
    def setValue(self, repr: str, index: int = ...) -> None:
        """setValue(*args, **kwargs)
        Overloaded function.

        1. setValue(self: _pdg.AttributeDictionary, value: UT_OptionsHolder, index: int = 0) -> None

        Sets the value of the attribute at the specific index

        2. setValue(self: _pdg.AttributeDictionary, repr: str, index: int = 0) -> None

        Sets the value of the attribute at the specified index to a string representation of a Python dictionary
        """
    def setValues(self, arg0: Sequence[Dictionary]) -> None:
        """setValues(self: _pdg.AttributeDictionary, arg0: UT_Array[UT_OptionsHolder]) -> None

        Sets the array value of the attribute
        """
    def truncate(self, arg0: int) -> None:
        """truncate(self: _pdg.AttributeDictionary, arg0: int) -> None

        Sets the array value of the attribute
        """
    def value(self, index: int = ...) -> Dictionary | None:
        """value(self: _pdg.AttributeDictionary, index: int = 0) -> object

        Returns the value of the attribute at the specified index
        """
    def __getitem__(self, index: int) -> Dictionary:
        """__getitem__(self: _pdg.AttributeDictionary, arg0: int) -> object

        Returns the value of the attribute at the specified index
        """
    def __iter__(self) -> Iterator[Dictionary]:
        """def __iter__(self) -> typing.Iterator[Any]"""
    def __setitem__(self, index: int, object: Dictionary) -> None:
        """__setitem__(self: _pdg.AttributeDictionary, arg0: int, arg1: UT_OptionsHolder) -> None

        Sets the value of the attribute at the specific index
        """
    @property
    def values(self) -> list[Dictionary]: ...

class AttributeDictionaryBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributeDictionaryBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributeDictionaryBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributeDictionaryBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributeDictionaryBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributeDictionaryBase) -> bool:
        """copyFrom(self: _pdg.AttributeDictionaryBase, arg0: _pdg.AttributeDictionaryBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeDictionaryBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeDictionaryBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeDictionaryBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeDictionaryBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributeDictionaryBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributeDictionaryBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributeDictionaryBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributeDictionaryBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributeDictionaryBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributeDictionaryBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributeDictionaryBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributeDictionaryBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeFile(AttributeFileBase):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def clear(self) -> None:
        """clear(self: _pdg.AttributeFile) -> None

        Clears the contents of the attribute
        """
    def reduce(self, merge_op: attribMergeType, stride: int = ...) -> None:
        """reduce(self: _pdg.AttributeFile, merge_op: _pdg.attribMergeType, stride: int = 1) -> None

        Applies a merge operation to the data to reduce it to a single value
        """
    def setValue(self, value: File, index: int = ...) -> None:
        """setValue(self: _pdg.AttributeFile, value: PDG_File, index: int = 0) -> None

        Sets the value of the attribute at the specific index
        """
    def setValues(self, arg0: Sequence[File]) -> None:
        """setValues(self: _pdg.AttributeFile, arg0: UT_Array[PDG_File]) -> None

        Sets the array value of the attribute
        """
    def truncate(self, arg0: int) -> None:
        """truncate(self: _pdg.AttributeFile, arg0: int) -> None

        Sets the array value of the attribute
        """
    def value(self, index: int = ...) -> File | None:
        """value(self: _pdg.AttributeFile, index: int = 0) -> object

        Returns the value of the attribute at the specified index
        """
    def valueForTag(self, index: int = ..., tag: str = ...) -> File | None:
        """valueForTag(self: _pdg.AttributeFile, index: int = 0, tag: str = '') -> object

        Returns the value in the attribute with the specified tag and index
        """
    def valuesForTag(self, tag: str = ...) -> list[File]:
        """valuesForTag(self: _pdg.AttributeFile, tag: str = '') -> object

        Returns the values in the attribute with the specified tag.
        """
    def __getitem__(self, index: int) -> File:
        """__getitem__(self: _pdg.AttributeFile, arg0: int) -> object

        Returns the value of the attribute at the specified index
        """
    def __iter__(self) -> Iterator[File]:
        """def __iter__(self) -> typing.Iterator[Any]"""
    def __setitem__(self, index: int, object: File) -> None:
        """__setitem__(self: _pdg.AttributeFile, arg0: int, arg1: PDG_File) -> None

        Sets the value of the attribute at the specific index
        """
    @property
    def values(self) -> list[File]: ...

class AttributeFileBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributeFileBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributeFileBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributeFileBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributeFileBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributeFileBase) -> bool:
        """copyFrom(self: _pdg.AttributeFileBase, arg0: _pdg.AttributeFileBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeFileBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeFileBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeFileBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeFileBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributeFileBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributeFileBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributeFileBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributeFileBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributeFileBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributeFileBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributeFileBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributeFileBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeFloat(AttributeFloatBase):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def clear(self) -> None:
        """clear(self: _pdg.AttributeFloat) -> None

        Clears the contents of the attribute
        """
    def reduce(self, merge_op: attribMergeType, stride: int = ...) -> None:
        """reduce(self: _pdg.AttributeFloat, merge_op: _pdg.attribMergeType, stride: int = 1) -> None

        Applies a merge operation to the data to reduce it to a single value
        """
    def setValue(self, value: float, index: int = ...) -> None:
        """setValue(self: _pdg.AttributeFloat, value: float, index: int = 0) -> None

        Sets the value of the attribute at the specific index
        """
    def setValues(self, arg0: Sequence[float]) -> None:
        """setValues(self: _pdg.AttributeFloat, arg0: UT_Array[float]) -> None

        Sets the array value of the attribute
        """
    def truncate(self, arg0: int) -> None:
        """truncate(self: _pdg.AttributeFloat, arg0: int) -> None

        Sets the array value of the attribute
        """
    def value(self, index: int = ...) -> float | None:
        """value(self: _pdg.AttributeFloat, index: int = 0) -> object

        Returns the value of the attribute at the specified index
        """
    def __getitem__(self, index: int) -> float:
        """__getitem__(self: _pdg.AttributeFloat, arg0: int) -> object

        Returns the value of the attribute at the specified index
        """
    def __iter__(self) -> Iterator[float]:
        """def __iter__(self) -> typing.Iterator[Any]"""
    def __setitem__(self, index: int, object: float) -> None:
        """__setitem__(self: _pdg.AttributeFloat, arg0: int, arg1: float) -> None

        Sets the value of the attribute at the specific index
        """
    @property
    def values(self) -> list[float]: ...

class AttributeFloatBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributeFloatBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributeFloatBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributeFloatBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributeFloatBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributeFloatBase) -> bool:
        """copyFrom(self: _pdg.AttributeFloatBase, arg0: _pdg.AttributeFloatBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeFloatBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeFloatBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeFloatBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeFloatBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributeFloatBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributeFloatBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributeFloatBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributeFloatBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributeFloatBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributeFloatBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributeFloatBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributeFloatBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeGeometry(AttributeGeometryBase):
    geometry: hou.Geometry
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def description(self) -> str: ...

class AttributeGeometryBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributeGeometryBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributeGeometryBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributeGeometryBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributeGeometryBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributeGeometryBase) -> bool:
        """copyFrom(self: _pdg.AttributeGeometryBase, arg0: _pdg.AttributeGeometryBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeGeometryBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeGeometryBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeGeometryBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeGeometryBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributeGeometryBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributeGeometryBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributeGeometryBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributeGeometryBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributeGeometryBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributeGeometryBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributeGeometryBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributeGeometryBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeInfo:
    InputFiles: ClassVar[str] = ...
    OutputFiles: ClassVar[str] = ...
    Version: ClassVar[int] = ...
    inputFiles: ClassVar[str] = ...
    outputFiles: ClassVar[str] = ...
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def inputAttribs(self) -> AttributeConfig: ...
    @property
    def outputAttribs(self) -> AttributeConfig: ...
    @property
    def upstreamAttribs(self) -> AttributeConfig: ...

class AttributeInt(AttributeIntBase):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asWorkItems(self, graph: Graph, include_none: bool = ...) -> list[WorkItem | None]:
        """asWorkItems(self: _pdg.AttributeInt, graph: PDG_Graph, include_none: bool = False) -> list

        Looks up a work item for each ID value in this attrib.
        """
    def clear(self) -> None:
        """clear(self: _pdg.AttributeInt) -> None

        Clears the contents of the attribute
        """
    def reduce(self, merge_op: attribMergeType, stride: int = ...) -> None:
        """reduce(self: _pdg.AttributeInt, merge_op: _pdg.attribMergeType, stride: int = 1) -> None

        Applies a merge operation to the data to reduce it to a single value
        """
    def setValue(self, value: int, index: int = ...) -> None:
        """setValue(self: _pdg.AttributeInt, value: int, index: int = 0) -> None

        Sets the value of the attribute at the specific index
        """
    def setValues(self, arg0: Sequence[int]) -> None:
        """setValues(self: _pdg.AttributeInt, arg0: UT_Array[int]) -> None

        Sets the array value of the attribute
        """
    def truncate(self, arg0: int) -> None:
        """truncate(self: _pdg.AttributeInt, arg0: int) -> None

        Sets the array value of the attribute
        """
    def value(self, index: int = ...) -> int | None:
        """value(self: _pdg.AttributeInt, index: int = 0) -> object

        Returns the value of the attribute at the specified index
        """
    def __getitem__(self, index: int) -> int:
        """__getitem__(self: _pdg.AttributeInt, arg0: int) -> object

        Returns the value of the attribute at the specified index
        """
    def __iter__(self) -> Iterator[int]:
        """def __iter__(self) -> typing.Iterator[Any]"""
    def __setitem__(self, index: int, object: int) -> None:
        """__setitem__(self: _pdg.AttributeInt, arg0: int, arg1: int) -> None

        Sets the value of the attribute at the specific index
        """
    @property
    def values(self) -> list[int]: ...

class AttributeIntBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributeIntBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributeIntBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributeIntBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributeIntBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributeIntBase) -> bool:
        """copyFrom(self: _pdg.AttributeIntBase, arg0: _pdg.AttributeIntBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeIntBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeIntBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeIntBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeIntBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributeIntBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributeIntBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributeIntBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributeIntBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributeIntBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributeIntBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributeIntBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributeIntBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeOwner:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addAttrib(self, name: str, type: _pdg.attribType, overwrite: attribOverwrite = ..., error_level: attribErrorLevel = ...) -> _Attribute:
        """addAttrib(self: _pdg.AttributeOwner, name: str, type: _pdg.attribType, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>, error_level: _pdg.attribErrorLevel = <attribErrorLevel.Error: 2>) -> object

        Creates a new attribute on the work item with specified name and
        type. If the attribute already exists and has the same type, the
        existing attribute is returned, else an exception is thrown
        """
    @overload
    def attrib(self, arg0: str) -> _Attribute | None:
        """attrib(*args, **kwargs)
        Overloaded function.

        1. attrib(self: _pdg.AttributeOwner, arg0: str) -> object

        Looks up an attribute by name

        2. attrib(self: _pdg.AttributeOwner, arg0: str, arg1: _pdg.attribType) -> object

        Looks up an attribute by name and type
        """
    @overload
    def attrib(self, arg0: str, arg1: _pdg.attribType) -> _Attribute | None:
        """attrib(*args, **kwargs)
        Overloaded function.

        1. attrib(self: _pdg.AttributeOwner, arg0: str) -> object

        Looks up an attribute by name

        2. attrib(self: _pdg.AttributeOwner, arg0: str, arg1: _pdg.attribType) -> object

        Looks up an attribute by name and type
        """
    def attribArray(self, arg0: str) -> Any:
        """attribArray(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the array value of the attribute with the specified name
        """
    @overload
    def attribHash(self, include_internal: bool = ..., include_unowned: bool = ..., only_static: bool = ...) -> int:
        """attribHash(*args, **kwargs)
        Overloaded function.

        1. attribHash(self: _pdg.AttributeOwner, include_internal: bool = True, include_unowned: bool = True, only_static: bool = False) -> int

        Returns a hash of attribute values, optionally including internal attributes

        2. attribHash(self: _pdg.AttributeOwner, filter: UT_Set[str], include_internal: bool = True, include_unowned: bool = True, only_static: bool = False) -> int

        Returns a hash of attribute values, optionally including internal attributes
        """
    @overload
    def attribHash(self, filter: Sequence[str], include_internal: bool = ..., include_unowned: bool = ..., only_static: bool = ...) -> int:
        """attribHash(*args, **kwargs)
        Overloaded function.

        1. attribHash(self: _pdg.AttributeOwner, include_internal: bool = True, include_unowned: bool = True, only_static: bool = False) -> int

        Returns a hash of attribute values, optionally including internal attributes

        2. attribHash(self: _pdg.AttributeOwner, filter: UT_Set[str], include_internal: bool = True, include_unowned: bool = True, only_static: bool = False) -> int

        Returns a hash of attribute values, optionally including internal attributes
        """
    def attribMatch(self, arg0: AttributePattern) -> list[str]:
        """attribMatch(self: _pdg.AttributeOwner, arg0: PDG_AttributePattern) -> object

        Returns the set of attribute names that match the input pattern

        """
    def attribNames(self, type: _pdg.attribType = ...) -> list[str]:
        """attribNames(self: _pdg.AttributeOwner, type: _pdg.attribType = <attribType.Undefined: -1>) -> object

        The set of attributes names currently stored on the work item.
        """
    def attribType(self, arg0: str) -> _pdg.attribType:
        """attribType(self: _pdg.AttributeOwner, arg0: str) -> _pdg.attribType

        Returns the type of the attribute with the specified name, or
        pdg.attributeType.Undefined if there is no attribute with that
        name on the work item
        """
    def attribValue(self, name: str, index: int = ...) -> Any:
        """attribValue(self: _pdg.AttributeOwner, name: str, index: int = 0) -> object

        Returns the value of the attribute with the specified name/index
        """
    def attribValues(self, type: _pdg.attribType = ...) -> (
        dict[str, int | float | str]
        | dict[str, list[int]]
        | dict[str, list[float]]
        | dict[str, list[str]]
        | dict[str, list[File]]
        | None
    ):
        """attribValues(self: _pdg.AttributeOwner, type: _pdg.attribType = <attribType.Undefined: -1>) -> object

        Looks up the map of name -> value for all attributes on the
        work item.
        """
    @overload
    def clearAttribs(self, arg0: _pdg.attribType) -> None:
        """clearAttribs(*args, **kwargs)
        Overloaded function.

        1. clearAttribs(self: _pdg.AttributeOwner, arg0: _pdg.attribType) -> None

        Clears all attributes of the specified type

        2. clearAttribs(self: _pdg.AttributeOwner) -> None

        Clears all attributes on the work item
        """
    @overload
    def clearAttribs(self) -> None:
        """clearAttribs(*args, **kwargs)
        Overloaded function.

        1. clearAttribs(self: _pdg.AttributeOwner, arg0: _pdg.attribType) -> None

        Clears all attributes of the specified type

        2. clearAttribs(self: _pdg.AttributeOwner) -> None

        Clears all attributes on the work item
        """
    def dictAttribArray(self, arg0: str) -> list[Dictionary] | None:
        """dictAttribArray(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the array value of the dict attribute with the
        specified name
        """
    def dictAttribValue(self, name: str, index: int = ...) -> Dictionary | None:
        """dictAttribValue(self: _pdg.AttributeOwner, name: str, index: int = 0) -> object

        Returns the value of the dict attribute with the specified
        name/index
        """
    def eraseAttrib(self, arg0: str) -> None:
        """eraseAttrib(self: _pdg.AttributeOwner, arg0: str) -> None

        Erases an attribute with the specified name
        """
    def fileAttribArray(self, arg0: str) -> list[File] | None:
        """fileAttribArray(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the array value of the file attribute with the
        specified name
        """
    def fileAttribValue(self, name: str, index: int = ...) -> File | None:
        """fileAttribValue(self: _pdg.AttributeOwner, name: str, index: int = 0) -> object

        Returns the value of the file attribute with the specified
        name/index
        """
    def floatAttribArray(self, arg0: str) -> list[float] | None:
        """floatAttribArray(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the array value of the float attribute with the
        specified name
        """
    def floatAttribValue(self, name: str, index: int = ...) -> float | None:
        """floatAttribValue(self: _pdg.AttributeOwner, name: str, index: int = 0) -> object

        Returns the value of the float attribute with the specified
        name/index
        """
    def geometryAttribValue(self, arg0: str) -> hou.Geometry | None:
        """geometryAttribValue(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the value of the geometry attribute with the specified
        name
        """
    def hasAttrib(self, arg0: str) -> bool:
        """hasAttrib(self: _pdg.AttributeOwner, arg0: str) -> bool

        Returns True if the work item has an attribute with the specified
        name, else returns False
        """
    def intAttribArray(self, arg0: str) -> list[int] | None:
        """intAttribArray(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the array value of the integer attribute with the
        specified name
        """
    def intAttribValue(self, name: str, index: int = ...) -> int | None:
        """intAttribValue(self: _pdg.AttributeOwner, name: str, index: int = 0) -> object

        Returns the value of the integer attribute with the specified
        name/index
        """
    def loadAttributes(self, arg0: str, arg1: attribCollisionStrategy) -> bool:
        """loadAttributes(self: _pdg.AttributeOwner, arg0: str, arg1: _pdg.attribCollisionStrategy) -> bool

        Loads attributes from a file in the JSON format
        """
    def lockAttributes(self, read: bool = ...) -> LockAttributesBlock:
        """lockAttributes(self: _pdg.AttributeOwner, read: bool = False) -> _pdg.LockAttributesBlock

        Locks the attributes of this work item. This is only needed when
        modifying a work item outside of a node callback, which will
        already ensure safe access to the work item.
        """
    def numAttribs(self, type: _pdg.attribType = ...) -> int:
        """numAttribs(self: _pdg.AttributeOwner, type: _pdg.attribType = <attribType.Undefined: -1>) -> int

        Returns the total number of attributes
        """
    def pyObjectAttribValue(self, arg0: str) -> Any:
        """pyObjectAttribValue(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the value of the PyObject attribute with the specified
        name
        """
    def renameAttrib(self, src_name: str, dst_name: str, overwrite_existing: bool = ...) -> None:
        """renameAttrib(self: _pdg.AttributeOwner, src_name: str, dst_name: str, overwrite_existing: bool = False) -> None

        Renames the specified attribute to a different name
        """
    def saveAttributes(self, arg0: str) -> bool:
        """saveAttributes(self: _pdg.AttributeOwner, arg0: str) -> bool

        Saves attributes to a file in the JSON format
        """
    def setAttribFlag(self, name: str, flag: attribFlag, value: bool = ...) -> None:
        """setAttribFlag(self: _pdg.AttributeOwner, name: str, flag: _pdg.attribFlag, value: bool = True) -> None

        Sets the flag on the specified attribute
        """
    @overload
    def setDictAttrib(self, name: str, value: Dictionary | Mapping[str, _DictArg], index: int = ..., overwrite: attribOverwrite = ...) -> None:
        """setDictAttrib(*args, **kwargs)
        Overloaded function.

        1. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: UT_OptionsHolder, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dictionary attribute value at the specified index. If
        the attribute not exist, it will be created

        2. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: dict, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dictionary attribute value at the specified index. If
        the attribute not exist, it will be created

        3. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[UT_OptionsHolder], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dict attribute array value. If the
        attribute does not exist, it will be created

        4. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[dict], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dict attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setDictAttrib(self, name: str, value: Sequence[Dictionary] | Sequence[Mapping[str, _DictArg]], overwrite: attribOverwrite = ...) -> None:
        """setDictAttrib(*args, **kwargs)
        Overloaded function.

        1. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: UT_OptionsHolder, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dictionary attribute value at the specified index. If
        the attribute not exist, it will be created

        2. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: dict, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dictionary attribute value at the specified index. If
        the attribute not exist, it will be created

        3. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[UT_OptionsHolder], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dict attribute array value. If the
        attribute does not exist, it will be created

        4. setDictAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[dict], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a dict attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setFileAttrib(self, name: str, value: File, index: int = ..., overwrite: attribOverwrite = ...) -> None:
        """setFileAttrib(*args, **kwargs)
        Overloaded function.

        1. setFileAttrib(self: _pdg.AttributeOwner, name: str, value: PDG_File, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a file attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setFileAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[PDG_File], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a file attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setFileAttrib(self, name: str, value: Sequence[File], overwrite: attribOverwrite = ...) -> None:
        """setFileAttrib(*args, **kwargs)
        Overloaded function.

        1. setFileAttrib(self: _pdg.AttributeOwner, name: str, value: PDG_File, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a file attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setFileAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[PDG_File], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a file attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setFloatAttrib(self, name: str, value: float, index: int = ..., overwrite: attribOverwrite = ...) -> None:
        """setFloatAttrib(*args, **kwargs)
        Overloaded function.

        1. setFloatAttrib(self: _pdg.AttributeOwner, name: str, value: float, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a float attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setFloatAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[float], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a float attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setFloatAttrib(self, name: str, value: Sequence[float], overwrite: attribOverwrite = ...) -> None:
        """setFloatAttrib(*args, **kwargs)
        Overloaded function.

        1. setFloatAttrib(self: _pdg.AttributeOwner, name: str, value: float, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a float attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setFloatAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[float], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a float attribute array value. If the
        attribute does not exist, it will be created
        """
    def setGeometryAttrib(self, name: str, geometry: hou.Geometry, overwrite: attribOverwrite = ...) -> None:
        """setGeometryAttrib(self: _pdg.AttributeOwner, name: str, geometry: object, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a geometry attribute value. If the attribute not exist,
        it will be created
        """
    @overload
    def setIntAttrib(self, name: str, value: int, index: int = ..., overwrite: attribOverwrite = ...) -> None:
        """setIntAttrib(*args, **kwargs)
        Overloaded function.

        1. setIntAttrib(self: _pdg.AttributeOwner, name: str, value: int, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets an integer attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setIntAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[int], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets an integer attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setIntAttrib(self, name: str, value: Sequence[int], overwrite: attribOverwrite = ...) -> None:
        """setIntAttrib(*args, **kwargs)
        Overloaded function.

        1. setIntAttrib(self: _pdg.AttributeOwner, name: str, value: int, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets an integer attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setIntAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[int], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets an integer attribute array value. If the
        attribute does not exist, it will be created
        """
    def setPyObjectAttrib(self, name: str, object: object, overwrite: attribOverwrite = ...) -> None:
        """setPyObjectAttrib(self: _pdg.AttributeOwner, name: str, object: object, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a python object attribute value. If the attribute not
        exist, it will be created
        """
    @overload
    def setStringAttrib(self, name: str, value: str, index: int = ..., overwrite: attribOverwrite = ...) -> None:
        """setStringAttrib(*args, **kwargs)
        Overloaded function.

        1. setStringAttrib(self: _pdg.AttributeOwner, name: str, value: str, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a string attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setStringAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[str], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a string attribute array value. If the
        attribute does not exist, it will be created
        """
    @overload
    def setStringAttrib(self, name: str, value: Sequence[str], overwrite: attribOverwrite = ...) -> None:
        """setStringAttrib(*args, **kwargs)
        Overloaded function.

        1. setStringAttrib(self: _pdg.AttributeOwner, name: str, value: str, index: int = 0, overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a string attribute value at the specified index. If the
        attribute does not exist, it will be created

        2. setStringAttrib(self: _pdg.AttributeOwner, name: str, value: UT_Array[str], overwrite: _pdg.attribOverwrite = <attribOverwrite.Match: 1>) -> None

        Sets a string attribute array value. If the
        attribute does not exist, it will be created
        """
    def stringAttribArray(self, arg0: str) -> list[str] | None:
        """stringAttribArray(self: _pdg.AttributeOwner, arg0: str) -> object

        Returns the array value of the string attribute with the
        specified name
        """
    def stringAttribValue(self, name: str, index: int = ...) -> str | None:
        """stringAttribValue(self: _pdg.AttributeOwner, name: str, index: int = 0) -> object

        Returns the value of the string attribute with the specified
        name/index
        """
    def timeDependentAttribs(self) -> list[str]:
        """timeDependentAttribs(self: _pdg.AttributeOwner) -> object

        Returns the set of time dependents attributes, if the work item
        is in a batch
        """
    def __getitem__(self, index: str) -> _Attribute:
        """__getitem__(self: _pdg.AttributeOwner, arg0: str) -> object

        Looks up an attribute by name
        """
    def __iter__(self) -> NoReturn:
        """__iter__(self: _pdg.AttributeOwner) -> object"""

class AttributePattern(BasePattern):
    def __init__(self, pattern: str, default_match_type: attribMatchType = ..., strict: bool = ..., delimiters: str = ...) -> None:
        """__init__(self: _pdg.AttributePattern, pattern: str, default_match_type: _pdg.attribMatchType = <attribMatchType.Plain: 4>, strict: bool = True, delimiters: str = ' \\t\\n\\r') -> None

        Returns a new pattern object from the specified string
        """
    def components(self, attribute: str, type: attribType = ...) -> tuple[str, str, str] | None:
        """components(self: _pdg.AttributePattern, attribute: str, type: _pdg.attribType = <attribType.Undefined: -1>) -> object

        Returns a tuple of match components if the string name + type
        match the pattern
        """
    def contains(self, attribute: str, type: attribType = ...) -> bool:
        """contains(self: _pdg.AttributePattern, attribute: str, type: _pdg.attribType = <attribType.Undefined: -1>) -> bool

        Returns true if the specified attribute string name + type are
        a match with the pattern
        """
    @staticmethod
    def isValidName(name: str, allow_internal: bool = ...) -> bool:
        """isValidName(name: str, allow_internal: bool = False) -> bool

        Returns true if the specified name is a valid attribute name
        """
    @staticmethod
    def makeValidName(arg0: str) -> str:
        """makeValidName(arg0: str) -> str

        Converts the input name to a valid attribute name by replacing
        invalid characters with an '_'
        """
    def multiComponents(self, input_names: Sequence[str] = ..., keep_plain: bool = ...) -> dict[str, tuple[str, str, str]]:
        """multiComponents(self: _pdg.AttributePattern, input_names: UT_Array[str] = [], keep_plain: bool = False) -> object

        Applies the pattern to a list of input names and returns a mapof matching name to component tuple
        """
    def multiMatch(self, input_names: Sequence[str] = ..., keep_plain: bool = ...) -> list[str]:
        """multiMatch(self: _pdg.AttributePattern, input_names: UT_Array[str] = [], keep_plain: bool = False) -> object

        Applies the pattern to a list of input names
        """

class AttributePyObject(AttributePyObjectBase):
    object: Any
    def __init__(self, *, no_constructor: Never) -> None: ...
    def queryF(self, arg0: str, arg1: int) -> float:
        """queryF(self: _pdg.AttributePyObject, arg0: str, arg1: int) -> float

        Makes a query against the nested array/dictionary stored in the
        Python object, and returns a float value
        """
    def queryP(self, arg0: str) -> Any:
        """queryP(self: _pdg.AttributePyObject, arg0: str) -> object

        Makes a query against the nested array/dictionary stored in the
        Pytohn object, and returns a py object value
        """
    def queryS(self, arg0: str, arg1: int) -> str:
        """queryS(self: _pdg.AttributePyObject, arg0: str, arg1: int) -> str

        Makes a query against the nested array/dictionary stored in the
        Python object, and returns a string value
        """
    def setLiteral(self, literal: str) -> None:
        """setLiteral(self: _pdg.AttributePyObject, literal: str) -> None

        Sets the object to a string containing Python literals
        """
    def setValue(self, object: object, index: int = ...) -> None:
        """setValue(self: _pdg.AttributePyObject, object: object, index: int = 0) -> None

        Sets the value of the attribute. The index is ignored for this type.
        """
    def setValues(self, arg0: object) -> None:
        """setValues(self: _pdg.AttributePyObject, arg0: object) -> None

        Sets the value of the attribute. The index is ignored for this type.
        """
    def value(self, index: int = ...) -> Any:
        """value(self: _pdg.AttributePyObject, index: int = 0) -> object

        Returns the Py Object stored in the attribute
        """
    @property
    def values(self) -> Any: ...

class AttributePyObjectBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributePyObjectBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributePyObjectBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributePyObjectBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributePyObjectBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributePyObjectBase) -> bool:
        """copyFrom(self: _pdg.AttributePyObjectBase, arg0: _pdg.AttributePyObjectBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributePyObjectBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributePyObjectBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributePyObjectBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributePyObjectBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributePyObjectBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributePyObjectBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributePyObjectBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributePyObjectBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributePyObjectBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributePyObjectBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributePyObjectBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributePyObjectBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeSplit:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def batchByFrame(arg0: Sequence[WorkItem] | ConstWorkItemList | WorkItemList) -> tuple[list[list[WorkItem]], list[WorkItem]]:
        """batchByFrame(arg0: UT_Array[PDG_WorkItem]) -> object

        [deprecated] Use pdg.FrameUtils.batchByFrame instead
        """
    @staticmethod
    def splitByAttribute(arg0: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, arg1: str, arg2: bool) -> tuple[dict[str, list[WorkItem]], list[WorkItem], list[str]]:
        """splitByAttribute(arg0: UT_Array[PDG_WorkItem], arg1: str, arg2: bool) -> object

        Splits the input work item list by the specified attribute.
        """
    @staticmethod
    def splitByFloat(arg0: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, arg1: str) -> tuple[dict[float, list[WorkItem]], list[WorkItem], list[float]]:
        """splitByFloat(arg0: UT_Array[PDG_WorkItem], arg1: str) -> object

        Splits the input work item list by the specified float attribute
        """
    @staticmethod
    def splitByInt(arg0: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, arg1: str) -> tuple[dict[int, list[WorkItem]], list[WorkItem], list[int]]:
        """splitByInt(arg0: UT_Array[PDG_WorkItem], arg1: str) -> object

        Splits the input work item list by the specified int attribute
        """
    @staticmethod
    def splitByString(arg0: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, arg1: str) -> tuple[dict[str, list[WorkItem]], list[WorkItem], list[str]]:
        """splitByString(arg0: UT_Array[PDG_WorkItem], arg1: str) -> object

        Splits the input work item list by the specified string attribute
        """

class AttributeString(AttributeStringBase):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def clear(self) -> None:
        """clear(self: _pdg.AttributeString) -> None

        Clears the contents of the attribute
        """
    def reduce(self, merge_op: attribMergeType, stride: int = ...) -> None:
        """reduce(self: _pdg.AttributeString, merge_op: _pdg.attribMergeType, stride: int = 1) -> None

        Applies a merge operation to the data to reduce it to a single value
        """
    def setValue(self, value: str, index: int = ...) -> None:
        """setValue(self: _pdg.AttributeString, value: str, index: int = 0) -> None

        Sets the value of the attribute at the specific index
        """
    def setValues(self, arg0: Sequence[str]) -> None:
        """setValues(self: _pdg.AttributeString, arg0: UT_Array[str]) -> None

        Sets the array value of the attribute
        """
    def truncate(self, arg0: int) -> None:
        """truncate(self: _pdg.AttributeString, arg0: int) -> None

        Sets the array value of the attribute
        """
    def value(self, index: int = ...) -> str | None:
        """value(self: _pdg.AttributeString, index: int = 0) -> object

        Returns the value of the attribute at the specified index
        """
    def __getitem__(self, index: int) -> str:
        """__getitem__(self: _pdg.AttributeString, arg0: int) -> object

        Returns the value of the attribute at the specified index
        """
    def __iter__(self) -> Iterator[str]:
        """def __iter__(self) -> typing.Iterator[Any]"""
    def __setitem__(self, index: int, object: str) -> None:
        """__setitem__(self: _pdg.AttributeString, arg0: int, arg1: str) -> None

        Sets the value of the attribute at the specific index
        """
    @property
    def values(self) -> list[str]: ...

class AttributeStringBase:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def asFile(self, index: int = ..., tag: str = ..., hash: int = ..., own: bool = ...) -> File:
        """asFile(self: _pdg.AttributeStringBase, index: int = 0, tag: str = '', hash: int = 0, own: bool = False) -> PDG_File

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asNumber(self, index: int = ...) -> float:
        """asNumber(self: _pdg.AttributeStringBase, index: int = 0) -> float

        Casts the value of the attribute at the specified index to a
        numeric value.
        """
    def asString(self, index: int = ...) -> str:
        """asString(self: _pdg.AttributeStringBase, index: int = 0) -> str

        Casts the value of the attribute at the specified index to a
        string value.
        """
    def asValues(self) -> str:
        """asValues(self: _pdg.AttributeStringBase) -> str

        Casts the values of attribute to space-separated string of values

        """
    def copyFrom(self, arg0: AttributeStringBase) -> bool:
        """copyFrom(self: _pdg.AttributeStringBase, arg0: _pdg.AttributeStringBase) -> bool

        Copies the value from another attribute into this one
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, overwrite_existing: bool = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeStringBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeStringBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    @overload
    def copyTo(self, attrib_owner: AttributeOwner, copy_type: attribCopyType = ..., deep_copy: bool = ...) -> bool:
        """copyTo(*args, **kwargs)
        Overloaded function.

        1. copyTo(self: _pdg.AttributeStringBase, attrib_owner: PDG_AttributeOwner, overwrite_existing: bool = True, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item

        2. copyTo(self: _pdg.AttributeStringBase, attrib_owner: PDG_AttributeOwner, copy_type: _pdg.attribCopyType = <attribCopyType.Overwrite: 2>, deep_copy: bool = False) -> bool

        Copies this attribute onto the specified work item
        """
    def hasAnyFlags(self, arg0: int) -> bool:
        """hasAnyFlags(self: _pdg.AttributeStringBase, arg0: int) -> bool

        Returns True if the attribute has any of the specified flags, 
        else false.
        """
    def hasFlag(self, arg0: attribFlag) -> bool:
        """hasFlag(self: _pdg.AttributeStringBase, arg0: _pdg.attribFlag) -> bool

        Returns True if the attribute has the specified flag, else false.
        """
    def hasFlags(self, arg0: int) -> bool:
        """hasFlags(self: _pdg.AttributeStringBase, arg0: int) -> bool

        Returns True if the attribute has the specified flags, else false.
        """
    def hash(self, value_index: int = ..., include_value: bool = ..., include_name: bool = ..., include_flags: bool = ...) -> int:
        """hash(self: _pdg.AttributeStringBase, value_index: int = -1, include_value: bool = True, include_name: bool = True, include_flags: bool = True) -> int

        Returns a hash of the attribute
        """
    @staticmethod
    def isValidName(arg0: str) -> bool:
        """isValidName(arg0: str) -> bool

        Returns true if the specified string is a valid attribute name.
        """
    def match(self, arg0: AttributePattern) -> bool:
        """match(self: _pdg.AttributeStringBase, arg0: PDG_AttributePattern) -> bool

        Return true if this attribute matches the
        specified pattern
        """
    def setFlag(self, flag: attribFlag, value: bool = ...) -> bool:
        """setFlag(self: _pdg.AttributeStringBase, flag: _pdg.attribFlag, value: bool = True) -> bool

        Sets the state of the specified flag to True or False
        """
    def setFlags(self, arg0: int) -> bool:
        """setFlags(self: _pdg.AttributeStringBase, arg0: int) -> bool

        Sets the flags to the specified bit pattern
        """
    def __len__(self) -> int:
        """__len__(self: _pdg.AttributeStringBase) -> int

        The length of the array stored by the attribute
        """
    @property
    def flags(self) -> int: ...
    @property
    def hasData(self) -> bool: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def isOwner(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> AttributeOwner: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> attribType: ...

class AttributeUtils:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def ignoreWarnings() -> IgnoreAttributeWarningsBlock:
        """ignoreWarnings() -> _pdg.IgnoreAttributeWarningsBlock"""

class BasePattern:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def errors(self) -> str: ...
    @property
    def isValid(self) -> bool: ...
    @property
    def pattern(self) -> str: ...

class BaseType:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def instanceCount(self) -> int: ...
    @property
    def instanceMemoryUsage(self) -> int: ...
    @property
    def isPrivate(self) -> bool: ...
    @property
    def language(self) -> _pdg.language: ...
    @property
    def typeLabel(self) -> str: ...
    @property
    def typeName(self) -> str: ...

class BaseTypeRegistry:
    def __init__(self, *, no_constructor: Never) -> None: ...

class BatchWorkItem(WorkItem):
    activationCount: int
    activationMode: batchActivation
    def __init__(self, *, no_constructor: Never) -> None: ...
    def appendSubItem(self) -> WorkItem:
        """appendSubItem(self: _pdg.BatchWorkItem) -> _pdg.WorkItem

        Appends a new item to the batch dynamically
        """
    def setActiveBatchIndex(self, arg0: int) -> WorkItem:
        """setActiveBatchIndex(self: _pdg.BatchWorkItem, arg0: int) -> _pdg.WorkItem

        Sets the active batch index while cooking
        """
    @property
    def activeBatchItem(self) -> WorkItem: ...
    @property
    def batchItems(self) -> list[WorkItem]: ...
    @property
    def batchName(self) -> str: ...
    @property
    def batchSize(self) -> int: ...
    @property
    def batchStart(self) -> int: ...
    @property
    def isDynamicBatch(self) -> bool: ...
    @property
    def offset(self) -> int: ...

class Command:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def description(self) -> str: ...
    @property
    def done(self) -> bool: ...

class CommandChunk(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...

class ConnectResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> tuple[Port, Port]: ...

class ConstWorkItemList:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def append(self, arg0: WorkItem) -> None:
        """append(self: _pdg.ConstWorkItemList, arg0: PDG_WorkItem) -> None"""
    def count(self, arg0: WorkItem) -> int:
        """count(self: _pdg.ConstWorkItemList, arg0: PDG_WorkItem) -> int"""
    @overload
    def extend(self, arg0: Sequence[WorkItem]) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _pdg.ConstWorkItemList, arg0: UT_Array[PDG_WorkItem]) -> None

        2. extend(self: _pdg.ConstWorkItemList, arg0: _pdg.ConstWorkItemList) -> None

        3. extend(self: _pdg.ConstWorkItemList, arg0: Iterable) -> None
        """
    @overload
    def extend(self, arg0: ConstWorkItemList) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _pdg.ConstWorkItemList, arg0: UT_Array[PDG_WorkItem]) -> None

        2. extend(self: _pdg.ConstWorkItemList, arg0: _pdg.ConstWorkItemList) -> None

        3. extend(self: _pdg.ConstWorkItemList, arg0: Iterable) -> None
        """
    @overload
    def extend(self, arg0: Iterable[WorkItem]) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _pdg.ConstWorkItemList, arg0: UT_Array[PDG_WorkItem]) -> None

        2. extend(self: _pdg.ConstWorkItemList, arg0: _pdg.ConstWorkItemList) -> None

        3. extend(self: _pdg.ConstWorkItemList, arg0: Iterable) -> None
        """
    def index(self, element: WorkItem, start: int = ..., stop: int = ...) -> int:
        """index(self: _pdg.ConstWorkItemList, element: PDG_WorkItem, start: int = 0, stop: int = -1) -> int"""
    def insert(self, arg0: int, arg1: WorkItem) -> None:
        """insert(self: _pdg.ConstWorkItemList, arg0: int, arg1: PDG_WorkItem) -> None"""
    def pop(self, index: int = ...) -> WorkItem:
        """pop(self: _pdg.ConstWorkItemList, index: int = -1) -> object"""
    def remove(self, arg0: WorkItem) -> None:
        """remove(self: _pdg.ConstWorkItemList, arg0: PDG_WorkItem) -> None"""
    def reverse(self) -> None:
        """reverse(self: _pdg.ConstWorkItemList) -> None"""
    def sort(self, key: Callable[[WorkItem], SupportsRichComparison] = ..., reverse: bool = ...) -> None:
        """sort(self: _pdg.ConstWorkItemList, key: Callable = None, reverse: bool = False) -> None"""
    def __bool__(self) -> bool:
        """__bool__(self: _pdg.ConstWorkItemList) -> bool"""
    def __delitem__(self, other: int) -> None:
        """__delitem__(self: _pdg.ConstWorkItemList, arg0: int) -> None"""
    @overload
    def __getitem__(self, index: int) -> WorkItem:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _pdg.ConstWorkItemList, arg0: int) -> PDG_WorkItem

        2. __getitem__(self: _pdg.ConstWorkItemList, arg0: slice) -> list
        """
    @overload
    def __getitem__(self, index: slice) -> list[WorkItem]:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _pdg.ConstWorkItemList, arg0: int) -> PDG_WorkItem

        2. __getitem__(self: _pdg.ConstWorkItemList, arg0: slice) -> list
        """
    def __iter__(self) -> Iterator[WorkItem]:
        """__iter__(self: _pdg.ConstWorkItemList) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _pdg.ConstWorkItemList) -> int"""
    @overload
    def __setitem__(self, index: int, object: WorkItem) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.ConstWorkItemList, arg0: int, arg1: PDG_WorkItem) -> None

        2. __setitem__(self: _pdg.ConstWorkItemList, arg0: slice, arg1: UT_Array[PDG_WorkItem]) -> None

        3. __setitem__(self: _pdg.ConstWorkItemList, arg0: slice, arg1: _pdg.ConstWorkItemList) -> None
        """
    @overload
    def __setitem__(self, index: slice, object: Sequence[WorkItem]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.ConstWorkItemList, arg0: int, arg1: PDG_WorkItem) -> None

        2. __setitem__(self: _pdg.ConstWorkItemList, arg0: slice, arg1: UT_Array[PDG_WorkItem]) -> None

        3. __setitem__(self: _pdg.ConstWorkItemList, arg0: slice, arg1: _pdg.ConstWorkItemList) -> None
        """
    @overload
    def __setitem__(self, index: slice, object: ConstWorkItemList) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.ConstWorkItemList, arg0: int, arg1: PDG_WorkItem) -> None

        2. __setitem__(self: _pdg.ConstWorkItemList, arg0: slice, arg1: UT_Array[PDG_WorkItem]) -> None

        3. __setitem__(self: _pdg.ConstWorkItemList, arg0: slice, arg1: _pdg.ConstWorkItemList) -> None
        """

class CookError(Exception): ...

class CookOptions(EvaluationOptions):
    checkpointPath: str
    checkpointRate: int
    checkpointingEnabled: bool
    cookTime: float
    cookType: _pdg.cookType
    nodeNames: list[str]
    saveScene: bool
    staticFilter: Filter
    def __init__(self) -> None:
        """__init__(self: _pdg.CookOptions) -> None

        Constructs a new cook options instance
        """

class DeferredTask:
    def __init__(self, *, no_constructor: Never) -> None: ...

class DeleteResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class Dependency(TypeInstance):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def key(self) -> str: ...
    @property
    def nodes(self) -> list[Node]: ...

class DependencyHolder:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addDependency(self, arg0: WorkItem, arg1: WorkItem) -> None:
        """addDependency(self: _pdg.DependencyHolder, arg0: PDG_WorkItem, arg1: PDG_WorkItem) -> None

        Adds a dependency pair to the holder
        """

class DependencyType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...

class Dictionary:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    @typing.overload
    def __init__(
        self, dict: Mapping[str, _DictArg], skip_invalid: bool = ..., default_array_type: attribType = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self, dict: Mapping[str, object], skip_invalid: Literal[True], default_array_type: attribType = ...
    ) -> None: ...
    @typing.overload
    def asDictionary(self, recursive: Literal[True] = ...) -> dict[str, _PlainDictValue]: ...
    @typing.overload
    def asDictionary(self, recursive: Literal[False]) -> dict[str, _DictValue]: ...
    @typing.overload
    def asDictionary(self, recursive: bool = ...) -> dict[str, _PlainDictValue] | dict[str, _DictValue]: ...
    def clear(self) -> None:
        """clear(self: _pdg.Dictionary) -> None

        Clears all key/values pairs in the dictionary
        """
    @typing.overload
    def fromDictionary(
        self,
        dict: Mapping[str, _DictArg],
        clear: bool = ...,
        skip_invalid: bool = ...,
        default_array_type: attribType = ...,
    ) -> None: ...
    @typing.overload
    def fromDictionary(
        self,
        dict: Mapping[str, object],
        clear: bool = ...,
        *,
        skip_invalid: Literal[True],
        default_array_type: attribType = ...,
    ) -> None: ...
    def fromString(self, string: str, clear: bool = ...) -> None:
        """fromString(self: _pdg.Dictionary, string: str, clear: bool = True) -> None

        Merges or replaces the contents of this dictionary with the input string representation of a Python dict
        """
    def get(self, key: str, default: _T | None = ...) -> _DictValue | _T | None:
        """get(self: _pdg.Dictionary, key: str, default: object = None) -> object

        Looks up an entry in the dictionary by key
        """
    def items(self) -> _DictionaryItemView:
        """items(self: _pdg.Dictionary) -> _pdg._DictionaryItemView

        Returns a view into the items in the dictionary
        """
    def keys(self) -> _DictionaryKeyView:
        """keys(self: _pdg.Dictionary) -> _pdg._DictionaryKeyView

        Returns a view into the keys in the dictionary
        """
    def pop(self, key: str, default: _T | None = ...) -> _DictValue | _T | None:
        """pop(self: _pdg.Dictionary, key: str, default: object = None) -> object

        Removes and returns the value with the specified key, or returns the default value if the key isn't found
        """
    @overload
    def set(self, arg0: str, arg1: int) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: float) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: str) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Dictionary) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Mapping[str, _DictArg]) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Sequence[int]) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Sequence[float]) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Sequence[str]) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Sequence[Dictionary]) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def set(self, arg0: str, arg1: Sequence[Mapping[str, _DictArg]]) -> None:
        """set(*args, **kwargs)
        Overloaded function.

        1. set(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. set(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. set(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. set(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. set(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. set(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. set(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    def setBool(self, arg0: str, arg1: bool) -> None:
        """setBool(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a boolean key/value
        """
    @overload
    def setDict(self, arg0: str, arg1: Dictionary) -> None:
        """setDict(*args, **kwargs)
        Overloaded function.

        1. setDict(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        2. setDict(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value
        """
    @overload
    def setDict(self, arg0: str, arg1: Mapping[str, _DictArg]) -> None:
        """setDict(*args, **kwargs)
        Overloaded function.

        1. setDict(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        2. setDict(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value
        """
    @overload
    def setDictArray(self, arg0: str, arg1: Sequence[Dictionary]) -> None:
        """setDictArray(*args, **kwargs)
        Overloaded function.

        1. setDictArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        2. setDictArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def setDictArray(self, arg0: str, arg1: Sequence[Mapping[str, _DictArg]]) -> None:
        """setDictArray(*args, **kwargs)
        Overloaded function.

        1. setDictArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        2. setDictArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    def setFloat(self, arg0: str, arg1: float) -> None:
        """setFloat(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a floating point key/value
        """
    def setFloatArray(self, arg0: str, arg1: Sequence[float]) -> None:
        """setFloatArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a floating point array key/value
        """
    def setInt(self, arg0: str, arg1: int) -> None:
        """setInt(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets an integer key/value
        """
    def setIntArray(self, arg0: str, arg1: Sequence[int]) -> None:
        """setIntArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets an integer array key/value
        """
    def setString(self, arg0: str, arg1: str) -> None:
        """setString(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a string key/value
        """
    def setStringArray(self, arg0: str, arg1: Sequence[str]) -> None:
        """setStringArray(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a string key/value
        """
    def values(self) -> _DictionaryValueView:
        """values(self: _pdg.Dictionary) -> _pdg._DictionaryValueView

        Returns a view into the values in the dictionary
        """
    def __contains__(self, other: str) -> bool:
        """__contains__(self: _pdg.Dictionary, arg0: str) -> bool

        Returns True if the specified key is present in the dictionary
        """
    def __delitem__(self, other: str) -> None:
        """__delitem__(self: _pdg.Dictionary, arg0: str) -> None

        Removes an item from the dictionary by key
        """
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _pdg.Dictionary, arg0: _pdg.Dictionary) -> bool

        Compares two dictionaries for equality
        """
    def __getitem__(self, index: str) -> _DictValue:
        """__getitem__(self: _pdg.Dictionary, arg0: str) -> object

        Looks up an entry in the dictionary by key
        """
    def __hash__(self) -> int:
        """__hash__(self: _pdg.Dictionary) -> int

        Returns a hash value for the dictionary
        """
    def __iter__(self) -> _DictionaryKeyIter:
        """__iter__(self: _pdg.Dictionary) -> object"""
    def __len__(self) -> int:
        """__len__(self: _pdg.Dictionary) -> int

        The number of entries in the dictionary
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(self: _pdg.Dictionary, arg0: _pdg.Dictionary) -> bool

        Compares two dictionaries for inequality
        """
    @overload
    def __setitem__(self, index: str, object: int) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: float) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: str) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Dictionary) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Mapping[str, _DictArg]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Sequence[int]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Sequence[float]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Sequence[str]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Sequence[Dictionary]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """
    @overload
    def __setitem__(self, index: str, object: Sequence[Mapping[str, _DictArg]]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: int) -> None

        Sets a dictionary key/value

        2. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: bool) -> None

        Sets a dictionary key/value

        3. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: float) -> None

        Sets a dictionary key/value

        4. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: str) -> None

        Sets a dictionary key/value

        5. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: _pdg.Dictionary) -> None

        Sets a dictionary key/value

        6. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: dict) -> None

        Sets a dictionary key/value

        7. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[int]) -> None

        Sets a dictionary key/value

        8. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[float]) -> None

        Sets a dictionary key/value

        9. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[str]) -> None

        Sets a dictionary key/value

        10. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[_pdg.Dictionary]) -> None

        Sets a dictionary key/value

        11. __setitem__(self: _pdg.Dictionary, arg0: str, arg1: UT_Array[dict]) -> None

        Sets a dictionary key/value
        """

class DisconnectResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class EvaluationContext:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def builtinFunctions() -> list[str]:
        """builtinFunctions() -> list

        Returns the builtin functions available in evaluation context
        """
    @staticmethod
    def dirtyAllAttribs() -> None:
        """dirtyAllAttribs() -> None

        Dirtys all attribute dependencies
        """
    @staticmethod
    def evaluateCode(arg0: str, arg1: bool) -> Any:
        """evaluateCode(arg0: str, arg1: bool) -> object

        Evaluate a string of Python code using the local context

        """
    @staticmethod
    def get() -> EvaluationContext:
        """get() -> _pdg.EvaluationContext

        Returns the local context for the current thread
        """
    @staticmethod
    def isEvaluating() -> bool:
        """isEvaluating() -> bool

        Returns true if the calling thread is evaluating a PDG workitem
        """
    @staticmethod
    def localDict() -> dict[str, Any]:
        """localDict() -> object

        Returns the local dictionary of extra arguments posted for
        use during expression evaluation
        """
    @staticmethod
    def setDict(arg0: dict[str, Any]) -> None:
        """setDict(arg0: dict) -> None

        Sets a dictionary of variables to use when evaluating
        expressions with the local context
        """
    @staticmethod
    def setGlobalSubItemIndex(arg0: int, arg1: bool) -> None:
        """setGlobalSubItemIndex(arg0: int, arg1: bool) -> None

        Sets the global sub item index, if the current global item is
        a batch work item
        """
    @staticmethod
    def setGlobalWorkItem(arg0: WorkItem, arg1: bool) -> None:
        """setGlobalWorkItem(arg0: PDG_WorkItem, arg1: bool) -> None

        Sets the global work item for UI display purposes
        """
    @staticmethod
    def setTimeDependentAttribs(names: Sequence[str], dirty: bool = ...) -> None:
        """setTimeDependentAttribs(names: UT_Set[str], dirty: bool = True) -> None

        Sets the global item dependent attributes flag, which is needed
        for cooking per-frame batch data
        """
    @staticmethod
    def workItem() -> WorkItem | None:
        """workItem() -> PDG_WorkItem

        Returns the local work item for the current thread if called
        during a cook callback, otherwise returns the global active
        workitem
        """
    @staticmethod
    def workItemDep() -> WorkItem | None:
        """workItemDep() -> PDG_WorkItem

        Returns the local work item for the current thread if called
        during a cook callback, otherwise returns the global active
        workitem. Also creates a dependency on the evaluating channel
        to the active PDG work item
        """

class EvaluationOptions:
    autoRecook: bool
    autoRecookInterval: int
    blocking: bool
    def __init__(self, *, no_constructor: Never) -> None: ...

class Event:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def context(self) -> GraphContext: ...
    @property
    def currentState(self) -> workItemState: ...
    @property
    def dependencyId(self) -> int: ...
    @property
    def lastState(self) -> workItemState: ...
    @property
    def message(self) -> str: ...
    @property
    def node(self) -> Node | None: ...
    @property
    def type(self) -> EventType: ...
    @property
    def workItemId(self) -> int: ...
    @property
    def workItemIds(self) -> list[int]: ...

class EventEmitter:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @overload
    def addEventHandler(self, handler: _EventCallback, pass_handler: bool = ...) -> PyEventHandler:
        """addEventHandler(*args, **kwargs)
        Overloaded function.

        1. addEventHandler(self: _pdg.EventEmitter, handler: object, pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler. If pass_handler is
        is set to True, the handler object itself is passed as the first
        argument to the callback function, in addition to the event itself.

        2. addEventHandler(self: _pdg.EventEmitter, handler: object, filter: PDG_EventType, pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler, with a filter for
        which events to process. If pass_handler is set to True, the
        handler object itself is passed as the first argument to the
        callback function, in addition to the event itself.

        3. addEventHandler(self: _pdg.EventEmitter, handler: object, event_types: UT_Array[PDG_EventType], pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler, with a list of
        pdg.EventType to process. If pass_handler is set to True, the
        handler object itself is passed as the first argument to the
        callback function, in addition to the event itself.
        """
    @overload
    def addEventHandler(self, handler: _EventCallback, filter: EventType, pass_handler: bool = ...) -> PyEventHandler:
        """addEventHandler(*args, **kwargs)
        Overloaded function.

        1. addEventHandler(self: _pdg.EventEmitter, handler: object, pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler. If pass_handler is
        is set to True, the handler object itself is passed as the first
        argument to the callback function, in addition to the event itself.

        2. addEventHandler(self: _pdg.EventEmitter, handler: object, filter: PDG_EventType, pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler, with a filter for
        which events to process. If pass_handler is set to True, the
        handler object itself is passed as the first argument to the
        callback function, in addition to the event itself.

        3. addEventHandler(self: _pdg.EventEmitter, handler: object, event_types: UT_Array[PDG_EventType], pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler, with a list of
        pdg.EventType to process. If pass_handler is set to True, the
        handler object itself is passed as the first argument to the
        callback function, in addition to the event itself.
        """
    @overload
    def addEventHandler(self, handler: _EventCallback, event_types: Sequence[EventType], pass_handler: bool = ...) -> PyEventHandler:
        """addEventHandler(*args, **kwargs)
        Overloaded function.

        1. addEventHandler(self: _pdg.EventEmitter, handler: object, pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler. If pass_handler is
        is set to True, the handler object itself is passed as the first
        argument to the callback function, in addition to the event itself.

        2. addEventHandler(self: _pdg.EventEmitter, handler: object, filter: PDG_EventType, pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler, with a filter for
        which events to process. If pass_handler is set to True, the
        handler object itself is passed as the first argument to the
        callback function, in addition to the event itself.

        3. addEventHandler(self: _pdg.EventEmitter, handler: object, event_types: UT_Array[PDG_EventType], pass_handler: bool = False) -> PYPDG_EventHandler

        Adds a Python callback as an event handler, with a list of
        pdg.EventType to process. If pass_handler is set to True, the
        handler object itself is passed as the first argument to the
        callback function, in addition to the event itself.
        """
    def hasEventHandler(self, arg0: _EventCallback) -> bool:
        """hasEventHandler(self: _pdg.EventEmitter, arg0: object) -> bool

        Returns True if the emitter has an event handler that uses the
        specified Python callback function
        """
    def removeAllEventHandlers(self) -> None:
        """removeAllEventHandlers(self: _pdg.EventEmitter) -> None

        Removes all event handlers from the node
        """
    def removeEventHandler(self, arg0: EventHandler) -> None:
        """removeEventHandler(self: _pdg.EventEmitter, arg0: PYPDG_EventHandler) -> None

        Removes an event handler from the node
        """
    @property
    def eventHandlers(self) -> list[EventHandler]: ...
    @property
    def supportedEventTypes(self) -> list[EventType]: ...

class EventHandler:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def removeFromAllEmitters(self) -> None:
        """removeFromAllEmitters(self: _pdg.EventHandler) -> None

        Removes all event emitters that have this handler assigned to them
        """
    @property
    def emitters(self) -> list[EventEmitter]: ...
    @property
    def language(self) -> _pdg.language: ...

class EventType:
    __members__: ClassVar[dict[str, EventType]] = ...  # read-only
    All: ClassVar[EventType] = ...
    CookComplete: ClassVar[EventType] = ...
    CookError: ClassVar[EventType] = ...
    CookStart: ClassVar[EventType] = ...
    CookWarning: ClassVar[EventType] = ...
    DirtyAll: ClassVar[EventType] = ...
    DirtyStart: ClassVar[EventType] = ...
    DirtyStop: ClassVar[EventType] = ...
    Log: ClassVar[EventType] = ...
    NodeClear: ClassVar[EventType] = ...
    NodeConnect: ClassVar[EventType] = ...
    NodeCooked: ClassVar[EventType] = ...
    NodeCreate: ClassVar[EventType] = ...
    NodeDisconnect: ClassVar[EventType] = ...
    NodeFirstCook: ClassVar[EventType] = ...
    NodeGenerated: ClassVar[EventType] = ...
    NodeProgressUpdate: ClassVar[EventType] = ...
    NodeRemove: ClassVar[EventType] = ...
    NodeRename: ClassVar[EventType] = ...
    NodeSetScheduler: ClassVar[EventType] = ...
    Null: ClassVar[EventType] = ...
    SchedulerAdded: ClassVar[EventType] = ...
    SchedulerRemoved: ClassVar[EventType] = ...
    ServiceClientChanged: ClassVar[EventType] = ...
    ServiceClientStarted: ClassVar[EventType] = ...
    ServiceManagerAll: ClassVar[EventType] = ...
    ServiceStartBegin: ClassVar[EventType] = ...
    ServiceStartEnd: ClassVar[EventType] = ...
    UISelect: ClassVar[EventType] = ...
    WorkItemAdd: ClassVar[EventType] = ...
    WorkItemAddDep: ClassVar[EventType] = ...
    WorkItemAddList: ClassVar[EventType] = ...
    WorkItemAddParent: ClassVar[EventType] = ...
    WorkItemAddStaticAncestor: ClassVar[EventType] = ...
    WorkItemCookPercentUpdate: ClassVar[EventType] = ...
    WorkItemFrame: ClassVar[EventType] = ...
    WorkItemMerge: ClassVar[EventType] = ...
    WorkItemOutputFiles: ClassVar[EventType] = ...
    WorkItemPriority: ClassVar[EventType] = ...
    WorkItemRemove: ClassVar[EventType] = ...
    WorkItemRemoveDep: ClassVar[EventType] = ...
    WorkItemRemoveList: ClassVar[EventType] = ...
    WorkItemRemoveParent: ClassVar[EventType] = ...
    WorkItemRemoveStaticAncestor: ClassVar[EventType] = ...
    WorkItemResult: ClassVar[EventType] = ...
    WorkItemSetDict: ClassVar[EventType] = ...
    WorkItemSetFile: ClassVar[EventType] = ...
    WorkItemSetFloat: ClassVar[EventType] = ...
    WorkItemSetGeometry: ClassVar[EventType] = ...
    WorkItemSetInt: ClassVar[EventType] = ...
    WorkItemSetPyObject: ClassVar[EventType] = ...
    WorkItemSetString: ClassVar[EventType] = ...
    WorkItemStateChange: ClassVar[EventType] = ...
    __entries: ClassVar[dict[str, tuple[EventType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.EventType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.EventType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.EventType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ExpressionError(Exception): ...

class FeedbackBegin(Processor):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def isFeedbackAttribs(self) -> bool:
        """isFeedbackAttribs(self: _pdg.FeedbackBegin) -> bool

        [read only] Set to True if the node is configured to feedback
        attributes
        """
    def isFeedbackFiles(self) -> bool:
        """isFeedbackFiles(self: _pdg.FeedbackBegin) -> bool

        [read only] Set to True if the node is configured to feedback
        output files
        """

class File:
    DefaultArchiveTag: ClassVar[str] = ...
    DefaultCsvTag: ClassVar[str] = ...
    DefaultDirTag: ClassVar[str] = ...
    DefaultFileTag: ClassVar[str] = ...
    DefaultGeoTag: ClassVar[str] = ...
    DefaultHdaTag: ClassVar[str] = ...
    DefaultHipTag: ClassVar[str] = ...
    DefaultImageTag: ClassVar[str] = ...
    DefaultPythonScriptTag: ClassVar[str] = ...
    DefaultSymLinkTag: ClassVar[str] = ...
    DefaultTxtTag: ClassVar[str] = ...
    DefaultUsdTag: ClassVar[str] = ...
    DefaultVideoTag: ClassVar[str] = ...
    hash: int
    owned: bool
    path: str
    size: int
    tag: str
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.File) -> None

        Constructs a new file object

        2. __init__(self: _pdg.File, arg0: str, arg1: bool) -> None

        Constructs a new file object

        3. __init__(self: _pdg.File, arg0: str, arg1: str, arg2: int, arg3: bool) -> None

        Constructs a new file object
        """
    @overload
    def __init__(self, arg0: str, arg1: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.File) -> None

        Constructs a new file object

        2. __init__(self: _pdg.File, arg0: str, arg1: bool) -> None

        Constructs a new file object

        3. __init__(self: _pdg.File, arg0: str, arg1: str, arg2: int, arg3: bool) -> None

        Constructs a new file object
        """
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int, arg3: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.File) -> None

        Constructs a new file object

        2. __init__(self: _pdg.File, arg0: str, arg1: bool) -> None

        Constructs a new file object

        3. __init__(self: _pdg.File, arg0: str, arg1: str, arg2: int, arg3: bool) -> None

        Constructs a new file object
        """
    def asTuple(self) -> tuple[str, str, int, bool]:
        """asTuple(self: _pdg.File) -> tuple

        Returns a tuple of the various fields on this file object
        """
    def localizePath(self, arg0: Scheduler) -> str:
        """localizePath(self: _pdg.File, arg0: PDG_Scheduler) -> str

        Localizes the path stored on this file object with the specified
        scheduler
        """
    @staticmethod
    def mapPath(path: str, zone: str) -> str:
        """mapPath(path: str, zone: str) -> str

        [deprecated[ Returns the mapped version of the given path for
        the given zone
        """
    @staticmethod
    def mapPathToLocal(path: str) -> str:
        """mapPathToLocal(path: str) -> str

        [deprecated] Returns the mapped version of the given path for
        the local zone
        """
    @staticmethod
    def mappingZone() -> str:
        """mappingZone() -> str

        [deprecated] Returns the local mapping zone
        """
    @staticmethod
    def pathMapJSON() -> str:
        """pathMapJSON() -> str

        [deprecated] Returns the PDG Path Map as a JSON string
        """
    @staticmethod
    def setMappingZone(zone: str) -> None:
        """setMappingZone(zone: str) -> None

        [deprecated] Sets the local mapping zone
        """
    @staticmethod
    def setPathMapJSON(arg0: str) -> None:
        """setPathMapJSON(arg0: str) -> None

        [deprecated] Sets the PDG Path Map from a JSON string
        """
    def updateStat(self, work_item: WorkItem | None = ..., force: bool = ...) -> None:
        """updateStat(self: _pdg.File, work_item: PDG_WorkItem = None, force: bool = False) -> None

        Updates the mod time and file size of the file. The work item is
        passed to any custom file handlers, but is not required for the
        built-in file stat implementation
        """
    def __eq__(self, other: object) -> bool:
        """__eq__(*args, **kwargs)
        Overloaded function.

        1. __eq__(self: _pdg.File, arg0: _pdg.File) -> bool

        Compares to file objects for equality

        2. __eq__(self: _pdg.File, arg0: str) -> bool

        Compares a file object against a string for equality
        """
    def __ge__(self, other: File | str) -> bool:
        """__ge__(*args, **kwargs)
        Overloaded function.

        1. __ge__(self: _pdg.File, arg0: _pdg.File) -> bool

        Return true if this file is ordered after or equal to the other

        2. __ge__(self: _pdg.File, arg0: str) -> bool

        Returns true if this file is ordered strictly after or equal to the string
        """
    def __getitem__(self, index: int) -> str | int | bool:
        """__getitem__(self: _pdg.File, arg0: int) -> object

        Index-based acessor for file components, for compatibility with
        older APIs
        """
    def __iter__(self) -> Iterator[str | int | bool]:
        """def __iter__(self) -> typing.Iterator[Any]"""
    def __gt__(self, other: File | str) -> bool:
        """__gt__(*args, **kwargs)
        Overloaded function.

        1. __gt__(self: _pdg.File, arg0: _pdg.File) -> bool

        Return true if this file is ordered stricly after the other

        2. __gt__(self: _pdg.File, arg0: str) -> bool

        Returns true if this file is ordered strictly after the string
        """
    def __le__(self, other: File | str) -> bool:
        """__le__(*args, **kwargs)
        Overloaded function.

        1. __le__(self: _pdg.File, arg0: _pdg.File) -> bool

        Return true if this file is ordered before or equal to the other

        2. __le__(self: _pdg.File, arg0: str) -> bool

        Returns true if this file is ordered strictly before or equal to the string
        """
    def __lt__(self, other: File | str) -> bool:
        """__lt__(*args, **kwargs)
        Overloaded function.

        1. __lt__(self: _pdg.File, arg0: _pdg.File) -> bool

        Return true if this file is ordered stricly before the other

        2. __lt__(self: _pdg.File, arg0: str) -> bool

        Returns true if this file is ordered strictly before the string
        """
    def __ne__(self, other: object) -> bool:
        """__ne__(*args, **kwargs)
        Overloaded function.

        1. __ne__(self: _pdg.File, arg0: _pdg.File) -> bool

        Compares to file objects for inequality

        2. __ne__(self: _pdg.File, arg0: str) -> bool

        Compares a file object against a string for inequality
        """
    @property
    def local_path(self) -> str: ...
    @property
    def type(self) -> fileType: ...

class FileDependency(Dependency):
    def __init__(self, *, no_constructor: Never) -> None: ...

class Filter:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.Filter) -> None

        Creates a new filter, defaulting to cooking everything

        2. __init__(self: _pdg.Filter, arg0: bool) -> None

        Creates a new filter with the desired strict mode flag and
        defaulting to cooking everything
        """
    @overload
    def __init__(self, arg0: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.Filter) -> None

        Creates a new filter, defaulting to cooking everything

        2. __init__(self: _pdg.Filter, arg0: bool) -> None

        Creates a new filter with the desired strict mode flag and
        defaulting to cooking everything
        """
    def appendToSet(self, arg0: int) -> None:
        """appendToSet(self: _pdg.Filter, arg0: int) -> None

        Appends a single work item id to the set
        """
    def setNone(self) -> None:
        """setNone(self: _pdg.Filter) -> None

        Resets the filter to the empty set
        """

class FilterPattern(BasePattern):
    def __init__(self, pattern: str) -> None:
        """__init__(self: _pdg.FilterPattern, pattern: str) -> None

        Returns a new pattern object from the specified string
        """
    @overload
    def match(self, attribute: str, value: str, component: int = ..., inclusive: bool = ...) -> bool:
        """match(*args, **kwargs)
        Overloaded function.

        1. match(self: _pdg.FilterPattern, attribute: str, value: str, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified string

        2. match(self: _pdg.FilterPattern, attribute: str, value: float, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        3. match(self: _pdg.FilterPattern, attribute: str, value: int, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        4. match(self: _pdg.FilterPattern, work_item: PDG_WorkItem, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified work item
        """
    @overload
    def match(self, attribute: str, value: float, component: int = ..., inclusive: bool = ...) -> bool:
        """match(*args, **kwargs)
        Overloaded function.

        1. match(self: _pdg.FilterPattern, attribute: str, value: str, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified string

        2. match(self: _pdg.FilterPattern, attribute: str, value: float, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        3. match(self: _pdg.FilterPattern, attribute: str, value: int, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        4. match(self: _pdg.FilterPattern, work_item: PDG_WorkItem, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified work item
        """
    @overload
    def match(self, work_item: WorkItem, inclusive: bool = ...) -> bool:
        """match(*args, **kwargs)
        Overloaded function.

        1. match(self: _pdg.FilterPattern, attribute: str, value: str, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified string

        2. match(self: _pdg.FilterPattern, attribute: str, value: float, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        3. match(self: _pdg.FilterPattern, attribute: str, value: int, component: int = 0, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        4. match(self: _pdg.FilterPattern, work_item: PDG_WorkItem, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified work item
        """

class FrameUtils:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def batchByFrame(arg0: Sequence[WorkItem] | ConstWorkItemList | WorkItemList) -> tuple[list[list[WorkItem]], list[WorkItem]]:
        """batchByFrame(arg0: UT_Array[PDG_WorkItem]) -> object

        Splits a list of work items into multiple lists for each
        frame range
        """
    @staticmethod
    def detectFrameRange(work_items: Sequence[WorkItem] | Sequence[float], step_precision: int = ...) -> tuple[float, float, float] | None:
        """detectFrameRange(*args, **kwargs)
        Overloaded function.

        1. detectFrameRange(work_items: UT_Array[PDG_WorkItem], step_precision: int = 100) -> object

        Detects the (start, end, step) frame range tuple for the
        specified list of work items. Ignores work items that don't have
        a frame value

        2. detectFrameRange(frames: UT_Array[float], step_precision: int = 100) -> object

        Detects the (start, end, step) frame range tuple for the
        specified list of frame values.
        """

class Graph(AttributeOwner):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def bindGlobalAttribute(self, arg0: str, arg1: WorkItem) -> None:
        """bindGlobalAttribute(self: _pdg.Graph, arg0: str, arg1: PDG_WorkItem) -> None

        Binds a global attribute to a work item
        """
    def boundAttributeWorkItem(self, arg0: str) -> WorkItem | None:
        """boundAttributeWorkItem(self: _pdg.Graph, arg0: str) -> PDG_WorkItem

        Returns the ID of the work item that the attribute is bound to
        """
    def dependencyForKey(self, arg0: str) -> Dependency | None:
        """dependencyForKey(self: _pdg.Graph, arg0: str) -> _pdg.Dependency

        Returns an external dependency for a given key
        """
    def dependencyGraph(self, expand: bool = ..., filter: Scheduler | None = ...) -> _DependencyGraph:
        """dependencyGraph(self: _pdg.Graph, expand: bool = True, filter: PDG_Scheduler = None) -> object

        Returns a tuple contain a map for work item->dependencies,work item->depenedents and a list of ready items
        """
    def dirty(self, arg0: bool) -> None:
        """dirty(self: _pdg.Graph, arg0: bool) -> None

        Deletes all work items in the graph
        """
    def node(self, arg0: str) -> Node | None:
        """node(self: _pdg.Graph, arg0: str) -> PDG_Node

        Looks up a node in the graph by it's name
        """
    @overload
    def nodePort(self, arg0: str, arg1: str) -> Port | None:
        """nodePort(*args, **kwargs)
        Overloaded function.

        1. nodePort(self: _pdg.Graph, arg0: str, arg1: str) -> PDG_Port

        Returns a port reference for a given node name and port name

        2. nodePort(self: _pdg.Graph, arg0: str) -> PDG_Port

        Returns a port reference for a give node and port name, in
        the format node.port
        """
    @overload
    def nodePort(self, arg0: str) -> Port | None:
        """nodePort(*args, **kwargs)
        Overloaded function.

        1. nodePort(self: _pdg.Graph, arg0: str, arg1: str) -> PDG_Port

        Returns a port reference for a given node name and port name

        2. nodePort(self: _pdg.Graph, arg0: str) -> PDG_Port

        Returns a port reference for a give node and port name, in
        the format node.port
        """
    def nodes(self) -> list[Node]:
        """nodes(self: _pdg.Graph) -> list

        Returns the list of nodes in the graph
        """
    def prepareDirty(self) -> WorkItemDirty:
        """prepareDirty(self: _pdg.Graph) -> PDG_WorkItemDirty

        Prepares a pdg.WorkItemDirty object for the graph's work items
        """
    def serialize(self, arg0: str) -> None:
        """serialize(self: _pdg.Graph, arg0: str) -> None

        Serializes the graph to a string
        """
    @staticmethod
    def workItem(arg0: int) -> WorkItem | None:
        """workItem(arg0: int) -> PDG_WorkItem

        Returns the work item with the specified id
        """
    def workItemById(self, arg0: int) -> WorkItem | None:
        """workItemById(self: _pdg.Graph, arg0: int) -> PDG_WorkItem

        Returns the work item with the specified id
        """
    def workItemByName(self, arg0: str) -> WorkItem | None:
        """workItemByName(self: _pdg.Graph, arg0: str) -> PDG_WorkItem

        Returns the work item with the specified name
        """
    def workItemsByIds(self, arg0: Sequence[int]) -> list[WorkItem]:
        """workItemsByIds(self: _pdg.Graph, arg0: UT_Array[int]) -> list

        Returns a list of work items for a given list of ids
        """
    @property
    def graphDescription(self) -> str: ...
    @property
    def nodeCount(self) -> int: ...

class GraphContext(EventEmitter):
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.GraphContext) -> None

        Creates a new context with the default name

        2. __init__(self: _pdg.GraphContext, arg0: str) -> None

        Creates a new context with the specified name
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.GraphContext) -> None

        Creates a new context with the default name

        2. __init__(self: _pdg.GraphContext, arg0: str) -> None

        Creates a new context with the specified name
        """
    @overload
    def addParameter(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: dataType, arg5: int) -> Port:
        """addParameter(*args, **kwargs)
        Overloaded function.

        1. addParameter(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: str, arg4: PDGT_Value::DataType, arg5: int) -> object

        [cmd] Adds a custom parameter to a node

        2. addParameter(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: UT_Array[str], arg4: PDGT_Value::DataType, arg5: int) -> object

        [cmd] Adds a custom parameter to a node
        """
    @overload
    def addParameter(self, arg0: str, arg1: str, arg2: str, arg3: Sequence[str], arg4: dataType, arg5: int) -> Port:
        """addParameter(*args, **kwargs)
        Overloaded function.

        1. addParameter(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: str, arg4: PDGT_Value::DataType, arg5: int) -> object

        [cmd] Adds a custom parameter to a node

        2. addParameter(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: UT_Array[str], arg4: PDGT_Value::DataType, arg5: int) -> object

        [cmd] Adds a custom parameter to a node
        """
    def addWorkItem(self, arg0: WorkItem.Serialization) -> None:
        """addWorkItem(self: _pdg.GraphContext, arg0: PDG_WorkItemSerialization) -> None

        [unsafe] Directly inserts a work item into the task graph.
        Should only be called from automatically generated
        serialization code as no validity checks are performed.
        """
    @overload
    def addWorkItemDependency(self, item_name: str, dep_name: str, required: bool, user_defined: bool = ...) -> None:
        """addWorkItemDependency(*args, **kwargs)
        Overloaded function.

        1. addWorkItemDependency(self: _pdg.GraphContext, item_name: str, dep_name: str, required: bool, user_defined: bool = True) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.

        2. addWorkItemDependency(self: _pdg.GraphContext, item_id: int, dep_id: int, required: bool, user_defined: bool = True) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.
        """
    @overload
    def addWorkItemDependency(self, item_id: int, dep_id: int, required: bool, user_defined: bool = ...) -> None:
        """addWorkItemDependency(*args, **kwargs)
        Overloaded function.

        1. addWorkItemDependency(self: _pdg.GraphContext, item_name: str, dep_name: str, required: bool, user_defined: bool = True) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.

        2. addWorkItemDependency(self: _pdg.GraphContext, item_id: int, dep_id: int, required: bool, user_defined: bool = True) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.
        """
    @overload
    def addWorkItemPropagateDep(self, arg0: str, arg1: str) -> None:
        """addWorkItemPropagateDep(*args, **kwargs)
        Overloaded function.

        1. addWorkItemPropagateDep(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.

        2. addWorkItemPropagateDep(self: _pdg.GraphContext, arg0: int, arg1: int) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.
        """
    @overload
    def addWorkItemPropagateDep(self, arg0: int, arg1: int) -> None:
        """addWorkItemPropagateDep(*args, **kwargs)
        Overloaded function.

        1. addWorkItemPropagateDep(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.

        2. addWorkItemPropagateDep(self: _pdg.GraphContext, arg0: int, arg1: int) -> None

        [unsafe] Directly sets dependencies on work items. Should
        only be called from generate serialization code as no
        validity checks are performed.
        """
    @overload
    def addWorkItemResults(self, arg0: str, arg1: Sequence[str], arg2: Sequence[str], arg3: Sequence[int], arg4: Sequence[bool], arg5: Sequence[bool]) -> None:
        """addWorkItemResults(*args, **kwargs)
        Overloaded function.

        1. addWorkItemResults(self: _pdg.GraphContext, arg0: str, arg1: UT_Array[str], arg2: UT_Array[str], arg3: UT_Array[int], arg4: UT_Array[bool], arg5: UT_Array[bool]) -> None

        [unsafe] Directly injects work item bake results into an
        existing work item. Should only be called from generated code
        as no validity checks are performed.

        2. addWorkItemResults(self: _pdg.GraphContext, arg0: int, arg1: UT_Array[str], arg2: UT_Array[str], arg3: UT_Array[int], arg4: UT_Array[bool], arg5: UT_Array[bool]) -> None

        [unsafe] Directly injects work item bake results into an
        existing work item. Should only be called from generated code
        as no validity checks are performed.
        """
    @overload
    def addWorkItemResults(self, arg0: int, arg1: Sequence[str], arg2: Sequence[str], arg3: Sequence[int], arg4: Sequence[bool], arg5: Sequence[bool]) -> None:
        """addWorkItemResults(*args, **kwargs)
        Overloaded function.

        1. addWorkItemResults(self: _pdg.GraphContext, arg0: str, arg1: UT_Array[str], arg2: UT_Array[str], arg3: UT_Array[int], arg4: UT_Array[bool], arg5: UT_Array[bool]) -> None

        [unsafe] Directly injects work item bake results into an
        existing work item. Should only be called from generated code
        as no validity checks are performed.

        2. addWorkItemResults(self: _pdg.GraphContext, arg0: int, arg1: UT_Array[str], arg2: UT_Array[str], arg3: UT_Array[int], arg4: UT_Array[bool], arg5: UT_Array[bool]) -> None

        [unsafe] Directly injects work item bake results into an
        existing work item. Should only be called from generated code
        as no validity checks are performed.
        """
    def beginDeserialization(self) -> None:
        """beginDeserialization(self: _pdg.GraphContext) -> None

        [unsafe] Run initial, graph-level deserialization logic
        """
    @staticmethod
    def byName(arg0: str) -> GraphContext | None:
        """byName(arg0: str) -> _pdg.GraphContext

        Returns the context with a specified name, or None if no such
        context exists
        """
    def cancelCook(self) -> None:
        """cancelCook(self: _pdg.GraphContext) -> None

        Cancels cooking
        """
    def cleanTempDirectory(self, arg0: str) -> None:
        """cleanTempDirectory(self: _pdg.GraphContext, arg0: str) -> None

        Cleans temporary directory
        """
    def commitChunk(self) -> None:
        """commitChunk(self: _pdg.GraphContext) -> None

        Commits the chunk
        """
    @overload
    def commitWorkItem(self, arg0: str) -> None:
        """commitWorkItem(*args, **kwargs)
        Overloaded function.

        1. commitWorkItem(self: _pdg.GraphContext, arg0: str) -> None

        [unsafe] Commits a pending work item add. Should only be called
        from generate serialization code


        2. commitWorkItem(self: _pdg.GraphContext, arg0: int) -> None

        [unsafe] Commits a pending work item add. Should only be called
        from generate serialization code

        """
    @overload
    def commitWorkItem(self, arg0: int) -> None:
        """commitWorkItem(*args, **kwargs)
        Overloaded function.

        1. commitWorkItem(self: _pdg.GraphContext, arg0: str) -> None

        [unsafe] Commits a pending work item add. Should only be called
        from generate serialization code


        2. commitWorkItem(self: _pdg.GraphContext, arg0: int) -> None

        [unsafe] Commits a pending work item add. Should only be called
        from generate serialization code

        """
    @overload
    def connect(self, arg0: str, arg1: str, arg2: str, arg3: str) -> tuple[Port, Port]:
        """connect(*args, **kwargs)
        Overloaded function.

        1. connect(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: str) -> object

        [cmd] Connects a port to another port

        2. connect(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Connects a node.port to another node.port
        """
    @overload
    def connect(self, arg0: str, arg1: str) -> tuple[Port, Port]:
        """connect(*args, **kwargs)
        Overloaded function.

        1. connect(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: str) -> object

        [cmd] Connects a port to another port

        2. connect(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Connects a node.port to another node.port
        """
    @overload
    def cook(self, arg0: CookOptions) -> bool:
        """cook(*args, **kwargs)
        Overloaded function.

        1. cook(self: _pdg.GraphContext, arg0: _pdg.CookOptions) -> bool

        Cooks the graph using the specified cook options

        2. cook(self: _pdg.GraphContext, block: bool, mode: _pdg.cookType = <cookType.Full: 0>, name: str = '', ids: _pdg.Filter = <_pdg.Filter object>) -> bool

        Cooks the graph using the specified arguments
        """
    @overload
    def cook(self, block: bool, mode: cookType = ..., name: str = ..., ids: Filter = ...) -> bool:
        """cook(*args, **kwargs)
        Overloaded function.

        1. cook(self: _pdg.GraphContext, arg0: _pdg.CookOptions) -> bool

        Cooks the graph using the specified cook options

        2. cook(self: _pdg.GraphContext, block: bool, mode: _pdg.cookType = <cookType.Full: 0>, name: str = '', ids: _pdg.Filter = <_pdg.Filter object>) -> bool

        Cooks the graph using the specified arguments
        """
    def cookItems(self, block: bool, ids: Sequence[int] = ..., name: str = ...) -> bool:
        """cookItems(self: _pdg.GraphContext, block: bool, ids: UT_Array[int] = [], name: str = '') -> bool

        Cooks the specified work items
        """
    def delete(self, arg0: str) -> bool:
        """delete(self: _pdg.GraphContext, arg0: str) -> object

        [cmd] Deletes a node from the graph
        """
    def deserializeWorkItemFromJSON(self, arg0: str) -> WorkItem:
        """deserializeWorkItemFromJSON(self: _pdg.GraphContext, arg0: str) -> object

        [unsafe] Deserializes the workitem from a JSON file as serialized 
        by serializeWorkItemToJSON().
        """
    @overload
    def disconnect(self, arg0: str, arg1: str, arg2: str, arg3: str) -> bool:
        """disconnect(*args, **kwargs)
        Overloaded function.

        1. disconnect(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: str) -> object

        [cmd] Disconnects one port from another

        2. disconnect(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Disconnects a node.port to another
        """
    @overload
    def disconnect(self, arg0: str, arg1: str) -> bool:
        """disconnect(*args, **kwargs)
        Overloaded function.

        1. disconnect(self: _pdg.GraphContext, arg0: str, arg1: str, arg2: str, arg3: str) -> object

        [cmd] Disconnects one port from another

        2. disconnect(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Disconnects a node.port to another
        """
    @staticmethod
    def findFile(arg0: str) -> str | None:
        """findFile(arg0: str) -> object

        Returns an absolute file path to a file on the PDG search path,
        or None of no file with the given name exists
        """
    def getSharedServerInfo(self, arg0: str) -> _SharedServerInfo | None:
        """getSharedServerInfo(self: _pdg.GraphContext, arg0: str) -> PDG_ValueArgs

        Gets the meta data for an existing sharedserver instance
        """
    @staticmethod
    def globFiles(arg0: str, arg1: str) -> list[str]:
        """globFiles(arg0: str, arg1: str) -> object

        Returns the list of all file paths matching a search pattern in
        the PDG search path
        """
    @staticmethod
    def globTypeFiles() -> list[str]:
        """globTypeFiles() -> object

        Return the list of all .py files in the types subpath

        """
    def memoryUsage(self) -> MemoryInfo:
        """memoryUsage(self: _pdg.GraphContext) -> PDG_MemoryInfo

        Returns memory usage info about the node
        """
    @staticmethod
    def names() -> list[str]:
        """names() -> UT_Array[str]

        Returns the list of active context names
        """
    @overload
    def openChunk(self, arg0: str) -> CommandChunk:
        """openChunk(*args, **kwargs)
        Overloaded function.

        1. openChunk(self: _pdg.GraphContext, arg0: str) -> _pdg.CommandChunk

        Opens a new command chunk

        2. openChunk(self: _pdg.GraphContext, arg0: bool, arg1: str) -> _pdg.CommandChunk

        Opens a new command Chunk with a delay flag. True indicates that
        the command chunk will only execute commands once the chunk has
        been commited
        """
    @overload
    def openChunk(self, arg0: bool, arg1: str) -> CommandChunk:
        """openChunk(*args, **kwargs)
        Overloaded function.

        1. openChunk(self: _pdg.GraphContext, arg0: str) -> _pdg.CommandChunk

        Opens a new command chunk

        2. openChunk(self: _pdg.GraphContext, arg0: bool, arg1: str) -> _pdg.CommandChunk

        Opens a new command Chunk with a delay flag. True indicates that
        the command chunk will only execute commands once the chunk has
        been commited
        """
    def pauseCook(self) -> None:
        """pauseCook(self: _pdg.GraphContext) -> None

        Pauses cooking
        """
    def redo(self) -> None:
        """redo(self: _pdg.GraphContext) -> None

        Redoes the next command or committed chunk
        """
    def removeDependency(self, arg0: str, arg1: str) -> bool:
        """removeDependency(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Removes an external dependency from a node
        """
    def renameNode(self, arg0: str, arg1: str) -> bool:
        """renameNode(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Renames a node
        """
    def rollbackChunk(self) -> None:
        """rollbackChunk(self: _pdg.GraphContext) -> None

        Reverts the chunk that is currently in progress
        """
    @overload
    def saveJSON(self, pretty_print: bool = ..., skip_defaults: bool = ...) -> str:
        """saveJSON(*args, **kwargs)
        Overloaded function.

        1. saveJSON(self: _pdg.GraphContext, pretty_print: bool = True, skip_defaults: bool = True) -> str

        Saves the nodes and schedulers from the graph to a JSON string

        2. saveJSON(self: _pdg.GraphContext, file_path: str, pretty_print: bool = True, skip_defaults: bool = True) -> None

        Saves the node and schedulers from the graph to a JSON file
        """
    @overload
    def saveJSON(self, file_path: str, pretty_print: bool = ..., skip_defaults: bool = ...) -> None:
        """saveJSON(*args, **kwargs)
        Overloaded function.

        1. saveJSON(self: _pdg.GraphContext, pretty_print: bool = True, skip_defaults: bool = True) -> str

        Saves the nodes and schedulers from the graph to a JSON string

        2. saveJSON(self: _pdg.GraphContext, file_path: str, pretty_print: bool = True, skip_defaults: bool = True) -> None

        Saves the node and schedulers from the graph to a JSON file
        """
    def schedulerForName(self, arg0: str) -> SchedulerBase | None:
        """schedulerForName(self: _pdg.GraphContext, arg0: str) -> PDG_Scheduler

        [read only] A reference to a pdg.Scheduler with a given name
        """
    def schedulerForTypeName(self, arg0: str) -> SchedulerBase | None:
        """schedulerForTypeName(self: _pdg.GraphContext, arg0: str) -> PDG_Scheduler

        [read only] A reference to the first pdg.Scheduler with the
        specified type name
        """
    @staticmethod
    def searchPath() -> list[str]:
        """searchPath() -> object

        Returns the pdg search path

        """
    @overload
    def serialize(self) -> str:
        """serialize(*args, **kwargs)
        Overloaded function.

        1. serialize(self: _pdg.GraphContext) -> str

        Serializes both the graph and task graph, and returns the
        resulting string.

        2. serialize(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes both the graph and task graph to a file. Extra code
        include at the top of the serialized output can be passed in.
        This method is effectively the same as calling serializeGraph
        followed by serializeWorkItems, and then writing both results to
        the same file.

        3. serialize(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes both the graph and task graph to a file. Extra code
        include at the top of the serialized output can be passed in.
        This method is effectively the same as calling serializeGraph
        followed by serializeWorkItems, and then writing both results to
        the same file.
        """
    @overload
    def serialize(self, arg0: str, arg1: str) -> None:
        """serialize(*args, **kwargs)
        Overloaded function.

        1. serialize(self: _pdg.GraphContext) -> str

        Serializes both the graph and task graph, and returns the
        resulting string.

        2. serialize(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes both the graph and task graph to a file. Extra code
        include at the top of the serialized output can be passed in.
        This method is effectively the same as calling serializeGraph
        followed by serializeWorkItems, and then writing both results to
        the same file.

        3. serialize(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes both the graph and task graph to a file. Extra code
        include at the top of the serialized output can be passed in.
        This method is effectively the same as calling serializeGraph
        followed by serializeWorkItems, and then writing both results to
        the same file.
        """
    @overload
    def serializeGraph(self) -> str:
        """serializeGraph(*args, **kwargs)
        Overloaded function.

        1. serializeGraph(self: _pdg.GraphContext) -> str

        Serializes the graph context to a string. This includes the
        nodes in the graph, external dependencies and schedulers.

        2. serializeGraph(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes the graph context to a file, using the above
        `serialize` method.
        """
    @overload
    def serializeGraph(self, arg0: str, arg1: str) -> None:
        """serializeGraph(*args, **kwargs)
        Overloaded function.

        1. serializeGraph(self: _pdg.GraphContext) -> str

        Serializes the graph context to a string. This includes the
        nodes in the graph, external dependencies and schedulers.

        2. serializeGraph(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes the graph context to a file, using the above
        `serialize` method.
        """
    def serializeWorkItemToJSON(self, work_item: WorkItem, pretty_print: bool = ...) -> str:
        """serializeWorkItemToJSON(self: _pdg.GraphContext, work_item: PDG_WorkItem, pretty_print: bool = False) -> str

        [unsafe] Serializes the workitem and upstream results to a JSON file
        """
    @overload
    def serializeWorkItems(self) -> str:
        """serializeWorkItems(*args, **kwargs)
        Overloaded function.

        1. serializeWorkItems(self: _pdg.GraphContext) -> str

        Serializes the work items and dependencies in the given context

        2. serializeWorkItems(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes the work items and dependencies in the given context
        to a given file. Extra code can be passed in to include at the
        top of the serialized file.
        """
    @overload
    def serializeWorkItems(self, arg0: str, arg1: str) -> None:
        """serializeWorkItems(*args, **kwargs)
        Overloaded function.

        1. serializeWorkItems(self: _pdg.GraphContext) -> str

        Serializes the work items and dependencies in the given context

        2. serializeWorkItems(self: _pdg.GraphContext, arg0: str, arg1: str) -> None

        Serializes the work items and dependencies in the given context
        to a given file. Extra code can be passed in to include at the
        top of the serialized file.
        """
    def setDefaultScheduler(self, arg0: str) -> bool:
        """setDefaultScheduler(self: _pdg.GraphContext, arg0: str) -> object

        [cmd] Sets the graph context's default scheduler
        """
    @typing.overload
    def setExpression(self, arg0: str, arg1: str, arg2: str, arg3: int) -> bool: ...
    @typing.overload
    def setExpression(self, arg0: str, arg1: str, arg2: str, arg3: int, arg4: bool) -> bool: ...
    def setScheduler(self, arg0: str, arg1: str) -> bool:
        """setScheduler(self: _pdg.GraphContext, arg0: str, arg1: str) -> object

        [cmd] Assigns a node's scheduler override
        """
    def undo(self) -> None:
        """undo(self: _pdg.GraphContext) -> None

        Undoes the last command or committed chunk
        """
    def waitAllEvents(self) -> None:
        """waitAllEvents(self: _pdg.GraphContext) -> None

        Waits all queued events to be emitted
        """
    @property
    def canceling(self) -> bool: ...
    @property
    def chunkDepth(self) -> int: ...
    @property
    def commandDescriptions(self) -> str: ...
    @property
    def cookOptions(self) -> CookOptions: ...
    @property
    def cookSet(self) -> list[Node]: ...
    @property
    def cooking(self) -> bool: ...
    @property
    def defaultScheduler(self) -> Scheduler: ...
    @property
    def graph(self) -> Graph: ...
    @property
    def name(self) -> str: ...
    @property
    def schedulers(self) -> list[SchedulerBase]: ...
    @property
    def stateCount(self) -> int: ...
    # The methods pdg/context.py adds. The extra arguments of addNode, addScheduler and
    # addDependency go to the python type's constructor.
    def addDependency(self, type_name: str, node_name: str, key: str, *args: Any, **kwargs: Any) -> Dependency: ...
    def addFileDependency(self, node_name: str, file_name: str) -> Dependency: ...
    def addNode(self, type_name: str, name: str = ..., *args: Any, **kwargs: Any) -> Node: ...
    def addScheduler(self, type_name: str, name: str = ..., *args: Any, **kwargs: Any) -> SchedulerBase: ...
    def deserializeWorkItems(self, filepath: str) -> None: ...
    def setExpressions(self, name: str, expressions: Mapping[str, str] | None, **kwargs: str) -> None: ...
    def setParameter(
        self, name: str, param_name: str, value: _ParmValue, index: int = ..., param_type: argType = ...
    ) -> None: ...
    def setParameters(self, name: str, parameters: Mapping[str, _ParmValue] | None, **kwargs: _ParmValue) -> None: ...
    def setValue(self, node: str, port: str, value: _ParmValue, index: int = ...) -> None: ...
    def setValues(self, name: str, values: Mapping[str, _ParmValue] | None, **kwargs: _ParmValue) -> None: ...

class IgnoreAttributeWarningsBlock:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __enter__(self) -> None:
        """__enter__(self: _pdg.IgnoreAttributeWarningsBlock) -> None"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdg.IgnoreAttributeWarningsBlock, arg0: object, arg1: object, arg2: object) -> bool"""

class InjectBlock:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __enter__(self) -> WorkItemHolder:
        """__enter__(self: _pdg.InjectBlock) -> PDG_WorkItemHolder"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdg.InjectBlock, arg0: object, arg1: object, arg2: object) -> bool"""

class JobScriptInfo:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def command(self) -> str: ...
    @property
    def extraArgs(self) -> str: ...
    @property
    def isApplyWedges(self) -> bool: ...
    @property
    def isMainThread(self) -> bool: ...
    @property
    def isNative(self) -> bool: ...
    @property
    def isStandardScript(self) -> bool: ...
    @property
    def moduleName(self) -> str: ...
    @property
    def pythonExecutable(self) -> str: ...
    @property
    def serviceTypeNames(self) -> list[str]: ...

class LockAttributesBlock:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __enter__(self) -> AttributeOwner:
        """__enter__(self: _pdg.LockAttributesBlock) -> PDG_AttributeOwner"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdg.LockAttributesBlock, arg0: object, arg1: object, arg2: object) -> bool"""

class Mapper(Node):
    def __init__(self, *, no_constructor: Never) -> None: ...

class MemoryInfo:
    attributeMemory: int
    graphMemory: int
    nodeMemory: int
    workItemMemory: int
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def totalMemory(self) -> int: ...

class Node(NodeInterface, EventEmitter):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def appendDirty(self, arg0: WorkItemDirty) -> None:
        """appendDirty(self: _pdg.Node, arg0: PDG_WorkItemDirty) -> None

        Appends the work items from this node to an existing
        pdg.WorkItemDirty object
        """
    def cancel(self) -> None:
        """cancel(self: _pdg.Node) -> None

        Cancels all work items associated with this node
        """
    def cook(self, arg0: bool) -> bool:
        """cook(self: _pdg.Node, arg0: bool) -> bool

        Cooks the graph down to this node, either as a blocking cook or a
        non-blocking cook depending on the parameter. This is a utility
        method for cooking the graph context with the pdg.cookType.Node
        option and this node as an argument
        """
    def cookError(self, arg0: str) -> None:
        """cookError(self: _pdg.Node, arg0: str) -> None

        Issues a cook error that appears as an Error event

        """
    def cookWarning(self, arg0: str) -> None:
        """cookWarning(self: _pdg.Node, arg0: str) -> None

        Issues a cook warning that appears as a Warning event

        """
    def dirty(self, arg0: bool) -> None:
        """dirty(self: _pdg.Node, arg0: bool) -> None

        Deletes the node's workitems
        """
    def memoryUsage(self) -> MemoryInfo:
        """memoryUsage(self: _pdg.Node) -> _pdg.MemoryInfo

        Returns memory usage info about the node
        """
    def nodeOptions(self, arg0: bool) -> NodeOptions:
        """nodeOptions(self: _pdg.Node, arg0: bool) -> _pdg.NodeOptions

        Returns the current node options for this instance
        """
    def outputFiles(self, arg0: bool) -> list[File]:
        """outputFiles(self: _pdg.Node, arg0: bool) -> UT_Array[_pdg.File]

        Returns the aggregate output files for all workitems on the node
        """
    def prepareDirty(self) -> WorkItemDirty:
        """prepareDirty(self: _pdg.Node) -> PDG_WorkItemDirty

        Prepares a pdg.WorkItemDirty object for the node's workitems
        """
    def reserveIndexBlock(self, arg0: int) -> int:
        """reserveIndexBlock(self: _pdg.Node, arg0: int) -> int

        Reserves a blcok of work item indices
        """
    def resultData(self, arg0: bool) -> list[File]:
        """resultData(self: _pdg.Node, arg0: bool) -> UT_Array[_pdg.File]

        [deprecated] Returns the aggregate output files for all workitems on the node
        """
    def stats(self) -> NodeStats:
        """stats(self: _pdg.Node) -> _pdg.NodeStats

        Returns the stat object for the node
        """
    def __rshift__(self, other: _NodeT) -> _NodeT:
        """__rshift__(self: _pdg.Node, arg0: _pdg.Node) -> object

        Connects a node 'output' port to another node's 'input' port
        """
    @property
    def context(self) -> GraphContext: ...
    @property
    def dependencies(self) -> list[Dependency]: ...
    @property
    def hasErrors(self) -> bool: ...
    @property
    def isCooked(self) -> bool: ...
    @property
    def isDynamic(self) -> bool: ...
    @property
    def isDynamicGenerator(self) -> bool: ...
    @property
    def loopDepth(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def nodeType(self) -> _pdg.nodeType: ...
    @property
    def partitions(self) -> WorkItemList: ...
    @property
    def regenerateReason(self) -> _pdg.regenerateReason: ...
    @property
    def scheduler(self) -> Scheduler: ...
    @property
    def serviceName(self) -> str: ...
    @property
    def type(self) -> NodeCallbackType: ...
    @property
    def workItems(self) -> WorkItemList: ...
    # The methods pdg/node.py adds. connect and disconnect take port names: they pass the ports
    # through str(), which for a Port gives `node.port`, not a name the node has.
    def addDependency(self, type_name: str, dep_key: str) -> Dependency: ...
    def addFileDependency(self, file_name: str) -> Dependency: ...
    def addParameter(self, name: str, label: str, tag: str | Sequence[str], param_type: dataType, size: int = ...) -> Port: ...
    def connect(self, out_port: str, node: Node, in_port: str) -> tuple[Port, Port]: ...
    def disconnect(self, out_port: str, node: Node, in_port: str) -> bool: ...
    def removeDependency(self, dep_key: str) -> bool: ...
    def setExpression(self, param_name: str, expression: str, index: int = ..., multiline: bool = ...) -> bool: ...
    def setExpressions(self, expressions: Mapping[str, str] | None = ..., **kwargs: str) -> None: ...
    def setParameter(self, name: str, value: _ParmValue, index: int = ...) -> None: ...
    def setParameters(self, parameters: Mapping[str, _ParmValue] | None = ..., **kwargs: _ParmValue) -> None: ...
    def setScheduler(self, scheduler_name: str) -> bool: ...
    def setValue(self, param_name: str, value: _ParmValue, index: int = ...) -> None: ...
    def setValues(self, values: Mapping[str, _ParmValue] | None = ..., **kwargs: _ParmValue) -> None: ...
    def __setitem__(self, key: str, value: Port | _ParmValue) -> None: ...

class NodeCallbackType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def isStaticGenerator(self) -> bool: ...
    @property
    def template(self) -> NodeInterface: ...

class NodeInterface:
    topNode: ClassVar[Callable[[NodeInterface], hou.TopNode | None]] = ...
    def __init__(self, *, no_constructor: Never) -> None: ...
    def default(self, arg0: str) -> _PortValue | None:
        """default(self: _pdg.NodeInterface, arg0: str) -> object

        Returns the default value assigned to a parameter
        """
    @overload
    def input(self, arg0: int) -> Port | None:
        """input(*args, **kwargs)
        Overloaded function.

        1. input(self: _pdg.NodeInterface, arg0: int) -> PDG_Port

        Returns the ith input port of the node

        2. input(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the input for a given port name
        """
    @overload
    def input(self, arg0: str) -> Port | None:
        """input(*args, **kwargs)
        Overloaded function.

        1. input(self: _pdg.NodeInterface, arg0: int) -> PDG_Port

        Returns the ith input port of the node

        2. input(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the input for a given port name
        """
    def inputsForNode(self, arg0: Node) -> list[Port]:
        """inputsForNode(self: PDG_Node, arg0: PDG_Node) -> list

        Returns the ports on this node that are connected to the given
        node, or the empty list if there are no connections
        """
    def inputsForWorkItem(self, arg0: WorkItem) -> list[Port]:
        """inputsForWorkItem(self: PDG_Node, arg0: PDG_WorkItem) -> list

        Returns the ports on this node that are connected to the node
        associated with the given work item, or the empty list if there
        are no connections
        """
    def isItemFromPort(self, arg0: WorkItem, arg1: str) -> bool:
        """isItemFromPort(self: _pdg.NodeInterface, arg0: PDG_WorkItem, arg1: str) -> bool

        Returns True if the work item was passed to this node via the
        specified port name
        """
    @overload
    def output(self, arg0: int) -> Port | None:
        """output(*args, **kwargs)
        Overloaded function.

        1. output(self: _pdg.NodeInterface, arg0: int) -> PDG_Port

        Returns the ith output port of the node

        2. output(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the output for a given port name
        """
    @overload
    def output(self, arg0: str) -> Port | None:
        """output(*args, **kwargs)
        Overloaded function.

        1. output(self: _pdg.NodeInterface, arg0: int) -> PDG_Port

        Returns the ith output port of the node

        2. output(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the output for a given port name
        """
    def parameter(self, name: str, multi: int = ...) -> Port | None:
        """parameter(self: _pdg.NodeInterface, name: str, multi: int = -1) -> PDG_Port

        Returns a parameter port with a specified name
        """
    def parametersForTag(self, arg0: str) -> list[Port]:
        """parametersForTag(self: _pdg.NodeInterface, arg0: str) -> list

        Returns a list of parameters for a given tag
        """
    @overload
    def port(self, arg0: portType, arg1: int) -> Port | None:
        """port(*args, **kwargs)
        Overloaded function.

        1. port(self: _pdg.NodeInterface, arg0: PDG_PortType, arg1: int) -> PDG_Port

        Returns the port with at an index and port type

        2. port(self: _pdg.NodeInterface, arg0: PDG_PortType, arg1: str) -> PDG_Port

        Returns the port with a specified name and port type

        3. port(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the port with the specified name
        """
    @overload
    def port(self, arg0: portType, arg1: str) -> Port | None:
        """port(*args, **kwargs)
        Overloaded function.

        1. port(self: _pdg.NodeInterface, arg0: PDG_PortType, arg1: int) -> PDG_Port

        Returns the port with at an index and port type

        2. port(self: _pdg.NodeInterface, arg0: PDG_PortType, arg1: str) -> PDG_Port

        Returns the port with a specified name and port type

        3. port(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the port with the specified name
        """
    @overload
    def port(self, arg0: str) -> Port | None:
        """port(*args, **kwargs)
        Overloaded function.

        1. port(self: _pdg.NodeInterface, arg0: PDG_PortType, arg1: int) -> PDG_Port

        Returns the port with at an index and port type

        2. port(self: _pdg.NodeInterface, arg0: PDG_PortType, arg1: str) -> PDG_Port

        Returns the port with a specified name and port type

        3. port(self: _pdg.NodeInterface, arg0: str) -> PDG_Port

        Returns the port with the specified name
        """
    def portCount(self, arg0: portType) -> int:
        """portCount(self: _pdg.NodeInterface, arg0: PDG_PortType) -> int

        Returns the number of ports of a given port type
        """
    def ports(self, arg0: portType) -> list[Port]:
        """ports(self: _pdg.NodeInterface, arg0: PDG_PortType) -> list[PDG_Port]

        Returns a list of ports for a given port type
        """
    def value(self, arg0: str) -> _PortValue | None:
        """value(self: _pdg.NodeInterface, arg0: str) -> object

        Returns the value assigned to a parameter
        """
    def __getitem__(self, index: str) -> Port:
        """__getitem__(self: _pdg.NodeInterface, arg0: object) -> PDG_Port

        Returns the port with the specified name
        """
    def __iter__(self) -> None:
        """__iter__(self: _pdg.NodeInterface) -> object

        nodes are not iterabled
        """
    @property
    def attributeInfo(self) -> AttributeInfo: ...
    @property
    def commonVars(self) -> dict[str, str]: ...
    @property
    def customId(self) -> int: ...
    @property
    def customParameters(self) -> list[Port]: ...
    @property
    def inputCount(self) -> int: ...
    @property
    def inputNames(self) -> list[str]: ...
    @property
    def inputs(self) -> list[Port]: ...
    @property
    def outputCount(self) -> int: ...
    @property
    def outputNames(self) -> list[str]: ...
    @property
    def outputs(self) -> list[Port]: ...
    @property
    def parameterCount(self) -> int: ...
    @property
    def parameterNames(self) -> list[str]: ...
    @property
    def parameters(self) -> list[Port]: ...
    @property
    def scriptInfo(self) -> JobScriptInfo: ...
    @property
    def templateName(self) -> str: ...
    @property
    def topNodeId(self) -> int: ...

class NodeOptions:
    allowDuplicateOutputs: bool
    description: str
    isAlwaysRegenerate: bool
    isClearFailures: bool
    isCompressWorkItemData: bool
    isDirtyOnIncomplete: bool
    isDirtyOnRegenerate: bool
    requiresCookedInputs: bool
    requiresEndBlock: bool
    requiresGeneratedInputs: bool
    requiresInputData: bool
    requiresSceneFile: bool
    serviceBlockCookType: _pdg.serviceBlockCookType
    serviceName: str
    stateFilter: list[workItemState]
    usesDynamicBatching: bool
    usesSharedServers: bool
    def __init__(self, *, no_constructor: Never) -> None: ...
    def setInputAttrib(self, arg0: str, arg1: attribOrigin | int) -> None:
        """setInputAttrib(self: _pdg.NodeOptions, arg0: str, arg1: int) -> None

        Sets the origin of the specified input attribute name
        """
    def setInputAttribDefault(self, arg0: attribOrigin | int) -> None:
        """setInputAttribDefault(self: _pdg.NodeOptions, arg0: int) -> None

        Sets the default origin for input attributes
        """
    def setOutputAttrib(self, arg0: str, arg1: attribOrigin | int) -> None:
        """setOutputAttrib(self: _pdg.NodeOptions, arg0: str, arg1: int) -> None

        Sets the origin of the specified output attribute name
        """
    def setOutputAttribDefault(self, arg0: attribOrigin | int) -> None:
        """setOutputAttribDefault(self: _pdg.NodeOptions, arg0: int) -> None

        Sets the default origin for output attributes
        """
    def setPortOrigin(self, arg0: str, arg1: int) -> None:
        """setPortOrigin(self: _pdg.NodeOptions, arg0: str, arg1: int) -> None

        Sets the evaluation origin for the specified parameter port name
        """
    @property
    def inputAttribs(self) -> AttributeConfig: ...
    @property
    def outputAttribs(self) -> AttributeConfig: ...
    @property
    def portOrigins(self) -> dict[str, int]: ...

class NodeStats:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def stat(self, arg0: nodeStatType) -> float:
        """stat(self: _pdg.NodeStats, arg0: _pdg.nodeStatType) -> float

        Returns the value for the specified node stat
        """
    def stateCount(self, arg0: workItemState) -> int:
        """stateCount(self: _pdg.NodeStats, arg0: PDG_WorkItemState) -> int

        Returns the total number of work items in the specified state
        """
    def workItemCount(self) -> int:
        """workItemCount(self: _pdg.NodeStats) -> int

        Returns the total number of work items in the node
        """
    @property
    def cookCount(self) -> int: ...
    @property
    def totalCookTime(self) -> float: ...
    @property
    def wallclockCookTime(self) -> float: ...

class PartitionHolder:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addItemToAllPartitions(self, arg0: WorkItem) -> None:
        """addItemToAllPartitions(self: _pdg.PartitionHolder, arg0: PDG_WorkItem) -> None

        Marks an item as being in all partitions on the node
        """
    @overload
    def addItemToPartition(self, work_item: WorkItem, index: int, required: bool = ...) -> None:
        """addItemToPartition(*args, **kwargs)
        Overloaded function.

        1. addItemToPartition(self: _pdg.PartitionHolder, work_item: PDG_WorkItem, index: int, required: bool = False) -> None

        Adds a work item to the partition with a given index. If the
        partition does not yet exist, a new one with that index is
        automatically created

        2. addItemToPartition(self: _pdg.PartitionHolder, work_item: PDG_WorkItem, named: str, required: bool = False) -> None

        Adds a work item to the partition with a given named. If the
        partition does not yet exist, a new one with that name is
        automatically created
        """
    @overload
    def addItemToPartition(self, work_item: WorkItem, named: str, required: bool = ...) -> None:
        """addItemToPartition(*args, **kwargs)
        Overloaded function.

        1. addItemToPartition(self: _pdg.PartitionHolder, work_item: PDG_WorkItem, index: int, required: bool = False) -> None

        Adds a work item to the partition with a given index. If the
        partition does not yet exist, a new one with that index is
        automatically created

        2. addItemToPartition(self: _pdg.PartitionHolder, work_item: PDG_WorkItem, named: str, required: bool = False) -> None

        Adds a work item to the partition with a given named. If the
        partition does not yet exist, a new one with that name is
        automatically created
        """
    @overload
    def setPartitionFrame(self, arg0: int, arg1: float) -> None:
        """setPartitionFrame(*args, **kwargs)
        Overloaded function.

        1. setPartitionFrame(self: _pdg.PartitionHolder, arg0: int, arg1: float) -> None

        Sets the frame of the partition with the given index

        2. setPartitionFrame(self: _pdg.PartitionHolder, arg0: str, arg1: float) -> None

        Sets the frame of the partition with the given name
        """
    @overload
    def setPartitionFrame(self, arg0: str, arg1: float) -> None:
        """setPartitionFrame(*args, **kwargs)
        Overloaded function.

        1. setPartitionFrame(self: _pdg.PartitionHolder, arg0: int, arg1: float) -> None

        Sets the frame of the partition with the given index

        2. setPartitionFrame(self: _pdg.PartitionHolder, arg0: str, arg1: float) -> None

        Sets the frame of the partition with the given name
        """
    @property
    def isSplitting(self) -> bool: ...
    @property
    def maxIndex(self) -> int: ...
    @property
    def splitAttribute(self) -> str: ...
    @property
    def splitMissing(self) -> list[WorkItem]: ...
    @property
    def splitValue(self) -> str: ...

class Partitioner(Node):
    def __init__(self, *, no_constructor: Never) -> None: ...

class PathMap:
    AllZone: ClassVar[str] = ...
    LinuxZone: ClassVar[str] = ...
    MacZone: ClassVar[str] = ...
    WindowsZone: ClassVar[str] = ...
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addPathMapping(self, zone: str, mapFrom: str, mapTo: str, createdBy: str = ..., matchType: pathMapMatchType = ...) -> None:
        """addPathMapping(self: _pdg.PathMap, zone: str, mapFrom: str, mapTo: str, createdBy: str = '', matchType: _pdg.pathMapMatchType = <pathMapMatchType.Contains: 0>) -> None

        Adds an entry to the path mapping table
        """
    def clearAllMappings(self) -> None:
        """clearAllMappings(self: _pdg.PathMap) -> None

        Clears all path mapping entries
        """
    def clearSchedulerMappings(self, arg0: str) -> None:
        """clearSchedulerMappings(self: _pdg.PathMap, arg0: str) -> None

        Clears path map entries added by the scheduler with the
        specified path
        """
    @staticmethod
    def edit() -> PathMapEditBlock:
        """edit() -> _pdg.PathMapEditBlock

        Returns a context manager that commits changes to the global path
        map when it concludes
        """
    @staticmethod
    def mapPath(path: str, zone: str) -> str:
        """mapPath(path: str, zone: str) -> str

        Returns the mapped version of the given path for the given zone
        """
    @staticmethod
    def mapPathToLocal(path: str) -> str:
        """mapPathToLocal(path: str) -> str

        Returns the mapped version of the given path for the local zone
        """
    @staticmethod
    def mappingZone() -> str:
        """mappingZone() -> str

        Returns the local mapping zone
        """
    @overload
    @staticmethod
    def mappings() -> list[PathMapEntry]:
        """mappings(*args, **kwargs)
        Overloaded function.

        1. mappings() -> UT_Array[_pdg.PathMapEntry]

        Returns the list of path mapping entries

        2. mappings(zone: str = '', createdBy: str = '') -> UT_Array[_pdg.PathMapEntry]

        Returns the list of path mappings filtered by the specified zone
        and/or scheduler
        """
    @overload
    @staticmethod
    def mappings(zone: str = ..., createdBy: str = ...) -> list[PathMapEntry]:
        """mappings(*args, **kwargs)
        Overloaded function.

        1. mappings() -> UT_Array[_pdg.PathMapEntry]

        Returns the list of path mapping entries

        2. mappings(zone: str = '', createdBy: str = '') -> UT_Array[_pdg.PathMapEntry]

        Returns the list of path mappings filtered by the specified zone
        and/or scheduler
        """
    @staticmethod
    def pathMapJSON() -> str:
        """pathMapJSON() -> str

        Returns the PDG Path Map as a JSON string
        """
    @staticmethod
    def setMappingZone(zone: str) -> None:
        """setMappingZone(zone: str) -> None

        Sets the local mapping zone
        """
    @staticmethod
    def setPathMapJSON(json_string: str, merge: bool = ...) -> None:
        """setPathMapJSON(json_string: str, merge: bool = False) -> None

        Sets the PDG Path Map from a JSON string
        """

class PathMapEditBlock:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __enter__(self) -> PathMap:
        """__enter__(self: _pdg.PathMapEditBlock) -> PDG_PathMap"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdg.PathMapEditBlock, arg0: object, arg1: object, arg2: object) -> bool"""

class PathMapEntry:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def createdBy(self) -> str: ...
    @property
    def mapFrom(self) -> str: ...
    @property
    def mapTo(self) -> str: ...
    @property
    def matchType(self) -> pathMapMatchType: ...
    @property
    def zone(self) -> str: ...

class Port:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def evaluate(self, work_item: WorkItem | None = ...) -> _PortValue:
        """evaluate(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression value of the port with respect to a
        specfic workitem
        """
    @overload
    def evaluateBool(self, work_item: WorkItem | None = ...) -> bool | tuple[bool, ...]:
        """evaluateBool(*args, **kwargs)
        Overloaded function.

        1. evaluateBool(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as an bool or bool tuple with respect to
        a specific work item

        2. evaluateBool(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as an bool for a particular index with
        respect to a specific work item

        3. evaluateBool(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as an bool for a particular index
        """
    @overload
    def evaluateBool(self, arg0: WorkItem, arg1: int) -> bool:
        """evaluateBool(*args, **kwargs)
        Overloaded function.

        1. evaluateBool(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as an bool or bool tuple with respect to
        a specific work item

        2. evaluateBool(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as an bool for a particular index with
        respect to a specific work item

        3. evaluateBool(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as an bool for a particular index
        """
    @overload
    def evaluateBool(self, arg0: int) -> int:
        """evaluateBool(*args, **kwargs)
        Overloaded function.

        1. evaluateBool(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as an bool or bool tuple with respect to
        a specific work item

        2. evaluateBool(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as an bool for a particular index with
        respect to a specific work item

        3. evaluateBool(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as an bool for a particular index
        """
    @overload
    def evaluateFloat(self, work_item: WorkItem | None = ...) -> float | tuple[float, ...]:
        """evaluateFloat(*args, **kwargs)
        Overloaded function.

        1. evaluateFloat(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a float or float tuple with respect
        to a specific work item

        2. evaluateFloat(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a float for a particular index with
        respect to a specific work item

        3. evaluateFloat(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a float for a particular index
        """
    @overload
    def evaluateFloat(self, arg0: WorkItem, arg1: int) -> float:
        """evaluateFloat(*args, **kwargs)
        Overloaded function.

        1. evaluateFloat(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a float or float tuple with respect
        to a specific work item

        2. evaluateFloat(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a float for a particular index with
        respect to a specific work item

        3. evaluateFloat(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a float for a particular index
        """
    @overload
    def evaluateFloat(self, arg0: int) -> float:
        """evaluateFloat(*args, **kwargs)
        Overloaded function.

        1. evaluateFloat(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a float or float tuple with respect
        to a specific work item

        2. evaluateFloat(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a float for a particular index with
        respect to a specific work item

        3. evaluateFloat(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a float for a particular index
        """
    @overload
    def evaluateInt(self, work_item: WorkItem | None = ...) -> int | tuple[int, ...]:
        """evaluateInt(*args, **kwargs)
        Overloaded function.

        1. evaluateInt(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as an int or int tuple with respect to
        a specific work item

        2. evaluateInt(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as an int for a particular index with
        respect to a specific work item

        3. evaluateInt(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as an int for a particular index
        """
    @overload
    def evaluateInt(self, arg0: WorkItem, arg1: int) -> int:
        """evaluateInt(*args, **kwargs)
        Overloaded function.

        1. evaluateInt(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as an int or int tuple with respect to
        a specific work item

        2. evaluateInt(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as an int for a particular index with
        respect to a specific work item

        3. evaluateInt(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as an int for a particular index
        """
    @overload
    def evaluateInt(self, arg0: int) -> int:
        """evaluateInt(*args, **kwargs)
        Overloaded function.

        1. evaluateInt(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as an int or int tuple with respect to
        a specific work item

        2. evaluateInt(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as an int for a particular index with
        respect to a specific work item

        3. evaluateInt(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as an int for a particular index
        """
    @overload
    def evaluateRawString(self, work_item: WorkItem | None = ...) -> str | tuple[str, ...]:
        """evaluateRawString(*args, **kwargs)
        Overloaded function.

        1. evaluateRawString(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a string with respect to a specific
        work item, without expression expansion

        2. evaluateRawString(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a string for a particular index,
        without expression expansion

        3. evaluateRawString(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a string for a particular index with
        respect to a specific work item, without expression expansion
        """
    @overload
    def evaluateRawString(self, arg0: WorkItem, arg1: int) -> str:
        """evaluateRawString(*args, **kwargs)
        Overloaded function.

        1. evaluateRawString(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a string with respect to a specific
        work item, without expression expansion

        2. evaluateRawString(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a string for a particular index,
        without expression expansion

        3. evaluateRawString(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a string for a particular index with
        respect to a specific work item, without expression expansion
        """
    @overload
    def evaluateRawString(self, arg0: int) -> str:
        """evaluateRawString(*args, **kwargs)
        Overloaded function.

        1. evaluateRawString(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a string with respect to a specific
        work item, without expression expansion

        2. evaluateRawString(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a string for a particular index,
        without expression expansion

        3. evaluateRawString(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a string for a particular index with
        respect to a specific work item, without expression expansion
        """
    @overload
    def evaluateString(self, work_item: WorkItem | None = ...) -> str | tuple[str, ...]:
        """evaluateString(*args, **kwargs)
        Overloaded function.

        1. evaluateString(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a string with respect to a specific
        work item

        2. evaluateString(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a string for a particular index

        3. evaluateString(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a string for a particular index with
        respect to a specific work item
        """
    @overload
    def evaluateString(self, arg0: WorkItem, arg1: int) -> str:
        """evaluateString(*args, **kwargs)
        Overloaded function.

        1. evaluateString(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a string with respect to a specific
        work item

        2. evaluateString(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a string for a particular index

        3. evaluateString(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a string for a particular index with
        respect to a specific work item
        """
    @overload
    def evaluateString(self, arg0: int) -> str:
        """evaluateString(*args, **kwargs)
        Overloaded function.

        1. evaluateString(self: _pdg.Port, work_item: PDG_WorkItem = None) -> object

        The evaluated expression as a string with respect to a specific
        work item

        2. evaluateString(self: _pdg.Port, arg0: PDG_WorkItem, arg1: int) -> object

        The evaluated expression as a string for a particular index

        3. evaluateString(self: _pdg.Port, arg0: int) -> object

        The evaluated expression as a string for a particular index with
        respect to a specific work item
        """
    def expression(self, arg0: int) -> str:
        """expression(self: _pdg.Port, arg0: int) -> str

        The expresson bound to the port, or empty string if no
        expression has been set.
        """
    def hasExpression(self, arg0: int) -> bool:
        """hasExpression(self: _pdg.Port, arg0: int) -> bool

        Returns True if the port has an expression assigned for the
        given index, else returns False
        """
    def hasTag(self, arg0: str) -> bool:
        """hasTag(self: _pdg.Port, arg0: str) -> bool

        Returns true if the port has the tag, else False

        """
    def __rshift__(self, other: Port) -> Port:
        """__rshift__(self: _pdg.Port, arg0: object) -> object

        Connects two ports together, equivalent to B = A 
        """
    @property
    def connections(self) -> list[Port]: ...
    @property
    def dataType(self) -> _pdg.dataType: ...
    @property
    def defaultValue(self) -> _PortValue: ...
    @property
    def expressionAttribs(self) -> list[str]: ...
    @property
    def expressionVars(self) -> dict[str, str]: ...
    @property
    def hasWorkItemExpression(self) -> bool: ...
    @property
    def isBuiltin(self) -> bool: ...
    @property
    def isCustom(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def node(self) -> Node: ...
    @property
    def portType(self) -> _pdg.portType: ...
    @property
    def size(self) -> int: ...
    @property
    def tags(self) -> list[str]: ...
    @property
    def value(self) -> _PortValue: ...

class Processor(Node):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def injectStaticItems(self) -> InjectBlock:
        """injectStaticItems(self: _pdg.Processor) -> _pdg.InjectBlock

        Returns a static injection holder, to be used with a Python
        context block
        """
    @property
    def cookType(self) -> workItemCookType: ...
    @property
    def staticWorkItems(self) -> WorkItemList: ...

class PyBaseObject:
    def __init__(self, *, no_constructor: Never) -> None: ...

class PyDeferredTask(DeferredTask, Generic[_R_co]):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def wait(self) -> _R_co | None:
        """wait(self: _pdg.PyDeferredTask) -> object

        Waits for the task to compelete
        """
    @property
    def errors(self) -> str: ...
    @property
    def result(self) -> _R_co | None: ...

class PyDependencyType(DependencyType, PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def typeObject(self) -> type[PyDependency]: ...

class PyEventHandler(EventHandler):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def callback(self) -> _EventCallback: ...

class PyNodeCallbackType(NodeCallbackType, PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def reload(self) -> None:
        """reload(self: _pdg.PyNodeCallbackType) -> None"""
    def setCustomCallback(self, arg0: str, arg1: Callable[..., object]) -> None:
        """setCustomCallback(self: _pdg.PyNodeCallbackType, arg0: str, arg1: object) -> None

        Adds a custom callback that takes priority over the ones defined
        by the underlying python object
        """
    @property
    def typeObject(self) -> type[PyNode]: ...

class PySchedulerType(SchedulerType, PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def reload(self) -> None:
        """reload(self: _pdg.PySchedulerType) -> None"""
    @property
    def typeObject(self) -> type[PyScheduler]: ...

class PyWorkItemData(WorkItemData):
    def __init__(self, *, no_constructor: Never) -> None: ...

class PyWorkItemDataType(WorkItemDataType, PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def typeObject(self) -> type[PyWorkItem]: ...

class RemoveDependencyResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class RenameNodeResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class Scheduler(SchedulerBase):
    def __init__(self, *, no_constructor: Never) -> None: ...

class SchedulerBase(TypeInstance, NodeInterface, EventEmitter):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def applicationBin(self, arg0: str, arg1: WorkItem) -> str:
        """applicationBin(self: _pdg.SchedulerBase, arg0: str, arg1: PDG_WorkItem) -> str

        Returns the full path to an executable for the given name.
        """
    def cleanTempDirectory(self) -> None:
        """cleanTempDirectory(self: _pdg.SchedulerBase) -> None

        Deletes the temporary directory and its contents.
        """
    def clearSharedServerInfo(self, arg0: str) -> None:
        """clearSharedServerInfo(self: _pdg.SchedulerBase, arg0: str) -> None

        Clears the meta data for an existing sharedserver instance
        """
    def cookError(self, arg0: str) -> None:
        """cookError(self: _pdg.SchedulerBase, arg0: str) -> None

        Issues a cook error that appears as an Error event

        """
    def cookWarning(self, arg0: str) -> None:
        """cookWarning(self: _pdg.SchedulerBase, arg0: str) -> None

        Issues a cook warning that appears as a Warning event

        """
    def cookWorkItem(self, arg0: WorkItem) -> bool:
        """cookWorkItem(self: _pdg.SchedulerBase, arg0: PDG_WorkItem) -> bool

        Cooks the specified work item
        """
    def dataDir(self, arg0: bool) -> str:
        """dataDir(self: _pdg.SchedulerBase, arg0: bool) -> str

        Returns the local or remote data directory path
        """
    def delocalizePath(self, arg0: str) -> str:
        """delocalizePath(self: _pdg.SchedulerBase, arg0: str) -> str

        Delocalizes a local file path to be based on __PDG_DIR__ if possible

        """
    def dependencyGraph(self, expand: bool = ...) -> _DependencyGraph:
        """dependencyGraph(self: _pdg.SchedulerBase, expand: bool = True) -> object

        Returns a tuple contain a map for work item->dependencies,work item->depenedents and a list of ready items
        """
    def endSharedServer(self, arg0: str) -> bool:
        """endSharedServer(self: _pdg.SchedulerBase, arg0: str) -> bool

        Closes an existing sharedserver instance
        """
    def evaluateBoolOverride(self, arg0: Node, arg1: str, arg2: str, arg3: WorkItem, arg4: bool) -> bool:
        """evaluateBoolOverride(self: _pdg.SchedulerBase, arg0: _pdg.Node, arg1: str, arg2: str, arg3: PDG_WorkItem, arg4: bool) -> object

        Evaluates a boolean parameter override, given a node and scheduler
        """
    def evaluateFloatOverride(self, arg0: Node, arg1: str, arg2: str, arg3: WorkItem, arg4: float) -> float:
        """evaluateFloatOverride(self: _pdg.SchedulerBase, arg0: _pdg.Node, arg1: str, arg2: str, arg3: PDG_WorkItem, arg4: float) -> object

        Evaluates a floating point parameter override, given a node and scheduler
        """
    def evaluateIntOverride(self, arg0: Node, arg1: str, arg2: str, arg3: WorkItem, arg4: int) -> int:
        """evaluateIntOverride(self: _pdg.SchedulerBase, arg0: _pdg.Node, arg1: str, arg2: str, arg3: PDG_WorkItem, arg4: int) -> object

        Evaluates an integer parameter override, given a node and scheduler
        """
    def evaluateStringOverride(self, arg0: Node, arg1: str, arg2: str, arg3: WorkItem, arg4: str) -> str:
        """evaluateStringOverride(self: _pdg.SchedulerBase, arg0: _pdg.Node, arg1: str, arg2: str, arg3: PDG_WorkItem, arg4: str) -> object

        Evaluates a floating point paramter override, given a node andscheduler
        """
    def expandCommandTokens(self, arg0: str, arg1: WorkItem) -> str:
        """expandCommandTokens(self: _pdg.SchedulerBase, arg0: str, arg1: PDG_WorkItem) -> str

        Expands special tokens in the command string
        """
    @overload
    def formatTransferPath(self, local_path: str, default_type: fileTransferType = ..., local: bool = ..., check_type: bool = ...) -> str:
        """formatTransferPath(*args, **kwargs)
        Overloaded function.

        1. formatTransferPath(self: _pdg.SchedulerBase, local_path: str, default_type: _pdg.fileTransferType = <fileTransferType.TempDir: 0>, local: bool = True, check_type: bool = True) -> str

        Returns the destination path for a local file transferd using
        the standard file transfer logic on this scheduler.

        2. formatTransferPath(self: _pdg.SchedulerBase, root_path: str, local_path: str, sub_path: str = '', default_type: _pdg.fileTransferType = <fileTransferType.TempDir: 0>, local: bool = True, check_type: bool = True) -> str

        Returns the destination path for a local file transferd using
        the standard file transfer logic on this scheduler. The path
        to the file relative to the root is preserved
        """
    @overload
    def formatTransferPath(self, root_path: str, local_path: str, sub_path: str = ..., default_type: fileTransferType = ..., local: bool = ..., check_type: bool = ...) -> str:
        """formatTransferPath(*args, **kwargs)
        Overloaded function.

        1. formatTransferPath(self: _pdg.SchedulerBase, local_path: str, default_type: _pdg.fileTransferType = <fileTransferType.TempDir: 0>, local: bool = True, check_type: bool = True) -> str

        Returns the destination path for a local file transferd using
        the standard file transfer logic on this scheduler.

        2. formatTransferPath(self: _pdg.SchedulerBase, root_path: str, local_path: str, sub_path: str = '', default_type: _pdg.fileTransferType = <fileTransferType.TempDir: 0>, local: bool = True, check_type: bool = True) -> str

        Returns the destination path for a local file transferd using
        the standard file transfer logic on this scheduler. The path
        to the file relative to the root is preserved
        """
    @staticmethod
    def getDefaultUserEnvironment() -> dict[str, str]:
        """getDefaultUserEnvironment() -> dict[str, str]

        Returns the default user environment.
        """
    def getLogURI(self, arg0: WorkItem) -> str:
        """getLogURI(self: _pdg.SchedulerBase, arg0: PDG_WorkItem) -> str

        returns a URI for the workitem cook log (text file)

        """
    def getPollingClient(self, *args: Never, **kwargs: Never) -> PDGNPollingClient | None:
        """getPollingClient(self: _pdg.SchedulerBase) -> PDGN::PDGN_PollingClientNNG

        Returns the MQ polling client for this scheduler, if applicable
        """
    def getSharedServerInfo(self, arg0: str) -> _SharedServerInfo | None:
        """getSharedServerInfo(self: _pdg.SchedulerBase, arg0: str) -> PDG_ValueArgs

        Gets the meta data for an existing sharedserver instance
        """
    def getSharedServers(self) -> list[str]:
        """getSharedServers(self: _pdg.SchedulerBase) -> UT_Array[str]

        Gets the list of sharedservers with metadata
        """
    def getStatusURI(self, arg0: WorkItem) -> str:
        """getStatusURI(self: _pdg.SchedulerBase, arg0: PDG_WorkItem) -> str

        returns a URI for the workitem status page if relevant

        """
    def isWorkItemReady(self, arg0: int, arg1: int) -> workItemReadyResult:
        """isWorkItemReady(self: _pdg.SchedulerBase, arg0: int, arg1: int) -> _pdg.workItemReadyResult

        Returns true if a work item is ready to cook, else false
        """
    def jobName(self, arg0: WorkItem) -> str:
        """jobName(self: _pdg.SchedulerBase, arg0: PDG_WorkItem) -> str

        Returns the job name for a specified work item
        """
    def localizePath(self, arg0: str) -> str:
        """localizePath(self: _pdg.SchedulerBase, arg0: str) -> str

        Localizes a remote file path

        """
    def logDir(self, arg0: bool) -> str:
        """logDir(self: _pdg.SchedulerBase, arg0: bool) -> str

        Returns the local or remote log directory path
        """
    @staticmethod
    def maxThreads() -> int:
        """maxThreads() -> int

        Returns the number of logical CPU cores available to the process.
        """
    def onWorkItemAddOutput(self, id: int, index: int, data: str, tag: str, hash_code: int, active_only: bool = ...) -> None:
        """onWorkItemAddOutput(self: _pdg.SchedulerBase, id: int, index: int, data: str, tag: str, hash_code: int, active_only: bool = False) -> None

        Informs the scheduler that a work item produced an output file
        """
    @overload
    def onWorkItemAddOutputs(self, id: int, index: int, data: Sequence[str], tag: str, hash_codes: Sequence[int], active_only: bool = ...) -> None:
        """onWorkItemAddOutputs(*args, **kwargs)
        Overloaded function.

        1. onWorkItemAddOutputs(self: _pdg.SchedulerBase, id: int, index: int, data: UT_Array[str], tag: str, hash_codes: UT_Array[int], active_only: bool = False) -> None

        Informs the scheduler that a work item produced an array of 
         output files

        2. onWorkItemAddOutputs(self: _pdg.SchedulerBase, id: int, index: int, data: UT_Array[str], tag: UT_Array[str], hash_codes: UT_Array[int], active_only: bool = False) -> None

        Informs the scheduler that a work item produced an array of 
         output files
        """
    @overload
    def onWorkItemAddOutputs(self, id: int, index: int, data: Sequence[str], tag: Sequence[str], hash_codes: Sequence[int], active_only: bool = ...) -> None:
        """onWorkItemAddOutputs(*args, **kwargs)
        Overloaded function.

        1. onWorkItemAddOutputs(self: _pdg.SchedulerBase, id: int, index: int, data: UT_Array[str], tag: str, hash_codes: UT_Array[int], active_only: bool = False) -> None

        Informs the scheduler that a work item produced an array of 
         output files

        2. onWorkItemAddOutputs(self: _pdg.SchedulerBase, id: int, index: int, data: UT_Array[str], tag: UT_Array[str], hash_codes: UT_Array[int], active_only: bool = False) -> None

        Informs the scheduler that a work item produced an array of 
         output files
        """
    def onWorkItemAppendLog(self, arg0: int, arg1: int, arg2: str, arg3: workItemLogType) -> None:
        """onWorkItemAppendLog(self: _pdg.SchedulerBase, arg0: int, arg1: int, arg2: str, arg3: PDG_WorkItemLogType) -> None

        Returns true if a work item is ready to cook, else false
        """
    def onWorkItemCanceled(self, arg0: int, arg1: int) -> None:
        """onWorkItemCanceled(self: _pdg.SchedulerBase, arg0: int, arg1: int) -> None

        Informs the scheduler that a work item was canceled
        """
    def onWorkItemFailed(self, arg0: int, arg1: int) -> None:
        """onWorkItemFailed(self: _pdg.SchedulerBase, arg0: int, arg1: int) -> None

        Informs the scheduler that a work item failed
        """
    def onWorkItemInvalidateCache(self, id: int, index: int) -> None:
        """onWorkItemInvalidateCache(self: _pdg.SchedulerBase, id: int, index: int) -> None

        Informs the scheduler that a work item's cache should be invalidated
        """
    def onWorkItemSetCookPercent(self, arg0: int, arg1: int, arg2: float) -> None:
        """onWorkItemSetCookPercent(self: _pdg.SchedulerBase, arg0: int, arg1: int, arg2: float) -> None

        Sets a cook percentage on the work item
        """
    def onWorkItemSetCustomState(self, arg0: int, arg1: int, arg2: str) -> None:
        """onWorkItemSetCustomState(self: _pdg.SchedulerBase, arg0: int, arg1: int, arg2: str) -> None

        Sets a custom state string on the work item
        """
    @overload
    def onWorkItemSetDictAttrib(self, id: int, index: int, attribute_name: str, values: Sequence[Dictionary]) -> None:
        """onWorkItemSetDictAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetDictAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[_pdg.Dictionary]) -> None

        Informs the scheduler that a work item produced a result file

        2. onWorkItemSetDictAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: _pdg.Dictionary, attrib_index: int) -> None

        Informs the scheduler that a work item produced a dictionary attrib
        """
    @overload
    def onWorkItemSetDictAttrib(self, id: int, index: int, attribute_name: str, value: Dictionary, attrib_index: int) -> None:
        """onWorkItemSetDictAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetDictAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[_pdg.Dictionary]) -> None

        Informs the scheduler that a work item produced a result file

        2. onWorkItemSetDictAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: _pdg.Dictionary, attrib_index: int) -> None

        Informs the scheduler that a work item produced a dictionary attrib
        """
    @overload
    def onWorkItemSetFileAttrib(self, id: int, index: int, attribute_name: str, values: Sequence[File]) -> None:
        """onWorkItemSetFileAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetFileAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[_pdg.File]) -> None

        Informs the scheduler that a work item produced a result file

        2. onWorkItemSetFileAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: _pdg.File, attrib_index: int) -> None

        Informs the scheduler that a work item produced a result file
        """
    @overload
    def onWorkItemSetFileAttrib(self, id: int, index: int, attribute_name: str, value: File, attrib_index: int) -> None:
        """onWorkItemSetFileAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetFileAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[_pdg.File]) -> None

        Informs the scheduler that a work item produced a result file

        2. onWorkItemSetFileAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: _pdg.File, attrib_index: int) -> None

        Informs the scheduler that a work item produced a result file
        """
    @overload
    def onWorkItemSetFloatAttrib(self, id: int, index: int, attribute_name: str, values: Sequence[float]) -> None:
        """onWorkItemSetFloatAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetFloatAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[float]) -> None

        Informs the scheduler that a work item produced a float attribute

        2. onWorkItemSetFloatAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: float, attrib_index: int) -> None

        Informs the scheduler that a work item produced a float attribute
        """
    @overload
    def onWorkItemSetFloatAttrib(self, id: int, index: int, attribute_name: str, value: float, attrib_index: int) -> None:
        """onWorkItemSetFloatAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetFloatAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[float]) -> None

        Informs the scheduler that a work item produced a float attribute

        2. onWorkItemSetFloatAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: float, attrib_index: int) -> None

        Informs the scheduler that a work item produced a float attribute
        """
    @overload
    def onWorkItemSetIntAttrib(self, id: int, index: int, attribute_name: str, values: Sequence[int]) -> None:
        """onWorkItemSetIntAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetIntAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[int]) -> None

        Informs the scheduler that a work item produced an int attribute

        2. onWorkItemSetIntAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: int, attrib_index: int) -> None

        Informs the scheduler that a work item produced an int attribute
        """
    @overload
    def onWorkItemSetIntAttrib(self, id: int, index: int, attribute_name: str, value: int, attrib_index: int) -> None:
        """onWorkItemSetIntAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetIntAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[int]) -> None

        Informs the scheduler that a work item produced an int attribute

        2. onWorkItemSetIntAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: int, attrib_index: int) -> None

        Informs the scheduler that a work item produced an int attribute
        """
    def onWorkItemSetPyObjectAttrib(self, id: int, index: int, attribute_name: str, value: str) -> None:
        """onWorkItemSetPyObjectAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: str) -> None

        Informs the scheduler that a work item produced a python object attribute.
        The given string should be a valid repr()
        """
    @overload
    def onWorkItemSetStringAttrib(self, id: int, index: int, attribute_name: str, values: Sequence[str]) -> None:
        """onWorkItemSetStringAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetStringAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[str]) -> None

        Informs the scheduler that a work item produced a string attribute

        2. onWorkItemSetStringAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: str, attrib_index: int) -> None

        Informs the scheduler that a work item produced a string attribute
        """
    @overload
    def onWorkItemSetStringAttrib(self, id: int, index: int, attribute_name: str, value: str, attrib_index: int) -> None:
        """onWorkItemSetStringAttrib(*args, **kwargs)
        Overloaded function.

        1. onWorkItemSetStringAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, values: UT_Array[str]) -> None

        Informs the scheduler that a work item produced a string attribute

        2. onWorkItemSetStringAttrib(self: _pdg.SchedulerBase, id: int, index: int, attribute_name: str, value: str, attrib_index: int) -> None

        Informs the scheduler that a work item produced a string attribute
        """
    def onWorkItemStartCook(self, id: int, index: int, clear_outputs: bool = ...) -> None:
        """onWorkItemStartCook(self: _pdg.SchedulerBase, id: int, index: int, clear_outputs: bool = False) -> None

        Informs the scheduler that a work item has begun executing
        """
    def onWorkItemSucceeded(self, arg0: int, arg1: int, arg2: float) -> None:
        """onWorkItemSucceeded(self: _pdg.SchedulerBase, arg0: int, arg1: int, arg2: float) -> None

        Informs the scheduler that a work item finished cooking
        """
    @staticmethod
    def platform() -> _pdg.platform:
        """platform() -> PDG_Platform

        Returns the current pdg.platform value for the system
        """
    @staticmethod
    def postExecProcess(arg0: int) -> None:
        """postExecProcess(arg0: int) -> None

        Should be called to configure a local subprocess after it has been started. Ensures that the subprocess lifetime is tied to the parent
        """
    @staticmethod
    def preExecProcess() -> None:
        """preExecProcess() -> None

        Should be called in a local subprocess just before child is executed (Posix only). Creates a new session and assigns with the groupid equal to the new pid, for use will os.killpg.  This ensures that the entire subprocess tree can be cleaned up.  Also ensures that the subprocess lifetime is tied to the parent with a SIGTERM being sent to the subprocess when the parent dies
        """
    def scriptDir(self, arg0: bool) -> str:
        """scriptDir(self: _pdg.SchedulerBase, arg0: bool) -> str

        Returns the local or remote script directory path (__PDG_SCRIPTDIR__)
        """
    def setAcceptInProcess(self, arg0: bool) -> None:
        """setAcceptInProcess(self: _pdg.SchedulerBase, arg0: bool) -> None

        Sets where or not the scheduler accepts in-process work items.
        """
    def setScriptDir(self, arg0: str, arg1: str) -> None:
        """setScriptDir(self: _pdg.SchedulerBase, arg0: str, arg1: str) -> None

        Sets the values of the local and remote script directory paths (__PDG_SCRIPTDIR__), \t     by default this is __PDG_TEMP__/scripts
        """
    def setSharedServerInfo(self, arg0: str, arg1: dict[str, Any] | _SharedServerInfo) -> str:
        """setSharedServerInfo(self: _pdg.SchedulerBase, arg0: str, arg1: PDG_ValueArgs) -> str

        Sets the meta data for an existing sharedserver instance
        """
    def setTempDir(self, arg0: str, arg1: str) -> None:
        """setTempDir(self: _pdg.SchedulerBase, arg0: str, arg1: str) -> None

        Sets the values of the local and remote temp directory paths (__PDG_TEMP__), \t     by default this is __PDG_DIR__/pdgtemp/<PID>
        """
    def setWorkingDir(self, arg0: str, arg1: str) -> None:
        """setWorkingDir(self: _pdg.SchedulerBase, arg0: str, arg1: str) -> None

        Sets the values of the local and remote working directory paths (__PDG_DIR__)
        """
    def startService(self, arg0: str, arg1: Service) -> bool:
        """startService(self: _pdg.SchedulerBase, arg0: str, arg1: PDG_Service) -> bool

        Starts the provided service with this scheduler
        """
    def stopService(self, arg0: str, arg1: Service, arg2: bool) -> bool:
        """stopService(self: _pdg.SchedulerBase, arg0: str, arg1: PDG_Service, arg2: bool) -> bool

        Stops a service that was started by this scheduler
        """
    def submitAsJob(self, arg0: str, arg1: str) -> str:
        """submitAsJob(self: _pdg.SchedulerBase, arg0: str, arg1: str) -> str

        Submit the current 

        """
    def tempDir(self, arg0: bool) -> str:
        """tempDir(self: _pdg.SchedulerBase, arg0: bool) -> str

        Returns the local or remote temp directory path (__PDG_TEMP__)
        """
    def transferFile(self, local_path: str, default_type: fileTransferType = ..., check_type: bool = ...) -> bool:
        """transferFile(*args, **kwargs)
        Overloaded function.

        1. transferFile(self: _pdg.SchedulerBase, local_path: str, default_type: _pdg.fileTransferType = <fileTransferType.TempDir: 0>, check_type: bool = True) -> bool

        Transfers the specified file to the scheduler's working dir


        2. transferFile(self: _pdg.SchedulerBase, root_path: str, local_path: str, sub_path: str, default_type: _pdg.fileTransferType = <fileTransferType.TempDir: 0>, check_type: bool = True) -> bool

        Transfers the specified file to the scheduler's working dir,
        and preserves the directory structure of the local file relative
        to the specified root directory
        """
    def workingDir(self, arg0: bool) -> str:
        """workingDir(self: _pdg.SchedulerBase, arg0: bool) -> str

        Returns the local or remote working directory path (__PDG_DIR__)
        """
    @property
    def context(self) -> GraphContext: ...
    @property
    def isCompressWorkItemData(self) -> bool: ...
    @property
    def isWaitForFailures(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def workItemDataSource(self) -> _pdg.workItemDataSource: ...
    # pdg/__init__.py's. The other arguments go to the function; waiting gives its result, or None
    # if the cook is canceled first. A `work_item` keyword is taken out of them, so those
    # overloads can't check them against the function (a ParamSpec can't leave out a keyword).
    @overload
    def runOnMainThread(self, wait: Literal[True], function: Callable[..., _R], *args: Any, work_item: WorkItem | None, **kwargs: Any) -> _R | None: ...
    @overload
    def runOnMainThread(self, wait: Literal[False], function: Callable[..., _R], *args: Any, work_item: WorkItem | None, **kwargs: Any) -> PyDeferredTask[_R]: ...
    @overload
    def runOnMainThread(self, wait: Literal[True], function: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R | None: ...
    @overload
    def runOnMainThread(self, wait: Literal[False], function: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> PyDeferredTask[_R]: ...
    @overload
    def runOnMainThread(self, wait: bool, function: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R | PyDeferredTask[_R] | None: ...

class SchedulerType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def parm_category(self) -> str: ...

class ScriptWorkItemData(WorkItemData):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def setScript(self, arg0: str) -> None:
        """setScript(self: _pdg.ScriptWorkItemData, arg0: str) -> None

        Sets the work item's script
        """
    @property
    def script(self) -> str: ...

class Service(TypeInstance):
    clientLogDir: str
    clientLogType: serviceClientLogType
    connectionTimeout: int
    data: Dictionary
    envVarNames: list[str]
    envVarValues: list[str]
    extraArguments: list[str]
    isAutoStart: bool
    isPersistent: bool
    memoryLimit: int
    memoryResetType: serviceResetType
    mqLogDir: str
    mqLogLevel: int
    mqPort: int
    mqUrl: str
    owner: serviceOwner
    poolSize: int
    port: int
    schedulerTypeName: str
    serviceSchedulerType: _pdg.serviceSchedulerType
    state: serviceState
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addClients(self, scheduler: SchedulerBase | None = ...) -> ServiceAddClientsBlock:
        """addClients(self: _pdg.Service, scheduler: _pdg.SchedulerBase = None) -> _pdg.ServiceAddClientsBlock

        Allows the service to accept new clients for the duration of the
        scoped block
        """
    def addPendingClient(self, arg0: str, arg1: int, arg2: int) -> ServiceClientInfo:
        """addPendingClient(self: _pdg.Service, arg0: str, arg1: int, arg2: int) -> _pdg.ServiceClientInfo

        Adds a pending service client, which will be waited on when
        calling pdg.Service.waitForClients
        """
    def clearScheduler(self) -> None:
        """clearScheduler(self: _pdg.Service) -> None

        Clears the scheduler associated with the service. The scheduler
        must be set again before the service can be started.
        """
    def client(self, arg0: str) -> ServiceClientInfo | None:
        """client(self: _pdg.Service, arg0: str) -> _pdg.ServiceClientInfo

        This methods returns the client info for the specified name

        """
    def getCommand(self, arg0: str, arg1: int, arg2: int) -> str:
        """getCommand(self: _pdg.Service, arg0: str, arg1: int, arg2: int) -> str

        Returns a service client's command string, which can be used by
        the caller to start the client process. It is the responsibility
        of the caller to expand any environment variables in the command
        string.
        """
    def getCommandArgs(self, arg0: str, arg1: int, arg2: int) -> list[str]:
        """getCommandArgs(self: _pdg.Service, arg0: str, arg1: int, arg2: int) -> list

        Returns a service client's command as a list of arguments, which
        can be used by the caller to start the client process. It is the
        responsibility of the caller to expand any environment variables
        in the command string.
        """
    def getPollingClient(self, *args: Never, **kwargs: Never) -> PDGNPollingClient | None:
        """getPollingClient(self: _pdg.Service) -> PDGN::PDGN_PollingClientNNG

        Returns the polling client for this service, or None if there is none
        """
    def getServiceClientName(self, arg0: int) -> str:
        """getServiceClientName(self: _pdg.Service, arg0: int) -> str

        This method returns the name of the client for the provided
        client number.
        """
    def schedulerContextName(self) -> str:
        """schedulerContextName(self: _pdg.Service) -> str

        Returns the name of the graph context of the scheduler
        associated with the service.
        """
    def schedulerName(self) -> str:
        """schedulerName(self: _pdg.Service) -> str

        Returns the name of the scheduler associated with the service
        """
    def setScheduler(self, arg0: str, arg1: str) -> None:
        """setScheduler(self: _pdg.Service, arg0: str, arg1: str) -> None

        Stores the name of the scheduler instance and its graph context
        associated with the service, which is used to stop and start the
        the service.
        """
    def stop(self, arg0: bool, arg1: bool) -> bool:
        """stop(self: _pdg.Service, arg0: bool, arg1: bool) -> bool

        Stops the service, including the MQ server and all clients.
        """
    @property
    def clients(self) -> list[str]: ...
    @property
    def command(self) -> str: ...
    @property
    def isInternal(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def runningScheduler(self) -> SchedulerBase | None: ...
    @property
    def script(self) -> str: ...

class ServiceAddClientsBlock:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __enter__(self) -> Service:
        """__enter__(self: _pdg.ServiceAddClientsBlock) -> PDG_Service"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self: _pdg.ServiceAddClientsBlock, arg0: object, arg1: object, arg2: object) -> bool"""

class ServiceClientInfo:
    id: int
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def address(self) -> str: ...
    @property
    def commandArgs(self) -> list[str]: ...
    @property
    def commandString(self) -> str: ...
    @property
    def isActive(self) -> bool: ...
    @property
    def isConnected(self) -> bool: ...
    @property
    def lock(self) -> int: ...
    @property
    def logPath(self) -> str: ...
    @property
    def memoryUsage(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def number(self) -> int: ...
    @property
    def port(self) -> int: ...
    @property
    def totalCooks(self) -> int: ...

class ServiceError(Exception): ...

class ServiceManager(EventEmitter):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def deregisterService(self, arg0: str) -> None:
        """deregisterService(self: _pdg.ServiceManager, arg0: str) -> None

        De-registers a service from the manager
        """
    @staticmethod
    def get() -> ServiceManager:
        """get() -> _pdg.ServiceManager

        Returns the static service manager instance
        """
    def getService(self, arg0: str) -> Service | None:
        """getService(self: _pdg.ServiceManager, arg0: str) -> _pdg.Service

        Returns the service if it is found by the service manager
        """
    def hasServiceSupport(self, arg0: SchedulerType) -> bool:
        """hasServiceSupport(self: _pdg.ServiceManager, arg0: _pdg.SchedulerType) -> bool

        Returns whether the scheduler type supports PDG services
        """
    def killClient(self, service_name: str, client_name: str = ...) -> bool:
        """killClient(self: _pdg.ServiceManager, service_name: str, client_name: str = '') -> bool

        Kills a client in a running service
        """
    def killService(self, name: str, ignore_stopped: bool = ...) -> bool:
        """killService(self: _pdg.ServiceManager, name: str, ignore_stopped: bool = False) -> bool

        Kills a registered service
        """
    def registerService(self, type_name: str, service_name: str, pool_size: int, port: int, auto_start: bool, client_logging_dir: str, mqserver_log_level: int = ..., mqserver_log_dir: str = ..., connection_timeout: int = ..., client_logging_type: serviceClientLogType = ..., persistent: bool = ...) -> Service:
        """registerService(self: _pdg.ServiceManager, type_name: str, service_name: str, pool_size: int, port: int, auto_start: bool, client_logging_dir: str, mqserver_log_level: int = 0, mqserver_log_dir: str = '$HOUDINI_TEMP_DIR', connection_timeout: int = 5000, client_logging_type: _pdg.serviceClientLogType = <serviceClientLogType.File: 2>, persistent: bool = True) -> _pdg.Service

        Registers a service
        """
    def registerSessionService(self, type_name: str, name: str, pool_size: int, port: int, auto_start: bool, client_log_dir: str, mqserver_log_level: int = ..., mqserver_log_dir: str = ..., connection_timeout: int = ..., client_logging_type: serviceClientLogType = ..., persistent: bool = ...) -> Service:
        """registerSessionService(self: _pdg.ServiceManager, type_name: str, name: str, pool_size: int, port: int, auto_start: bool, client_log_dir: str, mqserver_log_level: int = 0, mqserver_log_dir: str = '$HOUDINI_TEMP_DIR', connection_timeout: int = 5000, client_logging_type: _pdg.serviceClientLogType = <serviceClientLogType.File: 2>, persistent: bool = True) -> _pdg.Service

        Registers a session service
        """
    @overload
    def registeredServiceNames(self) -> list[str]:
        """registeredServiceNames(*args, **kwargs)
        Overloaded function.

        1. registeredServiceNames(self: _pdg.ServiceManager) -> UT_Array[str]

        Returns a list of the names of all the registered services

        2. registeredServiceNames(self: _pdg.ServiceManager, arg0: _pdg.serviceOwner) -> UT_Array[str]

        Returns a list of the names of all the registered services
        with the specified service owner
        """
    @overload
    def registeredServiceNames(self, arg0: serviceOwner) -> list[str]:
        """registeredServiceNames(*args, **kwargs)
        Overloaded function.

        1. registeredServiceNames(self: _pdg.ServiceManager) -> UT_Array[str]

        Returns a list of the names of all the registered services

        2. registeredServiceNames(self: _pdg.ServiceManager, arg0: _pdg.serviceOwner) -> UT_Array[str]

        Returns a list of the names of all the registered services
        with the specified service owner
        """
    def resetClient(self, service_name: str, client_name: str = ...) -> bool:
        """resetClient(self: _pdg.ServiceManager, service_name: str, client_name: str = '') -> bool

        Resets a client in a running service
        """
    def resetService(self, service_name: str, client_name: str = ...) -> bool:
        """resetService(self: _pdg.ServiceManager, service_name: str, client_name: str = '') -> bool

        [deprecated] Resets a registered service
        """
    def restartClient(self, service_name: str, client_name: str = ...) -> bool:
        """restartClient(self: _pdg.ServiceManager, service_name: str, client_name: str = '') -> bool

        Restarts a client in a running service
        """
    def resumeService(self, name: str, context: GraphContext | None = ...) -> bool:
        """resumeService(self: _pdg.ServiceManager, name: str, context: _pdg.GraphContext = None) -> bool

        Resumes any stopped clients in the service
        """
    @staticmethod
    def saveRegisteredServices() -> None:
        """saveRegisteredServices() -> None

        Saves the user's registered services
        """
    def startService(self, name: str, context: GraphContext | None = ..., background: bool = ..., allow_running: bool = ...) -> bool:
        """startService(self: _pdg.ServiceManager, name: str, context: _pdg.GraphContext = None, background: bool = False, allow_running: bool = False) -> bool

        Starts a registered service
        """
    def stopClient(self, service_name: str, client_name: str = ...) -> bool:
        """stopClient(self: _pdg.ServiceManager, service_name: str, client_name: str = '') -> bool

        Stops a client in a running service
        """
    def stopService(self, name: str, ignore_stopped: bool = ...) -> bool:
        """stopService(self: _pdg.ServiceManager, name: str, ignore_stopped: bool = False) -> bool

        Stops a registered service
        """

class ServiceType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def command(self) -> str: ...
    @property
    def isInternal(self) -> bool: ...

class SetDefaultSchedulerResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class SetExpressionResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class SetSchedulerResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class SetValueResult(Command):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def result(self) -> bool: ...

class TransferPair:
    def __init__(self, arg0: transferResult, arg1: int) -> None:
        """__init__(self: _pdg.TransferPair, arg0: _pdg.transferResult, arg1: int) -> None

        Constructs a new transfer pair
        """
    @staticmethod
    def cached() -> TransferPair:
        """cached() -> _pdg.TransferPair

        Constructs a transfer pair with a cached result
        """
    @staticmethod
    def failure() -> TransferPair:
        """failure() -> _pdg.TransferPair

        Constructs a transfer pair with a failure result
        """
    @staticmethod
    def skip() -> TransferPair:
        """skip() -> _pdg.TransferPair

        Constructs a transfer pair with a skip result
        """
    @staticmethod
    def success(cache_id: int = ...) -> TransferPair:
        """success(cache_id: int = 0) -> _pdg.TransferPair

        Constructs a transfer pair with a success result
        """
    @property
    def cacheId(self) -> int: ...
    @property
    def result(self) -> transferResult: ...

class TypeInstance:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def type(self) -> BaseType: ...
    @property
    def typeName(self) -> str: ...

class TypeRegistry(BaseTypeRegistry):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addExtensionTag(self, arg0: str, arg1: str) -> None:
        """addExtensionTag(self: _pdg.TypeRegistry, arg0: str, arg1: str) -> None

        Adds an extension -> file tag mapping
        """
    def addParentType(self, arg0: BaseType, arg1: str) -> None:
        """addParentType(self: _pdg.TypeRegistry, arg0: _pdg.BaseType, arg1: str) -> None

        Adds a single parent types to an existing registered type
        """
    def addParentTypes(self, arg0: BaseType, arg1: Sequence[str]) -> None:
        """addParentTypes(self: _pdg.TypeRegistry, arg0: _pdg.BaseType, arg1: UT_Array[str]) -> None

        Adds parent types to an existing registered type
        """
    def addTag(self, arg0: str) -> None:
        """addTag(self: _pdg.TypeRegistry, arg0: str) -> None

        Adds a tag without a corresponding file extension
        """
    def addTagViewer(self, tag: str, viewer: str, multiviewer: bool = ...) -> None:
        """addTagViewer(self: _pdg.TypeRegistry, tag: str, viewer: str, multiviewer: bool = False) -> None

        Adds an extenstion -> file tag mapping
        """
    def extToTag(self, arg0: str, arg1: str) -> str:
        """extToTag(self: _pdg.TypeRegistry, arg0: str, arg1: str) -> object

        Returns the result tag for a given file extension and default tag
        """
    def filteredTags(self, arg0: str) -> list[str]:
        """filteredTags(self: _pdg.TypeRegistry, arg0: str) -> object

        Returns the filtered, sorted set of file tags with thespecified prefix
        """
    @staticmethod
    def findFile(arg0: str) -> str | None:
        """findFile(arg0: str) -> object

        Returns an absolute file path to a file on the PDG search path,
        or None of no file with the given name exists
        """
    @staticmethod
    def globFiles(search: str, subdirectory: str, full_path: bool = ...) -> list[str]:
        """globFiles(search: str, subdirectory: str, full_path: bool = False) -> object

        Returns the list of all file paths matching a search pattern in
        the PDG search path
        """
    @staticmethod
    def globPythonModules(unique: bool = ..., full_path: bool = ...) -> list[str]:
        """globPythonModules(unique: bool = True, full_path: bool = False) -> object

        Return the list of all .py files in the types subpath

        """
    def isMultiViewer(self, arg0: str) -> bool:
        """isMultiViewer(self: _pdg.TypeRegistry, arg0: str) -> bool

        Returns true if the application used to view the tag supportsopening multiple files
        """
    def isViewable(self, arg0: str) -> bool:
        """isViewable(self: _pdg.TypeRegistry, arg0: str) -> object

        Returns true if the tag is viewable
        """
    @staticmethod
    def moduleSkipList() -> list[str]:
        """moduleSkipList() -> object

        Returns the list of file and directory names to skip when
        importing Python modules
        """
    def nodeCallbackType(self, arg0: str) -> NodeCallbackType | None:
        """nodeCallbackType(self: _pdg.TypeRegistry, arg0: str) -> _pdg.NodeCallbackType

        Returns the node callback type with the specified name, or None
        """
    def pathToExt(self, arg0: str) -> str:
        """pathToExt(self: _pdg.TypeRegistry, arg0: str) -> object

        Returns the full extension for the given path possibly including a known achive suffix, for example bgeo.sc 
        """
    def pathToTag(self, arg0: str) -> str:
        """pathToTag(self: _pdg.TypeRegistry, arg0: str) -> object

        Returns the result tag for a given file path
        """
    def pathToViewer(self, arg0: str) -> str:
        """pathToViewer(self: _pdg.TypeRegistry, arg0: str) -> object

        Returns the viewer application for a given file path
        """
    def registerCacheHandler(self, arg0: str, arg1: Callable[[str, File, WorkItem], cacheResult]) -> None:
        """registerCacheHandler(self: _pdg.TypeRegistry, arg0: str, arg1: object) -> None

        Registers a custom Python cache handler function
        """
    def registerDSOTypes(self, arg0: str) -> bool:
        """registerDSOTypes(self: _pdg.TypeRegistry, arg0: str) -> bool

        Register PDG types from a shared library
        """
    def registerDirtyHandler(self, handler: Callable[..., object], handler_type: dirtyHandlerType = ..., scheduler_filter: Sequence[str] = ..., node_filter: Sequence[str] = ..., requires_outputs: bool = ..., is_global: bool = ...) -> None:
        """registerDirtyHandler(self: _pdg.TypeRegistry, handler: object, handler_type: _pdg.dirtyHandlerType = <dirtyHandlerType.Any: 0>, scheduler_filter: UT_Set[str] = [], node_filter: UT_Set[str] = [], requires_outputs: bool = False, is_global: bool = False) -> None

        Registers a custom Python delete handler function
        """
    def registerHashHandler(self, arg0: str, arg1: Callable[[str, File, WorkItem], int]) -> None:
        """registerHashHandler(self: _pdg.TypeRegistry, arg0: str, arg1: object) -> None

        [Deprecated] Registers a custom Python hash function for hashing files
        """
    def registerModuleTypes(self, module: ModuleType, quiet: bool = ...) -> None:
        """registerModuleTypes(self: _pdg.TypeRegistry, module: object, quiet: bool = False) -> None

        Registers types from the specified Python module
        """
    def registerNode(self, type_object: type[PyNode], node_type: nodeType, name: str = ..., label: str = ..., category: str = ..., static_gen: bool = ..., sub_type: nodeSubtype = ...) -> PyNodeCallbackType:
        """registerNode(self: _pdg.TypeRegistry, type_object: object, node_type: _pdg.nodeType, name: str = '', label: str = '', category: str = '', static_gen: bool = True, sub_type: _pdg.nodeSubtype = <nodeSubtype.Normal: 0>) -> _pdg.BaseType

        Register a Python node type for use with PDG constructs
        """
    def registerPreflightHandler(self, handler: Callable[[GraphContext, CookOptions], bool], generate_graph: bool = ...) -> None:
        """registerPreflightHandler(self: _pdg.TypeRegistry, handler: object, generate_graph: bool = False) -> None

        Register a custom Python preflight handler function
        """
    def registerPythonPath(self, arg0: str, arg1: bool) -> None:
        """registerPythonPath(self: _pdg.TypeRegistry, arg0: str, arg1: bool) -> None

        Registers a Python module at an absolute path
        """
    def registerRegenerationHandler(self, arg0: Callable[[Node, list[WorkItem]], regenerateResult]) -> None:
        """registerRegenerationHandler(self: _pdg.TypeRegistry, arg0: object) -> None"""
    def registerScheduler(self, type_object: type[PyScheduler], name: str = ..., label: str = ..., parm_category: str = ..., node_category: str = ...) -> PySchedulerType:
        """registerScheduler(self: _pdg.TypeRegistry, type_object: object, name: str = '', label: str = '', parm_category: str = '', node_category: str = 'Schedulers') -> _pdg.BaseType

        Register a Python scheduler type for use with PDG constructs
        """
    def registerService(self, type_name: str, type_label: str, command: str, script: str, internal: bool = ...) -> ServiceType:
        """registerService(self: _pdg.TypeRegistry, type_name: str, type_label: str, command: str, script: str, internal: bool = False) -> PDG_ServiceType

        Registers a PDG service
        """
    def registerStatHandler(self, arg0: str, arg1: Callable[[str, File, WorkItem], int | tuple[int, int]]) -> None:
        """registerStatHandler(self: _pdg.TypeRegistry, arg0: str, arg1: object) -> None

        Registers a custom Python hash function for stating files
        """
    def registerTransferHandler(self, tag: str, handler: Callable[[str, str, File, WorkItem | None, SchedulerBase, int], TransferPair], use_mod_time: bool = ...) -> None:
        """registerTransferHandler(self: _pdg.TypeRegistry, tag: str, handler: object, use_mod_time: bool = False) -> None

        Registers a custom Python file transfer handler function
        """
    def registerWorkItem(self, type_object: type[PyWorkItem], name: str = ..., label: str = ...) -> PyWorkItemDataType:
        """registerWorkItem(self: _pdg.TypeRegistry, type_object: object, name: str = '', label: str = '') -> _pdg.BaseType

        Register a Python work item type for use with PDG constructs
        """
    def registeredType(self, arg0: _pdg.registeredType, arg1: str) -> BaseType | None:
        """registeredType(self: _pdg.TypeRegistry, arg0: _pdg.registeredType, arg1: str) -> _pdg.BaseType

        Returns a registered type object for a given type and name
        """
    def reloadCustomHandlers(self, existing: bool = ...) -> None:
        """reloadCustomHandlers(self: _pdg.TypeRegistry, existing: bool = True) -> None

        Reloads any custom handlers on the PDG search path
        """
    def schedulerType(self, arg0: str) -> SchedulerType | None:
        """schedulerType(self: _pdg.TypeRegistry, arg0: str) -> _pdg.SchedulerType

        Returns the scheduler type with the specified name, or None
        """
    @staticmethod
    def searchPath() -> list[str]:
        """searchPath() -> object

        Returns the pdg search path

        """
    def serviceType(self, arg0: str) -> ServiceType | None:
        """serviceType(self: _pdg.TypeRegistry, arg0: str) -> PDG_ServiceType

        Returns the service type with the specified name, or None
        """
    def setDefaultWorkItem(self, arg0: WorkItemDataType) -> None:
        """setDefaultWorkItem(self: _pdg.TypeRegistry, arg0: _pdg.WorkItemDataType) -> None

        Sets system default work item type to the given type, as returned by registerWorkItem
        """
    def setPySerializationModule(self, arg0: str) -> None:
        """setPySerializationModule(self: _pdg.TypeRegistry, arg0: str) -> None

        Sets the name of the module used for Python object attribute serialization
        """
    def tagToViewer(self, arg0: str) -> str:
        """tagToViewer(self: _pdg.TypeRegistry, arg0: str) -> object

        Returns the viewer application for a given data tag
        """
    def typeNames(self, type: _pdg.registeredType, include_aliases: bool = ...) -> list[str]:
        """typeNames(self: _pdg.TypeRegistry, type: _pdg.registeredType, include_aliases: bool = False) -> UT_Array[str]

        Returns the type names for a given class of register type
        """
    @staticmethod
    def types() -> TypeRegistry:
        """types() -> _pdg.TypeRegistry

        Returns the static type registry instance
        """
    def workItemDataType(self, arg0: str) -> WorkItemDataType | None:
        """workItemDataType(self: _pdg.TypeRegistry, arg0: str) -> _pdg.WorkItemDataType

        Returns the work item data type with the specified name, or None
        """
    @property
    def pySerializationModule(self) -> str: ...
    @property
    def tags(self) -> list[str]: ...

class ValuePattern(BasePattern):
    def __init__(self, pattern: str, delimiter: str = ...) -> None:
        """__init__(self: _pdg.ValuePattern, pattern: str, delimiter: str = ' ') -> None

        Returns a new pattern object from the specified string
        """
    def componentRange(self, index: int, inclusive: bool = ...) -> list[float] | None:
        """componentRange(self: _pdg.ValuePattern, index: int, inclusive: bool = False) -> object

        Returns the value range for the specified component
        """
    def componentStep(self, index: int) -> float:
        """componentStep(self: _pdg.ValuePattern, index: int) -> float

        Returns the step size for the component
        """
    @overload
    def contains(self, value: str, inclusive: bool = ...) -> bool:
        """contains(*args, **kwargs)
        Overloaded function.

        1. contains(self: _pdg.ValuePattern, value: str, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified string

        2. contains(self: _pdg.ValuePattern, value: float, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        3. contains(self: _pdg.ValuePattern, value: int, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float
        """
    @overload
    def contains(self, value: float, inclusive: bool = ...) -> bool:
        """contains(*args, **kwargs)
        Overloaded function.

        1. contains(self: _pdg.ValuePattern, value: str, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified string

        2. contains(self: _pdg.ValuePattern, value: float, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float

        3. contains(self: _pdg.ValuePattern, value: int, inclusive: bool = False) -> bool

        Returns true if the pattern contains the specified float
        """
    def containsRange(self, value: float, inclusive: bool = ...) -> list[float] | None:
        """containsRange(*args, **kwargs)
        Overloaded function.

        1. containsRange(self: _pdg.ValuePattern, value: float, inclusive: bool = False) -> object

        Returns the matched component range if the value is in the pattern

        2. containsRange(self: _pdg.ValuePattern, value: int, inclusive: bool = False) -> object

        Returns the matched component range if the value is in the pattern
        """
    def floatArray(self, sorted: bool = ..., inclusive: bool = ...) -> list[float]:
        """floatArray(self: _pdg.ValuePattern, sorted: bool = True, inclusive: bool = False) -> UT_Array[float]

        Returns the pattern values as a float value array
        """
    def floatArrayMap(self, sorted: bool = ..., inclusive: bool = ...) -> dict[int, list[float]]:
        """floatArrayMap(self: _pdg.ValuePattern, sorted: bool = True, inclusive: bool = False) -> dict[int, UT_Array[float]]

        Returns the pattern values as a float value array
        """
    def intArray(self, sorted: bool = ..., inclusive: bool = ...) -> list[int]:
        """intArray(self: _pdg.ValuePattern, sorted: bool = True, inclusive: bool = False) -> UT_Array[int]

        Returns the pattern values as an integer value array
        """
    def intArrayMap(self, sorted: bool = ..., inclusive: bool = ...) -> dict[int, list[int]]:
        """intArrayMap(self: _pdg.ValuePattern, sorted: bool = True, inclusive: bool = False) -> dict[int, UT_Array[int]]

        Returns the pattern values as a float value array
        """
    def stringArray(self, sorted: bool = ..., inclusive: bool = ...) -> list[str]:
        """stringArray(self: _pdg.ValuePattern, sorted: bool = True, inclusive: bool = False) -> UT_Array[str]

        Returns the pattern values as a string value array
        """
    def stringArrayMap(self, sorted: bool = ..., inclusive: bool = ...) -> dict[int, list[str]]:
        """stringArrayMap(self: _pdg.ValuePattern, sorted: bool = True, inclusive: bool = False) -> dict[int, UT_Array[str]]

        Returns the pattern values as a float value array
        """
    @property
    def hasVariableStep(self) -> bool: ...
    @property
    def isNumeric(self) -> bool: ...
    @property
    def minimumStep(self) -> float: ...

class WorkItem(EventEmitter, AttributeOwner):
    class Serialization:
        activationCount: int
        activationMode: batchActivation
        baseName: str
        batchCount: int
        batchIndex: int
        batchIsDynamic: bool
        batchName: str
        batchOffset: int
        batchParentId: int
        batchParentName: str
        batchPartialCook: bool
        cloneTargetId: int
        cloneTargetName: str
        command: str
        cookType: workItemCookType
        customData: str
        customDataType: str
        environment: dict[str, _EnvValue]
        executionType: workItemExecutionType
        frame: float
        frameStep: float
        hasFrame: bool
        id: int
        index: int
        inputExpansion: int
        isClearEnvironment: bool
        isCloneResultData: bool
        isControl: bool
        isFrozen: bool
        isNoGenerate: bool
        isPostCook: bool
        isStatic: bool
        loopBeginStackIds: list[int]
        loopBeginStackIters: list[int]
        loopBeginStackLockIds: list[int]
        loopBeginStackNames: list[str]
        loopBeginStackNumbers: list[int]
        loopBeginStackSizes: list[int]
        name: str
        nodeName: str
        parentId: int
        parentName: str
        priority: int
        state: workItemState
        staticAncestorNames: list[str]
        type: workItemType
        def __init__(self, version: int = ...) -> None:
            """__init__(self: _pdg.WorkItem.Serialization, version: int = 2) -> None

            Constructs a new work item serialization struct
            """
        def fromJSON(self, arg0: str) -> bool:
            """fromJSON(self: _pdg.WorkItem.Serialization, arg0: str) -> bool

            Loads the serialization fields from a string of JSON data and returns True on success
            """
        def loadAttributes(self, data: str, save_type: attribSaveType = ..., reset: bool = ...) -> bool:
            """loadAttributes(self: _pdg.WorkItem.Serialization, data: str, save_type: _pdg.attribSaveType = <attribSaveType.Flatten: 0>, reset: bool = True) -> bool

            Loads attrbutes from a string of JSON data and returns True on success
            """
    priority: int
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addEnvironmentVar(self, arg0: str, arg1: _EnvValue) -> None:
        """addEnvironmentVar(self: _pdg.WorkItem, arg0: str, arg1: PDGT_Value) -> None

        Adds a variable to the environment associated with the work item
        """
    def addError(self, message: str, fail_task: bool = ..., timestamp: bool = ...) -> None:
        """addError(self: _pdg.WorkItem, message: str, fail_task: bool = False, timestamp: bool = True) -> None

        Writes an error to the work item's in process log buffer
        """
    def addExpectedOutputFile(self, path: str, tag: str = ..., own: bool = ...) -> None:
        """addExpectedOutputFile(self: _pdg.WorkItem, path: str, tag: str = '', own: bool = True) -> None

        Adds an expected output file to the work item, which will be checked before cooking to determine if the item is cached
        """
    def addExpectedOutputFiles(self, paths: Sequence[str], tag: str = ..., own: bool = ...) -> None:
        """addExpectedOutputFiles(self: _pdg.WorkItem, paths: UT_Array[str], tag: str = '', own: bool = True) -> None

        Adds a list of expected output file to the work item, which will be checked before cooking to determine if the item is cached
        """
    def addExpectedResultData(self, path: str, tag: str = ..., own: bool = ...) -> None:
        """addExpectedResultData(self: _pdg.WorkItem, path: str, tag: str = '', own: bool = True) -> None

        [Deprecated] Adds an expected output file to the work item, which will be checked before cooking to determine if the item is cached
        """
    def addLog(self, log_type: workItemLogType, message: str, timestamp: bool = ..., verbosity: int = ...) -> None:
        """addLog(self: _pdg.WorkItem, log_type: _pdg.workItemLogType, message: str, timestamp: bool = True, verbosity: int = 0) -> None

        Writes log data into the work item's in process log buffer
        """
    def addMessage(self, message: str, timestamp: bool = ..., verbosity: int = ...) -> None:
        """addMessage(self: _pdg.WorkItem, message: str, timestamp: bool = True, verbosity: int = 0) -> None

        Writes a log message to the work item's in process log buffer
        """
    def addOutputFile(self, path: str, tag: str = ..., hash: int = ..., own: bool = ...) -> None:
        """addOutputFile(self: _pdg.WorkItem, path: str, tag: str = '', hash: int = 0, own: bool = True) -> None

        Adds an output file to the work item
        """
    @overload
    def addOutputFiles(self, paths: Sequence[str], tag: str = ..., hashes: Sequence[int] = ..., own: bool = ...) -> None:
        """addOutputFiles(*args, **kwargs)
        Overloaded function.

        1. addOutputFiles(self: _pdg.WorkItem, paths: UT_Array[str], tag: str = '', hashes: UT_Array[int] = [], own: bool = True) -> None

        Adds a list of output files to the work item

        2. addOutputFiles(self: _pdg.WorkItem, paths: UT_Array[str], tag: UT_Array[str] = [''], hashes: UT_Array[int] = [], own: bool = True) -> None

        Adds a list of output files to the work item
        """
    @overload
    def addOutputFiles(self, paths: Sequence[str], tag: Sequence[str] = ..., hashes: Sequence[int] = ..., own: bool = ...) -> None:
        """addOutputFiles(*args, **kwargs)
        Overloaded function.

        1. addOutputFiles(self: _pdg.WorkItem, paths: UT_Array[str], tag: str = '', hashes: UT_Array[int] = [], own: bool = True) -> None

        Adds a list of output files to the work item

        2. addOutputFiles(self: _pdg.WorkItem, paths: UT_Array[str], tag: UT_Array[str] = [''], hashes: UT_Array[int] = [], own: bool = True) -> None

        Adds a list of output files to the work item
        """
    def addResultData(self, path: str, tag: str = ..., hash: int = ..., own: bool = ...) -> None:
        """addResultData(self: _pdg.WorkItem, path: str, tag: str = '', hash: int = 0, own: bool = True) -> None

        [Deprecated] Adds an output file to the work item
        """
    def addWarning(self, message: str, timestamp: bool = ..., verbosity: int = ...) -> None:
        """addWarning(self: _pdg.WorkItem, message: str, timestamp: bool = True, verbosity: int = 0) -> None

        Writes a warning to the work item's in process log buffer
        """
    def cancel(self) -> None:
        """cancel(self: _pdg.WorkItem) -> None

        Cancels the work item, if it is cooking
        """
    def checkSubItem(self) -> bool:
        """checkSubItem(self: _pdg.WorkItem) -> bool

        Checks if the specified sub item is ready to cook
        """
    def clearEnvironment(self) -> None:
        """clearEnvironment(self: _pdg.WorkItem) -> None

        Clears the environment and stops downstream items from inheritingthe upstream environment
        """
    def clearExpectedOutputFiles(self) -> None:
        """clearExpectedOutputFiles(self: _pdg.WorkItem) -> None

        Clears any expected output files on the work item
        """
    def clearExpectedOutputs(self) -> None:
        """clearExpectedOutputs(self: _pdg.WorkItem) -> None

        [deprecated] Clears any expected output files on the work item
        """
    def clearOutputFiles(self) -> None:
        """clearOutputFiles(self: _pdg.WorkItem) -> None

        Clears any output files
        """
    def clearResultData(self) -> None:
        """clearResultData(self: _pdg.WorkItem) -> None

        [deprecated] Clears any output files
        """
    def cookSubItem(self, state: workItemState = ..., duration: float = ...) -> None:
        """cookSubItem(self: _pdg.WorkItem, state: _pdg.workItemState = <workItemState.CookedSuccess: 5>, duration: float = 0) -> None

        Marks the specified sub item as cooked
        """
    def cookWarning(self, arg0: str) -> None:
        """cookWarning(self: _pdg.WorkItem, arg0: str) -> None

        Adds a warning to the node which owns this work item
        """
    def createJSONPatch(self, pretty_print: bool = ...) -> str:
        """createJSONPatch(self: _pdg.WorkItem, pretty_print: bool = False) -> str

        Creates a patch from changes to the work item's output files
        and attributes
        """
    def dirty(self, arg0: bool, arg1: bool) -> None:
        """dirty(self: _pdg.WorkItem, arg0: bool, arg1: bool) -> None

        Dirties the work item and any dependents
        """
    def envLookup(self, arg0: str) -> _EnvValue | None:
        """envLookup(self: _pdg.WorkItem, arg0: str) -> object

        Looks up a key in the environment associated with the work item
        """
    def firstOutputFileForTag(self, arg0: str) -> str:
        """firstOutputFileForTag(self: _pdg.WorkItem, arg0: str) -> str

        Returns the first output file that matches the given tag
        """
    def firstResultDataForTag(self, arg0: str) -> str:
        """firstResultDataForTag(self: _pdg.WorkItem, arg0: str) -> str

        [deprecated] Returns the first output file that matches the given tag
        """
    def hasDependency(self, arg0: WorkItem) -> bool:
        """hasDependency(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool

        Returns true if the given work item is a dependency of this
        work item
        """
    def hasEnvironmentVar(self, arg0: str) -> bool:
        """hasEnvironmentVar(self: _pdg.WorkItem, arg0: str) -> bool

        Returns true if the work item has the specified environment var.
        """
    def inputFilesForTag(self, tag: str, include_expected: bool = ...) -> list[File]:
        """inputFilesForTag(self: _pdg.WorkItem, tag: str, include_expected: bool = False) -> UT_Array[_pdg.File]

        Returns a list of input files that match the given tag
        """
    def inputResultDataForTag(self, tag: str, include_expected: bool = ...) -> list[File]:
        """inputResultDataForTag(self: _pdg.WorkItem, tag: str, include_expected: bool = False) -> UT_Array[_pdg.File]

        [deprecated] Returns a list of input files that match the given tag
        """
    def invalidateCache(self) -> None:
        """invalidateCache(self: _pdg.WorkItem) -> None

        Dirties the cache state of the work item and any downstream
        dependents. This will foce any cache-capable nodes to recook
        instead of use their cache file
        """
    @staticmethod
    def loadJSONFile(arg0: str, arg1: bool) -> WorkItem:
        """loadJSONFile(arg0: str, arg1: bool) -> _pdg.WorkItem

        Loads a work item from a JSON file
        """
    @staticmethod
    def loadJSONString(arg0: str, arg1: bool) -> WorkItem:
        """loadJSONString(arg0: str, arg1: bool) -> _pdg.WorkItem

        Loads a work item from a JSON file
        """
    def localizePath(self, arg0: str) -> str:
        """localizePath(self: _pdg.WorkItem, arg0: str) -> str

        Localizes a file path with the work item's scheduler
        """
    def loopBegin(self, arg0: int) -> WorkItem | None:
        """loopBegin(self: _pdg.WorkItem, arg0: int) -> _pdg.WorkItem

        Returns the loop begin item for this work item, at the
        specified loop depth
        """
    def makeActive(self) -> ActiveItemBlock:
        """makeActive(self: _pdg.WorkItem) -> _pdg.ActiveItemBlock

        Makes this work item active for the duration of the scope. Used
        with in a Python with statement
        """
    def memoryUsage(self) -> MemoryInfo:
        """memoryUsage(self: _pdg.WorkItem) -> _pdg.MemoryInfo

        Returns memory usage info about the work item
        """
    def numericAttribute(self, arg0: str) -> float:
        """numericAttribute(self: _pdg.WorkItem, arg0: str) -> object

        Looks up a numeric attribute on the work item by name and index
        """
    def outputFilesForTag(self, tag: str, include_expected: bool = ...) -> list[File]:
        """outputFilesForTag(self: _pdg.WorkItem, tag: str, include_expected: bool = False) -> UT_Array[_pdg.File]

        Returns a list of output files that match the given tag
        """
    def platformCommand(self, platform: platform = ...) -> str:
        """platformCommand(self: _pdg.WorkItem, platform: _pdg.platform = <platform.Undefined: -1>) -> str

        Returns the command for the specified platform
        """
    def prepareDirty(self, arg0: bool) -> WorkItemDirty:
        """prepareDirty(self: _pdg.WorkItem, arg0: bool) -> _pdg.WorkItemDirty

        Prepares the work item and any dependents for dirting, and
        returns a pdg.WorkItemDirty object that describes the dirty
        operation
        """
    def resultDataForTag(self, tag: str, include_expected: bool = ...) -> list[File]:
        """resultDataForTag(self: _pdg.WorkItem, tag: str, include_expected: bool = False) -> UT_Array[_pdg.File]

        [deprecated] Returns a list of output files that match the given tag
        """
    @staticmethod
    def saveArrayDict(work_items: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, global_attributes: bool = ..., skip_defaults: bool = ...) -> Dictionary:
        """saveArrayDict(work_items: UT_Array[_pdg.WorkItem], global_attributes: bool = False, skip_defaults: bool = True) -> _pdg.Dictionary

        Saves and reutrns the array of work items as a pdg.Dictionary
        """
    @staticmethod
    def saveArrayJSONFile(path: str, work_items: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, pretty_print: bool = ..., global_attributes: bool = ..., skip_defaults: bool = ...) -> bool:
        """saveArrayJSONFile(path: str, work_items: UT_Array[_pdg.WorkItem], pretty_print: bool = False, global_attributes: bool = False, skip_defaults: bool = True) -> bool

        Saves the array of work items to a JSON file on disk
        """
    @staticmethod
    def saveArrayJSONString(work_items: Sequence[WorkItem] | ConstWorkItemList | WorkItemList, pretty_print: bool = ..., global_attributes: bool = ..., skip_defaults: bool = ...) -> str:
        """saveArrayJSONString(work_items: UT_Array[_pdg.WorkItem], pretty_print: bool = False, global_attributes: bool = False, skip_defaults: bool = True) -> str

        Saves and reutrns the array of work items as JSON string
        """
    def saveDict(self, global_attributes: bool = ..., skip_defaults: bool = ...) -> Dictionary:
        """saveDict(self: _pdg.WorkItem, global_attributes: bool = False, skip_defaults: bool = False) -> _pdg.Dictionary

        Saves and returns the work item as a pdg.Dictionary
        """
    def saveJSONFile(self, path: str, pretty_print: bool = ..., global_attributes: bool = ..., skip_defaults: bool = ...) -> bool:
        """saveJSONFile(self: _pdg.WorkItem, path: str, pretty_print: bool = False, global_attributes: bool = False, skip_defaults: bool = False) -> bool

        Saves the work item to a JSON file on disk
        """
    def saveJSONString(self, pretty_print: bool = ..., global_attributes: bool = ..., skip_defaults: bool = ...) -> str:
        """saveJSONString(self: _pdg.WorkItem, pretty_print: bool = False, global_attributes: bool = False, skip_defaults: bool = False) -> str

        Saves and returns the work item as JSON string
        """
    def savePythonDict(self) -> _WorkItemPythonDict:
        """savePythonDict(self: _pdg.WorkItem) -> dict

        Saves the work item and all of its fields to a Python dict
        """
    def serializeData(self) -> str:
        """serializeData(self: _pdg.WorkItem) -> str

        Serializes the work item data to a string
        """
    def serializeDataToFile(self, arg0: str) -> bool:
        """serializeDataToFile(self: _pdg.WorkItem, arg0: str) -> bool

        Serializes the work item data to a file
        """
    def setCommand(self, command: str, shell: bool = ...) -> bool:
        """setCommand(self: _pdg.WorkItem, command: str, shell: bool = False) -> bool

        Sets the work item command string
        """
    def setCookPercent(self, arg0: float) -> None:
        """setCookPercent(self: _pdg.WorkItem, arg0: float) -> None

        Set the current cooking progress percentage.
        """
    def setCustomState(self, arg0: str) -> None:
        """setCustomState(self: _pdg.WorkItem, arg0: str) -> None

        Sets the work item's custom state string
        """
    @overload
    def setFrame(self, arg0: float) -> bool:
        """setFrame(*args, **kwargs)
        Overloaded function.

        1. setFrame(self: _pdg.WorkItem, arg0: float) -> bool

        Sets the frame of the item

        2. setFrame(self: _pdg.WorkItem, arg0: float, arg1: float) -> bool

        Sets the frame of the item
        """
    @overload
    def setFrame(self, arg0: float, arg1: float) -> bool:
        """setFrame(*args, **kwargs)
        Overloaded function.

        1. setFrame(self: _pdg.WorkItem, arg0: float) -> bool

        Sets the frame of the item

        2. setFrame(self: _pdg.WorkItem, arg0: float, arg1: float) -> bool

        Sets the frame of the item
        """
    def setIsPostCook(self, arg0: bool) -> None:
        """setIsPostCook(self: _pdg.WorkItem, arg0: bool) -> None

        Sets the work item post cook flag
        """
    def setLabel(self, arg0: str) -> None:
        """setLabel(self: _pdg.WorkItem, arg0: str) -> None

        Sets the work item label
        """
    def setLoopInfo(self, iteration: int, number: int, size: int, lock: int = ...) -> None:
        """setLoopInfo(self: _pdg.WorkItem, iteration: int, number: int, size: int, lock: int = -1) -> None

        Updates the loop info for the work item
        """
    def setPlatformCommands(self, linux: str, mac: str, windows: str, shell: bool = ...) -> bool:
        """setPlatformCommands(self: _pdg.WorkItem, linux: str, mac: str, windows: str, shell: bool = False) -> bool

        Sets the work item command string
        """
    def startSubItem(self, wait: bool = ...) -> None:
        """startSubItem(self: _pdg.WorkItem, wait: bool = False) -> None

        Marks the specified sub item as cooking
        """
    def stats(self) -> WorkItemStats:
        """stats(self: _pdg.WorkItem) -> _pdg.WorkItemStats

        Returns the stat object for the work item
        """
    def stringAttribute(self, arg0: str) -> str:
        """stringAttribute(self: _pdg.WorkItem, arg0: str) -> object

        Looks up a string attribute on the work item by name and index
        """
    def transferFiles(self, update_cache: bool = ...) -> bool:
        """transferFiles(self: _pdg.WorkItem, update_cache: bool = True) -> bool

        Manually runs file transfer logic for any work item files attribs
        that have the pdg.attribFlag.Transfer flag set
        """
    def updateOutputFile(self, arg0: int, arg1: str, arg2: str, arg3: int, arg4: bool) -> None:
        """updateOutputFile(self: _pdg.WorkItem, arg0: int, arg1: str, arg2: str, arg3: int, arg4: bool) -> None

        Replaces the ouptut file at the given index, if that index is valid
        """
    def updateResultData(self, arg0: int, arg1: str, arg2: str, arg3: int, arg4: bool) -> None:
        """updateResultData(self: _pdg.WorkItem, arg0: int, arg1: str, arg2: str, arg3: int, arg4: bool) -> None

        [Deprecated] Replaces the ouptut file at the given index, if that index is valid
        """
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool"""
    def __ge__(self, other: WorkItem) -> bool:
        """__ge__(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool"""
    def __gt__(self, other: WorkItem) -> bool:
        """__gt__(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: _pdg.WorkItem) -> int"""
    def __le__(self, other: WorkItem) -> bool:
        """__le__(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool"""
    def __lt__(self, other: WorkItem) -> bool:
        """__lt__(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: _pdg.WorkItem, arg0: _pdg.WorkItem) -> bool"""
    @property
    def batchIndex(self) -> int: ...
    @property
    def batchParent(self) -> BatchWorkItem | None: ...
    @property
    def command(self) -> str: ...
    @property
    def context(self) -> GraphContext: ...
    @property
    def cookDuration(self) -> float: ...
    @property
    def cookPercent(self) -> float: ...
    @property
    def cookType(self) -> workItemCookType: ...
    @property
    def customState(self) -> str: ...
    @property
    def data(self) -> WorkItemData: ...
    @property
    def dependencies(self) -> ConstWorkItemList: ...
    @property
    def dependencyState(self) -> workItemState: ...
    @property
    def dependents(self) -> ConstWorkItemList: ...
    @property
    def environment(self) -> dict[str, _EnvValue]: ...
    @property
    def executionType(self) -> workItemExecutionType: ...
    @property
    def expectedInputFiles(self) -> list[File]: ...
    @property
    def expectedInputResultData(self) -> list[File]: ...
    @property
    def expectedOutputFiles(self) -> list[File]: ...
    @property
    def expectedResultData(self) -> list[File]: ...
    @property
    def failedDependencies(self) -> ConstWorkItemList: ...
    @property
    def frame(self) -> float: ...
    @property
    def frameStep(self) -> float: ...
    @property
    def graph(self) -> Graph: ...
    @property
    def hasCommand(self) -> bool: ...
    @property
    def hasCookPercent(self) -> bool: ...
    @property
    def hasCustomState(self) -> bool: ...
    @property
    def hasFrame(self) -> bool: ...
    @property
    def hasLabel(self) -> bool: ...
    @property
    def hasPlatformCommand(self) -> bool: ...
    @property
    def hasWarnings(self) -> bool: ...
    @property
    def id(self) -> int: ...
    @property
    def index(self) -> int: ...
    @property
    def inputFiles(self) -> list[File]: ...
    @property
    def inputResultData(self) -> list[File]: ...
    @property
    def isBatch(self) -> bool: ...
    @property
    def isCooked(self) -> bool: ...
    @property
    def isFrozen(self) -> bool: ...
    @property
    def isInProcess(self) -> bool: ...
    @property
    def isNoGenerate(self) -> bool: ...
    @property
    def isOutOfProcess(self) -> bool: ...
    @property
    def isPartition(self) -> bool: ...
    @property
    def isPostCook(self) -> bool: ...
    @property
    def isStatic(self) -> bool: ...
    @property
    def isSuccessful(self) -> bool: ...
    @property
    def isUnsuccessful(self) -> bool: ...
    @property
    def label(self) -> str: ...
    @property
    def logMessages(self) -> str: ...
    @property
    def logURI(self) -> str: ...
    @property
    def loopDepth(self) -> int: ...
    @property
    def loopIteration(self) -> int: ...
    @property
    def loopLock(self) -> int: ...
    @property
    def loopNumber(self) -> int: ...
    @property
    def loopSize(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def node(self) -> Node: ...
    @property
    def outputCacheState(self) -> workItemCacheState: ...
    @property
    def outputFiles(self) -> list[File]: ...
    @property
    def parent(self) -> WorkItem | None: ...
    @property
    def partitionItems(self) -> ConstWorkItemList: ...
    @property
    def resultData(self) -> list[File]: ...
    @property
    def scriptDir(self) -> str: ...
    @property
    def shouldRunInShell(self) -> bool: ...
    @property
    def state(self) -> workItemState: ...
    @property
    def statusURI(self) -> str: ...
    @property
    def tempDir(self) -> str: ...
    @property
    def type(self) -> workItemType: ...
    @property
    def workingDir(self) -> str: ...

class WorkItemData(TypeInstance):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def clearFloatData(self) -> bool:
        """clearFloatData(self: _pdg.WorkItemData) -> bool

        Clears all float data fields
        """
    def clearIntData(self) -> bool:
        """clearIntData(self: _pdg.WorkItemData) -> bool

        Clears all int data fields
        """
    def clearStringData(self) -> bool:
        """clearStringData(self: _pdg.WorkItemData) -> bool

        Clears all string data fields
        """
    def data(self, arg0: str, arg1: int) -> int | float | str | None:
        """data(self: _pdg.WorkItemData, arg0: str, arg1: int) -> object

        Returns a float/int or string data value for a given name and index
        """
    def dataArray(self, arg0: str) -> list[int] | list[float] | list[str] | None:
        """dataArray(self: _pdg.WorkItemData, arg0: str) -> object

        Returns a float/int or string data array for a given name
        """
    def deserializeString(self, arg0: str) -> bool:
        """deserializeString(self: _pdg.WorkItemData, arg0: str) -> bool

        Deserializes the data from a string
        """
    def floatData(self, arg0: str, arg1: int) -> float | None:
        """floatData(self: _pdg.WorkItemData, arg0: str, arg1: int) -> object

        Returns a floating point data value for a given name and index
        """
    def floatDataArray(self, arg0: str) -> list[float] | None:
        """floatDataArray(self: _pdg.WorkItemData, arg0: str) -> object

        Returns a floating point data array a given name
        """
    def intData(self, arg0: str, arg1: int) -> int | None:
        """intData(self: _pdg.WorkItemData, arg0: str, arg1: int) -> object

        Returns integer data for a given name and index
        """
    def intDataArray(self, arg0: str) -> list[int] | None:
        """intDataArray(self: _pdg.WorkItemData, arg0: str) -> object

        Returns an integer data array for a given name
        """
    def removeData(self, arg0: str, arg1: int) -> bool:
        """removeData(self: _pdg.WorkItemData, arg0: str, arg1: int) -> bool

        Removes an attribute by name
        """
    def setFloat(self, arg0: str, arg1: float, arg2: int) -> bool:
        """setFloat(self: _pdg.WorkItemData, arg0: str, arg1: float, arg2: int) -> bool

        Sets floating point data with a given name, value and
        parameter index
        """
    def setFloatArray(self, arg0: str, arg1: Sequence[float]) -> bool:
        """setFloatArray(self: _pdg.WorkItemData, arg0: str, arg1: UT_Array[float]) -> bool

        Sets a floating point data with a given name and
        array of data values
        """
    def setInt(self, arg0: str, arg1: int, arg2: int) -> bool:
        """setInt(self: _pdg.WorkItemData, arg0: str, arg1: int, arg2: int) -> bool

        Sets int data with a given name, value and vector 
        index
        """
    def setIntArray(self, arg0: str, arg1: Sequence[int]) -> bool:
        """setIntArray(self: _pdg.WorkItemData, arg0: str, arg1: UT_Array[int]) -> bool

        Sets int data with a given name and
        array of data values
        """
    def setString(self, arg0: str, arg1: str, arg2: int) -> bool:
        """setString(self: _pdg.WorkItemData, arg0: str, arg1: str, arg2: int) -> bool

        Sets string data with a given name and value
        """
    def setStringArray(self, arg0: str, arg1: Sequence[str]) -> bool:
        """setStringArray(self: _pdg.WorkItemData, arg0: str, arg1: UT_Array[str]) -> bool

        Sets string data with a given name and
        array of data values
        """
    def stringData(self, arg0: str, arg1: int) -> str | None:
        """stringData(self: _pdg.WorkItemData, arg0: str, arg1: int) -> object

        Returns string data for a given name
        """
    def stringDataArray(self, arg0: str) -> list[str] | None:
        """stringDataArray(self: _pdg.WorkItemData, arg0: str) -> object

        Returns a string data array for a given name
        """
    @property
    def allDataMap(self) -> dict[str, list[int] | list[float] | list[str]]: ...
    @property
    def floatDataMap(self) -> dict[str, list[float]]: ...
    @property
    def intDataMap(self) -> dict[str, list[int]]: ...
    @property
    def stringDataMap(self) -> dict[str, list[str]]: ...
    @property
    def workItem(self) -> WorkItem: ...

class WorkItemDataType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...

class WorkItemDirty:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def applyDirty(self, arg0: bool) -> None:
        """applyDirty(self: _pdg.WorkItemDirty, arg0: bool) -> None

        Applies the dirty operation contained this object, and clears
        all fields
        """
    def keepFilePath(self, arg0: str) -> None:
        """keepFilePath(self: _pdg.WorkItemDirty, arg0: str) -> None

        Marks a file path so that it's not deleted
        """
    @property
    def deleteSet(self) -> list[WorkItem]: ...
    @property
    def dirtyFiles(self) -> list[File]: ...
    @property
    def dirtySet(self) -> list[WorkItem]: ...
    @property
    def dirtyType(self) -> workItemDirtyType: ...
    @property
    def keepFiles(self) -> list[str]: ...

class WorkItemHolder(DependencyHolder):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addWorkItemArrayFromDict(self, dict: Dictionary, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> list[WorkItem]:
        """addWorkItemArrayFromDict(self: _pdg.WorkItemHolder, dict: _pdg.Dictionary, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> UT_Array[_pdg.WorkItem]

        Adds an array of work item to the holder by deserializing the
        given dictionary
        """
    def addWorkItemArrayFromJSONFile(self, file_path: str, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> list[WorkItem]:
        """addWorkItemArrayFromJSONFile(self: _pdg.WorkItemHolder, file_path: str, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> UT_Array[_pdg.WorkItem]

        Adds a work item array to the holder by deserializing the
        given JSON file
        """
    def addWorkItemArrayFromJSONString(self, json: str, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> list[WorkItem]:
        """addWorkItemArrayFromJSONString(self: _pdg.WorkItemHolder, json: str, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> UT_Array[_pdg.WorkItem]

        Adds an array of work item to the holder by deserializing the
        given JSON text
        """
    def addWorkItemFromDict(self, dict: Dictionary, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> WorkItem:
        """addWorkItemFromDict(self: _pdg.WorkItemHolder, dict: _pdg.Dictionary, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> _pdg.WorkItem

        Adds a work item to the holder by deserializing the given dictionary
        """
    def addWorkItemFromJSON(self, json: str, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> WorkItem:
        """addWorkItemFromJSON(self: _pdg.WorkItemHolder, json: str, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> _pdg.WorkItem

        Adds a work item to the holder by deserializing the given JSON text
        """
    def addWorkItemFromJSONFile(self, file_path: str, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> WorkItem:
        """addWorkItemFromJSONFile(self: _pdg.WorkItemHolder, file_path: str, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> _pdg.WorkItem

        Adds a work item to the holder by deserializing the given JSON file
        """
    def addWorkItemFromJSONString(self, json: str, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> WorkItem:
        """addWorkItemFromJSONString(self: _pdg.WorkItemHolder, json: str, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> _pdg.WorkItem

        Adds a work item to the holder by deserializing the given JSON text
        """
    def addWorkItemFromWorkItem(self, work_item: WorkItem, parent: WorkItem | None = ..., strategy: attribCollisionStrategy = ..., preserve_type: bool = ..., preserve_index: bool = ..., add_attributes: bool = ...) -> WorkItem:
        """addWorkItemFromWorkItem(self: _pdg.WorkItemHolder, work_item: _pdg.WorkItem, parent: _pdg.WorkItem = None, strategy: _pdg.attribCollisionStrategy = <attribCollisionStrategy.Replace: 1>, preserve_type: bool = False, preserve_index: bool = True, add_attributes: bool = True) -> _pdg.WorkItem

        Adds a work item to the holder by deserializing the given JSON text
        """
    def commit(self) -> None:
        """commit(self: _pdg.WorkItemHolder) -> None

        Commits the work items to the node, and clears the
        holder. It can continue to be used, though
        """
    def setCommitCount(self, arg0: int) -> None:
        """setCommitCount(self: _pdg.WorkItemHolder, arg0: int) -> None

        Sets the commit count, which determines how many items can be added to the holder before it commits them to the node. This functionality is only available when doing static work item generation
        """
    @property
    def allBatches(self) -> list[BatchWorkItem]: ...
    @property
    def allWorkItems(self) -> list[WorkItem]: ...
    @property
    def batches(self) -> list[BatchWorkItem]: ...
    @property
    def commitCount(self) -> int: ...
    @property
    def isEmpty(self) -> bool: ...
    @property
    def workItems(self) -> list[WorkItem]: ...
    # pdg/__init__.py's. Each option set (not None) overrides the field of the WorkItemOptions;
    # the extra arguments go to the python work item type.
    def addWorkItem(
        self,
        options: WorkItemOptions | None = ...,
        name: str | None = ...,
        typeName: str | None = ...,
        index: int | None = ...,
        priority: int | None = ...,
        cloneMode: cloneMode | None = ...,
        cloneTarget: WorkItem | None = ...,
        parent: WorkItem | None = ...,
        batchSize: int | None = ...,
        batchOffset: int | None = ...,
        batch: bool | None = ...,
        inProcess: bool | None = ...,
        isNoGenerate: bool | None = ...,
        preserveType: bool | None = ...,
        cloneResultData: bool | None = ...,
        cloneOutputFiles: bool | None = ...,
        parentArrayOffset: int | None = ...,
        parentArray: list[WorkItem] | None = ...,
        isServiceMode: bool | None = ...,
        cookType: workItemCookType | None = ...,
        isPartialCook: bool | None = ...,
        isDynamicBatch: bool | None = ...,
        *args: Any,
        **kwargs: Any,
    ) -> WorkItem: ...

class WorkItemList:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def append(self, arg0: WorkItem) -> None:
        """append(self: _pdg.WorkItemList, arg0: PDG_WorkItem) -> None"""
    def count(self, arg0: WorkItem) -> int:
        """count(self: _pdg.WorkItemList, arg0: PDG_WorkItem) -> int"""
    @overload
    def extend(self, arg0: Sequence[WorkItem]) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _pdg.WorkItemList, arg0: UT_Array[PDG_WorkItem]) -> None

        2. extend(self: _pdg.WorkItemList, arg0: _pdg.WorkItemList) -> None

        3. extend(self: _pdg.WorkItemList, arg0: Iterable) -> None
        """
    @overload
    def extend(self, arg0: WorkItemList) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _pdg.WorkItemList, arg0: UT_Array[PDG_WorkItem]) -> None

        2. extend(self: _pdg.WorkItemList, arg0: _pdg.WorkItemList) -> None

        3. extend(self: _pdg.WorkItemList, arg0: Iterable) -> None
        """
    @overload
    def extend(self, arg0: Iterable[WorkItem]) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _pdg.WorkItemList, arg0: UT_Array[PDG_WorkItem]) -> None

        2. extend(self: _pdg.WorkItemList, arg0: _pdg.WorkItemList) -> None

        3. extend(self: _pdg.WorkItemList, arg0: Iterable) -> None
        """
    def index(self, element: WorkItem, start: int = ..., stop: int = ...) -> int:
        """index(self: _pdg.WorkItemList, element: PDG_WorkItem, start: int = 0, stop: int = -1) -> int"""
    def insert(self, arg0: int, arg1: WorkItem) -> None:
        """insert(self: _pdg.WorkItemList, arg0: int, arg1: PDG_WorkItem) -> None"""
    def pop(self, index: int = ...) -> WorkItem:
        """pop(self: _pdg.WorkItemList, index: int = -1) -> object"""
    def remove(self, arg0: WorkItem) -> None:
        """remove(self: _pdg.WorkItemList, arg0: PDG_WorkItem) -> None"""
    def reverse(self) -> None:
        """reverse(self: _pdg.WorkItemList) -> None"""
    def sort(self, key: Callable[[WorkItem], SupportsRichComparison] = ..., reverse: bool = ...) -> None:
        """sort(self: _pdg.WorkItemList, key: Callable = None, reverse: bool = False) -> None"""
    def __bool__(self) -> bool:
        """__bool__(self: _pdg.WorkItemList) -> bool"""
    def __delitem__(self, other: int) -> None:
        """__delitem__(self: _pdg.WorkItemList, arg0: int) -> None"""
    @overload
    def __getitem__(self, index: int) -> WorkItem:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _pdg.WorkItemList, arg0: int) -> PDG_WorkItem

        2. __getitem__(self: _pdg.WorkItemList, arg0: slice) -> list
        """
    @overload
    def __getitem__(self, index: slice) -> list[WorkItem]:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _pdg.WorkItemList, arg0: int) -> PDG_WorkItem

        2. __getitem__(self: _pdg.WorkItemList, arg0: slice) -> list
        """
    def __iter__(self) -> Iterator[WorkItem]:
        """__iter__(self: _pdg.WorkItemList) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _pdg.WorkItemList) -> int"""
    @overload
    def __setitem__(self, index: int, object: WorkItem) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.WorkItemList, arg0: int, arg1: PDG_WorkItem) -> None

        2. __setitem__(self: _pdg.WorkItemList, arg0: slice, arg1: UT_Array[PDG_WorkItem]) -> None

        3. __setitem__(self: _pdg.WorkItemList, arg0: slice, arg1: _pdg.WorkItemList) -> None
        """
    @overload
    def __setitem__(self, index: slice, object: Sequence[WorkItem]) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.WorkItemList, arg0: int, arg1: PDG_WorkItem) -> None

        2. __setitem__(self: _pdg.WorkItemList, arg0: slice, arg1: UT_Array[PDG_WorkItem]) -> None

        3. __setitem__(self: _pdg.WorkItemList, arg0: slice, arg1: _pdg.WorkItemList) -> None
        """
    @overload
    def __setitem__(self, index: slice, object: WorkItemList) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _pdg.WorkItemList, arg0: int, arg1: PDG_WorkItem) -> None

        2. __setitem__(self: _pdg.WorkItemList, arg0: slice, arg1: UT_Array[PDG_WorkItem]) -> None

        3. __setitem__(self: _pdg.WorkItemList, arg0: slice, arg1: _pdg.WorkItemList) -> None
        """

class WorkItemOptions:
    batch: bool
    batchOffset: int
    batchSize: int
    cloneMode: _pdg.cloneMode
    cloneOutputFiles: bool
    cloneResultData: bool
    cloneTarget: WorkItem | None
    cookType: workItemCookType
    inProcess: bool
    index: int
    isDynamicBatch: bool
    isNoGenerate: bool
    isPartialCook: bool
    isServiceMode: bool
    name: str
    parent: WorkItem | None
    parentArray: list[WorkItem]
    parentArrayOffset: int
    preserveType: bool
    priority: int
    typeName: str
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.WorkItemOptions) -> None

        Constructs a new work item options instance

        2. __init__(self: _pdg.WorkItemOptions, arg0: _pdg.WorkItemOptions) -> None

        Copies an existing set of options
        """
    @overload
    def __init__(self, arg0: WorkItemOptions) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdg.WorkItemOptions) -> None

        Constructs a new work item options instance

        2. __init__(self: _pdg.WorkItemOptions, arg0: _pdg.WorkItemOptions) -> None

        Copies an existing set of options
        """

class WorkItemStats:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def stat(self, arg0: workItemStatType) -> float:
        """stat(self: _pdg.WorkItemStats, arg0: _pdg.workItemStatType) -> float"""
    @property
    def serviceClient(self) -> str: ...

class _DictionaryItemIter:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> _DictionaryItemIter:
        """__iter__(self: _pdg._DictionaryItemIter) -> _pdg._DictionaryItemIter"""
    def __next__(self) -> tuple[str, _DictValue]:
        """__next__(self: _pdg._DictionaryItemIter) -> object"""

class _DictionaryItemView:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> _DictionaryItemIter:
        """__iter__(self: _pdg._DictionaryItemView) -> _pdg._DictionaryItemIter"""
    def __len__(self) -> int:
        """__len__(self: _pdg._DictionaryItemView) -> int"""

class _DictionaryKeyIter:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> _DictionaryKeyIter:
        """__iter__(self: _pdg._DictionaryKeyIter) -> _pdg._DictionaryKeyIter"""
    def __next__(self) -> str:
        """__next__(self: _pdg._DictionaryKeyIter) -> str"""

class _DictionaryKeyView:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __contains__(self, other: str) -> bool:
        """__contains__(self: _pdg._DictionaryKeyView, arg0: str) -> bool"""
    def __iter__(self) -> _DictionaryKeyIter:
        """__iter__(self: _pdg._DictionaryKeyView) -> _pdg._DictionaryKeyIter"""
    def __len__(self) -> int:
        """__len__(self: _pdg._DictionaryKeyView) -> int"""

class _DictionaryValueIter:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> _DictionaryValueIter:
        """__iter__(self: _pdg._DictionaryValueIter) -> _pdg._DictionaryValueIter"""
    def __next__(self) -> _DictValue:
        """__next__(self: _pdg._DictionaryValueIter) -> object"""

class _DictionaryValueView:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> _DictionaryValueIter:
        """__iter__(self: _pdg._DictionaryValueView) -> _pdg._DictionaryValueIter"""
    def __len__(self) -> int:
        """__len__(self: _pdg._DictionaryValueView) -> int"""

class acceptResult:
    __members__: ClassVar[dict[str, acceptResult]] = ...  # read-only
    Accept: ClassVar[acceptResult] = ...
    Default: ClassVar[acceptResult] = ...
    Reject: ClassVar[acceptResult] = ...
    __entries: ClassVar[dict[str, tuple[acceptResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.acceptResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.acceptResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.acceptResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class argType:
    __members__: ClassVar[dict[str, argType]] = ...  # read-only
    Automatic: ClassVar[argType] = ...
    Expression: ClassVar[argType] = ...
    Value: ClassVar[argType] = ...
    __entries: ClassVar[dict[str, tuple[argType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.argType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.argType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.argType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribCollisionStrategy:
    __members__: ClassVar[dict[str, attribCollisionStrategy]] = ...  # read-only
    Error: ClassVar[attribCollisionStrategy] = ...
    Keep: ClassVar[attribCollisionStrategy] = ...
    Replace: ClassVar[attribCollisionStrategy] = ...
    __entries: ClassVar[dict[str, tuple[attribCollisionStrategy, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribCollisionStrategy, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribCollisionStrategy) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribCollisionStrategy) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribCopyType:
    __members__: ClassVar[dict[str, attribCopyType]] = ...  # read-only
    Append: ClassVar[attribCopyType] = ...
    New: ClassVar[attribCopyType] = ...
    Overwrite: ClassVar[attribCopyType] = ...
    OverwriteType: ClassVar[attribCopyType] = ...
    Prepend: ClassVar[attribCopyType] = ...
    Update: ClassVar[attribCopyType] = ...
    __entries: ClassVar[dict[str, tuple[attribCopyType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribCopyType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribCopyType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribCopyType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribErrorLevel:
    __members__: ClassVar[dict[str, attribErrorLevel]] = ...  # read-only
    Error: ClassVar[attribErrorLevel] = ...
    Quiet: ClassVar[attribErrorLevel] = ...
    Warn: ClassVar[attribErrorLevel] = ...
    __entries: ClassVar[dict[str, tuple[attribErrorLevel, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribErrorLevel, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribErrorLevel) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribErrorLevel) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribFlag:
    __members__: ClassVar[dict[str, attribFlag]] = ...  # read-only
    All: ClassVar[attribFlag] = ...
    Bound: ClassVar[attribFlag] = ...
    Dependent: ClassVar[attribFlag] = ...
    EnvExport: ClassVar[attribFlag] = ...
    InputFile: ClassVar[attribFlag] = ...
    Internal: ClassVar[attribFlag] = ...
    MemoryValue: ClassVar[attribFlag] = ...
    NoCopy: ClassVar[attribFlag] = ...
    NoDirty: ClassVar[attribFlag] = ...
    NoFlags: ClassVar[attribFlag] = ...
    Operator: ClassVar[attribFlag] = ...
    ReadOnly: ClassVar[attribFlag] = ...
    Timestamp: ClassVar[attribFlag] = ...
    Transfer: ClassVar[attribFlag] = ...
    Transient: ClassVar[attribFlag] = ...
    __entries: ClassVar[dict[str, tuple[attribFlag, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribFlag, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __ge__(self, other: attribFlag) -> bool:
        """__ge__(self: object, other: object) -> bool"""
    def __gt__(self, other: attribFlag) -> bool:
        """__gt__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribFlag) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribFlag) -> int"""
    def __le__(self, other: attribFlag) -> bool:
        """__le__(self: object, other: object) -> bool"""
    def __lt__(self, other: attribFlag) -> bool:
        """__lt__(self: object, other: object) -> bool"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribMatchType:
    __members__: ClassVar[dict[str, attribMatchType]] = ...  # read-only
    Both: ClassVar[attribMatchType] = ...
    Plain: ClassVar[attribMatchType] = ...
    Prefix: ClassVar[attribMatchType] = ...
    Suffix: ClassVar[attribMatchType] = ...
    __entries: ClassVar[dict[str, tuple[attribMatchType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribMatchType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribMatchType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribMatchType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribMergeType:
    __members__: ClassVar[dict[str, attribMergeType]] = ...  # read-only
    AppendArray: ClassVar[attribMergeType] = ...
    Average: ClassVar[attribMergeType] = ...
    FirstValue: ClassVar[attribMergeType] = ...
    Ignore: ClassVar[attribMergeType] = ...
    LastValue: ClassVar[attribMergeType] = ...
    Maximum: ClassVar[attribMergeType] = ...
    Median: ClassVar[attribMergeType] = ...
    Minimum: ClassVar[attribMergeType] = ...
    Mode: ClassVar[attribMergeType] = ...
    Sorted: ClassVar[attribMergeType] = ...
    SortedUnique: ClassVar[attribMergeType] = ...
    Sum: ClassVar[attribMergeType] = ...
    UniqueValues: ClassVar[attribMergeType] = ...
    __entries: ClassVar[dict[str, tuple[attribMergeType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribMergeType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribMergeType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribMergeType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribOrigin:
    __members__: ClassVar[dict[str, attribOrigin]] = ...  # read-only
    Cook: ClassVar[attribOrigin] = ...
    Expected: ClassVar[attribOrigin] = ...
    Generate: ClassVar[attribOrigin] = ...
    GenerateExpected: ClassVar[attribOrigin] = ...
    Undefined: ClassVar[attribOrigin] = ...
    __entries: ClassVar[dict[str, tuple[attribOrigin, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribOrigin, value: int) -> None"""
    def __and__(self, other: attribOrigin | int) -> int:
        """__and__(self: object, other: object) -> object"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __ge__(self, other: attribOrigin | int) -> bool:
        """__ge__(self: object, other: object) -> bool"""
    def __gt__(self, other: attribOrigin | int) -> bool:
        """__gt__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribOrigin) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribOrigin) -> int"""
    def __invert__(self) -> int:
        """__invert__(self: object) -> object"""
    def __le__(self, other: attribOrigin | int) -> bool:
        """__le__(self: object, other: object) -> bool"""
    def __lt__(self, other: attribOrigin | int) -> bool:
        """__lt__(self: object, other: object) -> bool"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __or__(self, other: attribOrigin | int) -> int:
        """__or__(self: object, other: object) -> object"""
    def __rand__(self, other: attribOrigin | int) -> int:
        """__rand__(self: object, other: object) -> object"""
    def __ror__(self, other: attribOrigin | int) -> int:
        """__ror__(self: object, other: object) -> object"""
    def __rxor__(self, other: attribOrigin | int) -> int:
        """__rxor__(self: object, other: object) -> object"""
    def __xor__(self, other: attribOrigin | int) -> int:
        """__xor__(self: object, other: object) -> object"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribOverwrite:
    __members__: ClassVar[dict[str, attribOverwrite]] = ...  # read-only
    Always: ClassVar[attribOverwrite] = ...
    Match: ClassVar[attribOverwrite] = ...
    Never: ClassVar[attribOverwrite] = ...
    __entries: ClassVar[dict[str, tuple[attribOverwrite, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribOverwrite, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribOverwrite) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribOverwrite) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribSaveType:
    __members__: ClassVar[dict[str, attribSaveType]] = ...  # read-only
    Dynamic: ClassVar[attribSaveType] = ...
    Flatten: ClassVar[attribSaveType] = ...
    Static: ClassVar[attribSaveType] = ...
    __entries: ClassVar[dict[str, tuple[attribSaveType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribSaveType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribSaveType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribSaveType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class attribType:
    __members__: ClassVar[dict[str, attribType]] = ...  # read-only
    Dict: ClassVar[attribType] = ...
    File: ClassVar[attribType] = ...
    Float: ClassVar[attribType] = ...
    Geometry: ClassVar[attribType] = ...
    Int: ClassVar[attribType] = ...
    PyObject: ClassVar[attribType] = ...
    String: ClassVar[attribType] = ...
    Undefined: ClassVar[attribType] = ...
    __entries: ClassVar[dict[str, tuple[attribType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.attribType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.attribType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.attribType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class batchActivation:
    __members__: ClassVar[dict[str, batchActivation]] = ...  # read-only
    All: ClassVar[batchActivation] = ...
    Any: ClassVar[batchActivation] = ...
    First: ClassVar[batchActivation] = ...
    Fixed: ClassVar[batchActivation] = ...
    __entries: ClassVar[dict[str, tuple[batchActivation, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.batchActivation, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.batchActivation) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.batchActivation) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class cacheMode:
    __members__: ClassVar[dict[str, cacheMode]] = ...  # read-only
    AlwaysRead: ClassVar[cacheMode] = ...
    AlwaysWrite: ClassVar[cacheMode] = ...
    Automatic: ClassVar[cacheMode] = ...
    AutomaticIgnore: ClassVar[cacheMode] = ...
    __entries: ClassVar[dict[str, tuple[cacheMode, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.cacheMode, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.cacheMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.cacheMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class cacheResult:
    __members__: ClassVar[dict[str, cacheResult]] = ...  # read-only
    Hit: ClassVar[cacheResult] = ...
    Miss: ClassVar[cacheResult] = ...
    Skip: ClassVar[cacheResult] = ...
    __entries: ClassVar[dict[str, tuple[cacheResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.cacheResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.cacheResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.cacheResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class cloneMode:
    __members__: ClassVar[dict[str, cloneMode]] = ...  # read-only
    Always: ClassVar[cloneMode] = ...
    Default: ClassVar[cloneMode] = ...
    Never: ClassVar[cloneMode] = ...
    __entries: ClassVar[dict[str, tuple[cloneMode, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.cloneMode, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.cloneMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.cloneMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class cookType:
    __members__: ClassVar[dict[str, cookType]] = ...  # read-only
    Full: ClassVar[cookType] = ...
    GenerateFull: ClassVar[cookType] = ...
    GenerateNode: ClassVar[cookType] = ...
    GenerateStatic: ClassVar[cookType] = ...
    Node: ClassVar[cookType] = ...
    StaticDepsFull: ClassVar[cookType] = ...
    StaticDepsGen: ClassVar[cookType] = ...
    StaticDepsNode: ClassVar[cookType] = ...
    __entries: ClassVar[dict[str, tuple[cookType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.cookType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.cookType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.cookType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class dataType:
    __members__: ClassVar[dict[str, dataType]] = ...  # read-only
    Float: ClassVar[dataType] = ...
    Integer: ClassVar[dataType] = ...
    Invalid: ClassVar[dataType] = ...
    String: ClassVar[dataType] = ...
    __entries: ClassVar[dict[str, tuple[dataType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.dataType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.dataType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.dataType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelCache:
    __members__: ClassVar[dict[str, debugLevelCache]] = ...  # read-only
    Handler: ClassVar[debugLevelCache] = ...
    Hit: ClassVar[debugLevelCache] = ...
    Id: ClassVar[debugLevelCache] = ...
    Miss: ClassVar[debugLevelCache] = ...
    Off: ClassVar[debugLevelCache] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelCache, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelCache, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelCache) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelCache) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelExpression:
    __members__: ClassVar[dict[str, debugLevelExpression]] = ...  # read-only
    Attributes: ClassVar[debugLevelExpression] = ...
    Off: ClassVar[debugLevelExpression] = ...
    TimeDependent: ClassVar[debugLevelExpression] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelExpression, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelExpression, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelExpression) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelExpression) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelNode:
    __members__: ClassVar[dict[str, debugLevelNode]] = ...  # read-only
    Callback: ClassVar[debugLevelNode] = ...
    Error: ClassVar[debugLevelNode] = ...
    Off: ClassVar[debugLevelNode] = ...
    Status: ClassVar[debugLevelNode] = ...
    Warning: ClassVar[debugLevelNode] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelNode, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelNode, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelNode) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelNode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelScheduler:
    __members__: ClassVar[dict[str, debugLevelScheduler]] = ...  # read-only
    Off: ClassVar[debugLevelScheduler] = ...
    Scheduling: ClassVar[debugLevelScheduler] = ...
    WorkItem: ClassVar[debugLevelScheduler] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelScheduler, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelScheduler, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelScheduler) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelScheduler) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelService:
    __members__: ClassVar[dict[str, debugLevelService]] = ...  # read-only
    ClientDefer: ClassVar[debugLevelService] = ...
    ClientUsage: ClassVar[debugLevelService] = ...
    Job: ClassVar[debugLevelService] = ...
    Off: ClassVar[debugLevelService] = ...
    Startup: ClassVar[debugLevelService] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelService, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelService, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelService) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelService) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelTransfer:
    __members__: ClassVar[dict[str, debugLevelTransfer]] = ...  # read-only
    All: ClassVar[debugLevelTransfer] = ...
    Failure: ClassVar[debugLevelTransfer] = ...
    Handler: ClassVar[debugLevelTransfer] = ...
    Off: ClassVar[debugLevelTransfer] = ...
    Success: ClassVar[debugLevelTransfer] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelTransfer, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelTransfer, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelTransfer) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelTransfer) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelTypeRegistration:
    __members__: ClassVar[dict[str, debugLevelTypeRegistration]] = ...  # read-only
    Failure: ClassVar[debugLevelTypeRegistration] = ...
    Info: ClassVar[debugLevelTypeRegistration] = ...
    Off: ClassVar[debugLevelTypeRegistration] = ...
    Success: ClassVar[debugLevelTypeRegistration] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelTypeRegistration, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelTypeRegistration, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelTypeRegistration) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelTypeRegistration) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLevelWorkItem:
    __members__: ClassVar[dict[str, debugLevelWorkItem]] = ...  # read-only
    All: ClassVar[debugLevelWorkItem] = ...
    Off: ClassVar[debugLevelWorkItem] = ...
    Scheduled: ClassVar[debugLevelWorkItem] = ...
    __entries: ClassVar[dict[str, tuple[debugLevelWorkItem, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLevelWorkItem, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLevelWorkItem) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLevelWorkItem) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugLogType:
    __members__: ClassVar[dict[str, debugLogType]] = ...  # read-only
    Cache: ClassVar[debugLogType] = ...
    Expression: ClassVar[debugLogType] = ...
    Node: ClassVar[debugLogType] = ...
    Scheduler: ClassVar[debugLogType] = ...
    Service: ClassVar[debugLogType] = ...
    Transfer: ClassVar[debugLogType] = ...
    TypeRegistration: ClassVar[debugLogType] = ...
    WorkItem: ClassVar[debugLogType] = ...
    __entries: ClassVar[dict[str, tuple[debugLogType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.debugLogType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.debugLogType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.debugLogType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class debugging:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def configureFromEnvironment(force: bool = ...) -> bool:
        """configureFromEnvironment(force: bool = False) -> bool

        Reconfigures the log levels based on PDG debug variables
        """
    @staticmethod
    def disableAll() -> None:
        """disableAll() -> None

        Disables all logging for all log types
        """
    @staticmethod
    def enableAll() -> None:
        """enableAll() -> None

        Enables all logging for all log types
        """
    @staticmethod
    def logLevel(arg0: debugLogType) -> _DebugLevel:
        """logLevel(arg0: _pdg.debugLogType) -> object

        Returns the log level for the specified log type
        """
    @staticmethod
    def setLogLevel(arg0: debugLogType, arg1: _DebugLevel) -> None:
        """setLogLevel(arg0: _pdg.debugLogType, arg1: object) -> None

        Sets a custom log level for the specified log type
        """
    @staticmethod
    def setVerbosity(arg0: int) -> None:
        """setVerbosity(arg0: int) -> None"""
    @staticmethod
    def typeLog(arg0: debugLevelTypeRegistration, arg1: str, arg2: str) -> None:
        """typeLog(arg0: _pdg.debugLevelTypeRegistration, arg1: str, arg2: str) -> None

        Writes a type loading log message to the PDG debug log
        """
    @staticmethod
    def verbosity() -> int:
        """verbosity() -> int"""
    @staticmethod
    def writeLog(arg0: str, arg1: str) -> None:
        """writeLog(arg0: str, arg1: str) -> None

        Writes a generic message to the PDG debug log
        """

class dirtyHandlerType:
    __members__: ClassVar[dict[str, dirtyHandlerType]] = ...  # read-only
    Any: ClassVar[dirtyHandlerType] = ...
    Delete: ClassVar[dirtyHandlerType] = ...
    Files: ClassVar[dirtyHandlerType] = ...
    __entries: ClassVar[dict[str, tuple[dirtyHandlerType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.dirtyHandlerType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.dirtyHandlerType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.dirtyHandlerType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class fileTransferType:
    __members__: ClassVar[dict[str, fileTransferType]] = ...  # read-only
    AssetDir: ClassVar[fileTransferType] = ...
    ScriptDir: ClassVar[fileTransferType] = ...
    TempDir: ClassVar[fileTransferType] = ...
    WorkingDir: ClassVar[fileTransferType] = ...
    __entries: ClassVar[dict[str, tuple[fileTransferType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.fileTransferType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.fileTransferType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.fileTransferType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class fileType:
    __members__: ClassVar[dict[str, fileType]] = ...  # read-only
    Expected: ClassVar[fileType] = ...
    Generated: ClassVar[fileType] = ...
    Runtime: ClassVar[fileType] = ...
    RuntimeExpected: ClassVar[fileType] = ...
    __entries: ClassVar[dict[str, tuple[fileType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.fileType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.fileType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.fileType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class generateWhen:
    __members__: ClassVar[dict[str, generateWhen]] = ...  # read-only
    AllUpstreamCooked: ClassVar[generateWhen] = ...
    AllUpstreamGenerated: ClassVar[generateWhen] = ...
    Automatic: ClassVar[generateWhen] = ...
    EachUpstreamCooked: ClassVar[generateWhen] = ...
    __entries: ClassVar[dict[str, tuple[generateWhen, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.generateWhen, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.generateWhen) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.generateWhen) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class generationType:
    __members__: ClassVar[dict[str, generationType]] = ...  # read-only
    Dynamic: ClassVar[generationType] = ...
    DynamicGenerate: ClassVar[generationType] = ...
    DynamicRegenerate: ClassVar[generationType] = ...
    Regenerate: ClassVar[generationType] = ...
    Static: ClassVar[generationType] = ...
    StaticGenerate: ClassVar[generationType] = ...
    StaticRegenerate: ClassVar[generationType] = ...
    __entries: ClassVar[dict[str, tuple[generationType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.generationType, value: int) -> None"""
    def __and__(self, other: generationType | int) -> int:
        """__and__(self: object, other: object) -> object"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __ge__(self, other: generationType | int) -> bool:
        """__ge__(self: object, other: object) -> bool"""
    def __gt__(self, other: generationType | int) -> bool:
        """__gt__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.generationType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.generationType) -> int"""
    def __invert__(self) -> int:
        """__invert__(self: object) -> object"""
    def __le__(self, other: generationType | int) -> bool:
        """__le__(self: object, other: object) -> bool"""
    def __lt__(self, other: generationType | int) -> bool:
        """__lt__(self: object, other: object) -> bool"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __or__(self, other: generationType | int) -> int:
        """__or__(self: object, other: object) -> object"""
    def __rand__(self, other: generationType | int) -> int:
        """__rand__(self: object, other: object) -> object"""
    def __ror__(self, other: generationType | int) -> int:
        """__ror__(self: object, other: object) -> object"""
    def __rxor__(self, other: generationType | int) -> int:
        """__rxor__(self: object, other: object) -> object"""
    def __xor__(self, other: generationType | int) -> int:
        """__xor__(self: object, other: object) -> object"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class language:
    __members__: ClassVar[dict[str, language]] = ...  # read-only
    Cpp: ClassVar[language] = ...
    Python: ClassVar[language] = ...
    __entries: ClassVar[dict[str, tuple[language, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.language, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.language) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.language) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class nodeStatType:
    __members__: ClassVar[dict[str, nodeStatType]] = ...  # read-only
    FirstCookTime: ClassVar[nodeStatType] = ...
    FirstGenerateTime: ClassVar[nodeStatType] = ...
    LastCookTime: ClassVar[nodeStatType] = ...
    LastGenerateTime: ClassVar[nodeStatType] = ...
    TotalCookTime: ClassVar[nodeStatType] = ...
    TotalGenerateTime: ClassVar[nodeStatType] = ...
    __entries: ClassVar[dict[str, tuple[nodeStatType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.nodeStatType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.nodeStatType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.nodeStatType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class nodeSubtype:
    __members__: ClassVar[dict[str, nodeSubtype]] = ...  # read-only
    FeedbackBegin: ClassVar[nodeSubtype] = ...
    FeedbackEnd: ClassVar[nodeSubtype] = ...
    Normal: ClassVar[nodeSubtype] = ...
    __entries: ClassVar[dict[str, tuple[nodeSubtype, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.nodeSubtype, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.nodeSubtype) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.nodeSubtype) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class nodeType:
    __members__: ClassVar[dict[str, nodeType]] = ...  # read-only
    Mapper: ClassVar[nodeType] = ...
    Partitioner: ClassVar[nodeType] = ...
    Processor: ClassVar[nodeType] = ...
    __entries: ClassVar[dict[str, tuple[nodeType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.nodeType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.nodeType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.nodeType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class pathMapMatchType:
    __members__: ClassVar[dict[str, pathMapMatchType]] = ...  # read-only
    Contains: ClassVar[pathMapMatchType] = ...
    Prefix: ClassVar[pathMapMatchType] = ...
    Suffix: ClassVar[pathMapMatchType] = ...
    __entries: ClassVar[dict[str, tuple[pathMapMatchType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.pathMapMatchType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.pathMapMatchType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.pathMapMatchType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class platform:
    __members__: ClassVar[dict[str, platform]] = ...  # read-only
    Linux: ClassVar[platform] = ...
    Mac: ClassVar[platform] = ...
    Undefined: ClassVar[platform] = ...
    Windows: ClassVar[platform] = ...
    __entries: ClassVar[dict[str, tuple[platform, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.platform, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.platform) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.platform) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class portType:
    __members__: ClassVar[dict[str, portType]] = ...  # read-only
    Input: ClassVar[portType] = ...
    Output: ClassVar[portType] = ...
    Parameter: ClassVar[portType] = ...
    __entries: ClassVar[dict[str, tuple[portType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.portType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.portType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.portType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class regenerateReason:
    __members__: ClassVar[dict[str, regenerateReason]] = ...  # read-only
    Always: ClassVar[regenerateReason] = ...
    Dirty: ClassVar[regenerateReason] = ...
    DirtyInvalidate: ClassVar[regenerateReason] = ...
    Full: ClassVar[regenerateReason] = ...
    Propagate: ClassVar[regenerateReason] = ...
    __entries: ClassVar[dict[str, tuple[regenerateReason, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.regenerateReason, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.regenerateReason) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.regenerateReason) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class regenerateResult:
    __members__: ClassVar[dict[str, regenerateResult]] = ...  # read-only
    All: ClassVar[regenerateResult] = ...
    Attributes: ClassVar[regenerateResult] = ...
    Never: ClassVar[regenerateResult] = ...
    Skip: ClassVar[regenerateResult] = ...
    __entries: ClassVar[dict[str, tuple[regenerateResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.regenerateResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.regenerateResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.regenerateResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class registeredType:
    __members__: ClassVar[dict[str, registeredType]] = ...  # read-only
    Dependency: ClassVar[registeredType] = ...
    Node: ClassVar[registeredType] = ...
    Scheduler: ClassVar[registeredType] = ...
    Service: ClassVar[registeredType] = ...
    WorkItem: ClassVar[registeredType] = ...
    __entries: ClassVar[dict[str, tuple[registeredType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.registeredType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.registeredType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.registeredType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class result:
    __members__: ClassVar[dict[str, result]] = ...  # read-only
    All: ClassVar[result] = ...
    Failure: ClassVar[result] = ...
    Missing: ClassVar[result] = ...
    Success: ClassVar[result] = ...
    __entries: ClassVar[dict[str, tuple[result, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.result, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.result) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.result) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class scheduleResult:
    __members__: ClassVar[dict[str, scheduleResult]] = ...  # read-only
    CookCanceled: ClassVar[scheduleResult] = ...
    CookFailed: ClassVar[scheduleResult] = ...
    CookSucceeded: ClassVar[scheduleResult] = ...
    Deferred: ClassVar[scheduleResult] = ...
    Failed: ClassVar[scheduleResult] = ...
    FullDeferred: ClassVar[scheduleResult] = ...
    Succeeded: ClassVar[scheduleResult] = ...
    __entries: ClassVar[dict[str, tuple[scheduleResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.scheduleResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.scheduleResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.scheduleResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class serviceBlockCookType:
    __members__: ClassVar[dict[str, serviceBlockCookType]] = ...  # read-only
    Always: ClassVar[serviceBlockCookType] = ...
    Match: ClassVar[serviceBlockCookType] = ...
    Never: ClassVar[serviceBlockCookType] = ...
    __entries: ClassVar[dict[str, tuple[serviceBlockCookType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.serviceBlockCookType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.serviceBlockCookType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.serviceBlockCookType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class serviceClientLogType:
    __members__: ClassVar[dict[str, serviceClientLogType]] = ...  # read-only
    File: ClassVar[serviceClientLogType] = ...
    Off: ClassVar[serviceClientLogType] = ...
    Stdout: ClassVar[serviceClientLogType] = ...
    __entries: ClassVar[dict[str, tuple[serviceClientLogType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.serviceClientLogType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.serviceClientLogType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.serviceClientLogType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class serviceOwner:
    __members__: ClassVar[dict[str, serviceOwner]] = ...  # read-only
    Scheduler: ClassVar[serviceOwner] = ...
    Session: ClassVar[serviceOwner] = ...
    __entries: ClassVar[dict[str, tuple[serviceOwner, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.serviceOwner, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.serviceOwner) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.serviceOwner) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class serviceResetType:
    __members__: ClassVar[dict[str, serviceResetType]] = ...  # read-only
    Off: ClassVar[serviceResetType] = ...
    Reset: ClassVar[serviceResetType] = ...
    Restart: ClassVar[serviceResetType] = ...
    __entries: ClassVar[dict[str, tuple[serviceResetType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.serviceResetType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.serviceResetType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.serviceResetType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class serviceSchedulerType:
    __members__: ClassVar[dict[str, serviceSchedulerType]] = ...  # read-only
    Default: ClassVar[serviceSchedulerType] = ...
    FirstType: ClassVar[serviceSchedulerType] = ...
    Instance: ClassVar[serviceSchedulerType] = ...
    __entries: ClassVar[dict[str, tuple[serviceSchedulerType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.serviceSchedulerType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.serviceSchedulerType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.serviceSchedulerType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class serviceState:
    __members__: ClassVar[dict[str, serviceState]] = ...  # read-only
    Running: ClassVar[serviceState] = ...
    Starting: ClassVar[serviceState] = ...
    Stopped: ClassVar[serviceState] = ...
    __entries: ClassVar[dict[str, tuple[serviceState, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.serviceState, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.serviceState) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.serviceState) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class tickResult:
    __members__: ClassVar[dict[str, tickResult]] = ...  # read-only
    SchedulerBusy: ClassVar[tickResult] = ...
    SchedulerCancelCook: ClassVar[tickResult] = ...
    SchedulerReady: ClassVar[tickResult] = ...
    __entries: ClassVar[dict[str, tuple[tickResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.tickResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.tickResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.tickResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class transferResult:
    __members__: ClassVar[dict[str, transferResult]] = ...  # read-only
    Cached: ClassVar[transferResult] = ...
    Failure: ClassVar[transferResult] = ...
    Skip: ClassVar[transferResult] = ...
    Success: ClassVar[transferResult] = ...
    __entries: ClassVar[dict[str, tuple[transferResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.transferResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.transferResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.transferResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemCacheState:
    __members__: ClassVar[dict[str, workItemCacheState]] = ...  # read-only
    Clean: ClassVar[workItemCacheState] = ...
    CleanPending: ClassVar[workItemCacheState] = ...
    DirtyAlways: ClassVar[workItemCacheState] = ...
    DirtyEmpty: ClassVar[workItemCacheState] = ...
    DirtyMissing: ClassVar[workItemCacheState] = ...
    DirtyNew: ClassVar[workItemCacheState] = ...
    DirtyStale: ClassVar[workItemCacheState] = ...
    Undefined: ClassVar[workItemCacheState] = ...
    __entries: ClassVar[dict[str, tuple[workItemCacheState, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemCacheState, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemCacheState) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemCacheState) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemCookType:
    __members__: ClassVar[dict[str, workItemCookType]] = ...  # read-only
    Automatic: ClassVar[workItemCookType] = ...
    Generate: ClassVar[workItemCookType] = ...
    InProcess: ClassVar[workItemCookType] = ...
    OutOfProcess: ClassVar[workItemCookType] = ...
    Service: ClassVar[workItemCookType] = ...
    __entries: ClassVar[dict[str, tuple[workItemCookType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemCookType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemCookType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemCookType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemDataSource:
    __members__: ClassVar[dict[str, workItemDataSource]] = ...  # read-only
    JSONFile: ClassVar[workItemDataSource] = ...
    RPCMessage: ClassVar[workItemDataSource] = ...
    __entries: ClassVar[dict[str, tuple[workItemDataSource, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemDataSource, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemDataSource) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemDataSource) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemDirtyType:
    __members__: ClassVar[dict[str, workItemDirtyType]] = ...  # read-only
    Graph: ClassVar[workItemDirtyType] = ...
    Invalid: ClassVar[workItemDirtyType] = ...
    Node: ClassVar[workItemDirtyType] = ...
    WorkItem: ClassVar[workItemDirtyType] = ...
    __entries: ClassVar[dict[str, tuple[workItemDirtyType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemDirtyType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemDirtyType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemDirtyType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemExecutionType:
    __members__: ClassVar[dict[str, workItemExecutionType]] = ...  # read-only
    Cleanup: ClassVar[workItemExecutionType] = ...
    LongRunning: ClassVar[workItemExecutionType] = ...
    Regular: ClassVar[workItemExecutionType] = ...
    __entries: ClassVar[dict[str, tuple[workItemExecutionType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemExecutionType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemExecutionType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemExecutionType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemLogType:
    __members__: ClassVar[dict[str, workItemLogType]] = ...  # read-only
    Error: ClassVar[workItemLogType] = ...
    Message: ClassVar[workItemLogType] = ...
    Raw: ClassVar[workItemLogType] = ...
    Warning: ClassVar[workItemLogType] = ...
    __entries: ClassVar[dict[str, tuple[workItemLogType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemLogType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemLogType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemLogType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemReadyResult:
    __members__: ClassVar[dict[str, workItemReadyResult]] = ...  # read-only
    WorkItemBlocked: ClassVar[workItemReadyResult] = ...
    WorkItemFailed: ClassVar[workItemReadyResult] = ...
    WorkItemReady: ClassVar[workItemReadyResult] = ...
    __entries: ClassVar[dict[str, tuple[workItemReadyResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemReadyResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemReadyResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemReadyResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemStatType:
    __members__: ClassVar[dict[str, workItemStatType]] = ...  # read-only
    CookEndTime: ClassVar[workItemStatType] = ...
    CookStartTime: ClassVar[workItemStatType] = ...
    FileSize: ClassVar[workItemStatType] = ...
    QueueTime: ClassVar[workItemStatType] = ...
    ScheduleTime: ClassVar[workItemStatType] = ...
    __entries: ClassVar[dict[str, tuple[workItemStatType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemStatType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemStatType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemStatType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemState:
    __members__: ClassVar[dict[str, workItemState]] = ...  # read-only
    CookedCache: ClassVar[workItemState] = ...
    CookedCancel: ClassVar[workItemState] = ...
    CookedFail: ClassVar[workItemState] = ...
    CookedSuccess: ClassVar[workItemState] = ...
    Cooking: ClassVar[workItemState] = ...
    Dirty: ClassVar[workItemState] = ...
    Scheduled: ClassVar[workItemState] = ...
    Uncooked: ClassVar[workItemState] = ...
    Undefined: ClassVar[workItemState] = ...
    Waiting: ClassVar[workItemState] = ...
    __entries: ClassVar[dict[str, tuple[workItemState, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemState, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemState) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemState) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class workItemType:
    __members__: ClassVar[dict[str, workItemType]] = ...  # read-only
    Batch: ClassVar[workItemType] = ...
    DynamicPartition: ClassVar[workItemType] = ...
    Partition: ClassVar[workItemType] = ...
    Regular: ClassVar[workItemType] = ...
    StaticPartition: ClassVar[workItemType] = ...
    StaticWrapper: ClassVar[workItemType] = ...
    __entries: ClassVar[dict[str, tuple[workItemType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdg.workItemType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdg.workItemType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdg.workItemType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...
