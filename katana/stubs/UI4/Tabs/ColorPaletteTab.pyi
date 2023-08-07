# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyImath
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Color as QT4Color
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SortablePanel as SortablePanel
import UI4 as UI4
import UI4.Widgets.SortablePanel
import Utils as Utils
from PyUtilModule.VirtualKatana import ColorPaletteManager as ColorPaletteManager, Widgets as Widgets
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

PluginRegistry: list

class ColorMathArea(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent) -> None: ...
    def _ColorMathArea__update(self, *args, **kwargs): ...
    def setGlobals(self, globalsDict): ...

class ColorPaletteEditor(UI4.Widgets.SortablePanel.SortablePanelFormWidget):
    globalsChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, policy, factory) -> None: ...
    def _ColorPaletteEditor__rebuildAllCB(self, args): ...
    def _ColorPaletteEditor__setupEventHandlers(self, enabled): ...
    def _freeze(self): ...
    def _thaw(self): ...
    def addColor(self): ...
    def buildAddMenu(self, menu): ...
    def clearAll(self): ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def emit_globalsChanged(self, *args, **kwargs): ...
    def getGlobals(self): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def updatePanels(self): ...

class ColorPalettePanel(BaseTab):
    def __init__(self, parent) -> None: ...
    def _ColorPalettePanel__colorPalette_globalsChanged_CB(self): ...
    def _ColorPalettePanel__createColorPalette(self, index: Incomplete | None = ...): ...
    def _ColorPalettePanel__recreatePolicy(self, args): ...

class CustomVector(PyImath.V3d):
    def __add__(self, other): ...
    def __mul__(self, other): ...
    def __sub__(self, other): ...
    def __truediv__(self, other): ...

class InputPanel(UI4.Widgets.SortablePanel.SortablePanelBase):
    def __init__(self, parent, name, policy, factory, callbackfcn) -> None: ...
    def adopt(self, layer): ...
    def getWidget(self): ...
