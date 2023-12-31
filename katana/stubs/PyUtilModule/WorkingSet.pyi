# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnAttribute
import typing
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet
from _typeshed import Incomplete
from typing import Any, ClassVar, Set, Tuple

class LocationStateMap(dict):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _LocationStateMap__tokenizeLocationPath(self, locationPath: str) -> list[str]: ...
    def deleteSubTree(self, locationPath: str, deleteRoot: bool = ...): ...
    def get(self, key: str, default: Incomplete | None = ...) -> Any: ...
    def getNearestSubTree(self, locationPath: str) -> Tuple[LocationStateMap, str]: ...
    def getSubTree(self, locationPath: str) -> LocationStateMap | None: ...
    def items(self, rootPath: Incomplete | None = ...) -> typing.Iterator: ...
    def keys(self, rootPath: Incomplete | None = ...) -> typing.Iterator: ...
    def pop(self, key: str, *args) -> Any: ...
    def values(self, rootPath: Incomplete | None = ...) -> typing.Iterator: ...
    def __contains__(self, key: str) -> bool: ...
    def __delitem__(self, key: str): ...
    def __getitem__(self, key: str) -> Any: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self, rootPath: Incomplete | None = ...) -> int: ...
    def __setitem__(self, key: str, value: object) -> None: ...

class WorkingSet:
    class State:
        Empty: ClassVar[int] = ...
        Excluded: ClassVar[int] = ...
        ExcludedWithChildren: ClassVar[int] = ...
        Included: ClassVar[int] = ...
        IncludedWithChildren: ClassVar[int] = ...
        @classmethod
        def coerceToBitmask(cls, bitmaskOrStates: int | list[int | None]) -> int: ...
        @classmethod
        def fromStateString(cls, stateString: str) -> int | None: ...
        @classmethod
        def getBitmaskFromStates(cls, states: list[int]) -> int: ...
        @classmethod
        def getStateString(cls, state: int) -> str: ...
        @classmethod
        def getStatesFromBitmask(cls, bitmask: int) -> list[int]: ...
        @classmethod
        def getValidStates(cls) -> list[int]: ...
        @classmethod
        def getValidStatesBitmask(cls) -> int: ...
        @classmethod
        def validate(cls, state: int): ...
    def __init__(self) -> None: ...
    def _WorkingSet__checkCallback(self, callback: typing.Callable, expectedArgNames: tuple[str, ...]): ...
    def _callAllowedStatesChangedCallbacks(self, sender): ...
    def _callLocationStateChangedCallbacks(self, locationStateChanges, sender): ...
    def _callWorkingSetClearedCallbacks(self): ...
    def addAllowedStatesChangedCallback(self, callback: typing.Callable): ...
    def addLocationStateChangedCallback(self, callback: typing.Callable): ...
    def addWorkingSetClearedCallback(self, callback: typing.Callable): ...
    def asGroupAttribute(self) -> PyFnAttribute.GroupAttribute: ...
    def clear(self, clearAllowedStates: bool = ..., sender: Incomplete | None = ..., useCallbacks: bool = ...) -> bool: ...
    def clearLocations(self, locationPathOrPaths: str | list[str], clearAllowedStates: bool = ..., clearGiven: bool = ..., clearChildren: bool = ..., sender: Incomplete | None = ..., useCallbacks: bool = ...) -> bool: ...
    def containsLocation(self, locationPath: str) -> bool: ...
    def excludeLocations(self, locationPathOrPaths: str | list[str], allowedStates: Incomplete | None = ..., sender: Incomplete | None = ...) -> bool: ...
    def excludeLocationsWithChildren(self, locationPathOrPaths: str | list[str], allowedStates: Incomplete | None = ..., sender: Incomplete | None = ...) -> bool: ...
    @classmethod
    def fromGroupAttribute(cls, groupAttribute: PyFnAttribute.GroupAttribute, sender: Incomplete | None = ..., useCallbacks: bool = ..., workingSetInstance: Incomplete | None = ...) -> WorkingSet: ...
    def getAllowedStates(self) -> list[int]: ...
    def getLocationAllowedStates(self, locationPath: str) -> list[int]: ...
    def getLocationState(self, locationPath: str) -> int: ...
    def getLocations(self, rootPath: Incomplete | None = ...) -> list[str]: ...
    def getLocationsAndStates(self, rootPath: Incomplete | None = ...) -> list[tuple[str, int]]: ...
    def getLocationsByState(self, state: int, rootPath: Incomplete | None = ...) -> list[str]: ...
    def getMinimumAllowedStateForLocation(self, locationPath: str) -> int | None: ...
    def getNumLocations(self, rootPath: Incomplete | None = ...) -> int: ...
    def getRootLocations(self) -> list[str]: ...
    def includeLocations(self, locationPathOrPaths: str | list[str], allowedStates: Incomplete | None = ..., sender: Incomplete | None = ...) -> bool: ...
    def includeLocationsWithChildren(self, locationPathOrPaths: str | list[str], allowedStates: Incomplete | None = ..., sender: Incomplete | None = ...) -> bool: ...
    def isIncludedLeafLocation(self, locationPath: str) -> bool: ...
    def isStateAllowed(self, state: int) -> bool: ...
    def isStateAllowedForLocation(self, locationPath: str, state: int) -> bool: ...
    def iterateLocationAncestors(self, locationPath: str, includeLocation: bool = ...) -> typing.Iterator: ...
    def matchesAnyChildren(self, locationPath: str, checkInheritance: bool = ...) -> bool: ...
    def matchesChildrenByInheritance(self, locationPath: str) -> bool: ...
    def matchesLocation(self, locationPath: str) -> bool: ...
    def removeAllCallbacks(self): ...
    def removeAllowedStatesChangedCallback(self, callback: typing.Callable): ...
    def removeLocationStateChangedCallback(self, callback: typing.Callable): ...
    def removeWorkingSetClearedCallback(self, callback: typing.Callable): ...
    def setAllowedStates(self, allowedStates: int | list[int | None], sender: Incomplete | None = ...) -> bool: ...
    def setLocationAllowedStates(self, locationPathOrPaths: str | list[str], allowedStates: int | list[int | None], sender: Incomplete | None = ...) -> bool: ...
    def setLocationStates(self, locationPathOrPaths: str | list[str], state: int, allowedStates: Incomplete | None = ..., sender: Incomplete | None = ..., useCallbacks: bool = ...) -> bool: ...
