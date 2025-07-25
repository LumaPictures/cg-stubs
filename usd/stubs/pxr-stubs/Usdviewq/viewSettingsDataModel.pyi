from . import settings as settings
from .common import CameraMaskModes as CameraMaskModes, ClearColors as ClearColors, ColorCorrectionModes as ColorCorrectionModes, HighlightColors as HighlightColors, PickModes as PickModes, PrintWarning as PrintWarning, RenderModes as RenderModes, SelectionHighlightModes as SelectionHighlightModes
from .freeCamera import FreeCamera as FreeCamera
from .qt import QtCore as QtCore
from .settings import StateSource as StateSource
from _typeshed import Incomplete
from pxr import Sdf as Sdf, UsdGeom as UsdGeom
from pxr.UsdAppUtils.complexityArgs import RefinementComplexities as RefinementComplexities
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup

_CLEAR_COLORS_DICT: Incomplete
_HIGHLIGHT_COLORS_DICT: Incomplete
DEFAULT_AMBIENT: float
DEFAULT_SPECULAR: float

def visibleViewSetting(f): ...
def invisibleViewSetting(f): ...
def freeCameraViewSetting(f): ...

class OCIOSettings:
    """Class to hold OCIO display, view, and colorSpace config settings
    as strings."""
    _display: Incomplete
    _view: Incomplete
    _colorSpace: Incomplete
    def __init__(self, display: str = '', view: str = '', colorSpace: str = '') -> None: ...
    @property
    def display(self): ...
    @property
    def view(self): ...
    @property
    def colorSpace(self): ...

class ViewSettingsDataModel(StateSource, QtCore.QObject):
    """Data model containing settings related to the rendered view of a USD
    file.
    """
    signalSettingChanged: Incomplete
    signalVisibleSettingChanged: Incomplete
    signalFreeCameraSettingChanged: Incomplete
    signalAutoComputeClippingPlanesChanged: Incomplete
    signalDefaultMaterialChanged: Incomplete
    signalStyleSettingsChanged: Incomplete
    _rootDataModel: Incomplete
    _cameraMaskColor: Incomplete
    _cameraReticlesColor: Incomplete
    _defaultMaterialAmbient: Incomplete
    _defaultMaterialSpecular: Incomplete
    _redrawOnScrub: Incomplete
    _renderMode: Incomplete
    _freeCameraFOV: Incomplete
    _freeCameraAspect: Incomplete
    _clippingPlaneNoneValue: Incomplete
    _freeCameraOverrideNear: Incomplete
    _freeCameraOverrideFar: Incomplete
    _lockFreeCameraAspect: Incomplete
    _colorCorrectionMode: Incomplete
    _ocioSettings: Incomplete
    _pickMode: Incomplete
    _selHighlightMode: Incomplete
    _highlightColorName: Incomplete
    _ambientLightOnly: Incomplete
    _domeLightEnabled: Incomplete
    _domeLightTexturesVisible: Incomplete
    _clearColorText: Incomplete
    _autoComputeClippingPlanes: Incomplete
    _showBBoxPlayback: Incomplete
    _showBBoxes: Incomplete
    _showAABBox: Incomplete
    _showOBBox: Incomplete
    _displayGuide: Incomplete
    _displayProxy: Incomplete
    _displayRender: Incomplete
    _displayPrimId: Incomplete
    _enableSceneMaterials: Incomplete
    _enableSceneLights: Incomplete
    _cullBackfaces: Incomplete
    _showInactivePrims: Incomplete
    _showAllPrototypePrims: Incomplete
    _showUndefinedPrims: Incomplete
    _showAbstractPrims: Incomplete
    _showPrimDisplayNames: Incomplete
    _rolloverPrimInfo: Incomplete
    _displayCameraOracles: Incomplete
    _cameraMaskMode: Incomplete
    _showMask_Outline: Incomplete
    _showReticles_Inside: Incomplete
    _showReticles_Outside: Incomplete
    _showHUD: Incomplete
    _showHUD_Info: Incomplete
    _showHUD_Complexity: Incomplete
    _showHUD_Performance: Incomplete
    _showHUD_GPUstats: Incomplete
    _complexity: Incomplete
    _freeCamera: Incomplete
    _cameraPath: Incomplete
    _fontSize: Incomplete
    def __init__(self, rootDataModel, parent) -> None: ...
    def onSaveState(self, state) -> None: ...
    @property
    def cameraMaskColor(self): ...
    @cameraMaskColor.setter
    def cameraMaskColor(self, color) -> None: ...
    @property
    def cameraReticlesColor(self): ...
    @cameraReticlesColor.setter
    def cameraReticlesColor(self, color) -> None: ...
    @property
    def defaultMaterialAmbient(self): ...
    @defaultMaterialAmbient.setter
    def defaultMaterialAmbient(self, value) -> None: ...
    @property
    def defaultMaterialSpecular(self): ...
    @defaultMaterialSpecular.setter
    def defaultMaterialSpecular(self, value) -> None: ...
    def setDefaultMaterial(self, ambient, specular) -> None: ...
    def resetDefaultMaterial(self) -> None: ...
    @property
    def complexity(self): ...
    @complexity.setter
    def complexity(self, value) -> None: ...
    @property
    def renderMode(self): ...
    @renderMode.setter
    def renderMode(self, value) -> None: ...
    @property
    def freeCameraFOV(self): ...
    @freeCameraFOV.setter
    def freeCameraFOV(self, value) -> None: ...
    @property
    def freeCameraOverrideNear(self):
        """Returns the free camera's near clipping plane value, if it has been
        overridden by the user. Returns None if there is no user-defined near
        clipping plane."""
    @freeCameraOverrideNear.setter
    def freeCameraOverrideNear(self, value) -> None:
        """Sets the near clipping plane to the given value. Passing in None will
        clear the current override."""
    @property
    def freeCameraOverrideFar(self):
        """Returns the free camera's far clipping plane value, if it has been
        overridden by the user. Returns None if there is no user-defined far
        clipping plane."""
    @freeCameraOverrideFar.setter
    def freeCameraOverrideFar(self, value) -> None:
        """Sets the far clipping plane to the given value. Passing in None will
        clear the current override."""
    @property
    def freeCameraAspect(self): ...
    @freeCameraAspect.setter
    def freeCameraAspect(self, value) -> None: ...
    def _frustumChanged(self) -> None:
        """
        Needed when updating any camera setting (including movements). Will not
        update the property viewer.
        """
    def _frustumSettingsChanged(self) -> None:
        """
        Needed when updating specific camera settings (e.g., aperture). See
        _updateFreeCameraData for the full list of dependent settings. Will
        update the property viewer.
        """
    def _updateFreeCameraData(self) -> None:
        """Updates member variables with the current free camera view settings.
        """
    @property
    def lockFreeCameraAspect(self): ...
    @lockFreeCameraAspect.setter
    def lockFreeCameraAspect(self, value) -> None: ...
    @property
    def colorCorrectionMode(self): ...
    @colorCorrectionMode.setter
    def colorCorrectionMode(self, value) -> None: ...
    @property
    def ocioSettings(self): ...
    def setOcioSettings(self, colorSpace: str = '', display: str = '', view: str = '') -> None:
        """Specifies the OCIO settings to be used. Setting the OCIO 'display'
           requires a 'view' to be specified."""
    @property
    def pickMode(self): ...
    @pickMode.setter
    def pickMode(self, value) -> None: ...
    @property
    def showAABBox(self): ...
    @showAABBox.setter
    def showAABBox(self, value) -> None: ...
    @property
    def showOBBox(self): ...
    @showOBBox.setter
    def showOBBox(self, value) -> None: ...
    @property
    def showBBoxes(self): ...
    @showBBoxes.setter
    def showBBoxes(self, value) -> None: ...
    @property
    def autoComputeClippingPlanes(self): ...
    @autoComputeClippingPlanes.setter
    def autoComputeClippingPlanes(self, value) -> None: ...
    @property
    def showBBoxPlayback(self): ...
    @showBBoxPlayback.setter
    def showBBoxPlayback(self, value) -> None: ...
    @property
    def displayGuide(self): ...
    @displayGuide.setter
    def displayGuide(self, value) -> None: ...
    @property
    def displayProxy(self): ...
    @displayProxy.setter
    def displayProxy(self, value) -> None: ...
    @property
    def displayRender(self): ...
    @displayRender.setter
    def displayRender(self, value) -> None: ...
    @property
    def displayCameraOracles(self): ...
    @displayCameraOracles.setter
    def displayCameraOracles(self, value) -> None: ...
    @property
    def displayPrimId(self): ...
    @displayPrimId.setter
    def displayPrimId(self, value) -> None: ...
    @property
    def enableSceneMaterials(self): ...
    @enableSceneMaterials.setter
    def enableSceneMaterials(self, value) -> None: ...
    @property
    def enableSceneLights(self): ...
    @enableSceneLights.setter
    def enableSceneLights(self, value) -> None: ...
    @property
    def cullBackfaces(self): ...
    @cullBackfaces.setter
    def cullBackfaces(self, value) -> None: ...
    @property
    def showInactivePrims(self): ...
    @showInactivePrims.setter
    def showInactivePrims(self, value) -> None: ...
    @property
    def showAllPrototypePrims(self): ...
    @showAllPrototypePrims.setter
    def showAllPrototypePrims(self, value) -> None: ...
    @property
    def showUndefinedPrims(self): ...
    @showUndefinedPrims.setter
    def showUndefinedPrims(self, value) -> None: ...
    @property
    def showAbstractPrims(self): ...
    @showAbstractPrims.setter
    def showAbstractPrims(self, value) -> None: ...
    @property
    def showPrimDisplayNames(self): ...
    @showPrimDisplayNames.setter
    def showPrimDisplayNames(self, value) -> None: ...
    @property
    def rolloverPrimInfo(self): ...
    @rolloverPrimInfo.setter
    def rolloverPrimInfo(self, value) -> None: ...
    @property
    def cameraMaskMode(self): ...
    @cameraMaskMode.setter
    def cameraMaskMode(self, value) -> None: ...
    @property
    def showMask(self): ...
    @property
    def showMask_Opaque(self): ...
    @property
    def showMask_Outline(self): ...
    @showMask_Outline.setter
    def showMask_Outline(self, value) -> None: ...
    @property
    def showReticles_Inside(self): ...
    @showReticles_Inside.setter
    def showReticles_Inside(self, value) -> None: ...
    @property
    def showReticles_Outside(self): ...
    @showReticles_Outside.setter
    def showReticles_Outside(self, value) -> None: ...
    @property
    def showHUD(self): ...
    @showHUD.setter
    def showHUD(self, value) -> None: ...
    @property
    def showHUD_Info(self): ...
    @showHUD_Info.setter
    def showHUD_Info(self, value) -> None: ...
    @property
    def showHUD_Complexity(self): ...
    @showHUD_Complexity.setter
    def showHUD_Complexity(self, value) -> None: ...
    @property
    def showHUD_Performance(self): ...
    @showHUD_Performance.setter
    def showHUD_Performance(self, value) -> None: ...
    @property
    def showHUD_GPUstats(self): ...
    @showHUD_GPUstats.setter
    def showHUD_GPUstats(self, value) -> None: ...
    @property
    def ambientLightOnly(self): ...
    @ambientLightOnly.setter
    def ambientLightOnly(self, value) -> None: ...
    @property
    def domeLightEnabled(self): ...
    @domeLightEnabled.setter
    def domeLightEnabled(self, value) -> None: ...
    @property
    def domeLightTexturesVisible(self): ...
    @domeLightTexturesVisible.setter
    def domeLightTexturesVisible(self, value) -> None: ...
    @property
    def clearColorText(self): ...
    @clearColorText.setter
    def clearColorText(self, value) -> None: ...
    @property
    def clearColor(self): ...
    @property
    def highlightColorName(self): ...
    @highlightColorName.setter
    def highlightColorName(self, value) -> None: ...
    @property
    def highlightColor(self): ...
    @property
    def selHighlightMode(self): ...
    @selHighlightMode.setter
    def selHighlightMode(self, value) -> None: ...
    @property
    def redrawOnScrub(self): ...
    @redrawOnScrub.setter
    def redrawOnScrub(self, value) -> None: ...
    @property
    def freeCamera(self): ...
    @freeCamera.setter
    def freeCamera(self, value) -> None: ...
    @property
    def cameraPath(self): ...
    @cameraPath.setter
    def cameraPath(self, value) -> None: ...
    @property
    def cameraPrim(self): ...
    @cameraPrim.setter
    def cameraPrim(self, value) -> None: ...
    @property
    def fontSize(self): ...
    @fontSize.setter
    def fontSize(self, value) -> None: ...
