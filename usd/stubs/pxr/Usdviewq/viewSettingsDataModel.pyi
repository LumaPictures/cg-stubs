import PySide6.QtCore
import pxr.Sdf as Sdf
import pxr.UsdGeom as UsdGeom
import pxr.Usdviewq.settings as settings
from pxr.UsdAppUtils.complexityArgs import RefinementComplexities as RefinementComplexities
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.common import CameraMaskModes as CameraMaskModes, ClearColors as ClearColors, ColorCorrectionModes as ColorCorrectionModes, HighlightColors as HighlightColors, PickModes as PickModes, PrintWarning as PrintWarning, RenderModes as RenderModes, SelectionHighlightModes as SelectionHighlightModes
from pxr.Usdviewq.freeCamera import FreeCamera as FreeCamera
from pxr.Usdviewq.settings import StateSource as StateSource
from typing import Any, Callable, ClassVar

freeCameraViewSetting: Callable
invisibleViewSetting: Callable
visibleViewSetting: Callable

class OCIOSettings:
    __init__: ClassVar[Callable] = ...
    @property
    def colorSpace(self) -> Any: ...
    @property
    def display(self) -> Any: ...
    @property
    def view(self) -> Any: ...

class ViewSettingsDataModel(PySide6.QtCore.QObject, StateSource):
    __init__: ClassVar[Callable] = ...
    _frustumChanged: ClassVar[Callable] = ...
    _frustumSettingsChanged: ClassVar[Callable] = ...
    _updateFreeCameraData: ClassVar[Callable] = ...
    onSaveState: ClassVar[Callable] = ...
    resetDefaultMaterial: ClassVar[Callable] = ...
    setDefaultMaterial: ClassVar[Callable] = ...
    setOcioSettings: ClassVar[Callable] = ...
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
    def signalAutoComputeClippingPlanesChanged(self, *args, **kwargs) -> Any: ...
    def signalDefaultMaterialChanged(self, *args, **kwargs) -> Any: ...
    def signalFreeCameraSettingChanged(self, *args, **kwargs) -> Any: ...
    def signalSettingChanged(self, *args, **kwargs) -> Any: ...
    def signalStyleSettingsChanged(self, *args, **kwargs) -> Any: ...
    def signalVisibleSettingChanged(self, *args, **kwargs) -> Any: ...
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