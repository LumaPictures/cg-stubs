import os
from collections.abc import Iterable, Sequence
from typing import Any, Literal, NotRequired, Required, TypeAlias, TypedDict, overload

import hou
from hutil.PySide import QtCore
from kinefx.ui.mixerpane import MixerPane
from kinefx.ui.mixerparmpanel import MixerParmPanel

# The mixer's item kinds, and a selection item: (kind, ids), the ids being (track, mixer index),
# (track, clip, mixer index), (track, fx, mixer index) or (track, clip, fx, mixer index).
_MixerItemType: TypeAlias = Literal["track", "clip", "trackfx", "clipfx"]
_MixerSelectionItem: TypeAlias = tuple[_MixerItemType, tuple[int, ...]]

# What kinefx.ui.mixerutils.buildItemDict() makes of a selection item.
class _MixerItemDict(TypedDict):
    type: _MixerItemType
    ids: tuple[int, ...]
    itemtype: _MixerSelectionItem
    parmnode: hou.OpNode | None
    currentnode: str | None
    parmfilter: str
    showfolders: list[str]
    key: str
    # Set by the mixer pane on the items it shows in the viewport.
    show_handle: NotRequired[bool]

# A source clip of the mixer, from the node's packed clips JSON.
class _PackedClip(TypedDict):
    name: str
    rate: float
    range: list[float]
    nested_mixer_path: str

# The mixer as JSON: the node's asJson() (which has more keys: colors, transforms, ...), and what
# Mixer.asDict() makes of Mixer.toJSON().  Numbers whole in the JSON load as ints, and the C++
# side writes the flags as 0/1 and the shapes and transitions as names ("linear", "blend").
class _EffectDict(TypedDict, total=False):
    name: Required[str]
    type: Required[str]
    mode: Required[str]
    nodepath: Required[str]
    enabled: Required[bool | int]
    outputrange0: float
    outputrange1: float

class _ClipFields(TypedDict):
    name: str
    enable: bool | int
    clip: str
    clipstart: float
    clipend: float
    cutstart: float
    cutend: float
    pos: float
    index: int
    speed: float
    inx: float
    inoutvalue: float
    inshape: int | str
    outx: float
    outshape: int | str
    transit: int | str
    transit_inx: float
    transit_iny: float
    transit_in0x: float
    transit_in0y: float
    transit_inshape: int | str
    transit_outx: float
    transit_outy: float
    transit_out0x: float
    transit_out0y: float
    transit_outshape: int | str
    extendbefore: int
    extendafter: int
    cyclebefore: int
    cycleafter: int
    ignorey: bool | int
    ignorerot: int

class _ClipDict(_ClipFields):
    effects: list[_EffectDict]

# Clip.toJSON(): the JSON dumper serializes the effects with dumper().
class _ClipJSON(_ClipFields):
    effects: list["Effect"]

class _TrackFields(TypedDict):
    name: str
    blendmode: str
    blendparent: str
    enable: bool | int
    weight: float
    joints: str

class _TrackDict(_TrackFields):
    clips: list[_ClipDict]
    effects: list[_EffectDict]

class _TrackJSON(_TrackFields):
    clips: list["Clip"]
    effects: list["Effect"]

class _MixerFields(TypedDict):
    clips: str
    start: float
    end: float
    rate: float

class _MixerDict(_MixerFields):
    tracks: list[_TrackDict]

class _MixerJSON(_MixerFields):
    tracks: list["Track"]

# A kinefx::motionmixer node that bindMixerMethods() has given the MotionMixer methods.
class _MixerNode(hou.SopNode):
    def asJson(self) -> str: ...
    def getEffectOutputRange(self, fx_name: str) -> list[float]: ...
    def copyMotionMixer(self, selection: Sequence[str]) -> None: ...
    def pasteMotionMixer(
        self,
        f: float,
        f_align: float | None,
        stretch_factor: float,
        target: str,
        do_cut: bool,
        cut_start: float,
        cut_end: float,
    ) -> list[str]: ...
    def addClips(self, track_i: int, source_names: Sequence[str], frame: float) -> list[str]: ...
    def addTrack(self, track_i: int = ...) -> str: ...
    def addTrackEffect(self, track_i: int, fxtype: str) -> list[str]: ...
    def addClipEffect(self, track_i: int, clip_i: int, fxtype: str) -> list[str]: ...
    def getTrackEffectInfo(self, fxname: str, fxtype: str) -> "EffectInfo": ...
    def getClipEffectInfo(self, fxname: str, fxtype: str) -> "EffectInfo": ...
    def getPackedClipsNames(self) -> list[str]: ...
    def getPackedClips(self) -> list[_PackedClip]: ...
    def getPackedClip(self, i: int) -> _PackedClip: ...
    def getTopMixer(self, return_none: bool = ...) -> hou.OpNode | None: ...
    def blockModify(self, on_off: bool, propagate: bool) -> None: ...

class MixerSignals(QtCore.QObject):
    selectionChanged: QtCore.Signal

# The JSON dumper's default: any object json can't serialize (duck-typed on toJSON()), so the
# __dict__ of one without it holds anything.
def dumper(obj: Any) -> _MixerJSON | _TrackJSON | _ClipJSON | _EffectDict | dict[str, Any]: ...

class EffectInfo:
    myNodePath: str
    def __init__(self, info: Sequence[str]) -> None: ...

def motionMixerTrackEffectInfo(self: hou.OpNode, fxname: str, fxtype: str) -> EffectInfo: ...
def motionMixerClipEffectInfo(self: hou.OpNode, fxname: str, fxtype: str) -> EffectInfo: ...
def motionMixerPackedClips(self: hou.OpNode) -> list[_PackedClip]: ...
def motionMixerPackedClip(self: hou.OpNode, i: int) -> _PackedClip: ...
def motionMixerGetTopMixer(self: hou.OpNode, return_none: bool = ...) -> hou.OpNode | None: ...
def bindMixerMethods(node: hou.OpNode | None) -> None: ...
# The node is one bindMixerMethods() has bound (it calls asJson()).
@overload
def getMixer(node: _MixerNode, cook: bool = ...) -> "Mixer": ...
@overload
def getMixer(node: None, cook: bool = ...) -> None: ...
@overload
def getMixer(node: _MixerNode | None, cook: bool = ...) -> "Mixer | None": ...

class EffectDef:
    myNode: hou.OpNode
    myNodeBegin: hou.OpNode | None
    myNodeOut: hou.OpNode | None
    myNodeCook: hou.OpNode | None
    myNodePath: str
    def __init__(self, node: hou.OpNode, ignoredparms: Iterable[str]) -> None: ...

class Effect:
    name: str
    myType: str
    myMode: str
    myNodePath: str
    myEnabled: bool | int
    myOutputRange: list[float] | None
    def __init__(self, name: str, effect: str, mode: str, nodepath: str, enabled: bool | int) -> None: ...
    def toJSON(self) -> _EffectDict: ...
    def loadFromDict(self, d: _EffectDict) -> None: ...

class Clip:
    name: str
    myClipName: str
    myEnable: bool | int
    myClipStart: float
    myClipEnd: float
    myCutStart: float
    myCutEnd: float
    myPos: float
    myIndex: int
    mySpeed: float
    myExtendBefore: int
    myExtendAfter: int
    myCycleBefore: int
    myCycleAfter: int
    myIgnoreY: bool | int
    myIgnoreRot: int
    myInStart: float
    myInShape: int | str
    myOutStart: float
    myOutShape: int | str
    myInOutValue: float
    myTransition: int | str
    myTransitInStart: float
    myTransitInValue: float
    myTransitInShape: int | str
    myTransitOutStart: float
    myTransitOutValue: float
    myTransitOutShape: int | str
    myEffects: list[Effect]
    # Only set by loadFromDict(), so toJSON() fails on a clip that was not loaded.
    myTransitIn0Start: float
    myTransitIn0Value: float
    myTransitOut0Start: float
    myTransitOut0Value: float
    def __init__(self, name: str, clipstart: float, index: int, clipname: str) -> None: ...
    def toJSON(self) -> _ClipJSON: ...
    def loadFromDict(self, d: _ClipDict) -> None: ...
    def addEffect(self, name: str, effect: str, nodepath: str, enabled: bool | int) -> Effect: ...
    def findFx(self, fx_name: str) -> tuple[int, Effect] | tuple[Literal[-1], None]: ...

class Track:
    name: str
    myWeight: float
    myJoints: str
    myClips: list[Clip]
    myBlendMode: str
    myBlendParent: str
    myEnable: bool | int
    myEffects: list[Effect]
    def __init__(self, name: str) -> None: ...
    def toJSON(self) -> _TrackJSON: ...
    def addClip(self, clip: Clip) -> None: ...
    def addEffect(self, name: str, effect: str, mode: str, nodepath: str, enabled: bool | int) -> Effect: ...
    def findFx(self, fx_name: str) -> tuple[int, Effect] | tuple[Literal[-1], None]: ...
    def findClip(self, clip_name: str) -> Clip | None: ...
    def clips(self) -> list[Clip]: ...
    def loadFromDict(self, mixer: "Mixer", d: _TrackDict) -> None: ...

class Mixer:
    myNode: _MixerNode | None
    myStart: float
    myEnd: float
    myRate: float
    myTracks: list[Track]
    mySignals: MixerSignals
    mySelection: list[_MixerSelectionItem]
    def __init__(self, node: _MixerNode | None = ...) -> None: ...
    def createTrack(self, trackname: str) -> Track: ...
    def addTrack(self, track: Track) -> Track: ...
    def tracks(self) -> list[Track]: ...
    def findTrack(self, track_name: str) -> tuple[int, Track] | tuple[Literal[-1], None]: ...
    def setSelection(self, selection: Iterable[_MixerSelectionItem]) -> None: ...
    def selectionItemDicts(self) -> list[_MixerItemDict]: ...
    def createClip(self, name: str, source_name: str, clipstart: float, index: int, track: Track | None = ...) -> Clip: ...
    def toJSON(self) -> _MixerJSON: ...
    def asJSON(self) -> str: ...
    def asDict(self) -> _MixerDict: ...
    def loadFromDict(self, d: _MixerDict) -> None: ...
    def saveJSON(self, filepath: str | os.PathLike[str]) -> None: ...

def motionMixerGetWidgetFromPaneTabName(panetab_name: str | MixerPane) -> MixerPane | None: ...
def motionMixerGetViewerPanes(current_node: hou.Node | None) -> list[hou.SceneViewer]: ...
def motionMixerGetMixerParmPanes(current_node: hou.Node | None) -> list[tuple[hou.PaneTab, MixerParmPanel]]: ...
def motionMixerGo(panetab_name: str | MixerPane, n: hou.OpNode, new_frame: float, push_path: bool = ...) -> None: ...
def motionMixerGoUp(panetab_name: str | MixerPane, node_path: str, new_frame: float) -> None: ...
def motionMixerGoInto(panetab_name: str | MixerPane, old_node_path: str, new_node_path: str, new_frame: float) -> None: ...
def motionMixerExtract(panetab_name: str | MixerPane) -> None: ...
def motionMixerCreateNested(panetab_name: str | MixerPane) -> None: ...
def motionMixerBakeToOverride(panetab_name: str | MixerPane) -> None: ...
def renameNestedSources(nested_mixer_paths: Iterable[str], new_name: str) -> Literal[True]: ...
def deleteNestedSources(nested_mixer_paths: Iterable[str]) -> Literal[True]: ...
