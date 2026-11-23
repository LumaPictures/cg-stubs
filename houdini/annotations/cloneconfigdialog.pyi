from typing import TypedDict

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

# The options a clone launcher plugin opens the dialog with (its kwargs, with defaults filled in).
class _CloneOptions(TypedDict, total=False):
    renderer: str
    thread_count: int
    connection_timeout: int
    width: float

class CloneConfigDialog(PySide6.QtWidgets.QDialog):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ..., options: _CloneOptions | None = ...) -> None: ...
