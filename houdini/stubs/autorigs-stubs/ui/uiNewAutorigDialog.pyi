# Houdini stubs generated from Houdini 22.0.466

import hou
from . import uiAssetContainer as uiAssetContainer, uiCreateTabs as uiCreateTabs, uiGeometryContainer as uiGeometryContainer
from autorigs.asset import moduleInfos as moduleInfos
from autorigs.asset.autoRigsAsset import _CreateValues
from autorigs.asset.autoRigsSettings import AutoRigsSettings as AutoRigsSettings
from autorigs.ui.uiAssetContainer import AssetNameContainer as AssetNameContainer, AssetTypeContainer as AssetTypeContainer
from autorigs.ui.uiGeometryContainer import UiGeometrySimple as UiGeometrySimple
from hutil.Qt import QtCore, QtWidgets

class UiNewAutorigDialog(QtCore.QObject):
    has_autorig_type: bool
    toggle_buttons_group: QtWidgets.QButtonGroup
    dialog_values: _CreateValues | None
    dialog: hou.qt.Dialog
    assettypewidget: AssetTypeContainer
    assetnamewidget: AssetNameContainer
    geometrysource: UiGeometrySimple
    autorigtype: QtWidgets.QWidget
    cancelbutton: QtWidgets.QPushButton
    createbutton: QtWidgets.QPushButton
    PRESET_BLANK: int
    PRESET_BIPED: int
    PRESET_QUADRUPED: int
    def __init__(self, has_autorig_type: bool = True) -> None: ...
    def exec_(self) -> int: ...
    def createAutorigTypeWidget(self) -> QtWidgets.QWidget: ...
    def typeExists(self, assettype: str) -> bool: ...
    def nameExists(self, assetname: str) -> bool: ...
    def accept(self) -> None: ...
    def reject(self) -> None: ...
    def setValues(self, assetname: str, assettype: str) -> None: ...
    def getValues(self) -> _CreateValues | None: ...
    def reset(self) -> None: ...
