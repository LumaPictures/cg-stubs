# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import QtCore
import QtWidgets
import ResourceFiles as ResourceFiles
import Utils as Utils
import QT4Widgets.WidgetUtils as WidgetUtils
from QT4Widgets.SortableTreeWidget import SortableTreeWidget as SortableTreeWidget, SortableTreeWidgetItem as SortableTreeWidgetItem
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from _typeshed import Incomplete
from typing import ClassVar
from typing import Tuple

MAX_SCREEN_HEIGHT_PERCENT_DEFAULT: float
MAX_SCREEN_WIDTH_PERCENT_DEFAULT: float

class FilterableCombo(PyQt5.QtWidgets.QWidget):
    class FocusSignalingLineEdit(PyQt5.QtWidgets.QLineEdit):
        focusIn: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        def focusInEvent(self, event): ...
    refreshItems: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    textChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, label, parent): ...
    def _FilterableCombo__fieldChanged(self): ...
    def _FilterableCombo__fieldFocusIn(self): ...
    def _FilterableCombo__popupAboutToShow(self): ...
    def _FilterableCombo__popupItemChosen(self, item, meta: Incomplete | None = ...): ...
    def event(self, event): ...
    def setItems(self, itemList): ...
    def setText(self, text, strict: bool = ...): ...
    def text(self): ...

class FilterablePopup(PyQt5.QtWidgets.QFrame):
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    arrowKeyPress: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    deleteKeyPress: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    hideSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    itemChosen: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    released: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    returnKeyPress: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    shiftKeyPress: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    showSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ...): ...
    def _FilterablePopup__buildWidgets(self): ...
    def _FilterablePopup__calculateGeometry(self) -> QtCore.QRect: ...
    def _FilterablePopup__chooseCurrent(self): ...
    def _FilterablePopup__clearFilterField(self): ...
    def _FilterablePopup__findScreen(self, desktop: PQDesktopWidget, globalPos: QPoint) -> int: ...
    def _FilterablePopup__findTabOrScrollAreaRect(self) -> QRect | None: ...
    def _FilterablePopup__findXYToFitInRect(self, currentPopupRect: QRect, enclosingRect: QRect) -> Tuple[int, int]: ...
    def _FilterablePopup__firstSelectedItem(self): ...
    def _FilterablePopup__itemChosen(self, item): ...
    def _FilterablePopup__mouseMoved(self, event): ...
    def _FilterablePopup__on_filterCombobox_activated(self, index): ...
    def _FilterablePopup__popupArrowKeyPress(self, key): ...
    def _FilterablePopup__popupReturnKeyPress(self, key): ...
    def _FilterablePopup__released(self): ...
    def _FilterablePopup__updateFilter(self, text: Incomplete | None = ...): ...
    def _buildTreeWidget(self): ...
    def addFilterByOption(self, name, callbackFnc): ...
    def addItem(self, text, pixmap: Incomplete | None = ..., meta: Incomplete | None = ..., item: Incomplete | None = ..., parentToItem: Incomplete | None = ...): ...
    def addOption(self, displayText, optionValues, defaultValue, callbackFnc, callbackWithIndex: bool = ...): ...
    def addSwitch(self, displayText, defaultValue, callbackFnc) -> QtWidgets.QCheckBox: ...
    def applyDefaultSize(self): ...
    def bottomToolbar(self): ...
    def chooseCustom(self, value, meta: Incomplete | None = ...): ...
    def clear(self): ...
    def clearFilterField(self): ...
    def displayActivityIndicator(self, display): ...
    def event(self, event): ...
    def focusFilterField(self): ...
    def getDesiredHeight(self): ...
    def getDesiredWidth(self): ...
    def getMaxScreenHeightPercentage(self) -> float: ...
    def getMaxScreenWidthPercentage(self) -> float: ...
    def getOption(self, name): ...
    def getWidgetSwitchArea(self): ...
    def hideEvent(self, e): ...
    def popup(self, globalPos): ...
    def selectItem(self, text): ...
    def setDesiredHeight(self, height): ...
    def setDesiredWidth(self, width): ...
    def setIconSize(self, size): ...
    def setMaxScreenHeightPercentage(self, maxScreenHeightPercentage: float): ...
    def setMaxScreenWidthPercentage(self, maxScreenWidthPercentage: float): ...
    def setSorting(self, state): ...
    def showEvent(self, e): ...
    def switchBox(self): ...
    def treeWidget(self): ...
    def updateActivityIndicator(self): ...
    def updateFilter(self): ...

class FilterablePopupButton(PyQt5.QtWidgets.QPushButton):
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    itemChosen: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    popupClosed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ..., buttonType: Incomplete | None = ...): ...
    def _FilterablePopupButton__popClicked(self): ...
    def _FilterablePopupButton__popupHidden(self): ...
    def _FilterablePopupButton__popupShow(self): ...
    def _buildPopupWindow(self): ...
    def forceUIUpdate(self): ...
    def getPopupWindow(self): ...
    def setButtonType(self, buttonType): ...
    def __del__(self): ...
    def __getattr__(self, name): ...

class _DeleteEatingLineEdit(PyQt5.QtWidgets.QLineEdit):
    deleteKeyPress: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def keyPressEvent(self, event): ...

class _TrackingTreeWidget(SortableTreeWidget):
    released: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    rightClick: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args): ...
    def event(self, event): ...
    def leaveEvent(self, e): ...
    def mouseMoveEvent(self, e): ...
    def mousePressEvent(self, e): ...
    def mouseReleaseEvent(self, e): ...
    def showEvent(self, event): ...