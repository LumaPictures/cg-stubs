import threading
from collections.abc import Callable, Mapping
from typing import Never, TypeVar, overload

import baseinfowindow
import pdgd
from _pdgd import DataLayerInterface, _PythonValue
from pdgd.util import PDGDObject
from PySide6 import QtCore, QtGui, QtWidgets

_V = TypeVar("_V")
_D = TypeVar("_D")

prop_keys: dict[str, str]

@overload
def getObjectProperty(object: Mapping[str, _V], prop_name: str) -> _V | str: ...
@overload
def getObjectProperty(object: Mapping[str, _V], prop_name: str, default_value: _D) -> _V | _D: ...
def getObjectProperty(object: Mapping[str, _V], prop_name: str, default_value: object = ...) -> object: ...
def getObjectPropertyArray(object: Mapping[str, _V], prop_name: str) -> _V | list[Never]: ...

class RemoteTaskInfoWindow(baseinfowindow.BaseInfoWindow):
    do_update: QtCore.Signal
    received_localized: QtCore.Signal
    node_object: PDGDObject | None
    my_parent: QtWidgets.QWidget | None
    pinned: bool
    ispinnable: bool
    ctrl_pressed: bool
    localized: bool
    readlog: bool
    scheduler_object: None
    graph_name: str
    data_layer: DataLayerInterface
    scheduler_name: str
    work_item_path: str
    localized_inputs: list[str]
    localized_expected_inputs: list[str]
    localized_outputs: list[str]
    localized_expected_outputs: list[str]
    enable_log: bool
    log_text: str | None
    wi_lock: threading.Lock
    wi_object: PDGDObject
    graph_object: PDGDObject
    pinbutton: QtWidgets.QToolButton
    localizebutton: QtWidgets.QToolButton
    reloadbutton: QtWidgets.QToolButton
    toolbar: QtWidgets.QFrame
    basicsection: baseinfowindow.HtmlInfoSection
    infosection: baseinfowindow.HtmlInfoSection
    logsection: baseinfowindow.HtmlInfoSection
    splitter: baseinfowindow.InfoSplitter
    def __init__(self, data_layer: DataLayerInterface, work_item_path: str, parent: QtWidgets.QWidget | None) -> None: ...
    def sendSchedulerCommand(self, command: str, param: _PythonValue, callback: Callable[[pdgd.ObjectProperty], object]) -> bool: ...
    def receivedLocalizedLogURI(self, log_uri: pdgd.ObjectProperty) -> None: ...
    def receivedLogURI(self, log_uri: pdgd.ObjectProperty) -> None: ...
    def receivedLocalized(self, paths: pdgd.ObjectProperty) -> None: ...
    def reposition(self, mousepos: QtCore.QPoint | None = ...) -> None: ...
    def pin(self) -> None: ...
    def display(self, data_layer: DataLayerInterface, work_item_path: str, mousepos: QtCore.QPoint, pinnable: bool = ...) -> None: ...
    def togglePinState(self) -> None: ...
    def toggleLocalizeState(self) -> None: ...
    def reload(self) -> None: ...
    def changeEvent(self, event: QtCore.QEvent) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def linkClicked(self, url: QtCore.QUrl) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def doUpdate(self) -> None: ...
