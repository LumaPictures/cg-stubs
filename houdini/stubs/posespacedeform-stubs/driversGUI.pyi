# Houdini stubs generated from Houdini 22.0.466

from .ui.uiActions import *
from .ui.uiLineEdit import *
from .ui.uiLineEditList import *
from .ui.uiNavigation import *
from .ui.uiParamLabelButton import *
from .ui.uiToggleButton import *
from .Builder import *
from .defaults import *
from .qtExtendedClasses import *
import hou
from PySide6 import QtGui as QtGui
from collections.abc import Sequence
from hutil.Qt import QtCore, QtWidgets
from posespacedeform.editGUI import ActiveEdit as ActiveEdit
from posespacedeform.ui.uiLineEdit import UiLineEdit as UiLineEdit
from posespacedeform.ui.uiLineEditList import UiLineEditList as UiLineEditList
from types import TracebackType
from typing import Protocol

class _DriverCallback(Protocol):
    def __call__(self, driver_type: int | None, transform_type: int | None, driver_path: str, relative_path: str) -> object: ...

FIX_PANE_WINDOW_TIMEOUT: int
BLINK_SELECTION_1_TIMEOUT: int
BLINK_SELECTION_2_TIMEOUT: int
BLINK_SELECTION_3_TIMEOUT: int
BLINK_SELECTION_4_TIMEOUT: int

class EditDriverGUI(QtWidgets.QDialog):
    callback: _DriverCallback
    primaryselect: UiLineEdit
    drivertypecombo: QtWidgets.QComboBox
    drivertypewidget: QtWidgets.QWidget
    transformcombo: QtWidgets.QComboBox
    transformwidget: QtWidgets.QWidget
    nodeselect: UiLineEdit
    parmselect: UiLineEdit
    parmtupleselect: UiLineEdit
    cregionselect: UiLineEdit
    relativeselect: UiLineEdit
    cancelpsd: QtWidgets.QPushButton
    openpsd: QtWidgets.QPushButton
    def __init__(self, pos: QtCore.QPoint, title: str, relative_node: hou.ChopNode | None, select_multiple: bool, callback: _DriverCallback) -> None: ...
    def initEditDriverGUI(self, driver_type: int, transform_type: int, driver_path: str, relative_path: str) -> None: ...
    def reject(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...

class DriversGUI(QtWidgets.QWidget):
    childGUI: EditDriverGUI | None
    drivers_node: hou.ChopNode | None
    psd_node: hou.SopNode | None
    master_set: dict[str, Sequence[int | str]]
    activeEdit: ActiveEdit | None
    driver_refresh: bool
    update_driver_index: int
    driverselect: UiLineEditList
    adddriver: QtWidgets.QPushButton
    driverparam: UiLineEdit
    drivertitle: QtWidgets.QLabel
    def __init__(self, activeEdit: ActiveEdit | None = None, title: str = '', toggleable: bool = False) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def initDriversGUI(self, psd_node: hou.SopNode | None, drivers_node: hou.ChopNode | None) -> None: ...
    def setDrivers(self, drivers_set: Sequence[Sequence[int | str]]) -> None: ...
    def getDrivers(self) -> list[Sequence[int | str]]: ...
    def refreshDrivers(self) -> None: ...
