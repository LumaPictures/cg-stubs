from .ui.uiActions import *
from .ui.uiLineEdit import *
from .ui.uiLineEditList import *
from .ui.uiNavigation import *
from .Builder import *
from .defaults import *
import hou
from PySide6 import QtGui as QtGui
from collections.abc import Sequence
from hutil.Qt import QtCore, QtWidgets
from posespacedeform.ui.uiLineEdit import UiLineEdit as UiLineEdit
from posespacedeform.ui.uiLineEditList import UiLineEditList as UiLineEditList, UiLineEditListItem as UiLineEditListItem

from typing import TypeAlias
from collections.abc import Callable
from typing import TypeAlias
_NetworkLayoutCallback: TypeAlias = Callable[[Sequence[hou.OpNode | None]], object]
UPDATE_PSD_LIST_TIMEOUT: int

class OpenGUI(QtWidgets.QDialog):
    objroot: str
    restgeo_node: hou.OpNode | None
    skelroot_node: hou.OpNode | None
    output_node: None
    psd_node: hou.OpNode | None
    poseshapessubnet_node: hou.OpNode | None
    posesubnet_node: hou.OpNode | None
    default_posestash: hou.OpNode | None
    default_pose: hou.OpNode | None
    drivers_node: hou.ChopNode | None
    transforms_node: hou.ChopNode | None
    setupPSDCallback: _NetworkLayoutCallback | None
    selectedItem: UiLineEditListItem | None
    exclude_nodes: Sequence[hou.OpNode | None]
    psdlistselect: UiLineEditList
    setuptype: UiLineEdit
    driverslist: UiLineEditList
    skintype: UiLineEdit
    blendattrib: UiLineEdit
    restgeoselect: UiLineEdit
    skelrootselect: UiLineEdit
    poseshapessubnetselect: UiLineEdit
    posesubnetselect: UiLineEdit
    cancelpsd: QtWidgets.QPushButton
    openpsd: QtWidgets.QPushButton
    advancedbox: QtWidgets.QGroupBox
    def __init__(self, pos: QtCore.QPoint, objroot: str = '/obj', exclude_nodes: Sequence[hou.OpNode | None] | None = None) -> None: ...
    def reject(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def setSetupPSDCallback(self, cb: _NetworkLayoutCallback | None) -> None: ...
    def selectPSDPath(self, psd_path: str) -> None: ...
    def UpdatePaths(self, psdpath: str | None) -> None: ...
