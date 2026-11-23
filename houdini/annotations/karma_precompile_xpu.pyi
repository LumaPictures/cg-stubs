from PySide6 import QtCore, QtWidgets

RED: str
GREEN: str
YELLOW: str
RESET: str

def run_terminal() -> None: ...
def run_interactive() -> None: ...

class _Precompiler(QtWidgets.QDialog):
    task: QtCore.QProcess | None
    log_widget: QtWidgets.QPlainTextEdit
    close_button: QtWidgets.QPushButton
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def terminate_child(self) -> None: ...
