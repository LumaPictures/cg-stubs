# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import pxr.Sdf as Sdf
import pxr.UsdGeom as UsdGeom
import pxr.Usdviewq.settings
import pxr.Usdviewq.settings as settings
from pxr.UsdAppUtils.complexityArgs import RefinementComplexities as RefinementComplexities
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.common import CameraMaskModes as CameraMaskModes, ClearColors as ClearColors, ColorCorrectionModes as ColorCorrectionModes, HighlightColors as HighlightColors, PickModes as PickModes, PrintWarning as PrintWarning, RenderModes as RenderModes, SelectionHighlightModes as SelectionHighlightModes
from pxr.Usdviewq.freeCamera import FreeCamera as FreeCamera
from pxr.Usdviewq.settings import StateSource as StateSource
from typing import Any, ClassVar

DEFAULT_AMBIENT: float
DEFAULT_SPECULAR: float
_CLEAR_COLORS_DICT: dict
_HIGHLIGHT_COLORS_DICT: dict

class OCIOSettings:
    def __init__(self, display: str = ..., view: str = ..., colorSpace: str = ...): ...
    @property
    def colorSpace(self) -> Any: ...
    @property
    def display(self) -> Any: ...
    @property
    def view(self) -> Any: ...

class ViewSettingsDataModel(PySide6.QtCore.QObject, pxr.Usdviewq.settings.StateSource):
    signalAutoComputeClippingPlanesChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalDefaultMaterialChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalFreeCameraSettingChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalSettingChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalStyleSettingsChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalVisibleSettingChanged: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    ambientLightOnly: Any
    autoComputeClippingPlanes: Any
    cameraMaskColor: Any
    cameraMaskMode: Any
    cameraPath: Any
    cameraPrim: Any
    cameraReticlesColor: Any
    clearColorText: Any
    colorCorrectionMode: Any
    complexity: Any
    cullBackfaces: Any
    defaultMaterialAmbient: Any
    defaultMaterialSpecular: Any
    displayCameraOracles: Any
    displayGuide: Any
    displayPrimId: Any
    displayProxy: Any
    displayRender: Any
    domeLightEnabled: Any
    domeLightTexturesVisible: Any
    enableSceneLights: Any
    enableSceneMaterials: Any
    fontSize: Any
    freeCamera: Any
    freeCameraAspect: Any
    freeCameraFOV: Any
    freeCameraOverrideFar: Any
    freeCameraOverrideNear: Any
    highlightColorName: Any
    lockFreeCameraAspect: Any
    pickMode: Any
    redrawOnScrub: Any
    renderMode: Any
    rolloverPrimInfo: Any
    selHighlightMode: Any
    showAABBox: Any
    showAbstractPrims: Any
    showAllPrototypePrims: Any
    showBBoxPlayback: Any
    showBBoxes: Any
    showHUD: Any
    showHUD_Complexity: Any
    showHUD_GPUstats: Any
    showHUD_Info: Any
    showHUD_Performance: Any
    showInactivePrims: Any
    showMask_Outline: Any
    showOBBox: Any
    showPrimDisplayNames: Any
    showReticles_Inside: Any
    showReticles_Outside: Any
    showUndefinedPrims: Any
    def __init__(self, rootDataModel, parent): ...
    def _frustumChanged(self): ...
    def _frustumSettingsChanged(self): ...
    def _updateFreeCameraData(self): ...
    def onSaveState(self, state): ...
    def resetDefaultMaterial(self): ...
    def setDefaultMaterial(self, *args, **kwargs): ...
    def setOcioSettings(self, *args, **kwargs): ...
    @property
    def clearColor(self) -> Any: ...
    @property
    def highlightColor(self) -> Any: ...
    @property
    def ocioSettings(self) -> Any: ...
    @property
    def showMask(self) -> Any: ...
    @property
    def showMask_Opaque(self) -> Any: ...

def freeCameraViewSetting(f): ...
def invisibleViewSetting(f): ...
def visibleViewSetting(f): ...
