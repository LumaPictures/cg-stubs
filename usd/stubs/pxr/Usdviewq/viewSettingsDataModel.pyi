# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import pxr.Sdf as Sdf
import pxr.UsdGeom as UsdGeom
import pxr.Usdviewq.settings
import pxr.Usdviewq.settings as settings
from _typeshed import Incomplete
from pxr.UsdAppUtils.complexityArgs import RefinementComplexities as RefinementComplexities
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.common import CameraMaskModes as CameraMaskModes, ClearColors as ClearColors, ColorCorrectionModes as ColorCorrectionModes, HighlightColors as HighlightColors, PickModes as PickModes, PrintWarning as PrintWarning, RenderModes as RenderModes, SelectionHighlightModes as SelectionHighlightModes
from pxr.Usdviewq.freeCamera import FreeCamera as FreeCamera
from pxr.Usdviewq.settings import StateSource as StateSource
from typing import ClassVar

DEFAULT_AMBIENT: float
DEFAULT_SPECULAR: float
_CLEAR_COLORS_DICT: dict
_HIGHLIGHT_COLORS_DICT: dict

class OCIOSettings:
    def __init__(self, display: str = ..., view: str = ..., colorSpace: str = ...) -> None: ...
    @property
    def colorSpace(self): ...
    @property
    def display(self): ...
    @property
    def view(self): ...

class ViewSettingsDataModel(pxr.Usdviewq.settings.StateSource, PySide6.QtCore.QObject):
    signalAutoComputeClippingPlanesChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalDefaultMaterialChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalFreeCameraSettingChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalSettingChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalStyleSettingsChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalVisibleSettingChanged: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    ambientLightOnly: Incomplete
    autoComputeClippingPlanes: Incomplete
    cameraMaskColor: Incomplete
    cameraMaskMode: Incomplete
    cameraPath: Incomplete
    cameraPrim: Incomplete
    cameraReticlesColor: Incomplete
    clearColorText: Incomplete
    colorCorrectionMode: Incomplete
    complexity: Incomplete
    cullBackfaces: Incomplete
    defaultMaterialAmbient: Incomplete
    defaultMaterialSpecular: Incomplete
    displayCameraOracles: Incomplete
    displayGuide: Incomplete
    displayPrimId: Incomplete
    displayProxy: Incomplete
    displayRender: Incomplete
    domeLightEnabled: Incomplete
    domeLightTexturesVisible: Incomplete
    enableSceneLights: Incomplete
    enableSceneMaterials: Incomplete
    fontSize: Incomplete
    freeCamera: Incomplete
    freeCameraAspect: Incomplete
    freeCameraFOV: Incomplete
    freeCameraOverrideFar: Incomplete
    freeCameraOverrideNear: Incomplete
    highlightColorName: Incomplete
    lockFreeCameraAspect: Incomplete
    pickMode: Incomplete
    redrawOnScrub: Incomplete
    renderMode: Incomplete
    rolloverPrimInfo: Incomplete
    selHighlightMode: Incomplete
    showAABBox: Incomplete
    showAbstractPrims: Incomplete
    showAllPrototypePrims: Incomplete
    showBBoxPlayback: Incomplete
    showBBoxes: Incomplete
    showHUD: Incomplete
    showHUD_Complexity: Incomplete
    showHUD_GPUstats: Incomplete
    showHUD_Info: Incomplete
    showHUD_Performance: Incomplete
    showInactivePrims: Incomplete
    showMask_Outline: Incomplete
    showOBBox: Incomplete
    showPrimDisplayNames: Incomplete
    showReticles_Inside: Incomplete
    showReticles_Outside: Incomplete
    showUndefinedPrims: Incomplete
    def __init__(self, rootDataModel, parent) -> None: ...
    def _frustumChanged(self): ...
    def _frustumSettingsChanged(self): ...
    def _updateFreeCameraData(self): ...
    def onSaveState(self, state): ...
    def resetDefaultMaterial(self): ...
    def setDefaultMaterial(self, *args, **kwargs): ...
    def setOcioSettings(self, *args, **kwargs): ...
    @property
    def clearColor(self): ...
    @property
    def highlightColor(self): ...
    @property
    def ocioSettings(self): ...
    @property
    def showMask(self): ...
    @property
    def showMask_Opaque(self): ...

def freeCameraViewSetting(f): ...
def invisibleViewSetting(f): ...
def visibleViewSetting(f): ...
