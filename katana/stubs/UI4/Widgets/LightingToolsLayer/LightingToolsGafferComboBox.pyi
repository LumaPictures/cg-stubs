# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PackageSuperToolAPI.BaseNode as BaseNode
import PackageSuperToolAPI.NodeUtils as NodeUtils
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from UI4.Widgets.LightingToolsLayer.LightingToolsUtils import GafferThreeListWatcher as GafferThreeListWatcher
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class EditMask:
    kHere: ClassVar[int] = ...
    kNone: ClassVar[int] = ...
    kNowhere: ClassVar[int] = ...
    kUpstream: ClassVar[int] = ...

class GafferButton(PyQt5.QtWidgets.QPushButton):
    kDimmedTextColor: ClassVar[str] = ...
    kHoverTextColor: ClassVar[str] = ...
    kIconSize: ClassVar[PyQt5.QtCore.QSize] = ...
    kNormalTextColor: ClassVar[str] = ...
    def __init__(self, gafferName: str, parent: Incomplete | None = ...) -> None: ...
    def getGafferNodeName(self) -> str: ...
    def getMasks(self) -> None: ...
    def isDimmed(self) -> bool: ...
    def setDimmed(self, isDimmed): ...
    def setMasks(self, lineMask: int, editMask: int): ...

class LightingToolsGafferComboBox(PyQt5.QtWidgets.QWidget):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _LightingToolsGafferComboBox__createDropdownButton(self): ...
    def _LightingToolsGafferComboBox__createDropdownMenu(self): ...
    def _LightingToolsGafferComboBox__onDropdownButtonPressed(self): ...
    def _LightingToolsGafferComboBox__onGafferListUpdated(self, gafferList: list[str]): ...
    def _LightingToolsGafferComboBox__onGafferSelected(self, gafferName: str): ...
    def _LightingToolsGafferComboBox__onNodeLocked(self): ...
    def _LightingToolsGafferComboBox__onNodegraphChanged(self): ...
    def _LightingToolsGafferComboBox__setGafferMasks(self, action: PyQt5.QtWidgets.QAction, lineMask: int, editMask: int, enableDimming: bool): ...
    def _LightingToolsGafferComboBox__setSelectedGafferNodeName(self, selectedGafferNodeName: str): ...
    def _LightingToolsGafferComboBox__updateDropdownButton(self, editMask: int): ...
    def _LightingToolsGafferComboBox__updateGafferHistory(self): ...
    def cycleSelectedGafferNode(self, delta: int = ...): ...
    def getGafferNodeName(self) -> str: ...
    def setSelectedLocations(self, locations: list[str]): ...

class LineMask:
    kIcon: ClassVar[int] = ...
    kLowerLine: ClassVar[int] = ...
    kNone: ClassVar[int] = ...
    kUpperLine: ClassVar[int] = ...
