# Houdini stubs generated from Houdini 22.0.466

from . import uiParamFile as uiParamFile, uiParamFloat as uiParamFloat, uiParamName as uiParamName
from .uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.asset.autoRigsSettings import AutoRigsSettings as AutoRigsSettings
from autorigs.ui.uiParamName import UiParamName as UiParamName
from hutil.Qt import QtWidgets

class UiGeometryCaptureFactory:
    def __init__(self) -> None: ...
    @classmethod
    def createCaptureWidget(cls) -> UiGeometryCaptureDefault: ...

class UiGeometryCaptureDefault(QtWidgets.QGroupBox):
    geoname: UiParamName
    capturenetwork: QtWidgets.QCheckBox
    displaydeform: QtWidgets.QCheckBox
    toggle: ToggleButtonsWidget
    GEOMETRY_CAPTURE_LABELS: list[str]
    GEOMETRY_CAPTURE_DEFAULT: int
    def __init__(self) -> None: ...
    def getCreateNetwork(self) -> bool: ...
    def getCaptureType(self) -> int: ...
    def getDisplayDeform(self) -> bool: ...
    def saveSettings(self, settingsdst: AutoRigsSettings) -> None: ...
    def updateSettings(self, autorigs_asset: AutoRigsAsset) -> None: ...
