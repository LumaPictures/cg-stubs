# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.GLDrawingRoutines as GLDrawingRoutines
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import UI4.Util.Events
import Utils as Utils
import collections
import enum
from UI4.Util.Events import EventProcessorHandler as EventProcessorHandler, LayerWorldDragEventProcessor as LayerWorldDragEventProcessor
from UI4.Util.TransformManipulatorLayer import TransformManipulatorLayer as TransformManipulatorLayer
from UI4.Util.TransformManipulatorLayer.TransformManipulatorLayer import COMPONENTS, COORDINATE_SYSTEM, PICK
from UI4.Util.UndoGrouping import UndoContextGuard as UndoContextGuard
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ParameterTransformGroupManipulator(TransformManipulatorLayer):
    _COMPONENTS_TO_PARAMS: ClassVar[dict] = ...
    _PARAMS_TO_COMPONENTS: ClassVar[dict] = ...
    def __init__(self, valuePolicy, autoKey: bool = ..., **kwargs) -> None: ...
    def _ParameterTransformGroupManipulator__setPolicyValueSingle(self, policy, value, final): ...
    def _ParameterTransformGroupManipulator__transformChanged(self, transforms): ...
    def _getPolicyValue(self, policyName): ...
    def _paramValueChanged(self, args): ...
    def _setPolicyValue(self, policyName, value, final): ...
    def _timeChanged(self, args): ...
    def _updateTransformsFromPolicy(self, changedTransforms: Incomplete | None = ...): ...
    def getValuePolicy(self): ...
    def processorFinished(self): ...
    def processorStarted(self, name): ...

class PivotEventProcessor(TransformEventProcessor):
    _NAME: ClassVar[str] = ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...

class RotateEventProcessor(TransformEventProcessor):
    _NAME: ClassVar[str] = ...
    _RotateEventProcessor__SNAP_INCREMENT: ClassVar[int] = ...
    _RotateEventProcessor__SNAP_KEY: ClassVar[PyQt5.QtCore.Qt.Key] = ...
    _RotateEventProcessor__SNAP_MODIFIER: ClassVar[PyQt5.QtCore.Qt.KeyboardModifier] = ...
    def __init__(self, layer, **kwargs) -> None: ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...

class ScaleEventProcessor(TransformEventProcessor):
    _NAME: ClassVar[str] = ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...

class ShearEventProcessor(TransformEventProcessor):
    _NAME: ClassVar[str] = ...
    _ShearEventProcessor__SHEAR_SNAP_EPS: ClassVar[float] = ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...

class TransformEventProcessor(UI4.Util.Events.LayerWorldDragEventProcessor):
    _NAME: ClassVar[str] = ...
    def __init__(self, layer, lockX: bool = ..., lockY: bool = ..., **kwargs) -> None: ...
    def _getLockX(self): ...
    def _getLockY(self): ...
    def finish(self, *args, **kwargs): ...

class TransformManipulatorLayer(QT4GLLayerStack.LayerStack.Layer, UI4.Util.Events.EventProcessorHandler):
    class COMPONENTS(enum.Enum):
        PIVOT: ClassVar[COMPONENTS] = ...
        ROTATE: ClassVar[COMPONENTS] = ...
        SCALE: ClassVar[COMPONENTS] = ...
        SHEAR: ClassVar[COMPONENTS] = ...
        TRANSLATE: ClassVar[COMPONENTS] = ...
        _member_map_: ClassVar[collections.OrderedDict] = ...
        _member_names_: ClassVar[list] = ...
        _member_type_: ClassVar[type[object]] = ...
        _value2member_map_: ClassVar[dict] = ...
        @classmethod
        def __init__(cls, value) -> None: ...
        def _generate_next_value_(self, name, start, count, last_values): ...

    class COORDINATE_SYSTEM(enum.Enum):
        LOCAL: ClassVar[COORDINATE_SYSTEM] = ...
        WINDOW: ClassVar[COORDINATE_SYSTEM] = ...
        WORLD: ClassVar[COORDINATE_SYSTEM] = ...
        _member_map_: ClassVar[collections.OrderedDict] = ...
        _member_names_: ClassVar[list] = ...
        _member_type_: ClassVar[type[object]] = ...
        _value2member_map_: ClassVar[dict] = ...
        @classmethod
        def __init__(cls, value) -> None: ...
        def _generate_next_value_(self, name, start, count, last_values): ...

    class PICK(enum.Enum):
        NONE: ClassVar[PICK] = ...
        PIVOT: ClassVar[PICK] = ...
        ROTATE: ClassVar[PICK] = ...
        SCALE_X: ClassVar[PICK] = ...
        SCALE_XY: ClassVar[PICK] = ...
        SCALE_Y: ClassVar[PICK] = ...
        SHEAR_X: ClassVar[PICK] = ...
        SHEAR_Y: ClassVar[PICK] = ...
        TRANSLATE_X: ClassVar[PICK] = ...
        TRANSLATE_XY: ClassVar[PICK] = ...
        TRANSLATE_Y: ClassVar[PICK] = ...
        _member_map_: ClassVar[collections.OrderedDict] = ...
        _member_names_: ClassVar[list] = ...
        _member_type_: ClassVar[type[object]] = ...
        _value2member_map_: ClassVar[dict] = ...
        @classmethod
        def __init__(cls, value) -> None: ...
        def _generate_next_value_(self, name, start, count, last_values): ...

    class _TransformManipulatorLayer__Suppressor:
        def __init__(self, layer) -> None: ...
        def __enter__(self): ...
        def __exit__(self, excType, excValue, tb): ...
    _TransformManipulatorLayer__HANDLE_LINEWIDTH: ClassVar[float] = ...
    _TransformManipulatorLayer__HANDLE_SIZE: ClassVar[float] = ...
    _TransformManipulatorLayer__LINEWIDTH: ClassVar[float] = ...
    _TransformManipulatorLayer__PICK_AREA_SIZE: ClassVar[int] = ...
    _TransformManipulatorLayer__SELECT_BUF_SIZE: ClassVar[int] = ...
    transformChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, name: Incomplete | None = ..., visible: bool = ..., interactive: bool = ..., enabled: bool = ...) -> None: ...
    def _TransformManipulatorLayer__drawManipulator(self, p, pick: bool = ..., shadow: bool = ...): ...
    def _TransformManipulatorLayer__emitTransformChanged(self, changeInfoDict): ...
    def _TransformManipulatorLayer__getEventProcessorForPick(self, pick): ...
    def _TransformManipulatorLayer__getWorldPointOnLocalAxisAtAngle(self, rotateAngleDegrees): ...
    def _TransformManipulatorLayer__paintManipulator(self, pick: bool = ...): ...
    def _TransformManipulatorLayer__pickManipulator(self, windowMousePos, modifiers): ...
    def _clearMatrix(self): ...
    def _getComponentMatrix(self, component, toPivot, fromPivot): ...
    def _processEvent(self, event): ...
    def getMatrix(self, applyScale: bool = ..., applyShear: bool = ..., splitAroundTranslate: bool = ...): ...
    def getOrder(self): ...
    def getPivot(self): ...
    def getRotation(self): ...
    def getScale(self): ...
    def getScaleMultiplier(self): ...
    def getShear(self): ...
    def getShearAddition(self): ...
    def getSignalSuppressor(self): ...
    def getTranslation(self): ...
    def isChanged(self): ...
    def isLocked(self, component): ...
    def makeIdentity(self): ...
    def mapFromLocal(self, point, sys, applyScale: bool = ..., applyShear: bool = ...): ...
    def mapToLocal(self, point, sys, applyScale: bool = ..., applyShear: bool = ...): ...
    def paintGL(self): ...
    def processEvent(self, event): ...
    def processorFinished(self): ...
    def processorStarted(self, name): ...
    def setLocked(self, component, isLocked): ...
    def setOrder(self, transformOrderTuple): ...
    def setPivot(self, pivot, emit: bool = ..., final: bool = ...): ...
    def setRotation(self, degrees, emit: bool = ..., final: bool = ...): ...
    def setScale(self, scale, emit: bool = ..., final: bool = ...): ...
    def setScaleMultiplier(self, sm): ...
    def setShear(self, shear, emit: bool = ..., final: bool = ...): ...
    def setShearAddition(self, xm): ...
    def setTranslation(self, translation: tuple, emit: bool = ..., final: bool = ...): ...
    def start(self, pick, event): ...
    def suppressSignals(self, v): ...

class TranslateEventProcessor(TransformEventProcessor):
    _NAME: ClassVar[str] = ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...
