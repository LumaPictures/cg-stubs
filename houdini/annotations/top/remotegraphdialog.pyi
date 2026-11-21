from collections.abc import Callable

import hou
from PySide6 import QtCore, QtGui, QtWidgets

class WaitThread(QtCore.QThread):
    failed: QtCore.Signal
    succeeded: QtCore.Signal
    address: str | None
    def __init__(self, get_address_fn: Callable[[], str | None], poll_period: float, parent: QtCore.QObject | None = ...) -> None: ...
    def run(self) -> None: ...
    def stop(self, result: int) -> None: ...

class RemoteGraphDialog(QtWidgets.QDialog):
    address: str | None
    node: hou.Node | None
    node_name: str
    node_id: int
    spinner_movie: QtGui.QMovie
    def __init__(self, get_address_fn: Callable[[], str | None], poll_period: float = ..., parent: QtWidgets.QWidget | None = ..., node_name: str = ...) -> None: ...
    def gotAddress(self, address: str) -> None: ...
    def failed(self) -> None: ...
