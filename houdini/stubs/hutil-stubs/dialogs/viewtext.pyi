# Houdini stubs generated from Houdini 22.0.466

from hutil.PySide import QtGui as QtGui, QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.TextSearch import TextSearch as TextSearch
from hutil.qt.TextView import TextView as TextView
from typing import Callable as Callable

MARGIN: int
PREF_WORD_WRAP: str

class ViewTextDialog(QtWidgets.QDialog):
    textview: TextView
    textsearch: TextSearch
    wordwrap: QtWidgets.QPushButton
    def __init__(self, gettext_fn: Callable[[], str], title: str) -> None: ...
    def setHighlighter(self, hilite: QtGui.QSyntaxHighlighter) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def showEvent(self, event: QtGui.QShowEvent) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def saveText(self) -> None: ...
