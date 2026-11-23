import hou
from husdui.models import PathListModel as PathListModel
from husdui.prefs import SimplePrefs as SimplePrefs
from husdui.views import PathListView as PathListView
from hutil.PySide import QtGui, QtWidgets

theSharedEditorWindow: EditSelectionRuleWindow | None
MARGIN: int
ICONSIZE: int

class EditSelectionRuleWindow(QtWidgets.QDialog):
    selectionrule: hou.LopSelectionRule | None
    originalrulename: str | None
    rulename: QtWidgets.QLineEdit
    duplicate: QtWidgets.QPushButton
    nodepath: QtWidgets.QLineEdit
    choosenode: QtWidgets.QToolButton
    icon: QtWidgets.QLineEdit
    chooseicon: QtWidgets.QToolButton
    allowinstanceproxies: QtWidgets.QCheckBox
    allowpointinstances: QtWidgets.QCheckBox
    pattern: QtWidgets.QTextEdit
    patternmenu: QtWidgets.QMenu
    patternmenubutton: hou.qt.MenuButton
    statusicon: QtWidgets.QToolButton
    summarylabel: QtWidgets.QLabel
    autorefresh: QtWidgets.QCheckBox
    refresh: QtWidgets.QToolButton
    results: PathListModel
    resultsview: PathListView
    PrefAutoRefresh: str
    def __init__(self) -> None: ...
    def apply(self) -> bool: ...
    def accept(self) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def display(self, node: hou.LopNode | None, selectionrulename: str) -> None: ...

def closeSelectionRuleEditor() -> None: ...
def createSelectionRuleEditor(node: hou.LopNode | None, selectionrule: str) -> EditSelectionRuleWindow: ...
