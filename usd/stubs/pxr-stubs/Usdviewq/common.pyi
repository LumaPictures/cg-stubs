# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtCore.Qt
import PySide6.QtGui
import pxr.Ar as Ar
import pxr.Kind as Kind
import pxr.Sdf as Sdf
import pxr.Tf as Tf
import pxr.Trace as Trace
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
import pxr.UsdShade as UsdShade
import pxr.UsdUtils.constantsGroup
import types
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.customAttributes import CustomAttribute as CustomAttribute
from typing import ClassVar

DEBUG_CLIPPING: str
ICON_DIR_ROOT: str
_icons: dict

class BusyContext:
    '''When used as a context object with python\'s "with" statement,
    will set Qt\'s busy cursor upon entry and pop it on exit.
    '''
    def __enter__(self): ...
    def __exit__(self, *args): ...

class CameraMaskModes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    FULL: ClassVar[str] = ...
    NONE: ClassVar[str] = ...
    PARTIAL: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class ClearColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    """Names of available background colors."""
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
    """Names of the default font family and monospace font family to be used
    with usdview"""
    FONT_FAMILY: ClassVar[str] = ...
    MONOSPACE_FONT_FAMILY: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class FixableDoubleValidator(PySide6.QtGui.QDoubleValidator):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent) -> None: ...
    def fixup(self, valStr): ...

class HighlightColors(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    """Names of available highlight colors for selected objects."""
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
    def __init__(self, identifier, realPath, offset, stage, timeCodesPerSecond, isMuted: bool = ..., depth: int = ...) -> None: ...
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
    """Raised when a prim does not exist at a valid path."""
    def __init__(self, path) -> None: ...

class PropertyNotFoundException(Exception):
    """Raised when a property does not exist at a valid path."""
    def __init__(self, path) -> None: ...

class PropertyViewDataRoles(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    ATTRIBUTE: ClassVar[str] = ...
    ATTRIBUTE_WITH_CONNNECTIONS: ClassVar[str] = ...
    COMPOSED: ClassVar[str] = ...
    CONNECTION: ClassVar[str] = ...
    NORMALIZED_NAME: ClassVar[int] = ...
    RELATIONSHIP: ClassVar[str] = ...
    RELATIONSHIP_WITH_TARGETS: ClassVar[str] = ...
    TARGET: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class PropertyViewIcons(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    _all: ClassVar[tuple] = ...
    @staticmethod
    def ATTRIBUTE(): ...
    @staticmethod
    def ATTRIBUTE_WITH_CONNECTIONS(): ...
    @staticmethod
    def COMPOSED(): ...
    @staticmethod
    def CONNECTION(): ...
    @staticmethod
    def RELATIONSHIP(): ...
    @staticmethod
    def RELATIONSHIP_WITH_TARGETS(): ...
    @staticmethod
    def TARGET(): ...

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
    '''Use as a context object with python\'s "with" statement, like so:
       with Timer("do some stuff", printTiming=True):
           doSomeStuff()

       If you want to defer printing timing information, one way to do so is as
       follows:
       with Timer("do some stuff") as t:
           doSomeStuff()
       if wantToPrintTime:
           t.PrintTime()
    '''
    def __init__(self, label, printTiming: bool = ...) -> None: ...
    def Invalidate(self): ...
    def PrintTime(self): ...
    def __enter__(self): ...
    def __exit__(self, excType: type[BaseException] | None, excVal: BaseException | None, excTB: types.TracebackType | None): ...

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
def Drange(start, stop, step):
    """Return a list whose first element is 'start' and the following elements
        (if any) are 'start' plus increasing whole multiples of 'step', up to but
        not greater than 'stop'.  For example:
        Drange(1, 3, 0.3) -> [1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8]"""
def DumpMallocTags(stage, contextStr): ...
def GetAssetCreationTime(primStack, assetIdentifier):
    '''Finds the weakest layer in which assetInfo.identifier is set to
        \'assetIdentifier\', and considers that an "asset-defining layer".
        If assetInfo.identifier is not set in any layer, assumes the weakest
        layer is the defining layer.  We then retrieve the creation time for
        the asset by stat\'ing the defining layer\'s real path.

        Returns a triple of strings: (fileDisplayName, creationTime, owner)'''
def GetEnclosingModelPrim(prim):
    """If 'prim' is inside/under a model of any kind, return the closest
        such ancestor prim - If 'prim' has no model ancestor, return None"""
def GetFileOwner(path): ...
def GetInstanceIdForIndex(prim, instanceIndex, time):
    """Attempt to find an authored Id value for the instance at index
        'instanceIndex' at time 'time', on the given prim 'prim', which we access
        as a UsdGeom.PointInstancer (whether it actually is or not, to provide
        some dynamic duck-typing for custom instancer types that support Ids.
        Returns 'None' if no ids attribute was found, or if instanceIndex is
        outside the bounds of the ids array."""
def GetInstanceIndicesForIds(prim, instanceIds, time):
    """Attempt to find the instance indices of a list of authored instance IDs
        for prim 'prim' at time 'time'. If the prim is not a PointInstancer or does
        not have authored IDs, returns None. If any ID from 'instanceIds' does not
        exist at the given time, its index is not added to the list (because it does
        not have an index)."""
def GetPrimLoadability(prim):
    '''Return a tuple of (isLoadable, isLoaded) for \'prim\', according to
        the following rules:
        A prim is loadable if it is active, and either of the following are true:
           * prim has a payload
           * prim is a model group
        The latter is useful because loading is recursive on a UsdStage, and it
        is convenient to be able to (e.g.) load everything loadable in a set.

        A prim \'isLoaded\' only if there are no unloaded prims beneath it, i.e.
        it is stating whether the prim is "fully loaded".  This
        is a debatable definition, but seems useful for usdview\'s purposes.'''
def GetPrimsLoadability(prims):
    """Follow the logic of GetPrimLoadability for each prim, combining
        results so that isLoadable is the disjunction of all prims, and
        isLoaded is the conjunction."""
def GetPropertyColor(prop, frame, hasValue, hasAuthoredValue, valueIsDefault): ...
def GetPropertyTextFont(prop, frame): ...
def GetRootLayerStackInfo(stage): ...
def GetShortStringForValue(prop, val): ...
def GetValueAndDisplayString(prop, time):
    """If `prop` is a timeSampled Sdf.AttributeSpec, compute a string specifying
        how many timeSamples it possesses.  Otherwise, compute the single default
        value, or targets for a relationship, or value at 'time' for a
        Usd.Attribute.  Return a tuple of a parameterless function that returns the
        resolved value at 'time', and the computed brief string for display.  We
        return a value-producing function rather than the value itself because for
        an Sdf.AttributeSpec with multiple timeSamples, the resolved value is
        *all* of the timeSamples, which can be expensive to compute, and is
        rarely needed.
    """
def HasSessionVis(prim):
    """Is there a session-layer override for visibility for 'prim'?"""
def InvisRootPrims(stage):
    """Make all defined root prims of stage be invisible,
        at Usd.TimeCode.Default()"""
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
