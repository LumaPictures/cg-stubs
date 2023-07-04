# mypy: disable_error_code = misc
import pxr.Ar as Ar
import pxr.Kind as Kind
import PySide6.QtCore.Qt
import PySide6.QtCore.Qt
import PySide6.QtGui
import pxr.Sdf as Sdf
import pxr.Tf as Tf
import pxr.Trace as Trace
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
import pxr.UsdShade as UsdShade
import pxr.UsdUtils.constantsGroup
from _typeshed import Incomplete
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.customAttributes import CustomAttribute as CustomAttribute
from typing import ClassVar

DEBUG_CLIPPING: str
ICON_DIR_ROOT: str
_icons: dict

class BusyContext:
    def __enter__(self): ...
    def __exit__(self, *args): ...

class CameraMaskModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    FULL: ClassVar[str] = ...
    NONE: ClassVar[str] = ...
    PARTIAL: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class ClearColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    BLACK: ClassVar[str] = ...
    DARK_GREY: ClassVar[str] = ...
    LIGHT_GREY: ClassVar[str] = ...
    WHITE: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class ColorCorrectionModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    DISABLED: ClassVar[str] = ...
    OPENCOLORIO: ClassVar[str] = ...
    SRGB: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class DefaultFontFamily(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    FONT_FAMILY: ClassVar[str] = ...
    MONOSPACE_FONT_FAMILY: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class FixableDoubleValidator(PySide6.QtGui.QDoubleValidator):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent): ...
    def fixup(self, valStr): ...

class HighlightColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    CYAN: ClassVar[str] = ...
    WHITE: ClassVar[str] = ...
    YELLOW: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class IncludedPurposes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    DEFAULT: ClassVar[str] = ...
    GUIDE: ClassVar[str] = ...
    PROXY: ClassVar[str] = ...
    RENDER: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class KeyboardShortcuts(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    FramingKey: ClassVar[PySide6.QtCore.Qt.Key] = ...
    _all: ClassVar[tuple] = ...

class LayerInfo:
    def __init__(self, identifier, realPath, offset, stage, timeCodesPerSecond: Incomplete | None = ..., isMuted: bool = ..., depth: int = ...): ...
    @classmethod
    def FromLayer(cls, layer, stage, offset, depth: int = ...): ...
    @classmethod
    def FromMutedLayerIdentifier(cls, identifier, parentLayer, stage, depth: int = ...): ...
    def GetHierarchicalDisplayString(self): ...
    def GetIdentifier(self): ...
    def GetOffset(self): ...
    def GetOffsetString(self): ...
    def GetOffsetTooltipString(self): ...
    def GetRealPath(self): ...
    def GetToolTipString(self): ...
    def IsMuted(self): ...

class PickModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    INSTANCES: ClassVar[str] = ...
    MODELS: ClassVar[str] = ...
    PRIMS: ClassVar[str] = ...
    PROTOTYPES: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class PrimNotFoundException(Exception):
    def __init__(self, path): ...

class PropertyNotFoundException(Exception):
    def __init__(self, path): ...

class PropertyViewDataRoles(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    ATTRIBUTE: ClassVar[str] = ...
    ATTRIBUTE_WITH_CONNNECTIONS: ClassVar[str] = ...
    COMPOSED: ClassVar[str] = ...
    CONNECTION: ClassVar[str] = ...
    RELATIONSHIP: ClassVar[str] = ...
    RELATIONSHIP_WITH_TARGETS: ClassVar[str] = ...
    TARGET: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class PropertyViewIcons(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    _all: ClassVar[tuple] = ...
    def ATTRIBUTE(self): ...
    def ATTRIBUTE_WITH_CONNECTIONS(self): ...
    def COMPOSED(self): ...
    def CONNECTION(self): ...
    def RELATIONSHIP(self): ...
    def RELATIONSHIP_WITH_TARGETS(self): ...
    def TARGET(self): ...

class PropertyViewIndex(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    NAME: ClassVar[int] = ...
    TYPE: ClassVar[int] = ...
    VALUE: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class RenderModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    FLAT_SHADED: ClassVar[str] = ...
    GEOM_FLAT: ClassVar[str] = ...
    GEOM_ONLY: ClassVar[str] = ...
    GEOM_SMOOTH: ClassVar[str] = ...
    HIDDEN_SURFACE_WIREFRAME: ClassVar[str] = ...
    POINTS: ClassVar[str] = ...
    SMOOTH_SHADED: ClassVar[str] = ...
    WIREFRAME: ClassVar[str] = ...
    WIREFRAME_ON_SURFACE: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class SelectionHighlightModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    ALWAYS: ClassVar[str] = ...
    NEVER: ClassVar[str] = ...
    ONLY_WHEN_PAUSED: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class ShadedRenderModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    FLAT_SHADED: ClassVar[str] = ...
    GEOM_FLAT: ClassVar[str] = ...
    GEOM_SMOOTH: ClassVar[str] = ...
    SMOOTH_SHADED: ClassVar[str] = ...
    WIREFRAME_ON_SURFACE: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class Timer:
    def __init__(self, label, printTiming: bool = ...): ...
    def Invalidate(self): ...
    def PrintTime(self): ...
    def __enter__(self): ...
    def __exit__(self, excType, excVal, excTB): ...

class UIBaseColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    DARK_YELLOW: ClassVar[PySide6.QtGui.QBrush] = ...
    LIGHT_SKY_BLUE: ClassVar[PySide6.QtGui.QBrush] = ...
    RED: ClassVar[PySide6.QtGui.QBrush] = ...
    _all: ClassVar[tuple] = ...

class UIFonts(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    ABSTRACT_PRIM: ClassVar[PySide6.QtGui.QFont] = ...
    BASE_POINT_SIZE: ClassVar[int] = ...
    BOLD: ClassVar[PySide6.QtGui.QFont] = ...
    BOLD_ITALIC: ClassVar[PySide6.QtGui.QFont] = ...
    DEFINED_PRIM: ClassVar[PySide6.QtGui.QFont] = ...
    INHERITED: ClassVar[PySide6.QtGui.QFont] = ...
    ITALIC: ClassVar[PySide6.QtGui.QFont] = ...
    NORMAL: ClassVar[PySide6.QtGui.QFont] = ...
    OVER_PRIM: ClassVar[PySide6.QtGui.QFont] = ...
    _all: ClassVar[tuple] = ...

class UIPrimTreeColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    ANCESTOR_OF_SELECTED: ClassVar[PySide6.QtGui.QBrush] = ...
    ANCESTOR_OF_SELECTED_HOVER: ClassVar[PySide6.QtGui.QBrush] = ...
    SELECTED: ClassVar[PySide6.QtGui.QBrush] = ...
    SELECTED_HOVER: ClassVar[PySide6.QtGui.QBrush] = ...
    UNSELECTED_HOVER: ClassVar[PySide6.QtGui.QBrush] = ...
    _all: ClassVar[tuple] = ...

class UIPrimTypeColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    HAS_ARCS: ClassVar[PySide6.QtGui.QBrush] = ...
    INSTANCE: ClassVar[PySide6.QtGui.QBrush] = ...
    NORMAL: ClassVar[PySide6.QtGui.QBrush] = ...
    PROTOTYPE: ClassVar[PySide6.QtGui.QBrush] = ...
    _all: ClassVar[tuple] = ...

class UIPropertyValueSourceColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    DEFAULT: ClassVar[PySide6.QtGui.QBrush] = ...
    FALLBACK: ClassVar[PySide6.QtGui.QBrush] = ...
    NONE: ClassVar[PySide6.QtGui.QBrush] = ...
    TIME_SAMPLE: ClassVar[PySide6.QtGui.QBrush] = ...
    VALUE_CLIPS: ClassVar[PySide6.QtGui.QBrush] = ...
    _all: ClassVar[tuple] = ...

def BoldenLabelText(text, substring): ...
def ColorizeLabelText(text, substring, r, g, b): ...
def Drange(start, stop, step): ...
def DumpMallocTags(stage, contextStr): ...
def GetAssetCreationTime(primStack, assetIdentifier): ...
def GetEnclosingModelPrim(prim): ...
def GetFileOwner(path): ...
def GetInstanceIdForIndex(prim, instanceIndex, time): ...
def GetInstanceIndicesForIds(prim, instanceIds, time): ...
def GetPrimLoadability(prim): ...
def GetPrimsLoadability(prims): ...
def GetPropertyColor(prop, frame, hasValue: Incomplete | None = ..., hasAuthoredValue: Incomplete | None = ..., valueIsDefault: Incomplete | None = ...): ...
def GetPropertyTextFont(prop, frame): ...
def GetRootLayerStackInfo(stage): ...
def GetShortStringForValue(prop, val): ...
def GetValueAndDisplayString(prop, time): ...
def HasSessionVis(prim): ...
def InvisRootPrims(stage): ...
def ItalicizeLabelText(text, substring): ...
def PrettyFormatSize(sz): ...
def PrintWarning(title, description): ...
def PropTreeWidgetTypeIsRel(tw): ...
def ReportMetricSize(sizeInBytes): ...
def ResetSessionVisibility(stage): ...
def _AddLayerTree(stage, layerTree, depth: int = ...): ...
def _AddLayerTreeWithMutedSubLayers(stage, layerTree, depth: int = ...): ...
def _DeferredIconLoad(path): ...
def _GetAttributeStatus(attribute, frame): ...
def _PropTreeWidgetGetRole(tw): ...
def _RemoveVisibilityRecursive(primSpec): ...
def _UpdateLabelText(text, substring, mode): ...