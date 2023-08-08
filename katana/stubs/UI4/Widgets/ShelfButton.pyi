# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.ExternalTools as ExternalTools
import UI4.Util.IconManager as IconManager
import UI4.KatanaPrefs as KatanaPrefs
import UI4.App.KeyboardShortcutManager as KeyboardShortcutManager
import UI4.Widgets.MessageBox as MessageBox
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyUtil.Shelves
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import Shelves as Shelves
import UI4 as UI4
import Utils as Utils
import typing
from QT4Widgets.FilterablePopupButton import FilterablePopupButton
from _typeshed import Incomplete
from typing import Callable, ClassVar, Set, Tuple

class DataStoreAction(PyQt5.QtWidgets.QAction):
    triggerWithData: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, text, parent, data) -> None: ...
    def _DataStoreAction__trigger(self): ...

class ItemCreateDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, shelf, parent) -> None: ...
    def _ItemCreateDialog__removeWarning(self): ...
    def _ItemCreateDialog__showWarning(self, txt: str): ...
    def _ItemCreateDialog__validateShortcut(self, shortcut: str): ...
    def getResult(self): ...

class ItemEditDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, item) -> None: ...

class ShelfButton(FilterablePopupButton):
    AllShelvesText: ClassVar[str] = ...
    INVALID_KEYBOARD_SHORTCUT: ClassVar[str] = ...
    NO_KEYBOARD_SHORTCUT: ClassVar[str] = ...
    VALID_KEYBOARD_SHORTCUT: ClassVar[str] = ...
    _ShelfButton__instanceMapper: ClassVar[dict] = ...
    _ShelfButton__shelfItemsShortcutID: ClassVar[dict] = ...
    def __init__(self, parent, prefKey: Incomplete | None = ..., shelfQueryCallback: Callable = ..., additionalEnvironmentCallback: typing.Optional[typing.Callable] = ..., shelfSuffix: str = ..., buttonType: Incomplete | None = ..., shortcutContextClassName: str = ...) -> None: ...
    def _ShelfButton__aboutToShow(self): ...
    def _ShelfButton__addMenuAboutToShow(self): ...
    def _ShelfButton__addShelf(self, shelf, nameType): ...
    def _ShelfButton__addShelfItems(self, shelf, shelfName): ...
    def _ShelfButton__addWarning(self, issue: str, path: str, shelfName: str, itemName: str, shortcut: str): ...
    def _ShelfButton__clearWarnings(self): ...
    def _ShelfButton__deleteItem(self, data): ...
    def _ShelfButton__doChosen(self, name, data, checkScope: bool = ...): ...
    def _ShelfButton__doFilterShelf(self, match, name, data): ...
    def _ShelfButton__formatWarningMessage(self, issue: str) -> tuple: ...
    def _ShelfButton__getCurrentShelf(self): ...
    def _ShelfButton__getKeyeventName(self, shelfName: str, itemUniqueName: str) -> str: ...
    def _ShelfButton__getShortcutForShelfItem(self, shelf: Shelves.Shelf, shelfItem: Shelves.ShelfItem) -> str: ...
    def _ShelfButton__isShortcutAlreadyInUse(self, shortcut): ...
    def _ShelfButton__newItem(self): ...
    def _ShelfButton__newShelf(self): ...
    def _ShelfButton__popupWarningDialog(self, title: str, issue: str): ...
    def _ShelfButton__queryShelves(self, forceReload: bool = ...): ...
    def _ShelfButton__registerKeyboardShortcut(self, shelf: PyUtil.Shelves.Shelf, shelfItem: PyUtil.Shelves.ShelfItem, validated: bool = ...): ...
    def _ShelfButton__reloadShelf(self): ...
    def _ShelfButton__reloadShelfIfDirty(self): ...
    def _ShelfButton__rightClick(self, event): ...
    def _ShelfButton__setInstancesDirty(self): ...
    def _ShelfButton__shelfChanged(self, eventName, eventId, *args): ...
    def _ShelfButton__shelfChosen(self, index: Incomplete | None = ...): ...
    def _ShelfButton__shelfCreated(self, eventName, eventID, shelf, **kwargs): ...
    def _ShelfButton__unregisterKeyboardShortcut(self, shelf: PyUtil.Shelves.Shelf, shelfItem: PyUtil.Shelves.ShelfItem): ...
    def _ShelfButton__updateChangedShortcuts(self, shelf: Shelves.Shelf, item: Shelves.ShelfItem, newShortcut: str): ...
    def _ShelfButton__updateScope(self, item: Shelves.ShelfItem, newScope: list): ...
    def _ShelfButton__updateShelfItems(self): ...
    def _ShelfButton__viewSource(self, data): ...
    def closeEvent(self, event: PyQt5.QtCore.QEvent): ...
    def enterEvent(self, event: PyQt5.QtCore.QEvent): ...
    @staticmethod
    def executeShelfScript(widget: PyQt5.QtWidgets.QWidget, shortcut: str): ...
    def getWarnings(self) -> dict: ...
    def keyboardShortcutPressed(self, shortcut): ...
    def leaveEvent(self, event: PyQt5.QtCore.QEvent): ...
    def logWarnings(self, objectHash: str = ..., title: str = ..., popupDialog: bool = ...): ...
    def setDirty(self, dirty: bool = ...): ...
    def unregisterEventHandlers(self): ...
    def validateKeyboardShortcut(self, shelfName: str, name: str, shortcut: str, path: str = ...) -> str: ...

class ShelfCreateDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self) -> None: ...
    def getResult(self): ...