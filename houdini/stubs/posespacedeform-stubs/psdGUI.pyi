# Houdini stubs generated from Houdini 22.0.466

from .ui.uiActions import *
from .ui.uiLineEdit import *
from .ui.uiNavigation import *
from .ui.uiParamLabelButton import *
from .ui.uiToggleButton import *
from .Builder import *
from .buildGUI import *
from .defaults import *
from .driversGUI import *
from .initGUI import *
from .nameGUI import *
from .openGUI import *
from .poseshapeGUI import *
from .qtExtendedClasses import *
import hou
from collections.abc import Callable, Sequence
from hutil.Qt import QtCore, QtGui, QtWidgets
from posespacedeform.buildGUI import BuildGUI as BuildGUI
from posespacedeform.driversGUI import DriversGUI as DriversGUI
from posespacedeform.editGUI import ActiveEdit as ActiveEdit
from posespacedeform.nameGUI import NameGUI as NameGUI
from posespacedeform.openGUI import OpenGUI as OpenGUI
from posespacedeform.poseshapeGUI import PoseShapeListGUI as PoseShapeListGUI
from posespacedeform.qtExtendedClasses import SwitchButton as SwitchButton

from typing import TypeAlias
from typing import TypeAlias
_NetworkLayoutCallback: TypeAlias = Callable[[Sequence[hou.OpNode | None]], object]
DRIVERS_REFRESH_TIMEOUT: int

class PSDGUI(QtWidgets.QScrollArea):
    label: str
    setup_type: int
    psd_node: hou.SopNode | None
    editPSDCallback: _NetworkLayoutCallback | None
    closeDialogCallback: Callable[[], object] | None
    childGUI: OpenGUI | BuildGUI | NameGUI | None
    activeEdit: ActiveEdit
    drivergui: DriversGUI
    poseshapegui: PoseShapeListGUI
    timer: QtCore.QTimer
    drivers_refresh: bool
    refreshing_related_psd_names: bool
    skelroot_node: hou.ObjNode | None
    drivers_node: hou.ChopNode | None
    menubar: hou.qt.MenuBar
    menunew: QtWidgets.QMenu
    menupose: QtWidgets.QMenu
    menugo: QtWidgets.QMenu
    poseaddpsd: QtGui.QAction
    posecopytonewpsd: QtGui.QAction
    posemovetonewpsd: QtGui.QAction
    psdpathlayout: QtWidgets.QHBoxLayout
    psdpath: QtWidgets.QComboBox
    psdpathlabel: QtWidgets.QLabel
    psdpathjumpbutton: QtWidgets.QToolButton
    psdbutton: SwitchButton
    addpose: QtWidgets.QPushButton
    currentdriver: QtWidgets.QLabel
    psdlayout: QtWidgets.QVBoxLayout
    mainlayout: QtWidgets.QVBoxLayout
    widget: QtWidgets.QWidget
    def __init__(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def reset(self) -> None: ...
    def initPSDGUI(self, network_layout: Sequence[hou.OpNode | None]) -> None: ...
    def startDriversRefresh(self) -> None: ...
    def stopDriversRefresh(self) -> None: ...
    def refreshDrivers(self) -> None: ...
    def setSetupPSDCallback(self, edit_fcn: _NetworkLayoutCallback | None, close_fcn: Callable[[], object] | None) -> None: ...
    def setPSDUninitialized(self) -> None: ...
    def jumpToPSDNode(self) -> None: ...
