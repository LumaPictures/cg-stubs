# Houdini stubs generated from Houdini 22.0.466

from _pdg import *
from .toplevel import *
import logging
import typing
from . import context as context, types as types
from .dependency import PyDependency as PyDependency
from .mapper import PyMapper as PyMapper
from .partitioner import PyPartitioner as PyPartitioner
from .processor import PyProcessor as PyProcessor
from .scheduler import PyScheduler as PyScheduler
from .workitem import PyWorkItem as PyWorkItem
from _pdg import Event as Event, WorkItem as WorkItem
from collections import deque
from collections.abc import Callable as Callable, Iterable
from typing import Any, Literal, TypeGuard

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
logger: logging.Logger

def defaultErrorHandler(event: Event) -> None: ...
def envVar(item: WorkItem, var: str) -> int | float | str:
    """
    Returns an environment variable value for a given work item and env var
    name. Raises a TypeError if the workitem is None or a KeyError if the
    var name does not exist
    item        item to search
    var         environment varialbe name
    """
def strData(item: WorkItem, field: str, index: int = 0) -> str:
    """
    Returns string data with the given name and index.
    Raises ValueError if not found.
    item        item to search
    field       data field name
    index       index of data in string array
    """
def strDataArray(item: WorkItem, field: str) -> list[str]:
    """
    Returns string data array for the given name.
    Raises ValueError if not found.
    item        item to search
    field       data field name
    """
def hasStrData(item: WorkItem, field: str, index: int = 0) -> bool:
    """
    Returns True if the item has string data with the given name
    and the given index.
    item        item to search
    field       string tag for data
    index       index of data in int array
    """
def intData(item: WorkItem, field: str, index: int = 0) -> int:
    """
    Returns int data with the given tag and index.
    Raises ValueError if not found.
    item        item to search
    field       string tag for data
    index       index of data in int array
    """
def intDataArray(item: WorkItem, field: str) -> list[int]:
    """
    Returns int data array for the given tag.
    Raises ValueError if not found.
    item        item to search
    field       string tag for data
    """
def hasIntData(item: WorkItem, field: str, index: int = 0) -> bool:
    """
    Returns True if the item has int data with the given name
    and the given index.
    item        item to search
    field       string tag for data
    index       index of data in int array
    """
def floatData(item: WorkItem, field: str, index: int = 0) -> float:
    """
    Returns float data with the given tag and index.
    Raises ValueError if not found.
    item        item to search
    field       string tag for data
    index       index of data in float array
    """
def floatDataArray(item: WorkItem, field: str) -> list[float]:
    """
    Returns float data array for the given tag.
    Raises ValueError if not found.
    item        item to search
    field       string tag for data
    """
def hasFloatData(item: WorkItem, field: str, index: int = 0) -> bool:
    """
    Returns True if the item has float data with the given name
    and the given index.
    item        item to search
    field       string tag for data
    index       index of data in int array
    """

class SearchType:
    ImmediateParent: int
    UpstreamTraversePartitions: int
    UpstreamStopAtPartitions: int

def find_first_of(item_list: deque[WorkItem], pred: Callable[[WorkItem], _T | None], stop_at_partition: bool) -> tuple[_T, WorkItem] | None:
    """
    Finds the first upstream item in a breadth-first
    traversal of the dependency graph which returns
    a non-None result from the predicate.
    Returns (predicate result, matching item) or None

    item_list           collections.deque of leaf items to start at
    pred                Predicate which returns None unless item matches
    stop_at_parition    True means search does not enter partions
    """
@typing.overload
def resultData(item: WorkItem, tag: str, localized: bool = ..., as_list: Literal[False] = ...) -> str | None: ...
@typing.overload
def resultData(item: WorkItem, tag: str, localized: bool, as_list: Literal[True]) -> list[str] | None: ...
@typing.overload
def resultData(item: WorkItem, tag: str, localized: bool = ..., *, as_list: Literal[True]) -> list[str] | None: ...
@typing.overload
def resultData(item: WorkItem, tag: str, localized: bool = ..., as_list: bool = ...) -> str | list[str] | None: ...
def hasResultData(item: WorkItem, tag: str) -> bool:
    """
    Returns True if there is matching resultData in the given item.
    item        item to search
    tag         tag to search for
    """
@typing.overload
def resultDataIndex(item: WorkItem, tag: str, index: int, default: str = ..., localized: bool = ...) -> str: ...
@typing.overload
def resultDataIndex(item: WorkItem, tag: str, index: int, default: _T, localized: bool = ...) -> str | _T: ...
@typing.overload
def findResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = ..., as_list: Literal[False] = ...) -> str | None: ...
@typing.overload
def findResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool, as_list: Literal[True]) -> list[str] | None: ...
@typing.overload
def findResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = ..., *, as_list: Literal[True]) -> list[str] | None: ...
@typing.overload
def findResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = ..., as_list: bool = ...) -> str | list[str] | None: ...
@typing.overload
def findDirectResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = ..., as_list: Literal[False] = ...) -> str | None: ...
@typing.overload
def findDirectResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool, as_list: Literal[True]) -> list[str] | None: ...
@typing.overload
def findDirectResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = ..., *, as_list: Literal[True]) -> list[str] | None: ...
@typing.overload
def findDirectResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = ..., as_list: bool = ...) -> str | list[str] | None: ...
def collectDirectResultData(item: WorkItem | Iterable[WorkItem], tag: str, localized: bool = False) -> list[str]:
    """
    Returns a list of matching result data, if the given item is a list
    it will return a combined list of all matching results.  Does not do
    any task graph traversal.
    item        item or list of items to search
    tag         tag to search for
    localized   True means localize the results, False to return as-is
    """
def findData(item: WorkItem, name: str) -> Any:
    """
    Does a breadth-first search for item data by name all the way to the static
    ancestors
    Returns the matching value.
    Returns None if not found.
    item        item to search
    name        name to search for
    """
def findDirectData(item: WorkItem, name: str) -> Any:
    """
    Does a breadth-first search for item data by name but stops search at partitions.
    Returns the matching value.
    Returns None if not found.
    item        item to search
    name        name to search for
    """
def resultTagMenu(prefix: str) -> list[str]: ...
def generateWhenMenu() -> list[str]: ...
def cacheModeMenu() -> list[str]: ...
def mergeOperationMenu() -> list[str]: ...
def isIterable(obj: object) -> TypeGuard[Iterable[Any]]:
    """Return True if the specified object is an iterable type but not a string
        and False otherwise."""
def genericGeneratorPresets() -> list[str]:
    """Returns preset commands to be used by the genericgenerator TOP.
        Each two elements represents a menu option, the first element is the
        command and the second is the option label.
    """
