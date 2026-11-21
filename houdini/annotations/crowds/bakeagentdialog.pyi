import hou
from PySide6 import QtCore, QtWidgets

class BakeAgentDialog(QtCore.QObject):
    SOURCE_SCENE: int
    SOURCE_FBX: int
    SOURCE_USD: int
    SOURCE_LOP: int
    thePathFieldSize: int
    theNameFieldSize: int
    enable_agentname: bool
    sourceobjectfield: QtWidgets.QLineEdit
    sourcebuttongroup: QtWidgets.QButtonGroup
    sourcestack: QtWidgets.QStackedWidget
    sourcelopfield: QtWidgets.QLineEdit
    fbxfilepathfield: QtWidgets.QLineEdit
    usdfilepathfield: QtWidgets.QLineEdit
    dialog: hou.qt.Dialog
    agentnamefield: QtWidgets.QLineEdit
    clipnamefield: QtWidgets.QLineEdit
    fbxclipnamefield: QtWidgets.QLineEdit
    clipnamestack: QtWidgets.QStackedWidget
    dialogbuttons: QtWidgets.QDialogButtonBox
    def __init__(self, title: str, enable_agentname: bool = ..., selected_object: hou.Node | None = ...) -> None: ...
    def exec(self) -> int: ...
    def sourceType(self) -> int: ...
    def agentName(self) -> str: ...
    def clipName(self) -> str: ...
    def subnet(self) -> hou.Node | None: ...
    def lopNode(self) -> hou.Node | None: ...
    def filePath(self) -> str: ...
