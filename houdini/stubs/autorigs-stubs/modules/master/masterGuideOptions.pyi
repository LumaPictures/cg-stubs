# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.master.buildMasterGuide import MasterGuide as MasterGuide
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from collections.abc import Sequence
from hutil.Qt import QtGui, QtWidgets
from typing import NoReturn, NotRequired, TypedDict

class _MasterOptionsJson(TypedDict):
    controllabel: bool
    controllabeltype: int
    customcontrollabel: str
    rigscale: NotRequired[float]
    hversion: NotRequired[Sequence[str]]

class ModuleOptionsWidget(QtWidgets.QWidget):
    autorigs_asset: AutoRigsAsset
    geoSkinName: str
    optionsWidgets: list[QtWidgets.QWidget]
    buildguides: MasterGuide
    modulenode: hou.ObjNode | None
    iconPath: str
    defaultIcon: QtGui.QIcon
    upperlayout: QtWidgets.QVBoxLayout
    assetlabelLayout: QtWidgets.QHBoxLayout
    useAssetNameLabel: QtWidgets.QCheckBox
    useAssetNameButton: hou.qt.ComboBox
    customLabelLayout: QtWidgets.QHBoxLayout
    customLabelLabel: QtWidgets.QLabel
    customLabelLineEdit: QtWidgets.QLineEdit
    standInGeoNode: str
    geoGuideNode: hou.ObjNode | None
    rigscale: UiParamFloat
    assetGlobalScaleLayout: QtWidgets.QHBoxLayout
    geoSkin: hou.ObjNode | None
    customLabelSwitch: hou.SopNode | None
    geoGuideFont: hou.SopNode | None
    customLabelSwitchIndex: hou.Parm | None
    fontTextField: hou.Parm | None
    customLabel: str
    hversion: str
    def __init__(self, autorigs_asset: AutoRigsAsset, buildguides: MasterGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getMainLayout(self) -> QtWidgets.QVBoxLayout: ...
    def getRigscale(self) -> float: ...
    def getHversion(self) -> str: ...
    def getSaveDate(self) -> NoReturn: ...
    def getSaveTime(self) -> NoReturn: ...
    def setOptions(self) -> None: ...
    def getIsAssetNameLabelChecked(self) -> bool: ...
    def toJSON(self) -> _MasterOptionsJson: ...
    def fromJSON(self, json: _MasterOptionsJson) -> bool: ...
    def addControlLabel(self, state: int) -> None: ...
    def labelType(self) -> None: ...
    def onTextFieldFinishedEditing(self) -> None: ...
