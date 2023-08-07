# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.ExternalTools as ExternalTools
import UI4.App.Icon as Icon
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.App.Splash as Splash
import UI4.App.Splash
from typing import Set, Tuple

class AboutKatanaDialog(PyQt5.QtWidgets.QDialog, UI4.App.Splash.SplashScreenMixin):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget) -> None: ...
    def _AboutKatanaDialog__on_aboutQtButton_clicked(self): ...
    def _AboutKatanaDialog__on_copyrightButton_clicked(self): ...
    def _AboutKatanaDialog__on_creditsButton_clicked(self): ...
    def mousePressEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
    def sizeHint(self) -> PyQt5.QtCore.QSize: ...

class TextDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, text: str, parent: PyQt5.QtWidgets.QWidget) -> None: ...
    def _TextDialog__on_richTextLabel_linkActivated(self, link: str): ...
    def showEvent(self, event: PyQt5.QtGui.QShowEvent): ...

def AboutKatana(window): ...
