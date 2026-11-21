import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from . import brushpanel as brushpanel
from edit.lop import panel as panel
from hutil.Qt import QtWidgets
from layout.brushitemmodel import BrushInfoManager, BrushItemModel, _BrushInfo
from paintinstances.brushpanel import BrushToolBar as BrushToolBar
from typing import TypedDict

class _PythonPanelKwargs(TypedDict):
    paneTab: hou.PaneTab

class InstancerPathEdit(QtWidgets.QLineEdit):
    commitRequested: PySide6.QtCore.Signal
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...
    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None: ...

class LopPaintInstancesPanel(QtWidgets.QWidget):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def model(self) -> BrushItemModel: ...
    def onBrushSelected(self, brush_info: _BrushInfo) -> None:
        """ Update the command toolbar title with the current
            selected brush label.
        """
    def onInstancerPathEdited(self) -> None: ...
    def onDisplayBrushDebugger(self) -> None: ...
    def onCreateNewBrush(self) -> None: ...
    def onAssetReload(self) -> None: ...
    def brushInfoManager(self) -> BrushInfoManager: ...
    def brushToolbar(self) -> BrushToolBar: ...
    def onActivate(self, kwargs: _PythonPanelKwargs) -> None:
        """ Called by the pypanel framework.
        """
    def onDeactivate(self) -> None:
        """ Called by the pypanel framework.
        """
    def onDestroy(self) -> None: ...
    def onNodePathChanged(self, node: hou.OpNode | None) -> None: ...
