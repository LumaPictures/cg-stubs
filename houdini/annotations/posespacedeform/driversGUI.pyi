from collections.abc import Sequence
from types import TracebackType
from typing import Protocol

import hou
from PySide6 import QtCore, QtGui, QtWidgets

from posespacedeform.editGUI import ActiveEdit
from posespacedeform.ui.uiLineEdit import UiLineEdit
from posespacedeform.ui.uiLineEditList import UiLineEditList

class _DriverCallback(Protocol):
    def __call__(
        self, driver_type: int | None, transform_type: int | None, driver_path: str, relative_path: str
    ) -> object: ...

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
    def __init__(
        self,
        pos: QtCore.QPoint,
        title: str,
        relative_node: hou.ChopNode | None,
        select_multiple: bool,
        callback: _DriverCallback,
    ) -> None: ...
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
    def __init__(self, activeEdit: ActiveEdit | None = ..., title: str = ..., toggleable: bool = ...) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def initDriversGUI(self, psd_node: hou.SopNode | None, drivers_node: hou.ChopNode | None) -> None: ...
    def setDrivers(self, drivers_set: Sequence[Sequence[int | str]]) -> None: ...
    def getDrivers(self) -> list[Sequence[int | str]]: ...
    def refreshDrivers(self) -> None: ...
