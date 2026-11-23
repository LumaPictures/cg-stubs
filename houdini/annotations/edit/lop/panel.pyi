from PySide6 import QtGui, QtWidgets

ICON_SIZE: int
DEBUG: bool
MARGIN: int
BUTTON_SIZE: int
ICON_MARGIN: int
TEXT_MARGIN: int
REMOVE_ICON: QtGui.QIcon
VISIBLE_ICON: QtGui.QIcon
RETARGET_ICON: QtGui.QIcon
FLATLIST_ICON: QtGui.QIcon
CONDENSEDTREE_ICON: QtGui.QIcon
FULLTREE_ICON: QtGui.QIcon
X_ICON: QtGui.QIcon
T_ICON: QtGui.QIcon
R_ICON: QtGui.QIcon
S_ICON: QtGui.QIcon
G_ICON: QtGui.QIcon

class LopEditPanel(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def updateFromNode(self) -> None: ...

class LopEditWidget(QtWidgets.QWidget):
    PrefDisplayMode: str
    PrefDisplayXforms: str
    PrefShowAllPrims: str
    PrefXformSpace: str
    PrefXformColsWidth: str
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def retarget(self) -> None: ...
    def buildToolbar(self) -> QtWidgets.QHBoxLayout: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def updateFromNode(self) -> None: ...
