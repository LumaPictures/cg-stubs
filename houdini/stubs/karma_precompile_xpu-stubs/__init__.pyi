from hutil.Qt import QtCore, QtWidgets

RED: str
GREEN: str
YELLOW: str
RESET: str

def run_terminal() -> None:
    """ Do the precompiling of the shader permutations """

class _Precompiler(QtWidgets.QDialog):
    task: QtCore.QProcess | None
    log_widget: QtWidgets.QPlainTextEdit
    close_button: QtWidgets.QPushButton
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def terminate_child(self) -> None:
        """ Terminate the child process """

def run_interactive() -> None:
    """ Run in a Qt Window """
