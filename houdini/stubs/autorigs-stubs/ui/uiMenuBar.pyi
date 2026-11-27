import PySide6.QtWidgets
import hou
from . import uiNewAutorigDialog as uiNewAutorigDialog
from PySide6 import QtGui as QtGui
from autorigs.asset import autoRigsAsset as autoRigsAsset, moduleInfos as moduleInfos
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset, _AssetJson, _CreateValues
from autorigs.ui.uiCharacterTabs import UiCharacterTabs as UiCharacterTabs
from autorigs.ui.uiCreateTabs import UiCreateTabs as UiCreateTabs
from autorigs.ui.uiNewAutorigDialog import UiNewAutorigDialog as UiNewAutorigDialog
from hutil.PySide import QtCore, QtWidgets

class UiMenuBar(QtCore.QObject):
    menu_bar: hou.qt.MenuBar
    charactertabs: UiCharacterTabs
    createtabs: UiCreateTabs
    loadexistingasset: QtGui.QAction
    loadrecentmenu: PySide6.QtWidgets.QMenu
    load_no_recent: QtGui.QAction
    doesnotexist_title: str
    doesnotexist_message: str
    notacharacter_title: str
    notacharacter_message: str
    builtcharacter_title: str
    builtcharacter_message: str
    invalidjson_title: str
    invalidjson_message: str
    noactiveautorig_title: str
    noactiveautorig_message: str
    saveresult_title: str
    saveresult_message: str
    new_nopreset_dialog: UiNewAutorigDialog
    newautorig_dialog: UiNewAutorigDialog
    NO_RECENT: str
    MAX_RECENTS: int
    JSON_ASSET_SECTION: str
    BIPED_PRESET_ACTION: str
    QUADRUPED_PRESET_ACTION: str
    def __init__(self, parent: QtWidgets.QWidget, charactertabs: UiCharacterTabs, createtabs: UiCreateTabs) -> None: ...
    def menuBar(self) -> hou.qt.MenuBar:
        """Accessor for the menu bar widget."""
    def createMessageDialog(self, windowtext: str, text: str) -> QtWidgets.QMessageBox: ...
    def removeActionWithSamePath(self, path: str) -> None: ...
    def addToRecentMenu(self, nodepath: str) -> None: ...
    def newAutorigFromCustom(self, jsonobj: _AssetJson, create_values: _CreateValues) -> None: ...
    def newAutorig(self) -> None: ...
    def newAutorigFromSettings(self, create_values: _CreateValues) -> AutoRigsAsset: ...
    def getAssetNodeValidJsonObj(self, nodepath: str, builtmatter: bool) -> tuple[hou.OpNode, _AssetJson] | tuple[None, None]: ...
    def loadFromNodePath(self, path: str) -> None: ...
