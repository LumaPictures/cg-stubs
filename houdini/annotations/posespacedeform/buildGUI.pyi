from collections.abc import Callable, Sequence
from typing import TypeAlias

import hou
from PySide6 import QtCore, QtGui, QtWidgets

from posespacedeform.driversGUI import DriversGUI
from posespacedeform.qtExtendedClasses import ToggleableWidget
from posespacedeform.ui.uiLineEdit import UiLineEdit

_NetworkLayoutCallback: TypeAlias = Callable[[Sequence[hou.OpNode | None]], object]

AUTO_SELECT_SKINNING_TYPE: bool

class BuildGUI(QtWidgets.QDialog):
    setup_name_default: str
    input_node: hou.OpNode | None
    input_default_msg: str
    driversgui: DriversGUI
    restgeo_node: hou.OpNode | None
    restgeo_default_msg: str
    skelroot_node: hou.OpNode | None
    skelroot_default_msg: str
    poseshapessubnet_node: hou.OpNode | None
    poseshapessubnet_default_msg: str
    posesubnet_node: hou.OpNode | None
    posesubnet_default_msg: str
    setup_type: int
    skin_type: int
    skinblend_attrib: str
    setupPSDCallback: _NetworkLayoutCallback | None
    default_pose: hou.OpNode | None
    default_posestash: hou.OpNode | None
    nameselect: UiLineEdit
    inputselect: UiLineEdit
    inputpathbar: QtWidgets.QToolBar
    skintypecombo: QtWidgets.QComboBox
    skintypewidget: QtWidgets.QWidget
    skinblendattribcombo: QtWidgets.QComboBox
    skinblendwidget: QtWidgets.QWidget
    restgeoselect: UiLineEdit
    restposefromcombo: QtWidgets.QComboBox
    restposefromwidget: QtWidgets.QWidget
    skelrootselect: UiLineEdit
    poseshapessubnetselect: UiLineEdit
    posesubnetselect: UiLineEdit
    cancelpsd: QtWidgets.QPushButton
    openpsd: QtWidgets.QPushButton
    optionsbox: ToggleableWidget
    closed_options_height: int
    def __init__(
        self,
        setup_type: int,
        pos: QtCore.QPoint,
        init_network_layout: Sequence[hou.OpNode | None] | None = ...,
        init_network_config: Sequence[hou.OpNode | int | str | None] | None = ...,
        init_drivers_node: hou.ChopNode | None = ...,
    ) -> None: ...
    def accept(self) -> None: ...
    def reject(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def setSetupPSDCallback(self, cb: _NetworkLayoutCallback | None) -> None: ...
    def UpdatePaths(self) -> None: ...
