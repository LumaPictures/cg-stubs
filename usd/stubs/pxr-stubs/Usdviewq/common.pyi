from .customAttributes import CustomAttribute as CustomAttribute
from .qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete
from pxr import Ar as Ar, Kind as Kind, Sdf as Sdf, Tf as Tf, Trace as Trace, Usd as Usd, UsdGeom as UsdGeom, UsdShade as UsdShade
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup

DEBUG_CLIPPING: str

class ClearColors(ConstantsGroup):
    """Names of available background colors."""
    BLACK: str
    DARK_GREY: str
    LIGHT_GREY: str
    WHITE: str

class DefaultFontFamily(ConstantsGroup):
    """Names of the default font family and monospace font family to be used
    with usdview"""
    FONT_FAMILY: str
    MONOSPACE_FONT_FAMILY: str

class HighlightColors(ConstantsGroup):
    """Names of available highlight colors for selected objects."""
    WHITE: str
    YELLOW: str
    CYAN: str

class UIBaseColors(ConstantsGroup):
    RED: Incomplete
    LIGHT_SKY_BLUE: Incomplete
    DARK_YELLOW: Incomplete

class UIPrimTypeColors(ConstantsGroup):
    HAS_ARCS: Incomplete
    NORMAL: Incomplete
    INSTANCE: Incomplete
    PROTOTYPE: Incomplete

class UIPrimTreeColors(ConstantsGroup):
    SELECTED: Incomplete
    SELECTED_HOVER: Incomplete
    ANCESTOR_OF_SELECTED: Incomplete
    ANCESTOR_OF_SELECTED_HOVER: Incomplete
    UNSELECTED_HOVER: Incomplete

class UIPropertyValueSourceColors(ConstantsGroup):
    FALLBACK: Incomplete
    TIME_SAMPLE: Incomplete
    DEFAULT: Incomplete
    NONE: Incomplete
    VALUE_CLIPS: Incomplete

class UIFonts(ConstantsGroup):
    BASE_POINT_SIZE: int
    ITALIC: Incomplete
    NORMAL: Incomplete
    BOLD: Incomplete
    BOLD_ITALIC: Incomplete
    OVER_PRIM = ITALIC
    DEFINED_PRIM = BOLD
    ABSTRACT_PRIM = NORMAL
    INHERITED: Incomplete

class KeyboardShortcuts(ConstantsGroup):
    FramingKey: Incomplete

class PropertyViewIndex(ConstantsGroup):
    TYPE: Incomplete
    NAME: Incomplete
    VALUE: Incomplete

ICON_DIR_ROOT: Incomplete
_icons: Incomplete

def _DeferredIconLoad(path): ...

class PropertyViewIcons(ConstantsGroup):
    ATTRIBUTE: Incomplete
    ATTRIBUTE_WITH_CONNECTIONS: Incomplete
    RELATIONSHIP: Incomplete
    RELATIONSHIP_WITH_TARGETS: Incomplete
    TARGET: Incomplete
    CONNECTION: Incomplete
    COMPOSED: Incomplete

class PropertyViewDataRoles(ConstantsGroup):
    ATTRIBUTE: str
    RELATIONSHIP: str
    ATTRIBUTE_WITH_CONNNECTIONS: str
    RELATIONSHIP_WITH_TARGETS: str
    TARGET: str
    CONNECTION: str
    COMPOSED: str
    NORMALIZED_NAME: Incomplete

class RenderModes(ConstantsGroup):
    WIREFRAME: str
    WIREFRAME_ON_SURFACE: str
    SMOOTH_SHADED: str
    FLAT_SHADED: str
    POINTS: str
    GEOM_ONLY: str
    GEOM_FLAT: str
    GEOM_SMOOTH: str
    HIDDEN_SURFACE_WIREFRAME: str

class ShadedRenderModes(ConstantsGroup):
    SMOOTH_SHADED: Incomplete
    FLAT_SHADED: Incomplete
    WIREFRAME_ON_SURFACE: Incomplete
    GEOM_FLAT: Incomplete
    GEOM_SMOOTH: Incomplete

class ColorCorrectionModes(ConstantsGroup):
    DISABLED: str
    SRGB: str
    OPENCOLORIO: str

class PickModes(ConstantsGroup):
    PRIMS: str
    MODELS: str
    INSTANCES: str
    PROTOTYPES: str

class SelectionHighlightModes(ConstantsGroup):
    NEVER: str
    ONLY_WHEN_PAUSED: str
    ALWAYS: str

class CameraMaskModes(ConstantsGroup):
    NONE: str
    PARTIAL: str
    FULL: str

class IncludedPurposes(ConstantsGroup):
    DEFAULT: Incomplete
    PROXY: Incomplete
    GUIDE: Incomplete
    RENDER: Incomplete

def _PropTreeWidgetGetRole(tw): ...
def PropTreeWidgetTypeIsRel(tw): ...
def _UpdateLabelText(text, substring, mode): ...
def ItalicizeLabelText(text, substring): ...
def BoldenLabelText(text, substring): ...
def ColorizeLabelText(text, substring, r, g, b): ...
def PrintWarning(title, description) -> None: ...
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
def GetShortStringForValue(prop, val): ...
def ReportMetricSize(sizeInBytes): ...
def _GetAttributeStatus(attribute, frame): ...
def GetPropertyTextFont(prop, frame): ...
def GetPropertyColor(prop, frame, hasValue: Incomplete | None = None, hasAuthoredValue: Incomplete | None = None, valueIsDefault: Incomplete | None = None): ...

class LayerInfo:
    _identifier: Incomplete
    _realPath: Incomplete
    _offset: Incomplete
    _stage: Incomplete
    _timeCodesPerSecond: Incomplete
    _isMuted: Incomplete
    _depth: Incomplete
    def __init__(self, identifier, realPath, offset, stage, timeCodesPerSecond: Incomplete | None = None, isMuted: bool = False, depth: int = 0) -> None: ...
    @classmethod
    def FromLayer(cls, layer, stage, offset, depth: int = 0): ...
    @classmethod
    def FromMutedLayerIdentifier(cls, identifier, parentLayer, stage, depth: int = 0): ...
    def GetIdentifier(self): ...
    def GetRealPath(self): ...
    def IsMuted(self): ...
    def GetOffset(self): ...
    def GetOffsetString(self): ...
    def GetOffsetTooltipString(self): ...
    def GetToolTipString(self): ...
    def GetHierarchicalDisplayString(self): ...

def _AddLayerTree(stage, layerTree, depth: int = 0): ...
def _AddLayerTreeWithMutedSubLayers(stage, layerTree, depth: int = 0): ...
def GetRootLayerStackInfo(stage): ...
def PrettyFormatSize(sz): ...

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
    _printTiming: Incomplete
    _ittUtilTaskEnd: Incomplete
    _label: Incomplete
    _isValid: bool
    def __init__(self, label, printTiming: bool = False) -> None: ...
    _stopwatch: Incomplete
    interval: int
    def __enter__(self): ...
    def __exit__(self, excType: type[BaseException] | None, excVal: BaseException | None, excTB: types.TracebackType | None) -> None: ...  # type: ignore[name-defined]
    def Invalidate(self) -> None: ...
    def PrintTime(self) -> None: ...

class BusyContext:
    '''When used as a context object with python\'s "with" statement,
    will set Qt\'s busy cursor upon entry and pop it on exit.
    '''
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def InvisRootPrims(stage) -> None:
    """Make all defined root prims of stage be invisible,
    at Usd.TimeCode.Default()"""
def _RemoveVisibilityRecursive(primSpec) -> None: ...
def ResetSessionVisibility(stage) -> None: ...
def HasSessionVis(prim):
    """Is there a session-layer override for visibility for 'prim'?"""
def GetEnclosingModelPrim(prim):
    """If 'prim' is inside/under a model of any kind, return the closest
    such ancestor prim - If 'prim' has no model ancestor, return None"""
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
def GetFileOwner(path): ...
def GetAssetCreationTime(primStack, assetIdentifier):
    '''Finds the weakest layer in which assetInfo.identifier is set to
    \'assetIdentifier\', and considers that an "asset-defining layer".
    If assetInfo.identifier is not set in any layer, assumes the weakest
    layer is the defining layer.  We then retrieve the creation time for
    the asset by stat\'ing the defining layer\'s real path.

    Returns a triple of strings: (fileDisplayName, creationTime, owner)'''
def DumpMallocTags(stage, contextStr) -> None: ...
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
def Drange(start, stop, step):
    """Return a list whose first element is 'start' and the following elements
    (if any) are 'start' plus increasing whole multiples of 'step', up to but
    not greater than 'stop'.  For example:
    Drange(1, 3, 0.3) -> [1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8]"""

class PrimNotFoundException(Exception):
    """Raised when a prim does not exist at a valid path."""
    def __init__(self, path) -> None: ...

class PropertyNotFoundException(Exception):
    """Raised when a property does not exist at a valid path."""
    def __init__(self, path) -> None: ...

class FixableDoubleValidator(QtGui.QDoubleValidator):
    """This class implements a fixup() method for QDoubleValidator
    (see method for specific behavior).  To work around the brokenness
    of Pyside's fixup() wrapping, we allow the validator to directly
    update its parent if it is a QLineEdit, from within fixup().  Thus
    every QLineEdit must possess its own unique FixableDoubleValidator.
    
    The fixup method we supply (which can be usefully called directly)
    applies clamping and rounding to enforce the QDoubleValidator's
    range and decimals settings."""
    _lineEdit: Incomplete
    def __init__(self, parent) -> None: ...
    def fixup(self, valStr) -> None: ...
