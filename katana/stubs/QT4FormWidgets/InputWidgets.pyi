# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.FWidget as FWidget
import QT4FormWidgets.PaintingUtils as PaintingUtils
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets.FWidget
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import ResourceFiles as ResourceFiles
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class HelpButton(PyQt5.QtWidgets.QPushButton):
    _HelpButton__pixmaps: ClassVar[dict] = ...
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, helpName: str = ..., helpText: str = ...) -> None: ...
    def _displayHelpDialog(self): ...
    def contextMenuEvent(self, event): ...
    def getHelpText(self): ...
    def mousePressEvent(self, event): ...
    def setHelpText(self, helpText): ...

class HelpDialog(PyQt5.QtWidgets.QFrame):
    class DragLabel(PyQt5.QtWidgets.QLabel):
        def __init__(self, label, parent) -> None: ...
        def mouseMoveEvent(self, ev): ...
        def mousePressEvent(self, ev): ...
        def mouseReleaseEvent(self, ev): ...
    _HelpDialog__instances: ClassVar[set] = ...
    _HelpDialog__pixmaps: ClassVar[dict] = ...
    def __init__(self, helpText, parent: Incomplete | None = ..., caption: str = ...) -> None: ...
    def _HelpDialog__buildChildren(self, helpText): ...
    def _HelpDialog__linkClicked_callback(self, url: str): ...
    def closeEvent(self, event): ...
    def positionAtGlobalPoint(self, point, screenID: Incomplete | None = ...): ...
    def showEvent(self, event): ...
    def tearOff(self): ...

class HelpFWidget(QT4FormWidgets.FWidget.FPixmap):
    _HelpFWidget__pixmaps: ClassVar[dict] = ...
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent) -> None: ...
    def _HelpFWidget__loadResources(self): ...
    def _displayHelpDialog(self): ...
    def contextMenuEvent(self, event): ...
    def getHelpName(self): ...
    def getHelpText(self): ...
    def getHelpType(self): ...
    def isHelpEnabled(self): ...
    def mousePressEvent(self, event): ...
    def updateAppearance(self): ...

class InputComboBox(PyQt5.QtWidgets.QComboBox):
    EMITS_CUSTOM_FOCUS_EVENTS: ClassVar[bool] = ...
    gotFocus: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    itemChosen: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    lostFocus: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args) -> None: ...
    def _InputComboBox__activated(self, index: Incomplete | None = ...): ...
    def _InputComboBox__lineEditGotFocus(self): ...
    def _InputComboBox__lineEditLostFocus(self): ...
    def keyPressEvent(self, event): ...
    def mousePressEvent(self, event): ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
    def setMinimal(self, minimal: bool): ...
    def setReadOnly(self, state): ...
    def setText(self, text): ...
    def showPopup(self): ...
    def text(self, index: int = ...): ...
    def wheelEvent(self, event): ...

class InputLineEdit(PyQt5.QtWidgets.QLineEdit):
    EMITS_CUSTOM_FOCUS_EVENTS: ClassVar[bool] = ...
    _InputLineEdit__selectAllOnFocus: ClassVar[bool] = ...
    _InputLineEdit__singleDigitScrollingEnabled: ClassVar[bool] = ...
    decrement: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    dragEnterEventSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    dragStarted: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    dropEventSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    gotFocus: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    increment: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    lostFocus: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    scrollDigitDown: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    scrollDigitUp: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args) -> None: ...
    @classmethod
    def _InputLineEdit__findFirstLeadingZeroScrollBlockIndex(cls, text: str, index: int) -> int: ...
    @classmethod
    def _InputLineEdit__findLeadingZeroBlock(cls, text: str, index: int) -> int: ...
    @classmethod
    def _InputLineEdit__findScrollBlockHexIndex(cls, text: str, index: int) -> int: ...
    @classmethod
    def _InputLineEdit__findScrollStartIndex(cls, text: str, index: int) -> int: ...
    @classmethod
    def _InputLineEdit__flipScrollDigitSign(cls, text: str, firstZeroIndex: int, index: int, isHex: bool) -> tuple[str, int]: ...
    @classmethod
    def _InputLineEdit__isScrollBlockHex(cls, text: str, index: int) -> bool: ...
    @classmethod
    def _InputLineEdit__isScrollBlockNegative(cls, text: str, index: int) -> bool: ...
    @classmethod
    def _InputLineEdit__prepareScrollTextAndIndex(cls, text: str, index: int, isInt: bool) -> tuple[str, int]: ...
    @classmethod
    def _InputLineEdit__removeLeadingZeroesFromBlock(cls, text: str, index: int) -> tuple[str, int]: ...
    def _InputLineEdit__scrollCursorPosFromSelection(self) -> int: ...
    def _InputLineEdit__scrollDigitCommon(self, text, cursorPos, scrollFunction, invScrollFunction) -> tuple[str, int]: ...
    @classmethod
    def _InputLineEdit__scrollDigitDown(cls, text: str, index: int, isInt: bool) -> tuple[str, int]: ...
    def _InputLineEdit__scrollDigitDownCB(self): ...
    @classmethod
    def _InputLineEdit__scrollDigitUp(cls, text: str, index: int, isInt: bool) -> tuple[str, int]: ...
    def _InputLineEdit__scrollDigitUpCB(self): ...
    def _InputLineEdit__startDrag(self): ...
    def contextMenuEvent(self, event): ...
    def customEvent(self, event): ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def focusInEvent(self, event): ...
    def focusOutEvent(self, event): ...
    def hideEvent(self, event): ...
    def keyPressEvent(self, event): ...
    def mouseMoveEvent(self, event): ...
    def mousePressEvent(self, event): ...
    def mouseReleaseEvent(self, event): ...
    def setFloatScrollingEnabled(self, value: bool): ...
    def setReadOnly(self, state): ...
    @classmethod
    def setSelectAllOnFocus(cls, selectAllOnFocus): ...
    @classmethod
    def setSingleDigitScrolling(cls, value: bool): ...
    def setText(self, text): ...
    def sizeHint(self): ...
    def wheelEvent(self, event): ...

class InputTextEdit(PyQt5.QtWidgets.QTextEdit):
    EMITS_CUSTOM_FOCUS_EVENTS: ClassVar[bool] = ...
    contextMenuEventSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    enterPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    gotFocus: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    lostFocus: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args) -> None: ...
    def contextMenuEvent(self, event): ...
    def focusInEvent(self, event): ...
    def focusOutEvent(self, event): ...
    def hideEvent(self, event): ...
    def keyPressEvent(self, event): ...
    def setReadOnly(self, state): ...
    def sizeHint(self): ...
    def text(self): ...
