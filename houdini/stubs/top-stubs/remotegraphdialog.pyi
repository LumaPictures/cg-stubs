# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable
from hutil.Qt import QtCore, QtGui, QtWidgets

class WaitThread(QtCore.QThread):
    address: str | None
    failed: QtCore.Signal
    succeeded: QtCore.Signal
    def __init__(self, get_address_fn: Callable[[], str | None], poll_period: float, parent: QtCore.QObject | None = None) -> None: ...
    def run(self) -> None: ...
    def stop(self, result: int) -> None: ...

class RemoteGraphDialog(QtWidgets.QDialog):
    address: str | None
    node: hou.Node | None
    node_name: str
    node_id: int
    spinner_movie: QtGui.QMovie
    def __init__(self, get_address_fn: Callable[[], str | None], poll_period: float = 1.0, parent: QtWidgets.QWidget | None = None, node_name: str = '') -> None: ...
    def gotAddress(self, address: str) -> None: ...
    def failed(self) -> None: ...
