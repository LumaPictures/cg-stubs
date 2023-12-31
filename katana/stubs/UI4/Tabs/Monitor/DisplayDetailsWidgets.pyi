# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.AnamorphDisplayOptions as AnamorphDisplayOptions
import CatalogAPI as CatalogAPI
import UI4.Util.DrawState as DrawState
import PyQt5.QtWidgets
import QT4Color as QT4Color
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from QT4Widgets.PopdownLabel import PopdownLabel
from UI4.Tabs.Monitor.MenuUtils import AddDisplayVisualizationActionsToMenu as AddDisplayVisualizationActionsToMenu, AddImageChannelActionsToMenu as AddImageChannelActionsToMenu, AddPixelCheckControlsToMenu as AddPixelCheckControlsToMenu, AddViewControlsToMenu as AddViewControlsToMenu, AddZoomActionsToMenu as AddZoomActionsToMenu
from typing import ClassVar, Set, Tuple

class ColorAction(PyQt5.QtWidgets.QAction):
    def __init__(self, parent, text, valuePolicy, changeCB) -> None: ...
    def _ColorAction__colorChanged(self, vpEvent): ...
    def _ColorAction__triggered(self, *args): ...
    def setupEvents(self, enable): ...

class DisplayChannelsLabel(PopdownLabel):
    def __init__(self, monitorWidget, viewIndex, parent) -> None: ...
    def buildMenu(self, menu): ...
    def getDrawState(self): ...
    def updateState(self): ...

class DisplayExposureLabel(PyQt5.QtWidgets.QLabel):
    def __init__(self, monitorWidget, viewIndex, parent) -> None: ...
    def getDrawState(self): ...
    def getText(self): ...
    def isDefault(self): ...
    def mousePressEvent(self, ev): ...
    def updateState(self): ...

class DisplayScaleLabel(PyQt5.QtWidgets.QFrame):
    def __init__(self, monitorWidget: MonitorWidget, parent: QWidget) -> None: ...
    def _DisplayScaleLabel__onImageModeApplied(self): ...

class DisplayVisualizationLabel(PopdownLabel):
    def __init__(self, monitorWidget, viewIndex, parent) -> None: ...
    def buildMenu(self, menu): ...
    def getDrawState(self): ...
    def updateState(self): ...

class InputColorspaceLabel(PopdownLabel):
    def __init__(self, monitorWidget, viewIndex, parent) -> None: ...
    def buildMenu(self, menu): ...
    def getDrawState(self): ...
    def updateState(self): ...

class LayerSelectionLabel(PopdownLabel):
    LAYER_TOOLTIP_TEMPLATE: ClassVar[str] = ...
    def __init__(self, monitorWidget, viewIndex, parent, previousLayerShortcut, nextLayerShortcut, alternateDefaultLayerShortcut) -> None: ...
    def _LayerSelectionLabel__getLayerList(self): ...
    def _LayerSelectionLabel__offsetLayerSelection(self, offset): ...
    def alternateDefaultLayer(self): ...
    def buildMenu(self, menu): ...
    def getDrawState(self): ...
    def resetAlternateLayer(self): ...
    def selectNextLayer(self): ...
    def selectPreviousLayer(self): ...
    def updateState(self): ...

class MatteMultLabel(PopdownLabel):
    def __init__(self, monitorWidget, viewIndex, parent) -> None: ...
    def buildMenu(self, menu): ...
    def getDrawState(self): ...
    def updateState(self): ...

class SwipeModeLabel(PopdownLabel):
    def __init__(self, monitorWidget, *args) -> None: ...
    def _SwipeModeLabel__buildModeList(self, menu, actionGroup, selectedMode, modeList): ...
    def buildMenu(self, menu): ...
    def updateState(self): ...

class _DisplayScalePopdown(PopdownLabel):
    def __init__(self, monitorWidget: MonitorWidget, parent: QWidget) -> None: ...
    def buildMenu(self, menu): ...
    def layerStack_scaleChanged_CB(self, x, final): ...
    def updateState(self): ...
