# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils as Utils
import typing
from NodeGraphTab.NodegraphPanel import NodegraphPanel
from _typeshed import Incomplete
from typing import Any, Set, Tuple

class LayeredMenu:
    def __init__(self, populateCallback: typing.Callable, actionCallback: typing.Callable, keyboardShortcut: str, alwaysPopulate: bool = ..., onlyMatchWordStart: bool = ..., sortAlphabetically: bool = ..., checkAvailabilityCallback: typing.Optional[typing.Callable] = ...) -> None: ...
    def addEntry(self, value: object, text: Incomplete | None = ..., color: Incomplete | None = ..., size: Incomplete | None = ..., textColor: Incomplete | None = ...): ...
    def alwaysPopulate(self) -> bool: ...
    def checkAvailability(self, tab: NodegraphPanel) -> bool: ...
    def clear(self): ...
    def getAssociatedRenderer(self) -> str: ...
    def getChosenValue(self) -> Any | None: ...
    def getEntries(self) -> list[LayeredMenuEntry]: ...
    def getKeyboardShortcut(self) -> str: ...
    def isPopulated(self) -> bool: ...
    def onEntryChosen(self, value: object, tab: NodegraphPanel) -> Any | None: ...
    def onlyMatchWordStart(self) -> bool: ...
    def populate(self, tab: NodegraphPanel) -> bool: ...
    def setAssociatedRenderer(self, associatedRenderer: str): ...
    def setChosenValue(self, value: object | None): ...
    def shouldSortAlphabetically(self) -> bool: ...

class LayeredMenuEntry:
    def __init__(self, value: object, text: Incomplete | None = ..., color: Incomplete | None = ..., size: Incomplete | None = ..., textColor: Incomplete | None = ...) -> None: ...
    def getColor(self) -> None | None: ...
    def getSize(self) -> None | None: ...
    def getText(self) -> str: ...
    def getTextColor(self) -> None | None: ...
    def getValue(self) -> Any: ...

def GetLayeredMenu(layeredMenuID: str) -> LayeredMenu | None: ...
def GetLayeredMenuIDByAssociatedRenderer(associatedRenderer: str) -> str | None: ...
def GetLayeredMenuIDs() -> list[str]: ...
def RegisterLayeredMenu(layeredMenu: LayeredMenu, layeredMenuID: str): ...
