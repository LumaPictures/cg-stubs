# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Any, ClassVar, overload

CHANGE_TYPE_BEGIN: FCurve.ChangeType
CHANGE_TYPE_END: FCurve.ChangeType
CHANGE_TYPE_INTERMEDIATE: FCurve.ChangeType
CHANGE_TYPE_NORMAL: FCurve.ChangeType
CLAMPED_TANGENT: Tangent.TangentType
CURVE_ASSIGNED: FCurveObserver.CurveIntrinsicType
CURVE_CLEARED: FCurveObserver.CurveIntrinsicType
CURVE_NAME_CHANGED: FCurveObserver.CurveIntrinsicType
CURVE_SWAPPED: FCurveObserver.CurveIntrinsicType
FIXED_TANGENT: Tangent.TangentType
FLAT_TANGENT: Tangent.TangentType
KEYFRAME_BREAKDOWN_CHANGED: FCurveObserver.KeyframeIntrinsicType
KEYFRAME_POSITION_CHANGED: FCurveObserver.KeyframeIntrinsicType
KEYFRAME_UNIFIED_CHANGED: FCurveObserver.KeyframeIntrinsicType
LINEAR_TANGENT: Tangent.TangentType
PLATEAU_TANGENT: Tangent.TangentType
SEGMENT_INTERPOLATOR_CHANGED: FCurveObserver.SegmentIntrinsicType
SMOOTH_NORMAL_TANGENT: Tangent.TangentType
SMOOTH_TANGENT: Tangent.TangentType
TANGENT_LOCKED_WEIGHT_CHANGED: FCurveObserver.TangentIntrinsicType
TANGENT_TYPE_CHANGED: FCurveObserver.TangentIntrinsicType
TANGENT_VECTOR_CHANGED: FCurveObserver.TangentIntrinsicType
TANGENT_WEIGHTED_CHANGED: FCurveObserver.TangentIntrinsicType

class ContainerObserver:
    def __init__(self) -> None: ...
    @overload
    def containerChanged(self, arg0: FCurveContainer) -> None: ...
    @overload
    def containerChanged(self) -> Any: ...

class FCurve:
    class ChangeType:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        cBegin: ClassVar[FCurve.ChangeType] = ...
        cEnd: ClassVar[FCurve.ChangeType] = ...
        cIntermediate: ClassVar[FCurve.ChangeType] = ...
        cNormal: ClassVar[FCurve.ChangeType] = ...
        def __init__(self, arg0: int) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> Any: ...
        def __hash__(self) -> int: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __setstate__(self, state) -> Any: ...
        @property
        def name(self) -> str: ...
    cBegin: ClassVar[FCurve.ChangeType] = ...
    cEnd: ClassVar[FCurve.ChangeType] = ...
    cIntermediate: ClassVar[FCurve.ChangeType] = ...
    cNormal: ClassVar[FCurve.ChangeType] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def clear(self) -> None: ...
    @overload
    def clearProperties(self) -> None: ...
    @overload
    def clearProperties(self) -> Any: ...
    def copy(self) -> FCurve: ...
    def eval(self, arg0: float) -> float: ...
    def evalAcceleration(self, arg0: float) -> float: ...
    def evalVelocity(self, arg0: float) -> float: ...
    def findSegment(self, *args, **kwargs) -> Any: ...
    def getKeyframes(self) -> list: ...
    def getName(self) -> str: ...
    def getProperties(self) -> dict: ...
    def getProperty(self, arg0: str) -> str: ...
    def getSegments(self) -> list: ...
    @overload
    def insertSegment(self) -> Any: ...
    @overload
    def insertSegment(self) -> Any: ...
    def notifyChanged(self) -> None: ...
    @overload
    def removeSegment(self, arg0) -> None: ...
    @overload
    def removeSegment(self) -> Any: ...
    @overload
    def setChangeType(self, arg0: int) -> None: ...
    @overload
    def setChangeType(self) -> Any: ...
    def setName(self, arg0: str) -> None: ...
    def setProperty(self, arg0: str, arg1: str) -> bool: ...
    def sizeProperties(self) -> int: ...
    def subscribe(self, arg0) -> None: ...
    @overload
    @classmethod
    def subscribeGlobal(cls, arg0) -> None: ...
    @overload
    @classmethod
    def subscribeGlobal(cls) -> Any: ...
    def swap(self, arg0: FCurve) -> None: ...
    @overload
    def unsubscribe(self, arg0) -> None: ...
    @overload
    def unsubscribe(self) -> Any: ...
    @overload
    @classmethod
    def unsubscribeGlobal(cls, arg0) -> None: ...
    @overload
    @classmethod
    def unsubscribeGlobal(cls) -> Any: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> FCurve: ...
    def __eq__(self, arg0: FCurve) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, arg0: FCurve) -> bool: ...

class FCurveContainer:
    def __init__(self) -> None: ...
    def addCurve(self, arg0: FCurve) -> None: ...
    def clear(self) -> None: ...
    @overload
    def clearProperties(self) -> None: ...
    @overload
    def clearProperties(self) -> Any: ...
    def getCurves(self) -> list: ...
    def getProperties(self) -> dict: ...
    def getProperty(self, arg0: str) -> str: ...
    @overload
    def readCurves(self, arg0: str) -> None: ...
    @overload
    def readCurves(self) -> Any: ...
    @overload
    def readCurves(self) -> Any: ...
    @overload
    def readCurves(self) -> Any: ...
    @overload
    def readCurves(self) -> Any: ...
    def removeCurve(self, arg0: FCurve) -> None: ...
    def setProperty(self, arg0: str, arg1: str) -> bool: ...
    def size(self) -> int: ...
    def sizeProperties(self) -> int: ...
    def subscribe(self, arg0) -> None: ...
    @overload
    def unsubscribe(self, arg0) -> None: ...
    @overload
    def unsubscribe(self) -> Any: ...
    def writeCurves(self, arg0: str, arg1: str) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, arg0: FCurveContainer) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, arg0: FCurveContainer) -> bool: ...

class FCurveObserver:
    class CurveIntrinsicType:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        cAssigned: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
        cCleared: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
        cNameChanged: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
        cSwapped: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
        def __init__(self, arg0: int) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> Any: ...
        def __hash__(self) -> int: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __setstate__(self, state) -> Any: ...
        @property
        def name(self) -> str: ...
    class KeyframeIntrinsicType:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        cBreakdownChanged: ClassVar[FCurveObserver.KeyframeIntrinsicType] = ...
        cPositionChanged: ClassVar[FCurveObserver.KeyframeIntrinsicType] = ...
        cUnifiedChanged: ClassVar[FCurveObserver.KeyframeIntrinsicType] = ...
        def __init__(self, arg0: int) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> Any: ...
        def __hash__(self) -> int: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __setstate__(self, state) -> Any: ...
        @property
        def name(self) -> str: ...
    class SegmentIntrinsicType:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        cInterpolatorChanged: ClassVar[FCurveObserver.SegmentIntrinsicType] = ...
        def __init__(self, arg0: int) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> Any: ...
        def __hash__(self) -> int: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __setstate__(self, state) -> Any: ...
        @property
        def name(self) -> str: ...
    class TangentIntrinsicType:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        cLockedWeightChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
        cTypeChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
        cVectorChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
        cWeightedChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
        def __init__(self, arg0: int) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> Any: ...
        def __hash__(self) -> int: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __setstate__(self, state) -> Any: ...
        @property
        def name(self) -> str: ...
    cAssigned: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
    cBreakdownChanged: ClassVar[FCurveObserver.KeyframeIntrinsicType] = ...
    cCleared: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
    cInterpolatorChanged: ClassVar[FCurveObserver.SegmentIntrinsicType] = ...
    cLockedWeightChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
    cNameChanged: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
    cPositionChanged: ClassVar[FCurveObserver.KeyframeIntrinsicType] = ...
    cSwapped: ClassVar[FCurveObserver.CurveIntrinsicType] = ...
    cTypeChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
    cUnifiedChanged: ClassVar[FCurveObserver.KeyframeIntrinsicType] = ...
    cVectorChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
    cWeightedChanged: ClassVar[FCurveObserver.TangentIntrinsicType] = ...
    def __init__(self) -> None: ...
    @overload
    def beginValueChange(self, arg0: FCurve) -> None: ...
    @overload
    def beginValueChange(self) -> Any: ...
    def curveChanged(self, arg0: FCurve) -> None: ...
    def curveIntrinsicChanged(self, arg0: FCurve, arg1) -> None: ...
    def curvePropertyChanged(self, arg0: FCurve, arg1: str, arg2: str) -> None: ...
    @overload
    def endValueChange(self, arg0: FCurve) -> None: ...
    @overload
    def endValueChange(self) -> Any: ...
    @overload
    def intermediateValueChange(self, arg0: FCurve) -> None: ...
    @overload
    def intermediateValueChange(self) -> Any: ...
    def keyframeChanged(self, arg0: Keyframe) -> None: ...
    def keyframeIntrinsicChanged(self, arg0: Keyframe, arg1) -> None: ...
    def keyframePropertyChanged(self, arg0: Keyframe, arg1: str, arg2: str) -> None: ...
    def segmentAdded(self, arg0: FCurve, arg1: Segment) -> None: ...
    def segmentChanged(self, arg0: Segment) -> None: ...
    def segmentIntrinsicChanged(self, arg0: Segment, arg1) -> None: ...
    def segmentPropertyChanged(self, arg0: Segment, arg1: str, arg2: str) -> None: ...
    def segmentRemoved(self, arg0: FCurve, arg1: Segment) -> None: ...
    def tangentChanged(self, arg0: Tangent) -> None: ...
    def tangentIntrinsicChanged(self, arg0: Tangent, arg1) -> None: ...
    def tangentPropertyChanged(self, arg0: Tangent, arg1: str, arg2: str) -> None: ...

class Interpolator:
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self) -> float: ...

class Keyframe:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float) -> None: ...
    @overload
    def clearProperties(self) -> None: ...
    @overload
    def clearProperties(self) -> Any: ...
    def get(self) -> tuple: ...
    def getInTangent(self, *args, **kwargs) -> Any: ...
    def getLeftSegment(self) -> Segment: ...
    @classmethod
    def getMinSeparation(cls) -> float: ...
    def getOutTangent(self, *args, **kwargs) -> Any: ...
    def getOwningCurve(self) -> FCurve: ...
    def getProperties(self) -> dict: ...
    def getProperty(self, key: str) -> str: ...
    def getRightSegment(self) -> Segment: ...
    def getSegments(self) -> tuple: ...
    def getTangents(self) -> tuple: ...
    def getX(self) -> float: ...
    def getY(self) -> float: ...
    def isBreakdown(self) -> bool: ...
    def isTangentsUnified(self) -> bool: ...
    def set(self, x: float, y: float) -> None: ...
    def setBreakdown(self, arg0: bool) -> None: ...
    def setProperty(self, key: str, value: str) -> bool: ...
    def setTangentsUnified(self, arg0: bool) -> None: ...
    def setX(self, arg0: float) -> None: ...
    @overload
    def setY(self, arg0: float) -> None: ...
    @overload
    def setY(self, y) -> Any: ...
    def sizeProperties(self) -> int: ...
    def __hash__(self) -> int: ...
    def __lt__(self, arg0: Keyframe) -> bool: ...

class ParentSelectionObserver:
    def __init__(self, *args, **kwargs) -> None: ...

class Segment:
    def __init__(self) -> None: ...
    @overload
    def clearProperties(self) -> None: ...
    @overload
    def clearProperties(self) -> Any: ...
    def eval(self, arg0: float) -> float: ...
    def getExpression(self) -> str: ...
    def getFirstDerivative(self, arg0: float) -> float: ...
    def getInTangent(self, *args, **kwargs) -> Any: ...
    def getKeys(self) -> tuple: ...
    def getLeftKey(self, *args, **kwargs) -> Any: ...
    def getOutTangent(self, *args, **kwargs) -> Any: ...
    def getOwningCurve(self) -> FCurve: ...
    def getProperties(self) -> dict: ...
    def getProperty(self, arg0: str) -> str: ...
    def getRangeExtents(self, arg0: float, arg1: float) -> tuple: ...
    def getRightKey(self, *args, **kwargs) -> Any: ...
    def getSecondDerivative(self, arg0: float) -> float: ...
    def getTangents(self) -> tuple: ...
    def setExpression(self, arg0: str) -> None: ...
    def setProperty(self, arg0: str, arg1: str) -> None: ...
    def sizeProperties(self) -> int: ...
    def usesTangents(self) -> bool: ...
    def __eq__(self, arg0: Segment) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, arg0: Segment) -> bool: ...

class Selection:
    def __init__(self, arg0: FCurveContainer) -> None: ...
    def clear(self) -> None: ...
    @overload
    def deselect(self, arg0: FCurve) -> None: ...
    @overload
    def deselect(self, arg0: Segment) -> None: ...
    @overload
    def deselect(self, arg0: Keyframe) -> None: ...
    @overload
    def deselect(self, arg0: Tangent) -> None: ...
    def getCurves(self) -> FCurveContainer: ...
    def getSelectedCurves(self) -> list: ...
    def getSelectedKeyframes(self) -> list: ...
    def getSelectedSegments(self) -> list: ...
    def getSelectedTangents(self) -> list: ...
    @overload
    def isSelected(self, arg0: FCurve) -> bool: ...
    @overload
    def isSelected(self, arg0: Segment) -> bool: ...
    @overload
    def isSelected(self, arg0: Keyframe) -> bool: ...
    @overload
    def isSelected(self, arg0: Tangent) -> bool: ...
    @overload
    def select(self, arg0: FCurve) -> None: ...
    @overload
    def select(self, arg0: Segment) -> None: ...
    @overload
    def select(self, arg0: Keyframe) -> None: ...
    @overload
    def select(self, arg0: Tangent) -> None: ...
    def subscribe(self, observer) -> None: ...
    @overload
    def unsubscribe(self, observer) -> None: ...
    @overload
    def unsubscribe(self) -> Any: ...

class SelectionObserver(ParentSelectionObserver):
    def __init__(self) -> None: ...
    @overload
    def deselected(self, arg0: FCurve) -> None: ...
    @overload
    def deselected(self) -> Any: ...
    @overload
    def deselected(self, arg0: Segment) -> None: ...
    @overload
    def deselected(self) -> Any: ...
    @overload
    def deselected(self, arg0: Keyframe) -> None: ...
    @overload
    def deselected(self) -> Any: ...
    @overload
    def deselected(self, arg0: Tangent) -> None: ...
    @overload
    def deselected(self) -> Any: ...
    @overload
    def selected(self, arg0: FCurve) -> None: ...
    @overload
    def selected(self) -> Any: ...
    @overload
    def selected(self, arg0: Segment) -> None: ...
    @overload
    def selected(self) -> Any: ...
    @overload
    def selected(self, arg0: Keyframe) -> None: ...
    @overload
    def selected(self) -> Any: ...
    @overload
    def selected(self, arg0: Tangent) -> None: ...
    @overload
    def selected(self) -> Any: ...
    @overload
    def selectionCleared(self) -> None: ...
    @overload
    def selectionCleared(self) -> Any: ...

class Tangent:
    class TangentType:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        cClamped: ClassVar[Tangent.TangentType] = ...
        cFixed: ClassVar[Tangent.TangentType] = ...
        cFlat: ClassVar[Tangent.TangentType] = ...
        cLinear: ClassVar[Tangent.TangentType] = ...
        cSmooth: ClassVar[Tangent.TangentType] = ...
        cSmoothNormal: ClassVar[Tangent.TangentType] = ...
        def __init__(self, arg0: int) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> Any: ...
        def __hash__(self) -> int: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __setstate__(self, state) -> Any: ...
        @property
        def name(self) -> str: ...
    cClamped: ClassVar[Tangent.TangentType] = ...
    cFixed: ClassVar[Tangent.TangentType] = ...
    cFlat: ClassVar[Tangent.TangentType] = ...
    cLinear: ClassVar[Tangent.TangentType] = ...
    cSmooth: ClassVar[Tangent.TangentType] = ...
    cSmoothNormal: ClassVar[Tangent.TangentType] = ...
    def __init__(self) -> None: ...
    @overload
    def clearProperties(self) -> None: ...
    @overload
    def clearProperties(self) -> Any: ...
    def get(self) -> tuple: ...
    def getAngle(self) -> float: ...
    def getOpposingTangent(self) -> Tangent: ...
    def getOwningCurve(self) -> FCurve: ...
    def getOwningKeyframe(self) -> Keyframe: ...
    def getOwningSegment(self) -> Segment: ...
    def getProperties(self) -> dict: ...
    def getProperty(self, key: str) -> str: ...
    def getType(self, *args, **kwargs) -> Any: ...
    def getWeight(self) -> float: ...
    def getX(self) -> float: ...
    def getY(self) -> float: ...
    def isInTangent(self) -> bool: ...
    def isWeightLocked(self) -> bool: ...
    def isWeighted(self) -> bool: ...
    def set(self, x: float, y: float) -> None: ...
    def setAngle(self, angle: float) -> None: ...
    def setProperty(self, key: str, value: str) -> bool: ...
    def setType(self, type) -> None: ...
    def setWeight(self, weight: float) -> None: ...
    def setWeightLocked(self, arg0: bool) -> None: ...
    def setWeighted(self, arg0: bool) -> None: ...
    def setX(self, x: float) -> None: ...
    def setY(self, y: float) -> None: ...
    def sizeProperties(self) -> int: ...
    def __eq__(self, arg0: Tangent) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, arg0: Tangent) -> bool: ...

def GetGridSettings(curve: FCurve) -> tuple: ...
def GetNamespace() -> dict: ...
def HasGridSettings(curve: FCurve) -> bool: ...
def IsEditable(curve: FCurve) -> bool: ...
@overload
def IsLocked(curve: FCurve) -> bool: ...
@overload
def IsLocked(keyframe: Keyframe) -> bool: ...
def IsVisible(curve: FCurve) -> bool: ...
def ReadContainerFromString(string: str, container: FCurveContainer = ...) -> FCurveContainer: ...
def ReadFromBinaryString(binaryString: str, curve: FCurve = ...) -> FCurve: ...
def ReadFromXMLString(xmlString: str, curve: FCurve = ...) -> FCurve: ...
def RemoveGridSettings(curve: FCurve) -> None: ...
def SetEditable(curve: FCurve, isEditable: bool) -> None: ...
@overload
def SetGridSettings(arg0: FCurve, arg1: list[tuple[float, float, float, float]]) -> None: ...
@overload
def SetGridSettings(arg0: FCurve, arg1: float, arg2: float, arg3: float, arg4: float) -> None: ...
@overload
def SetLocked(curve: FCurve, isLocked: bool) -> None: ...
@overload
def SetLocked(keyframe: Keyframe, isLocked: bool) -> None: ...
def SetVisible(curve: FCurve, isVisible: bool) -> None: ...
def WriteContainerToString(container: FCurveContainer, format: str = ...) -> bytes: ...
def WriteToBinaryString(curve: FCurve) -> bytes: ...
def WriteToXMLString(curve: FCurve) -> str: ...