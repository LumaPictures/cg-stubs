import hou
from PySide6 import QtCore

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.asset.autoRigsSettings import AutoRigsSettings
from autorigs.ui.uiAssetContainer import UiAssetDefault
from autorigs.ui.uiGeometryCapture import UiGeometryCaptureDefault
from autorigs.ui.uiGeometryContainer import UiGeometryDefault

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
