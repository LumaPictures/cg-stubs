# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.asset.autoRigsSettings import AutoRigsSettings as AutoRigsSettings
from autorigs.ui.uiAssetContainer import UiAssetDefault as UiAssetDefault
from autorigs.ui.uiGeometryCapture import UiGeometryCaptureDefault as UiGeometryCaptureDefault
from autorigs.ui.uiGeometryContainer import UiGeometryDefault as UiGeometryDefault
from hutil.Qt import QtCore

class UiCharacterSettings(QtCore.QObject):
    dialog: hou.qt.Dialog
    autorigs_asset: AutoRigsAsset
    assetsettings: UiAssetDefault
    geometrysettings: UiGeometryDefault
    geometrycapturesettings: UiGeometryCaptureDefault
    hasnewsettings: bool
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def show(self) -> None: ...
    def updateSettings(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def reset(self) -> None: ...
    def accept(self) -> None: ...
    def getNewSettings(self) -> AutoRigsSettings | None: ...
