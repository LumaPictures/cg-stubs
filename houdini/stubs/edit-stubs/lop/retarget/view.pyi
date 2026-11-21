import modelview
from PySide6 import QtGui as QtGui
from hutil.Qt import QtCore, QtWidgets

class EditTreeView(modelview.TreeView):
    deletePressed: QtCore.Signal
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
