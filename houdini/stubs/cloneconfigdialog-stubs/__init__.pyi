import PySide6.QtWidgets
from hutil.Qt import QtWidgets
from typing import TypedDict

class _CloneOptions(TypedDict, total=False):
    renderer: str
    thread_count: int
    connection_timeout: int
    width: float

class CloneConfigDialog(QtWidgets.QDialog):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None, options: _CloneOptions | None = None) -> None: ...
