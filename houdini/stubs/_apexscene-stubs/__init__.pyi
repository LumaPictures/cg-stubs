from collections.abc import Iterable, Iterator, Sequence
from typing import Any, ClassVar, Generic, Literal, Never, TypeVar, overload, type_check_only

import _apex
import hou
from apex.control_2 import ControlMapping, ControlTransformData
import typing

_T = TypeVar("_T")
_V = TypeVar("_V")
import _apex
from _typeshed import Incomplete
from typing import Any, ClassVar, Iterator, overload

class AbstractControl(Control):
    lock_range: bool
    parm_data: _apex.Dict
    show_x: bool
    show_y: bool
    spare_promoted: list[tuple[str, Never]]
    use_x_max_lock: bool
    use_x_min_lock: bool
    use_y_max_lock: bool
    use_y_min_lock: bool
    x_max: float
    x_max_lock: float
    x_min: float
    x_min_lock: float
    x_parm: str | None
    y_max: float
    y_max_lock: float
    y_min: float
    y_min_lock: float
    y_parm: str | None
    def __init__(self, scene: Scene, path: str, rig_path: str, nodeid: int = ...) -> None:
        """__init__(self: _apexscene.AbstractControl, scene: pyapex::PYAPEX_SceneHandle, path: APEX_Path, rig_path: APEX_Path, nodeid: APEX_NodeID = -1) -> None"""

class AnimLayer:
    def __init__(self) -> None:
        """__init__(self: _apexscene.AnimLayer) -> None"""
    @staticmethod
    def buildLayerDataGeometry(geo: hou.Geometry, additive: bool = ..., muted: bool = ..., locked: bool = ..., soloed: bool = ..., child_layers: Sequence[str] = ..., color: hou.Color | None = ..., guid: str = ...) -> None:
        """buildLayerDataGeometry(geo: object, additive: bool = True, muted: bool = False, locked: bool = False, soloed: bool = False, child_layers: UT_Array[str] = [], color: object = None, guid: str = '') -> None"""
    def color(self) -> hou.Color:
        """color(self: _apexscene.AnimLayer) -> object"""
    def destroyWeightKeyframe(self, scene: Scene, frame: float) -> None:
        """destroyWeightKeyframe(self: _apexscene.AnimLayer, scene: _apexscene.Scene, frame: float) -> None"""
    def getLayeredDataPath(self, arg0: str, arg1: str) -> str:
        """getLayeredDataPath(self: _apexscene.AnimLayer, arg0: str, arg1: str) -> str"""
    def insertWeightKeyframe(self, scene: Scene, frame: float) -> None:
        """insertWeightKeyframe(self: _apexscene.AnimLayer, scene: _apexscene.Scene, frame: float) -> None"""
    def isAdditive(self) -> bool:
        """isAdditive(self: _apexscene.AnimLayer) -> bool"""
    def isBaseLayer(self) -> bool:
        """isBaseLayer(self: _apexscene.AnimLayer) -> bool"""
    def isInherited(self) -> bool:
        """isInherited(self: _apexscene.AnimLayer) -> bool"""
    def isLocked(self) -> bool:
        """isLocked(self: _apexscene.AnimLayer) -> bool"""
    def isMuted(self) -> bool:
        """isMuted(self: _apexscene.AnimLayer) -> bool"""
    def isSoloed(self) -> bool:
        """isSoloed(self: _apexscene.AnimLayer) -> bool"""
    def lock(self) -> None:
        """lock(self: _apexscene.AnimLayer) -> None"""
    def mute(self) -> None:
        """mute(self: _apexscene.AnimLayer) -> None"""
    def resetWeightToDefault(self, scene: Scene, frame: float) -> None:
        """resetWeightToDefault(self: _apexscene.AnimLayer, scene: _apexscene.Scene, frame: float) -> None"""
    def setAdditive(self, arg0: bool) -> None:
        """setAdditive(self: _apexscene.AnimLayer, arg0: bool) -> None"""
    def setChildren(self, arg0: Sequence[str]) -> None:
        """setChildren(self: _apexscene.AnimLayer, arg0: UT_Array[str]) -> None"""
    def setColor(self, arg0: hou.Color) -> None:
        """setColor(self: _apexscene.AnimLayer, arg0: object) -> None"""
    def setDirty(self, arg0: bool) -> None:
        """setDirty(self: _apexscene.AnimLayer, arg0: bool) -> None"""
    def setWeight(self, scene: Scene, value: float, frame: float, force_key: bool = ...) -> None:
        """setWeight(self: _apexscene.AnimLayer, scene: _apexscene.Scene, value: float, frame: float, force_key: bool = False) -> None"""
    def solo(self) -> None:
        """solo(self: _apexscene.AnimLayer) -> None"""
    def unlock(self) -> None:
        """unlock(self: _apexscene.AnimLayer) -> None"""
    def unmute(self) -> None:
        """unmute(self: _apexscene.AnimLayer) -> None"""
    def unsolo(self) -> None:
        """unsolo(self: _apexscene.AnimLayer) -> None"""
    def weight(self, scene: Scene, frame: float) -> float:
        """weight(self: _apexscene.AnimLayer, scene: _apexscene.Scene, frame: float) -> float"""
    @property
    def children(self) -> list[str]: ...
    @property
    def folder_path(self) -> str: ...
    @property
    def geo_path(self) -> str: ...
    @property
    def name(self) -> str: ...

class ChannelMergeMode:
    __members__: ClassVar[dict[str, ChannelMergeMode]] = ...  # read-only
    Blend: ClassVar[ChannelMergeMode] = ...
    Insert: ClassVar[ChannelMergeMode] = ...
    Replace: ClassVar[ChannelMergeMode] = ...
    __entries: ClassVar[dict[str, tuple[ChannelMergeMode, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _apexscene.ChannelMergeMode, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _apexscene.ChannelMergeMode) -> int"""
    def __int__(self) -> int:
        """__int__(self: _apexscene.ChannelMergeMode) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ChannelPrimBindings:
    def __init__(self, rig_path: str, geo_path: str, src_pattern: str = ..., dst_pattern: str = ...) -> None:
        """__init__(self: _apexscene.ChannelPrimBindings, rig_path: str, geo_path: str, src_pattern: str = '*', dst_pattern: str = '*') -> None"""
    def activeLayerGeoPath(self, arg0: Scene) -> str:
        """activeLayerGeoPath(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene) -> str"""
    @overload
    def bakeToGeometry(self, scene: Scene, geo: hou.Geometry, start_layer: str = ..., end_layer: str = ..., pattern: str = ...) -> bool:
        """bakeToGeometry(*args, **kwargs)
        Overloaded function.

        1. bakeToGeometry(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, geo: object, start_layer: str = 'BaseAnimation', end_layer: str = '', pattern: str = '*') -> bool

        2. bakeToGeometry(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, geo: object, start_frame: float, end_frame: float, sample_rate: float = 1.0, start_layer: str = 'BaseAnimation', end_layer: str = '', pattern: str = '*') -> bool
        """
    @overload
    def bakeToGeometry(self, scene: Scene, geo: hou.Geometry, start_frame: float, end_frame: float, sample_rate: float = ..., start_layer: str = ..., end_layer: str = ..., pattern: str = ...) -> bool:
        """bakeToGeometry(*args, **kwargs)
        Overloaded function.

        1. bakeToGeometry(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, geo: object, start_layer: str = 'BaseAnimation', end_layer: str = '', pattern: str = '*') -> bool

        2. bakeToGeometry(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, geo: object, start_frame: float, end_frame: float, sample_rate: float = 1.0, start_layer: str = 'BaseAnimation', end_layer: str = '', pattern: str = '*') -> bool
        """
    def channelCollectionName(self) -> str:
        """channelCollectionName(self: _apexscene.ChannelPrimBindings) -> str"""
    def channelHasKeyAtFrame(self, arg0: Scene, arg1: str, arg2: float) -> bool:
        """channelHasKeyAtFrame(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: str, arg2: float) -> bool"""
    def channelHasKeyframes(self, arg0: Scene, arg1: str) -> bool:
        """channelHasKeyframes(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: str) -> bool"""
    def channelIsPending(self, arg0: Scene, arg1: str) -> bool:
        """channelIsPending(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: str) -> bool"""
    def clearChannels(self, scene: Scene, pattern: str = ..., layer: str = ..., component_indices: Sequence[int] | None = ..., time: float | None = ...) -> None:
        """clearChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, pattern: str = '*', layer: str = 'BaseAnimation', component_indices: Optional[list[int]] = None, time: Optional[float] = None) -> None"""
    def clearPending(self, scene: Scene, pattern: str = ...) -> None:
        """clearPending(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, pattern: str = None) -> None"""
    def computeKeysFromDict(self, scene: Scene, parms: _apex.Dict, frame: float) -> _apex.Dict:
        """computeKeysFromDict(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parms: _apex.Dict, frame: float) -> _apex.Dict"""
    def constructLayer(self, arg0: Scene, arg1: str) -> str:
        """constructLayer(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: str) -> str"""
    def createNewChannels(self, scene: Scene, py_channel_prims: hou.Geometry, parmtype: str, parmname: str, layer: str = ...) -> None:
        """createNewChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, py_channel_prims: object, parmtype: str, parmname: str, layer: str = 'BaseAnimation') -> None"""
    @overload
    def deleteChannels(self, scene: Scene, parmname: str, layer: str = ...) -> None:
        """deleteChannels(*args, **kwargs)
        Overloaded function.

        1. deleteChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parmname: str, layer: str = 'BaseAnimation') -> None

        2. deleteChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parms: list[str], layer: str = 'BaseAnimation') -> None
        """
    @overload
    def deleteChannels(self, scene: Scene, parms: Sequence[str], layer: str = ...) -> None:
        """deleteChannels(*args, **kwargs)
        Overloaded function.

        1. deleteChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parmname: str, layer: str = 'BaseAnimation') -> None

        2. deleteChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parms: list[str], layer: str = 'BaseAnimation') -> None
        """
    def getChangeCount(self) -> int:
        """getChangeCount(self: _apexscene.ChannelPrimBindings) -> int"""
    def getChannelNamesForParms(self, arg0: Scene, arg1: Sequence[str]) -> dict[str, list[str]]:
        """getChannelNamesForParms(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: list[str]) -> dict[str, list[str]]"""
    def getKeyedTimes(self, scene: Scene, pattern: str = ..., start_layer: str = ..., end_layer: str = ..., ignore_muted: bool = ...) -> list[float]:
        """getKeyedTimes(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, pattern: str = '*', start_layer: str = 'BaseAnimation', end_layer: str = '', ignore_muted: bool = True) -> list[float]"""
    def getKeyedTimesForParm(self, scene: Scene, parm_name: str, start_layer: str = ..., end_layer: str = ..., include_layer_weights: bool = ..., ignore_muted: bool = ...) -> list[float]:
        """getKeyedTimesForParm(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parm_name: str, start_layer: str = 'BaseAnimation', end_layer: str = '', include_layer_weights: bool = True, ignore_muted: bool = True) -> list[float]"""
    def getStaticParms(self, scene: Scene) -> _apex.Dict:
        """getStaticParms(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene) -> _apex.Dict"""
    def getUniqueId(self) -> int:
        """getUniqueId(self: _apexscene.ChannelPrimBindings) -> int"""
    def hasLayer(self, arg0: str) -> bool:
        """hasLayer(self: _apexscene.ChannelPrimBindings, arg0: str) -> bool"""
    def hasParm(self, parmname: str, layer: str = ...) -> bool:
        """hasParm(self: _apexscene.ChannelPrimBindings, parmname: str, layer: str = 'BaseAnimation') -> bool"""
    def incrementChangeCount(self) -> None:
        """incrementChangeCount(self: _apexscene.ChannelPrimBindings) -> None"""
    def isMuted(self) -> bool:
        """isMuted(self: _apexscene.ChannelPrimBindings) -> bool"""
    def keyedFrameRange(self, scene: Scene, layers: Sequence[str] = ...) -> hou.Vector2 | None:
        """keyedFrameRange(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, layers: list[str] = []) -> object"""
    def layerGeoPath(self, arg0: str) -> str:
        """layerGeoPath(self: _apexscene.ChannelPrimBindings, arg0: str) -> str"""
    def mergeChannelPrimitives(self, scene: Scene, py_geo: hou.Geometry, src_start_frame: float, src_end_frame: float, dst_start_frame: float, pattern: str = ..., mode: ChannelMergeMode = ..., blend_p: float = ..., cached_values: _apex.Dict | None = ...) -> None:
        """mergeChannelPrimitives(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, py_geo: object, src_start_frame: float, src_end_frame: float, dst_start_frame: float, pattern: str = '*', mode: _apexscene.ChannelMergeMode = <ChannelMergeMode.Replace: 0>, blend_p: float = 1.0, cached_values: Optional[_apex.Dict] = None) -> None"""
    def mute(self) -> None:
        """mute(self: _apexscene.ChannelPrimBindings) -> None"""
    def parms(self, layer: str = ...) -> list[str]:
        """parms(self: _apexscene.ChannelPrimBindings, layer: str = 'BaseAnimation') -> UT_Array[str]"""
    def removeKeys(self, scene: Scene, frame: float, pattern: str = ..., component_indices: Sequence[int] | None = ..., write_to_muted_layer: bool = ..., layer: str = ...) -> None:
        """removeKeys(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, frame: float, pattern: str = '*', component_indices: Optional[list[int]] = None, write_to_muted_layer: bool = False, layer: str = '') -> None"""
    def renameChannels(self, scene: Scene, name_mapping: dict[str, str], overwrite_existing: bool = ...) -> bool:
        """renameChannels(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, name_mapping: dict[str, str], overwrite_existing: bool = False) -> bool"""
    def renameStaticParms(self, scene: Scene, parm_mapping: dict[str, str], overwrite_existing: bool = ...) -> None:
        """renameStaticParms(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, parm_mapping: dict[str, str], overwrite_existing: bool = False) -> None"""
    def setDefaultFromDict(self, scene: Scene, pattern: str = ..., layer: str = ..., initializing: bool = ...) -> None:
        """setDefaultFromDict(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, pattern: str = '*', layer: str = 'BaseAnimation', initializing: bool = False) -> None"""
    def setDefaultFromValue(self, scene: Scene, value: float, pattern: str = ..., layer: str = ...) -> None:
        """setDefaultFromValue(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, value: float, pattern: str = '*', layer: str = 'BaseAnimation') -> None"""
    def setKeysFromDict(self, scene: Scene, frame: float, add_missing: bool, pattern: str = ..., autokey: bool = ..., autocommit: bool = ..., component_indices: Sequence[int] | None = ..., only_existing: bool = ..., autokey_tuples: bool = ..., force_key: bool = ..., write_to_muted_layer: bool = ..., layer: str = ...) -> None:
        """setKeysFromDict(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, frame: float, add_missing: bool, pattern: str = '*', autokey: bool = True, autocommit: bool = True, component_indices: Optional[list[int]] = None, only_existing: bool = False, autokey_tuples: bool = False, force_key: bool = False, write_to_muted_layer: bool = False, layer: str = '') -> None"""
    def setLayerGeometry(self, arg0: Scene, arg1: str, arg2: hou.Geometry) -> None:
        """setLayerGeometry(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: str, arg2: object) -> None"""
    def setNeedsUpdate(self) -> None:
        """setNeedsUpdate(self: _apexscene.ChannelPrimBindings) -> None"""
    def setStaticParmsFromDict(self, scene: Scene, dict: _apex.Dict) -> None:
        """setStaticParmsFromDict(self: _apexscene.ChannelPrimBindings, scene: _apexscene.Scene, dict: _apex.Dict) -> None"""
    def unmute(self) -> None:
        """unmute(self: _apexscene.ChannelPrimBindings) -> None"""
    def updateFromChannelPrims(self, arg0: Scene, arg1: float) -> None:
        """updateFromChannelPrims(self: _apexscene.ChannelPrimBindings, arg0: _apexscene.Scene, arg1: float) -> None"""
    @property
    def geo_path(self) -> str: ...
    @property
    def rig_path(self) -> str: ...

class Constraint:
    def __init__(self, scene: Scene, graph_path: str, driven: _apex.Dict, drivers: _apex.Dict, name: str = ..., label: str = ...) -> None:
        """__init__(self: _apexscene.Constraint, scene: pyapex::PYAPEX_SceneHandle, graph_path: str, driven: _apex.Dict, drivers: _apex.Dict, name: str = '', label: str = '') -> None"""
    def activeOutputKey(self) -> str:
        """activeOutputKey(self: _apexscene.Constraint) -> str"""
    def addsControls(self) -> bool:
        """addsControls(self: _apexscene.Constraint) -> bool"""
    @staticmethod
    def buildFromDict(scene: Scene, driven_path: str, entry: _apex.Dict, name: str = ...) -> Constraint:
        """buildFromDict(scene: pyapex::PYAPEX_SceneHandle, driven_path: str, entry: _apex.Dict, name: str = '') -> _apexscene.Constraint"""
    def controlColor(self, arg0: int) -> hou.Vector3:
        """controlColor(self: _apexscene.Constraint, arg0: int) -> Vector3"""
    def controlScale(self, arg0: int) -> float:
        """controlScale(self: _apexscene.Constraint, arg0: int) -> float"""
    def controlShape(self, arg0: int) -> str:
        """controlShape(self: _apexscene.Constraint, arg0: int) -> str"""
    def drivenDict(self) -> _apex.Dict:
        """drivenDict(self: _apexscene.Constraint) -> _apex.Dict"""
    def drivenPath(self) -> str:
        """drivenPath(self: _apexscene.Constraint) -> str"""
    def drivenRigPath(self) -> str:
        """drivenRigPath(self: _apexscene.Constraint) -> str"""
    def driverDict(self) -> _apex.Dict:
        """driverDict(self: _apexscene.Constraint) -> _apex.Dict"""
    def enabled(self) -> bool:
        """enabled(self: _apexscene.Constraint) -> bool"""
    def entry(self) -> _apex.Dict:
        """entry(self: _apexscene.Constraint) -> _apex.Dict"""
    def findControl(self, arg0: str) -> int:
        """findControl(self: _apexscene.Constraint, arg0: str) -> int"""
    def getBlend(self, arg0: Scene) -> float:
        """getBlend(self: _apexscene.Constraint, arg0: pyapex::PYAPEX_SceneHandle) -> float"""
    def getControlPaths(self, include_external: bool = ..., include_internal: bool = ...) -> list[str]:
        """getControlPaths(self: _apexscene.Constraint, include_external: bool = True, include_internal: bool = False) -> UT_Array[str]"""
    def hidden(self) -> bool:
        """hidden(self: _apexscene.Constraint) -> bool"""
    def label(self) -> str:
        """label(self: _apexscene.Constraint) -> str"""
    def loadControlShapesFromProperties(self) -> None:
        """loadControlShapesFromProperties(self: _apexscene.Constraint) -> None"""
    def name(self) -> str:
        """name(self: _apexscene.Constraint) -> str"""
    def parameters(self) -> _apex.Dict:
        """parameters(self: _apexscene.Constraint) -> _apex.Dict"""
    def path(self) -> str:
        """path(self: _apexscene.Constraint) -> str"""
    def pinned(self) -> bool:
        """pinned(self: _apexscene.Constraint) -> bool"""
    def properties(self) -> _apex.Dict:
        """properties(self: _apexscene.Constraint) -> _apex.Dict"""
    def rigPath(self) -> str:
        """rigPath(self: _apexscene.Constraint) -> str"""
    def saveControlShapesToProperties(self) -> None:
        """saveControlShapesToProperties(self: _apexscene.Constraint) -> None"""
    def selected(self) -> bool:
        """selected(self: _apexscene.Constraint) -> bool"""
    def setAddsControls(self, arg0: bool) -> None:
        """setAddsControls(self: _apexscene.Constraint, arg0: bool) -> None"""
    def setControlColor(self, arg0: int, arg1: hou.Vector3) -> None:
        """setControlColor(self: _apexscene.Constraint, arg0: int, arg1: Vector3) -> None"""
    def setControlScale(self, arg0: int, arg1: float) -> None:
        """setControlScale(self: _apexscene.Constraint, arg0: int, arg1: float) -> None"""
    def setControlShape(self, arg0: int, arg1: str) -> None:
        """setControlShape(self: _apexscene.Constraint, arg0: int, arg1: str) -> None"""
    def setEnabled(self, arg0: bool) -> None:
        """setEnabled(self: _apexscene.Constraint, arg0: bool) -> None"""
    def setHidden(self, arg0: bool) -> None:
        """setHidden(self: _apexscene.Constraint, arg0: bool) -> None"""
    def setLabel(self, arg0: str) -> None:
        """setLabel(self: _apexscene.Constraint, arg0: str) -> None"""
    def setPinned(self, arg0: bool) -> None:
        """setPinned(self: _apexscene.Constraint, arg0: bool) -> None"""
    def setProperties(self, arg0: _apex.Dict) -> None:
        """setProperties(self: _apexscene.Constraint, arg0: _apex.Dict) -> None"""
    def setSelected(self, arg0: bool) -> None:
        """setSelected(self: _apexscene.Constraint, arg0: bool) -> None"""
    def setVisible(self, arg0: bool) -> None:
        """setVisible(self: _apexscene.Constraint, arg0: bool) -> None"""
    def type(self) -> ConstraintType:
        """type(self: _apexscene.Constraint) -> _apexscene.ConstraintType"""
    def typePath(self) -> str:
        """typePath(self: _apexscene.Constraint) -> str"""
    def updateControlTemplate(self, geo: hou.Geometry) -> None:
        """updateControlTemplate(self: _apexscene.Constraint, geo: object) -> None"""
    def updateParameters(self, arg0: _apex.Dict) -> None:
        """updateParameters(self: _apexscene.Constraint, arg0: _apex.Dict) -> None"""
    def valid(self) -> bool:
        """valid(self: _apexscene.Constraint) -> bool"""
    def visible(self) -> bool:
        """visible(self: _apexscene.Constraint) -> bool"""

class ConstraintManager:
    def __init__(self, arg0: str) -> None:
        """__init__(self: _apexscene.ConstraintManager, arg0: str) -> None"""
    def baseGraph(self) -> _apex.Graph:
        """baseGraph(self: _apexscene.ConstraintManager) -> _apex.Graph"""
    def buildConstraintPath(self, arg0: str) -> str:
        """buildConstraintPath(self: _apexscene.ConstraintManager, arg0: str) -> str"""
    def clear(self) -> None:
        """clear(self: _apexscene.ConstraintManager) -> None"""
    def currentGraphKey(self) -> str:
        """currentGraphKey(self: _apexscene.ConstraintManager) -> str"""
    def folder(self) -> str:
        """folder(self: _apexscene.ConstraintManager) -> str"""
    def getConstraint(self, path: str, active: bool = ...) -> Constraint | None:
        """getConstraint(self: _apexscene.ConstraintManager, path: str, active: bool = False) -> _apexscene.Constraint"""
    def getConstraintForControl(self, ctrl_path: str, active: bool = ..., allow_driven: bool = ...) -> Constraint | None:
        """getConstraintForControl(self: _apexscene.ConstraintManager, ctrl_path: str, active: bool = False, allow_driven: bool = True) -> _apexscene.Constraint"""
    def getConstraints(self, active: bool = ...) -> list[Constraint]:
        """getConstraints(self: _apexscene.ConstraintManager, active: bool = False) -> UT_Array[_apexscene.Constraint]"""
    def getConstraintsDrivingControl(self, ctrl_path: str, active: bool = ...) -> list[Constraint]:
        """getConstraintsDrivingControl(self: _apexscene.ConstraintManager, ctrl_path: str, active: bool = False) -> UT_Array[_apexscene.Constraint]"""
    def getConstraintsDrivingRig(self, rig_path: str, active: bool = ...) -> list[Constraint]:
        """getConstraintsDrivingRig(self: _apexscene.ConstraintManager, rig_path: str, active: bool = False) -> UT_Array[_apexscene.Constraint]"""
    def getDrivingRigs(self, arg0: str) -> list[str]:
        """getDrivingRigs(self: _apexscene.ConstraintManager, arg0: str) -> UT_Array[str]"""
    def graph(self, key: str = ...) -> _apex.Graph:
        """graph(self: _apexscene.ConstraintManager, key: str = '') -> _apex.Graph"""
    def loadConstraint(self, scene: Scene, last: bool = ...) -> None:
        """loadConstraint(self: _apexscene.ConstraintManager, scene: pyapex::PYAPEX_SceneHandle, last: bool = True) -> None"""
    def loadConstraintParms(self, arg0: Scene) -> None:
        """loadConstraintParms(self: _apexscene.ConstraintManager, arg0: pyapex::PYAPEX_SceneHandle) -> None"""
    def loadFromDict(self, arg0: Scene, arg1: _apex.Dict) -> None:
        """loadFromDict(self: _apexscene.ConstraintManager, arg0: pyapex::PYAPEX_SceneHandle, arg1: _apex.Dict) -> None"""
    def loadFromGeometry(self, scene: Scene, geo: hou.Geometry) -> bool:
        """loadFromGeometry(self: _apexscene.ConstraintManager, scene: pyapex::PYAPEX_SceneHandle, geo: object) -> bool"""
    def path(self) -> str:
        """path(self: _apexscene.ConstraintManager) -> str"""
    def popConstraint(self, arg0: str) -> Constraint | None:
        """popConstraint(self: _apexscene.ConstraintManager, arg0: str) -> _apexscene.Constraint"""
    def pushConstraint(self, constraint: Constraint, force_unique: bool = ...) -> None:
        """pushConstraint(self: _apexscene.ConstraintManager, constraint: _apexscene.Constraint, force_unique: bool = False) -> None"""
    def saveToGeometry(self, geo: hou.Geometry) -> None:
        """saveToGeometry(self: _apexscene.ConstraintManager, geo: object) -> None"""
    def size(self) -> int:
        """size(self: _apexscene.ConstraintManager) -> int"""

class ConstraintType:
    def __init__(self, arg0: _apex.Graph) -> None:
        """__init__(self: _apexscene.ConstraintType, arg0: _apex.Graph) -> None"""
    def bindings(self) -> _apex.Dict:
        """bindings(self: _apexscene.ConstraintType) -> _apex.Dict"""
    def controlGraph(self) -> _apex.Graph:
        """controlGraph(self: _apexscene.ConstraintType) -> _apex.Graph"""
    def controlNames(self) -> list[str]:
        """controlNames(self: _apexscene.ConstraintType) -> UT_Array[str]"""
    def controlParms(self) -> list[str]:
        """controlParms(self: _apexscene.ConstraintType) -> UT_Array[str]"""
    def externalControlNames(self) -> list[str]:
        """externalControlNames(self: _apexscene.ConstraintType) -> UT_Array[str]"""
    def graph(self) -> _apex.Graph:
        """graph(self: _apexscene.ConstraintType) -> _apex.Graph"""
    def hasActiveOutput(self) -> bool:
        """hasActiveOutput(self: _apexscene.ConstraintType) -> bool"""
    def internalControlNames(self) -> list[str]:
        """internalControlNames(self: _apexscene.ConstraintType) -> UT_Array[str]"""
    def outputBindings(self) -> _apex.Dict:
        """outputBindings(self: _apexscene.ConstraintType) -> _apex.Dict"""

class Control:
    animatable: bool
    data_path: str
    enable: bool
    group_name: str | None
    internal: bool
    joint: str
    name: str
    node_parms: _apex.Dict
    node_properties: _apex.Dict
    parent_path: str
    path: str
    rig_path: str
    type_alias: str | None
    type_name: str
    def __init__(self, scene: Scene, path: str, rig_path: str) -> None:
        """__init__(self: _apexscene.Control, scene: pyapex::PYAPEX_SceneHandle, path: APEX_Path, rig_path: APEX_Path) -> None"""
    def getGroupPath(self) -> str:
        """getGroupPath(self: _apexscene.Control) -> APEX_Path"""
    def getPromotedParms(self, channels: bool = ...) -> list[str]:
        """getPromotedParms(self: _apexscene.Control, channels: bool = False) -> UT_Array[str]"""
    def hasGroup(self) -> bool:
        """hasGroup(self: _apexscene.Control) -> bool"""
    def isGroupPrimary(self) -> bool:
        """isGroupPrimary(self: _apexscene.Control) -> bool"""

class ControlDataMap:
    def __init__(self) -> None:
        """__init__(self: _apexscene.ControlDataMap) -> None"""
    def items(self) -> ItemsView[_apex.Dict]:
        """items(self: _apexscene.ControlDataMap) -> _apexscene.ItemsView"""
    def keys(self) -> KeysView:
        """keys(self: _apexscene.ControlDataMap) -> _apexscene.KeysView"""
    def values(self) -> ValuesView[_apex.Dict]:
        """values(self: _apexscene.ControlDataMap) -> _apexscene.ValuesView"""
    def __bool__(self) -> bool:
        """__bool__(self: _apexscene.ControlDataMap) -> bool

        Check whether the map is nonempty
        """
    @overload
    def __contains__(self, other: str) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apexscene.ControlDataMap, arg0: str) -> bool

        2. __contains__(self: _apexscene.ControlDataMap, arg0: object) -> bool
        """
    @overload
    def __contains__(self, other: object) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apexscene.ControlDataMap, arg0: str) -> bool

        2. __contains__(self: _apexscene.ControlDataMap, arg0: object) -> bool
        """
    def __delitem__(self, other: str) -> None:
        """__delitem__(self: _apexscene.ControlDataMap, arg0: str) -> None"""
    def __getitem__(self, index: str) -> _apex.Dict:
        """__getitem__(self: _apexscene.ControlDataMap, arg0: str) -> _apex.Dict"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apexscene.ControlDataMap) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(self: _apexscene.ControlDataMap) -> int"""
    def __setitem__(self, index: str, object: _apex.Dict) -> None:
        """__setitem__(self: _apexscene.ControlDataMap, arg0: str, arg1: _apex.Dict) -> None"""

class ControlGroup:
    animatable: bool
    member_parms: _apex.Dict
    name: str
    node_parms: _apex.Dict
    node_properties: _apex.Dict
    parm_order: list[str]
    path: str
    primary: str | None
    rig_path: str
    visibility_mode: int
    def __init__(self, scene: Scene, path: str, rig_path: str) -> None:
        """__init__(self: _apexscene.ControlGroup, scene: pyapex::PYAPEX_SceneHandle, path: APEX_Path, rig_path: APEX_Path) -> None"""
    def getMembers(self, inclusive: bool = ...) -> list[str]:
        """getMembers(self: _apexscene.ControlGroup, inclusive: bool = True) -> UT_Array[str]"""
    def isMember(self, arg0: str) -> bool:
        """isMember(self: _apexscene.ControlGroup, arg0: str) -> bool"""

class ControlManager:
    _control_data: ControlDataMap
    controlGroups: dict[str, ControlGroup]
    controls: ControlMap
    def __init__(self) -> None:
        """__init__(self: _apexscene.ControlManager) -> None"""
    def addAbstractControl(self, arg0: Scene, arg1: str) -> None:
        """addAbstractControl(self: _apexscene.ControlManager, arg0: pyapex::PYAPEX_SceneHandle, arg1: APEX_Path) -> None"""
    def addControl(self, arg0: Scene, arg1: str) -> None:
        """addControl(self: _apexscene.ControlManager, arg0: pyapex::PYAPEX_SceneHandle, arg1: APEX_Path) -> None"""
    def addControlsFromRig(self, arg0: Scene, arg1: str) -> None:
        """addControlsFromRig(self: _apexscene.ControlManager, arg0: pyapex::PYAPEX_SceneHandle, arg1: APEX_Path) -> None"""
    def clear(self) -> None:
        """clear(self: _apexscene.ControlManager) -> None"""
    def controlPaths(self) -> list[str]:
        """controlPaths(self: _apexscene.ControlManager) -> UT_Array[str]"""
    def removeControl(self, arg0: str) -> None:
        """removeControl(self: _apexscene.ControlManager, arg0: APEX_Path) -> None"""
    def removeRig(self, arg0: str) -> None:
        """removeRig(self: _apexscene.ControlManager, arg0: APEX_Path) -> None"""
    # The rest are added by apex.control_2.ControlManagerExtension.
    @overload
    def getControls(self, ordered: Literal[True]) -> list[Control]: ...
    @overload
    def getControls(self, ordered: Literal[False] = False) -> ValuesView[Control]: ...
    @overload
    def getControls(self, ordered: bool = False) -> list[Control] | ValuesView[Control]: ...
    def findControls(self, pattern: str) -> list[Control]: ...
    def generatePattern(self, rig_path: str) -> str: ...
    def update(self, scene: Scene, pattern: str | None = None, use_minimal_pattern: bool = False) -> None: ...
    def updateEnabledControls(self, scene: Scene) -> None: ...
    def getTempControl(self, scene: Scene, ctrl_path: str, rig_path: str) -> Control: ...
    def getControlXform(self, ctrl_path: str) -> hou.Matrix4: ...
    def getControlData(self, ctrl_path: str) -> ControlTransformData: ...
    def _getControlProperties(self, ctrl_path: str) -> _apex.Dict: ...
    def getControlGadgetData(self, ctrl_path: str) -> _apex.Dict: ...
    def getControlGadgetType(self, ctrl_path: str) -> str | None: ...
    def getScrollData(
        self, ctrl_path: str
    ) -> tuple[str, float | int | bool, Literal["Float", "Bool", "Int"], bool] | tuple[None, None, None, None]: ...
    def getParmLimit(self, ctrl_path: str, parm: str, min: bool = True, use_soft_lock: bool = True) -> float | hou.Vector3 | None: ...
    def getControlMapping(self, ctrl_path: str, include_groups: bool = False) -> ControlMapping: ...
    def getRotateParms(self) -> dict[str, list[str]]: ...
    @overload
    def controlsByProperty(
        self, ctrl_path: str, trigger_type: str = "trigger:selection:names", descendants: Literal[False] = False
    ) -> _apex.StringArray | None: ...
    @overload
    def controlsByProperty(
        self, ctrl_path: str, trigger_type: str = "trigger:selection:names", descendants: bool = False
    ) -> _apex.StringArray | list[str] | None: ...
    def controlMapByProperty(self, ctrl_path: str, trigger_type: str = "snap:enddrag") -> dict[str, str]: ...
    def hasProperty(self, ctrl_path: str, property_name: str = "trigger:selection:names") -> bool: ...
    def getProperty(
        self, ctrl_path: str, property_name: str = "trigger:selection:names", default: _T | None = None
    ) -> _apex._Value | _T | None: ...
    def isSelectable(self, ctrl_path: str) -> bool: ...
    def showHandle(self, ctrl_path: str) -> bool: ...
    def isOrbit(self, ctrl_path: str) -> bool: ...
    def externalRigParms(self, ctrl_path: str) -> _apex._Value | None: ...
    def getPropertiesScriptCallback(self, ctrl_path: str, event_type: str = "selection") -> str | None: ...
    def controlGroupData(self, control_paths: Iterable[str] | None = None) -> tuple[list[str], list[str], list[str]]: ...
    def getGroup(self, ctrl_path: str) -> ControlGroup | None: ...
    def getGroupPrimary(self, ctrl_path: str) -> str | None: ...
    def containsGroup(self, ctrl_paths: Iterable[str]) -> bool: ...
    def isGroupPath(self, ctrl_path: str) -> bool: ...

class ControlMap:
    def __init__(self) -> None:
        """__init__(self: _apexscene.ControlMap) -> None"""
    def get(self, arg0: str | None, arg1: Control | None) -> Control | None:
        """get(self: _apexscene.ControlMap, arg0: Optional[str], arg1: Optional[APEXA_Control]) -> Optional[APEXA_Control]"""
    def items(self) -> ItemsView[Control]:
        """items(self: _apexscene.ControlMap) -> _apexscene.ItemsView"""
    def keys(self) -> KeysView:
        """keys(self: _apexscene.ControlMap) -> _apexscene.KeysView"""
    def values(self) -> ValuesView[Control]:
        """values(self: _apexscene.ControlMap) -> _apexscene.ValuesView"""
    def __bool__(self) -> bool:
        """__bool__(self: _apexscene.ControlMap) -> bool

        Check whether the map is nonempty
        """
    @overload
    def __contains__(self, other: str) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apexscene.ControlMap, arg0: str) -> bool

        2. __contains__(self: _apexscene.ControlMap, arg0: object) -> bool
        """
    @overload
    def __contains__(self, other: object) -> bool:
        """__contains__(*args, **kwargs)
        Overloaded function.

        1. __contains__(self: _apexscene.ControlMap, arg0: str) -> bool

        2. __contains__(self: _apexscene.ControlMap, arg0: object) -> bool
        """
    def __delitem__(self, other: str) -> None:
        """__delitem__(self: _apexscene.ControlMap, arg0: str) -> None"""
    def __getitem__(self, index: str) -> Control:
        """__getitem__(self: _apexscene.ControlMap, arg0: str) -> APEXA_Control"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apexscene.ControlMap) -> Iterator[str]"""
    def __len__(self) -> int:
        """__len__(*args, **kwargs)
        Overloaded function.

        1. __len__(self: _apexscene.ControlMap) -> int

        2. __len__(self: _apexscene.ControlMap) -> int
        """
    def __setitem__(self, index: str, object: Control) -> None:
        """__setitem__(self: _apexscene.ControlMap, arg0: str, arg1: APEXA_Control) -> None"""

class InputGeometries:
    def __init__(self) -> None:
        """__init__(self: _apexscene.InputGeometries) -> None"""
    def loadFromPackedHierarchy(self, geo: hou.Geometry, pattern: str = ...) -> None:
        """loadFromPackedHierarchy(self: _apexscene.InputGeometries, geo: object, pattern: str = '*') -> None"""
    def setGeometry(self, path: str, geo: hou.Geometry) -> None:
        """setGeometry(self: _apexscene.InputGeometries, path: str, geo: object) -> None"""
    @property
    def folder_properties(self) -> _apex.Dict: ...
    @property
    def geos(self) -> _apex.Dict: ...

class ItemsView(Generic[_V]):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> Iterator[tuple[str, _V]]:
        """__iter__(self: _apexscene.ItemsView) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _apexscene.ItemsView) -> int"""

class KeysView:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __contains__(self, other: object) -> bool:
        """__contains__(self: _apexscene.KeysView, arg0: object) -> bool"""
    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _apexscene.KeysView) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _apexscene.KeysView) -> int"""

class MultiControl:
    def __init__(self, arg0: str) -> None:
        """__init__(self: _apexscene.MultiControl, arg0: str) -> None"""
    def controlsVisible(self) -> bool:
        """controlsVisible(self: _apexscene.MultiControl) -> bool"""
    def isVisible(self) -> bool:
        """isVisible(self: _apexscene.MultiControl) -> bool"""
    def show(self, arg0: bool) -> None:
        """show(self: _apexscene.MultiControl, arg0: bool) -> None"""
    def showControls(self, arg0: bool) -> None:
        """showControls(self: _apexscene.MultiControl, arg0: bool) -> None"""
    @property
    def name(self) -> str: ...

class Scene:
    def __init__(self, enable_sop_geo: bool = ...) -> None:
        """__init__(self: _apexscene.Scene, enable_sop_geo: bool = True) -> None"""
    def activeLayer(self) -> AnimLayer | None:
        """activeLayer(self: _apexscene.Scene) -> APEXA_AnimLayer"""
    def addAnimationCachingBlocker(self) -> None:
        """addAnimationCachingBlocker(self: _apexscene.Scene) -> None"""
    def addChannelPrimBinding(self, data_path: str = ..., animation_geo: hou.Geometry | None = ..., rig_path: str = ...) -> tuple[str, str]:
        """addChannelPrimBinding(self: _apexscene.Scene, data_path: str = '/animation/default.clip/anim', animation_geo: object = None, rig_path: str = '') -> tuple[str, str]"""
    def addConstraint(self, arg0: str) -> None:
        """addConstraint(self: _apexscene.Scene, arg0: str) -> None"""
    def addControlGraphForRig(self, arg0: str) -> None:
        """addControlGraphForRig(self: _apexscene.Scene, arg0: str) -> None"""
    def addControls(self, controls: Sequence[Control], primary_control: str = ...) -> None:
        """addControls(self: _apexscene.Scene, controls: list[_apexscene.Control], primary_control: str = None) -> None"""
    def addLayer(self, name: str, parent: str = ..., additive: bool = ..., activate: bool = ..., index: int = ...) -> str:
        """addLayer(self: _apexscene.Scene, name: str, parent: str = 'BaseAnimation', additive: bool = False, activate: bool = True, index: int = -1) -> str"""
    def addRigToEvaluation(self, path: str) -> None:
        """addRigToEvaluation(self: _apexscene.Scene, path: str) -> None"""
    def changeCount(self) -> int:
        """changeCount(self: _apexscene.Scene) -> int"""
    def clearAnimationCachingBlockers(self) -> None:
        """clearAnimationCachingBlockers(self: _apexscene.Scene) -> None"""
    def clearControls(self) -> None:
        """clearControls(self: _apexscene.Scene) -> None"""
    def createAnimBinding(self, arg0: str) -> tuple[str, str]:
        """createAnimBinding(self: _apexscene.Scene, arg0: str) -> tuple[str, str]"""
    def dataPaths(self) -> list[str]:
        """dataPaths(self: _apexscene.Scene) -> UT_Array[str]"""
    def deleteLayer(self, layer: str) -> bool:
        """deleteLayer(self: _apexscene.Scene, layer: str) -> bool"""
    def enableAnimation(self, arg0: bool) -> None:
        """enableAnimation(self: _apexscene.Scene, arg0: bool) -> None"""
    def enableParallelEvaluation(self, on: bool) -> None:
        """enableParallelEvaluation(self: _apexscene.Scene, on: bool) -> None"""
    def evaluateTrackedRigData(self) -> None:
        """evaluateTrackedRigData(self: _apexscene.Scene) -> None"""
    def findDataPaths(self, pattern: str) -> list[str]:
        """findDataPaths(self: _apexscene.Scene, pattern: str) -> UT_Array[str]"""
    def flattenedLayers(self, only_evaluated: bool = ...) -> list[AnimLayer]:
        """flattenedLayers(self: _apexscene.Scene, only_evaluated: bool = False) -> UT_Array[APEXA_AnimLayer]"""
    def forkInheritedLayers(self, layers: Sequence[str]) -> bool:
        """forkInheritedLayers(self: _apexscene.Scene, layers: UT_Array[str]) -> bool"""
    def geometryFolderProperties(self, arg0: str) -> _apex.Dict:
        """geometryFolderProperties(self: _apexscene.Scene, arg0: APEX_Path) -> _apex.Dict"""
    def getActiveClipPath(self) -> str:
        """getActiveClipPath(self: _apexscene.Scene) -> str"""
    def getConstraintDataPath(self, folder: str = ..., layer: str | None = ...) -> str:
        """getConstraintDataPath(self: _apexscene.Scene, folder: str = '', layer: Optional[str] = None) -> str"""
    def getConstraintGraph(self, path: str) -> _apex.Graph:
        """getConstraintGraph(self: _apexscene.Scene, path: str) -> _apex.Graph"""
    def getConstraintRigPath(self, rig_path: str, folder: str = ...) -> str:
        """getConstraintRigPath(self: _apexscene.Scene, rig_path: str, folder: str = '') -> str"""
    def getConstraintType(self, graph_path: str) -> ConstraintType:
        """getConstraintType(self: _apexscene.Scene, graph_path: str) -> _apexscene.ConstraintType"""
    def getData(self, arg0: str) -> Any:
        """getData(self: _apexscene.Scene, arg0: object) -> object"""
    def getEnableSopGeometries(self) -> bool:
        """getEnableSopGeometries(self: _apexscene.Scene) -> bool"""
    def getGraphOutputData(self, path: str, key: str | None = ..., pattern: str | None = ...) -> _apex._Value | None:
        """getGraphOutputData(self: _apexscene.Scene, path: str, key: Optional[str] = None, pattern: Optional[str] = None) -> object"""
    def getSaveInheritedLayers(self) -> bool:
        """getSaveInheritedLayers(self: _apexscene.Scene) -> bool"""
    def getTransientDataPath(self, type_name: str, folder: str = ..., layer: str | None = ...) -> str:
        """getTransientDataPath(self: _apexscene.Scene, type_name: str, folder: str = '', layer: Optional[str] = None) -> str"""
    def haltAnimationCaching(self) -> None:
        """haltAnimationCaching(self: _apexscene.Scene) -> None"""
    def hasSopGeometries(self) -> bool:
        """hasSopGeometries(self: _apexscene.Scene) -> bool"""
    def incrementChangeCount(self) -> None:
        """incrementChangeCount(self: _apexscene.Scene) -> None"""
    def initializeAnimStack(self, default_clip_path: str = ...) -> None:
        """initializeAnimStack(self: _apexscene.Scene, default_clip_path: str = '/animation/default.clip') -> None"""
    def isConstraintEnabled(self, path: str) -> bool:
        """isConstraintEnabled(self: _apexscene.Scene, path: str) -> bool"""
    @staticmethod
    def isGeometryLoadable(arg0: hou.Geometry) -> bool:
        """isGeometryLoadable(arg0: object) -> bool"""
    def isLayerEditable(self, name: str) -> bool:
        """isLayerEditable(self: _apexscene.Scene, name: str) -> bool"""
    def layer(self, name: str) -> AnimLayer | None:
        """layer(self: _apexscene.Scene, name: str) -> APEXA_AnimLayer"""
    def layerControlPaths(self, name: str) -> dict[str, list[str]]:
        """layerControlPaths(self: _apexscene.Scene, name: str) -> dict[str, UT_Array[str]]"""
    def layerIndex(self, name: str) -> int:
        """layerIndex(self: _apexscene.Scene, name: str) -> int"""
    def layerParent(self, name: str) -> str:
        """layerParent(self: _apexscene.Scene, name: str) -> str"""
    def layers(self) -> dict[str, AnimLayer]:
        """layers(self: _apexscene.Scene) -> dict[str, APEXA_AnimLayer]"""
    def loadCharacterFromGeometry(self, character_name: str, geo: hou.Geometry, folder_properties: _apex.Dict = ...) -> None:
        """loadCharacterFromGeometry(self: _apexscene.Scene, character_name: str, geo: object, folder_properties: _apex.Dict = <apex.Dict {}>) -> None"""
    def loadDataFromGeometry(self, geo: hou.Geometry, data_path: str) -> None:
        """loadDataFromGeometry(self: _apexscene.Scene, geo: object, data_path: str) -> None"""
    def loadFromGeometry(self, arg0: hou.Geometry) -> None:
        """loadFromGeometry(self: _apexscene.Scene, arg0: object) -> None"""
    def loadRigGraph(self, path: str, scene_graph: SceneGraph) -> None:
        """loadRigGraph(self: _apexscene.Scene, path: str, scene_graph: _apexscene.SceneGraph) -> None"""
    def moveLayers(self, source_parent: str, source_layers: Sequence[int], destination_parent: str, destination_index: int) -> bool:
        """moveLayers(self: _apexscene.Scene, source_parent: str, source_layers: UT_Array[int], destination_parent: str, destination_index: int) -> bool"""
    def outputBindings(self) -> list[str]:
        """outputBindings(self: _apexscene.Scene) -> UT_Array[str]"""
    def popData(self, arg0: str) -> Any:
        """popData(self: _apexscene.Scene, arg0: str) -> object"""
    def removeAnimationCachingBlocker(self) -> None:
        """removeAnimationCachingBlocker(self: _apexscene.Scene) -> None"""
    def removeConstraint(self, constraint_path: str, remove_data: bool = ...) -> None:
        """removeConstraint(self: _apexscene.Scene, constraint_path: str, remove_data: bool = False) -> None"""
    def removeRigFromEvaluation(self, path: str) -> None:
        """removeRigFromEvaluation(self: _apexscene.Scene, path: str) -> None"""
    def renameLayer(self, old_name: str, new_name: str) -> str:
        """renameLayer(self: _apexscene.Scene, old_name: str, new_name: str) -> str"""
    def saveToGeometry(self, geo: hou.Geometry, pattern: str = ..., input_geo: hou.Geometry | None = ..., debug: bool = ...) -> None:
        """saveToGeometry(self: _apexscene.Scene, geo: object, pattern: str = '*', input_geo: object = None, debug: bool = False) -> None"""
    def setActiveClip(self, arg0: str) -> None:
        """setActiveClip(self: _apexscene.Scene, arg0: str) -> None"""
    def setActiveLayer(self, name: str) -> None:
        """setActiveLayer(self: _apexscene.Scene, name: str) -> None"""
    def setAnimationCachingMode(self, arg0: int) -> None:
        """setAnimationCachingMode(self: _apexscene.Scene, arg0: int) -> None"""
    def setData(self, arg0: str, arg1: object) -> None:
        """setData(self: _apexscene.Scene, arg0: APEX_Path, arg1: object) -> None"""
    def setEnableSopGeometries(self, on: bool) -> None:
        """setEnableSopGeometries(self: _apexscene.Scene, on: bool) -> None"""
    def setEvaluateOnly(self, on: bool) -> None:
        """setEvaluateOnly(self: _apexscene.Scene, on: bool) -> None"""
    def setGeometryFolderProperties(self, arg0: str, arg1: _apex.Dict) -> None:
        """setGeometryFolderProperties(self: _apexscene.Scene, arg0: APEX_Path, arg1: _apex.Dict) -> None"""
    def setGraphDirty(self, arg0: str) -> None:
        """setGraphDirty(self: _apexscene.Scene, arg0: str) -> None"""
    def setSaveInheritedLayers(self, arg0: bool) -> None:
        """setSaveInheritedLayers(self: _apexscene.Scene, arg0: bool) -> None"""
    def startAnimationCaching(self) -> None:
        """startAnimationCaching(self: _apexscene.Scene) -> None"""
    def updateDirtyRigs(self) -> None:
        """updateDirtyRigs(self: _apexscene.Scene) -> None"""
    def updateEvaluationParms(self, arg0: float) -> None:
        """updateEvaluationParms(self: _apexscene.Scene, arg0: float) -> None"""
    def writeToGeometry(self, geo: hou.Geometry, pattern: str = ...) -> None:
        """writeToGeometry(self: _apexscene.Scene, geo: object, pattern: str = '*') -> object"""
    @property
    def control_manager(self) -> ControlManager: ...
    @property
    def control_scheduler(self) -> _apex.Graph: ...

class SceneCharacter:
    rig: str
    def __init__(self, arg0: str, arg1: _apex.Dict) -> None:
        """__init__(self: _apexscene.SceneCharacter, arg0: str, arg1: _apex.Dict) -> None"""
    def isVisible(self) -> bool:
        """isVisible(self: _apexscene.SceneCharacter) -> bool"""
    def show(self, arg0: bool) -> None:
        """show(self: _apexscene.SceneCharacter, arg0: bool) -> None"""
    @property
    def folder_properties(self) -> _apex.Dict: ...
    @property
    def input_geos(self) -> InputGeometries: ...
    @property
    def name(self) -> str: ...

class SceneGraph:
    control_manager: ControlManager
    control_template: hou.Geometry
    graph: _apex.Graph
    graph_parms: _apex.Dict
    name: str
    @typing.overload
    def __init__(self,
        name: str,
        graph: _apex.Graph,
        folder_properties: _apex.Dict = ...,
        should_write_to_geometry: bool = ...,
    ) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apexscene.SceneGraph, name: str, graph: _apex.Graph, folder_properties: _apex.Dict = <apex.Dict {}>, should_write_to_geometry: bool = True) -> None

        2. __init__(self: _apexscene.SceneGraph, name: str, graph: Geometry, folder_properties: _apex.Dict = <apex.Dict {}>, should_write_to_geometry: bool = True) -> None
        """
    @typing.overload
    def __init__(self,
        name: str,
        graph: hou.Geometry,
        folder_properties: _apex.Dict = ...,
        should_write_to_geometry: bool = ...,
    ) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _apexscene.SceneGraph, name: str, graph: _apex.Graph, folder_properties: _apex.Dict = <apex.Dict {}>, should_write_to_geometry: bool = True) -> None

        2. __init__(self: _apexscene.SceneGraph, name: str, graph: Geometry, folder_properties: _apex.Dict = <apex.Dict {}>, should_write_to_geometry: bool = True) -> None
        """
    def cachingEnabled(self) -> bool:
        """cachingEnabled(self: _apexscene.SceneGraph) -> bool"""
    def clearTrackedOutputs(self) -> None:
        """clearTrackedOutputs(self: _apexscene.SceneGraph) -> None"""
    def constrainable(self) -> bool:
        """constrainable(self: _apexscene.SceneGraph) -> bool"""
    def controlShapeLibrary(self) -> hou.Geometry:
        """controlShapeLibrary(self: _apexscene.SceneGraph) -> object"""
    def getLevelsOfDetail(self, arg0: str) -> list[str]:
        """getLevelsOfDetail(self: _apexscene.SceneGraph, arg0: str) -> UT_Array[str]"""
    def hasControlGraph(self) -> bool:
        """hasControlGraph(self: _apexscene.SceneGraph) -> bool"""
    def mirrorAxis(self) -> hou.Vector3:
        """mirrorAxis(self: _apexscene.SceneGraph) -> Vector3"""
    def parameterBindings(self) -> _apex.Dict | None:
        """parameterBindings(self: _apexscene.SceneGraph) -> Optional[_apex.Dict]"""
    def setCachingEnabled(self, arg0: bool) -> None:
        """setCachingEnabled(self: _apexscene.SceneGraph, arg0: bool) -> None"""
    def setConstrainable(self, arg0: bool) -> None:
        """setConstrainable(self: _apexscene.SceneGraph, arg0: bool) -> None"""
    def setDirty(self, recompile: bool = ...) -> None:
        """setDirty(self: _apexscene.SceneGraph, recompile: bool = False) -> None"""
    def setParameterBinding(self, arg0: str, arg1: str | None) -> None:
        """setParameterBinding(self: _apexscene.SceneGraph, arg0: str, arg1: Optional[str]) -> None"""
    def showTrackedOutput(self, arg0: str, arg1: str, arg2: bool) -> None:
        """showTrackedOutput(self: _apexscene.SceneGraph, arg0: str, arg1: str, arg2: bool) -> None"""
    def trackOutput(self, arg0: str, arg1: str) -> None:
        """trackOutput(self: _apexscene.SceneGraph, arg0: str, arg1: str) -> None"""
    @property
    def controls(self) -> _apex.Graph: ...

class SceneTool:
    def __init__(self, arg0: str) -> None:
        """__init__(self: _apexscene.SceneTool, arg0: str) -> None"""
    def isFolderVisible(self) -> bool:
        """isFolderVisible(self: _apexscene.SceneTool) -> bool"""
    def isVisible(self) -> bool:
        """isVisible(self: _apexscene.SceneTool) -> bool"""
    def show(self, arg0: bool) -> None:
        """show(self: _apexscene.SceneTool, arg0: bool) -> None"""
    def showFolder(self, arg0: bool) -> None:
        """showFolder(self: _apexscene.SceneTool, arg0: bool) -> None"""
    @property
    def name(self) -> str: ...

class TransformControl(Control):
    r_max: hou.Vector3
    r_max_lock: hou.Vector3
    r_min: hou.Vector3
    r_min_lock: hou.Vector3
    r_parm: str | None
    r_use_max: bool
    r_use_max_lock: bool
    r_use_min: bool
    r_use_min_lock: bool
    s_max: hou.Vector3
    s_max_lock: hou.Vector3
    s_min: hou.Vector3
    s_min_lock: hou.Vector3
    s_parm: str | None
    s_use_max: bool
    s_use_max_lock: bool
    s_use_min: bool
    s_use_min_lock: bool
    t_max: hou.Vector3
    t_max_lock: hou.Vector3
    t_min: hou.Vector3
    t_min_lock: hou.Vector3
    t_parm: str | None
    t_use_max: bool
    t_use_max_lock: bool
    t_use_min: bool
    t_use_min_lock: bool
    def __init__(self, scene: Scene, path: str, rig_path: str, nodeid: int = ...) -> None:
        """__init__(self: _apexscene.TransformControl, scene: pyapex::PYAPEX_SceneHandle, path: APEX_Path, rig_path: APEX_Path, nodeid: APEX_NodeID = -1) -> None"""
    @staticmethod
    def hasPromotedInputs(arg0: _apex.Graph, arg1: int) -> bool:
        """hasPromotedInputs(arg0: _apex.Graph, arg1: APEX_NodeID) -> bool"""

class ValuesView(Generic[_V]):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def __iter__(self) -> Iterator[_V]:
        """__iter__(self: _apexscene.ValuesView) -> Iterator"""
    def __len__(self) -> int:
        """__len__(self: _apexscene.ValuesView) -> int"""

def createCachedScene() -> Scene:
    """createCachedScene() -> _apexscene.Scene"""
def getOutputShapeNamesFromRig(arg0: _apex.Graph) -> list[str]:
    """getOutputShapeNamesFromRig(arg0: _apex.Graph) -> UT_Array[str]"""
def getRigNameFromPath(arg0: str) -> str:
    """getRigNameFromPath(arg0: str) -> str"""
def grabCachedScene(valid_geometry: hou.Geometry) -> Scene | None:
    """grabCachedScene(valid_geometry: object) -> object"""
def matchControlsFromTemplate(geo: hou.Geometry, attr_name: str, invert: bool = ..., bits: int = ..., get_name: bool = ...) -> list[str]:
    """matchControlsFromTemplate(geo: object, attr_name: str, invert: bool = False, bits: int = 4294967295, get_name: bool = False) -> UT_Array[str]"""
@overload
def setControlTemplateBits(geo: hou.Geometry, attr_name: str, ctrl_paths: Sequence[str], on: bool, bits: int = ...) -> bool:
    """setControlTemplateBits(*args, **kwargs)
    Overloaded function.

    1. setControlTemplateBits(geo: object, attr_name: str, ctrl_paths: UT_Array[str], on: bool, bits: int = 1) -> bool

    2. setControlTemplateBits(geo: object, attr_name: str, group_pattern: str, on: bool, bits: int = 1) -> bool
    """
@overload
def setControlTemplateBits(geo: hou.Geometry, attr_name: str, group_pattern: str, on: bool, bits: int = ...) -> bool:
    """setControlTemplateBits(*args, **kwargs)
    Overloaded function.

    1. setControlTemplateBits(geo: object, attr_name: str, ctrl_paths: UT_Array[str], on: bool, bits: int = 1) -> bool

    2. setControlTemplateBits(geo: object, attr_name: str, group_pattern: str, on: bool, bits: int = 1) -> bool
    """
def unregisterCachedScene(scene: Scene) -> None:
    """unregisterCachedScene(scene: _apexscene.Scene) -> None"""
def updateCachedSceneGeometry(scene: Scene, valid_geometry: hou.Geometry) -> None:
    """updateCachedSceneGeometry(scene: _apexscene.Scene, valid_geometry: object) -> None"""
