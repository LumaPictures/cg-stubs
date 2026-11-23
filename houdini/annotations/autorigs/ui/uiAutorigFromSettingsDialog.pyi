from typing import TypedDict

import hou
from PySide6 import QtCore, QtWidgets

from autorigs.ui.uiAssetContainer import AssetNameContainer, AssetTypeContainer, UiAssetPathOptions
from autorigs.ui.uiGeometryCapture import UiGeometryCaptureDefault
from autorigs.ui.uiParamFile import UiParamFileIcon
from autorigs.asset.autoRigsAsset import _AssetJson

class _DialogValues(TypedDict):
    assetname: str
    assettype: str
    customcontrollabel: str
    controllabel: bool
    controllabeltype: int
    capturenetwork: bool
    capturetype: int
    displaydeform: bool
    asseticonpath: str
    assetcurrentindex: int
    assetcurrentdata: str | None

class UiAutorigFromSettingsDialog(QtCore.QObject):
    jsonobj: _AssetJson
    dialog: hou.qt.Dialog
    assettypewidget: AssetTypeContainer
    assetnamewidget: AssetNameContainer
    useAssetNameLabel: QtWidgets.QCheckBox
    useAssetNameButton: hou.qt.ComboBox
    customLabelLayout: QtWidgets.QHBoxLayout
    customLabelLineEdit: QtWidgets.QLineEdit
    assetpath: UiAssetPathOptions
    customiconpath: UiParamFileIcon
    geometrycapturesettings: UiGeometryCaptureDefault
    cancelbutton: QtWidgets.QPushButton
    createbutton: QtWidgets.QPushButton
    dialog_values: _DialogValues | None

    def __init__(self, jsonobj: _AssetJson) -> None: ...
    def exec_(self) -> int: ...
    def accept(self) -> None: ...
    def reject(self) -> None: ...
    def setValues(
        self,
        assetname: str,
        assettype: str,
        controllabel: bool,
        controllabeltype: int,
        customcontrollabel: str,
        capturenetwork: bool,
        capturetype: int,
        displaydeform: bool,
        asseticonpath: str,
        assetcurrentindex: int,
        assetcurrentdata: str | None,
    ) -> None: ...
    def getValues(self) -> _DialogValues | None: ...
    def addControlLabel(self, state: int) -> None: ...
    def labelType(self) -> None: ...
    def reset(self) -> None: ...
