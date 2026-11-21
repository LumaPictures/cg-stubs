# Houdini stubs generated from Houdini 22.0.466

import hou
from husdui.models import PathListModel as PathListModel
from husdui.prefs import SimplePrefs as SimplePrefs
from husdui.views import PathListView as PathListView
from hutil.PySide import QtGui, QtWidgets
from pxr import Usd

theSharedEditorWindow: EditPrimPatternWindow | None
MARGIN: int
ICONSIZE: int

class EditPrimPatternWindow(QtWidgets.QDialog):
    selectionrule: hou.LopSelectionRule | None
    originalrulename: None
    nodelabel: QtWidgets.QLabel
    parameterlabel: QtWidgets.QLabel
    allowinstanceproxieslabel: QtWidgets.QLabel
    ispathexpression: QtWidgets.QCheckBox
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
    applybutton: QtWidgets.QPushButton
    node: hou.OpNode | None
    parm: hou.Parm | None
    ispathexpressionparm: hou.Parm | None
    allowpointinstancesparm: hou.Parm | None
    stage: Usd.Stage | None
    lop: hou.LopNode | None
    PrefAutoRefresh: str
    def __init__(self) -> None: ...
    def cancel(self) -> None: ...
    def apply(self) -> None: ...
    def accept(self) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def display(self, node: hou.OpNode, parm: hou.Parm, stageorlop: Usd.Stage | hou.Node | None, allowinstanceproxies: bool, ispathexpressionparm: hou.Parm | None, allowpointinstancesparm: hou.Parm | None) -> None: ...
    def displayModal(self, stageorlop: Usd.Stage | hou.Node | None, initialpattern: str, allowinstanceproxies: bool, ispathexpressionparm: hou.Parm | None, allowpointinstancesparm: hou.Parm | None) -> str | None: ...

def closePrimPatternEditor() -> None: ...
def createPrimPatternEditor(node: hou.OpNode, parm: hou.Parm, stageorlop: Usd.Stage | hou.Node | None, allowinstanceproxies: bool, ispathexpressionparm: hou.Parm | None = None, allowpointinstancesparm: hou.Parm | None = None) -> EditPrimPatternWindow: ...
def getPrimPattern(stageorlop: Usd.Stage | hou.Node | None, initialpattern: str, allowinstanceproxies: bool, ispathexpressionparm: hou.Parm | None = None, allowpointinstancesparm: hou.Parm | None = None) -> str | None: ...
