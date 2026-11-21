import hou
import PySide6.QtWidgets
from PySide6 import QtCore, QtGui, QtWidgets

from autorigs.asset.autoRigsAsset import AutoRigsAsset, _AssetJson, _CreateValues
from autorigs.ui.uiCharacterTabs import UiCharacterTabs
from autorigs.ui.uiCreateTabs import UiCreateTabs
from autorigs.ui.uiNewAutorigDialog import UiNewAutorigDialog

class UiMenuBar(QtCore.QObject):
    NO_RECENT: str
    MAX_RECENTS: int
    JSON_ASSET_SECTION: str
    BIPED_PRESET_ACTION: str
    QUADRUPED_PRESET_ACTION: str
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

    def __init__(self, parent: QtWidgets.QWidget, charactertabs: UiCharacterTabs, createtabs: UiCreateTabs) -> None: ...
    def menuBar(self) -> hou.qt.MenuBar: ...
    def createMessageDialog(self, windowtext: str, text: str) -> QtWidgets.QMessageBox: ...
    def removeActionWithSamePath(self, path: str) -> None: ...
    def addToRecentMenu(self, nodepath: str) -> None: ...
    def newAutorigFromCustom(self, jsonobj: _AssetJson, create_values: _CreateValues) -> None: ...
    def newAutorig(self) -> None: ...
    def newAutorigFromSettings(self, create_values: _CreateValues) -> AutoRigsAsset: ...
    def getAssetNodeValidJsonObj(self, nodepath: str, builtmatter: bool) -> tuple[hou.Node, _AssetJson] | tuple[None, None]: ...
    def loadFromNodePath(self, path: str) -> None: ...
