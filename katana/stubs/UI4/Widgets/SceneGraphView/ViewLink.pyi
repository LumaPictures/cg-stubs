# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import SceneGraphViewColumn
import abc
import typing
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ViewLink(abc.ABC):
    _abc_impl: ClassVar[_abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    def addOrUpdateLocation(self, handle, topLevelHandle): ...
    def addOrUpdateTopLevelLocation(self, topLevelHandle): ...
    def allowMultipleSelection(self) -> bool: ...
    def clearExpandedLocationsRegistry(self, clearCurrent: bool = ...): ...
    def collapseLocation(self, handle, topLevelHandle): ...
    def evaluateFilterRules(self, handle: Incomplete | None = ..., topLevelHandle: Incomplete | None = ...): ...
    def expandLocation(self, handle, topLevelHandle): ...
    def frozenWhenHidden(self) -> bool: ...
    def getAllLocations(self): ...
    def getChildLocations(self, locationPath, topLevelLocationPath, visibleOnly: bool = ..., allDescendants: bool = ...): ...
    def getOverrideNodeAndParameterName(self, locationPath: str, attributeName: str) -> None: ...
    def getSelectedLocations(self): ...
    def getUpdateSuppressor(self): ...
    def getWidget(self): ...
    def isLocationExpanded(self, handle, topLevelHandle) -> bool: ...
    def removeLocation(self, handle, topLevelHandle): ...
    def removeTopLevelLocation(self, topLevelHandle): ...
    def resetModel(self): ...
    def saveExpandedLocations(self): ...
    def scrollToLocation(self, handle: SceneGraphHandle, topLevelHandle: SceneGraphHandle): ...
    def selectChildLocations(self, replaceSelection: bool = ...): ...
    def selectLocations(self, locations, replaceSelection: bool = ...): ...
    def selectParentLocations(self, replaceSelection: bool = ...): ...
    def setAboutToDragCallback(self, callback): ...
    def setAllowMultipleSelection(self, allowMultipleSelection: bool): ...
    def setAttributeDataChildren(self, handle: SceneGraphHandle, topLevelHandle: SceneGraphHandle, attributeDataChildren): ...
    def setColumnTitles(self, columnTitleInfo: list[SceneGraphViewColumn.SceneGraphColumnTitle]): ...
    def setColumnWidths(self, columnWidths): ...
    def setContextMenuEventCallback(self, callback): ...
    def setDragMoveEventCallback(self, callback: typing.Callable): ...
    def setDropEventCallback(self, callback: typing.Callable): ...
    def setExpandsOnDoubleClick(self, expandsOnDoubleClick: bool): ...
    def setFrozenWhenHidden(self, frozenWhenHidden: bool = ...): ...
    def setKeyPressEventCallback(self, callback): ...
    def setOverrideParameterRequestCallback(self, callback: typing.Callable): ...
    def setSelectionChangedCallback(self, callback): ...
    def setSelectionState(self, topLevelLocationPath, locationPath, selected): ...
    def sortChildrenUnderLocation(self, handle: SceneGraphHandle, topLevelHandle: SceneGraphHandle): ...
    def sortTopLevelLocations(self): ...
    def updateItemDelegates(self): ...
    def updateLocationIcons(self, handle, topLevelHandle): ...
    def updateSelection(self, selectedLocations, deselectedLocations): ...
    def updateViewport(self): ...
