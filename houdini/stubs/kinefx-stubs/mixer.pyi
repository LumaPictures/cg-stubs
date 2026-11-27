import hou
import os
import typing
from collections.abc import Iterable, Sequence
from hutil.PySide import QtCore
from kinefx.ui.mixerpane import MixerPane as MixerPane
from kinefx.ui.mixerparmpanel import MixerParmPanel as MixerParmPanel
from typing import Any, Literal, NotRequired, Required, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_MixerItemType: TypeAlias = Literal['track', 'clip', 'trackfx', 'clipfx']
_MixerSelectionItem: TypeAlias = tuple[_MixerItemType, tuple[int, ...]]
class _MixerItemDict(TypedDict):
    type: _MixerItemType
    ids: tuple[int, ...]
    itemtype: _MixerSelectionItem
    parmnode: hou.OpNode | None
    currentnode: str | None
    parmfilter: str
    showfolders: list[str]
    key: str
    show_handle: NotRequired[bool]

class _PackedClip(TypedDict):
    name: str
    rate: float
    range: list[float]
    nested_mixer_path: str

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

class _ClipJSON(_ClipFields):
    effects: list['Effect']

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
    clips: list['Clip']
    effects: list['Effect']

class _MixerFields(TypedDict):
    clips: str
    start: float
    end: float
    rate: float

class _MixerDict(_MixerFields):
    tracks: list[_TrackDict]

class _MixerJSON(_MixerFields):
    tracks: list['Track']

class _MixerNode(hou.SopNode):
    def asJson(self) -> str: ...
    def getEffectOutputRange(self, fx_name: str) -> list[float]: ...
    def copyMotionMixer(self, selection: Sequence[str]) -> None: ...
    def pasteMotionMixer(self, f: float, f_align: float | None, stretch_factor: float, target: str, do_cut: bool, cut_start: float, cut_end: float) -> list[str]: ...
    def addClips(self, track_i: int, source_names: Sequence[str], frame: float) -> list[str]: ...
    def addTrack(self, track_i: int = ...) -> str: ...
    def addTrackEffect(self, track_i: int, fxtype: str) -> list[str]: ...
    def addClipEffect(self, track_i: int, clip_i: int, fxtype: str) -> list[str]: ...
    def getTrackEffectInfo(self, fxname: str, fxtype: str) -> EffectInfo: ...
    def getClipEffectInfo(self, fxname: str, fxtype: str) -> EffectInfo: ...
    def getPackedClipsNames(self) -> list[str]: ...
    def getPackedClips(self) -> list[_PackedClip]: ...
    def getPackedClip(self, i: int) -> _PackedClip: ...
    def getTopMixer(self, return_none: bool = ...) -> hou.OpNode | None: ...
    def blockModify(self, on_off: bool, propagate: bool) -> None: ...

class MixerSignals(QtCore.QObject):
    """Qt signal emitter for Mixer"""
    selectionChanged: QtCore.Signal

def dumper(obj: Any) -> _MixerJSON | _TrackJSON | _ClipJSON | _EffectDict | dict[str, Any]:
    """ json dumping helper, call toJSON when possible."""

class EffectInfo:
    """ Ctor from an info string array return by the _kinefx methods"""
    myNodePath: str
    def __init__(self, info: Sequence[str]) -> None: ...

def motionMixerTrackEffectInfo(self: hou.OpNode, fxname: str, fxtype: str) -> EffectInfo:
    """ Wrapper to return a python class instead of an array of strings"""
def motionMixerClipEffectInfo(self: hou.OpNode, fxname: str, fxtype: str) -> EffectInfo:
    """ Wrapper to return a python class instead of an array of strings"""
def motionMixerPackedClips(self: hou.OpNode) -> list[_PackedClip]: ...
def motionMixerPackedClip(self: hou.OpNode, i: int) -> _PackedClip: ...
def motionMixerGetTopMixer(self: hou.OpNode, return_none: bool = True) -> hou.OpNode | None:
    """ Find the top mixer and look for shared sources.
        Returns None if the mixer is a top level mixer."""
def bindMixerMethods(node: hou.OpNode | None) -> None:
    """ Attach MotionMixer pybind methods to @node."""
@typing.overload
def getMixer(node: _MixerNode, cook: bool = ...) -> Mixer: ...
@typing.overload
def getMixer(node: None, cook: bool = ...) -> None: ...
@typing.overload
def getMixer(node: _MixerNode | None, cook: bool = ...) -> Mixer | None: ...

class EffectDef:
    """ An effect definition to be applied to a track of clip instance. 
        It is bound to an hda, and spare parameters are created on the mixer
        hda to go along with it. An effect is applied inplace using a single 
        input motion clip.
    """
    myNode: hou.OpNode
    myNodeBegin: hou.OpNode | None
    myNodeOut: hou.OpNode | None
    myNodeCook: hou.OpNode | None
    myNodePath: str
    def __init__(self, node: hou.OpNode, ignoredparms: Iterable[str]) -> None:
        """ EffectDef ctor
            @node A SOP node inside the effects hda representing the effect.
            @ignoredparms list of parameter names to ignore. Mainly to 
            workaround subnets the lack of an invisibility flag on invisible
            subnet parameters such as subnet input labels.
        """

class Effect:
    """ A Mixer Effect instance for clips or tracks."""
    name: str
    myType: str
    myMode: str
    myNodePath: str
    myEnabled: bool | int
    myOutputRange: list[float] | None
    def __init__(self, name: str, effect: str, mode: str, nodepath: str, enabled: bool | int) -> None:
        """ Effect ctor.
            @name Effect instance name. Doesn't include the parent track or 
            clip name.
            @effect EffectDef type as a string.
            @mode Effect mode for track effects. 'local' or 'global'.
            @nodepath An absolute node path pointing to a node when to 
            retreive parameter values.
            @enabled .
        """
    def toJSON(self) -> _EffectDict:
        """ Convert Effect to a dictionary for the JSON dumper."""
    def loadFromDict(self, d: _EffectDict) -> None:
        """ Load Effect from a dict. This is for extra objects we own.
         @d Dict to load from."""

class Clip:
    """ A Mixer Clip instance can be cut and offseted."""
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
    myTransitIn0Start: float
    myTransitIn0Value: float
    myTransitOut0Start: float
    myTransitOut0Value: float
    def __init__(self, name: str, clipstart: float, index: int, clipname: str) -> None: ...
    def toJSON(self) -> _ClipJSON:
        """ Convert Clip to a dictionary for the JSON dumper."""
    def loadFromDict(self, d: _ClipDict) -> None:
        """ Load Clip from a dict. This is called from Track.loadFromDict and
            most over the work is done by the Clip ctor.
            @d Dict to load from.
        """
    def addEffect(self, name: str, effect: str, nodepath: str, enabled: bool | int) -> Effect:
        """ Add a Clip Effect
            @name Used as a Label and to uniquely identify the track effect.
            @effect EffectDef type, matching a registered effect.
            @nodepath String to resolve a node path later.
            @enabled
        """
    def findFx(self, fx_name: str) -> tuple[int, Effect] | tuple[Literal[-1], None]: ...

class Track:
    """ Mixer Track, holding a list of Mixer Clips """
    name: str
    myWeight: float
    myJoints: str
    myClips: list[Clip]
    myBlendMode: str
    myBlendParent: str
    myEnable: bool | int
    myEffects: list[Effect]
    def __init__(self, name: str) -> None:
        """ Track ctor. 
            @name Track name.
        """
    def toJSON(self) -> _TrackJSON:
        """ Convert Track to a dictionary for the JSON dumper."""
    def addClip(self, clip: Clip) -> None:
        """ Add an existing clip instance.
            @clip Clip instance.
        """
    def addEffect(self, name: str, effect: str, mode: str, nodepath: str, enabled: bool | int) -> Effect:
        """ Add a Track Effect
            @name Used as a Label and to uniquely identify the track effect.
            @effect EffectDef type, matching a registered effect.
            @mode Effect mode, 'local' or 'global'.
            @nodepath String to resolve a node path later.
            @enabled
        """
    def findFx(self, fx_name: str) -> tuple[int, Effect] | tuple[Literal[-1], None]: ...
    def findClip(self, clip_name: str) -> Clip | None: ...
    def clips(self) -> list[Clip]:
        """Return the array of Clip."""
    def loadFromDict(self, mixer: Mixer, d: _TrackDict) -> None:
        """ Load Track from a dict. This is called from Track.loadFromDict and
            most over the work is done by the Clip ctor.
            @Mixer Parent Mixer used to create the clip.
            @d Dict to load from.
        """

class Mixer:
    """ Mixer holding the tracks """
    myNode: _MixerNode | None
    myStart: float
    myEnd: float
    myRate: float
    myTracks: list[Track]
    mySignals: MixerSignals
    mySelection: list[_MixerSelectionItem]
    def __init__(self, node: _MixerNode | None = None) -> None:
        """ Create an empty mixer, must have the clips."""
    def createTrack(self, trackname: str) -> Track:
        """ Create a track.
            @trackname, name of the track. No name checks done.
        """
    def addTrack(self, track: Track) -> Track:
        """ Add an existing track.
            @track Track
        """
    def tracks(self) -> list[Track]:
        """ Returns the array of tracks. """
    def findTrack(self, track_name: str) -> tuple[int, Track] | tuple[Literal[-1], None]: ...
    def setSelection(self, selection: Iterable[_MixerSelectionItem]) -> None:
        """Store selection and notify listeners.
           @selection list of (type, ids) tuples, e.g. [('clip', (0,1,0))]
        """
    def selectionItemDicts(self) -> list[_MixerItemDict]:
        """Build item dicts from stored selection.
        """
    def createClip(self, name: str, source_name: str, clipstart: float, index: int, track: Track | None = None) -> Clip:
        """ Create a Mixer Clip using a Source Clip Name from the Clip
            Collection.
            @name Name for the new Mixer Clip
            @source_name Name of a source clip to use.
            @clipstart Frame
            @index original clip index
            @track Optional Parent Track.
        """
    def toJSON(self) -> _MixerJSON:
        """ Convert Mixer to a dictionary for the JSON dumper."""
    def asJSON(self) -> str:
        """ Serialize to JSON string"""
    def asDict(self) -> _MixerDict:
        """ Serialize to dict."""
    def loadFromDict(self, d: _MixerDict) -> None:
        """ Load the Mixer from a dictionnary.
            @d Dict to load from.
        """
    def saveJSON(self, filepath: str | os.PathLike[str]) -> None:
        """ Save the mixer to a JSON file.
            @filepath File Path to save to. Will throw an exception on failure.
            This won't saved the clip contents, only the mixer dict.
        """

def motionMixerGetWidgetFromPaneTabName(panetab_name: str | MixerPane) -> MixerPane | None: ...
def motionMixerGetViewerPanes(current_node: hou.Node | None) -> list[hou.SceneViewer]: ...
def motionMixerGetMixerParmPanes(current_node: hou.Node | None) -> list[tuple[hou.PaneTab, MixerParmPanel]]: ...
def motionMixerGo(panetab_name: str | MixerPane, n: hou.OpNode, new_frame: float, push_path: bool = False) -> None: ...
def motionMixerGoUp(panetab_name: str | MixerPane, node_path: str, new_frame: float) -> None: ...
def motionMixerGoInto(panetab_name: str | MixerPane, old_node_path: str, new_node_path: str, new_frame: float) -> None: ...
def motionMixerExtract(panetab_name: str | MixerPane) -> None: ...
def motionMixerCreateNested(panetab_name: str | MixerPane) -> None: ...
def motionMixerBakeToOverride(panetab_name: str | MixerPane) -> None: ...
def renameNestedSources(nested_mixer_paths: Iterable[str], new_name: str) -> Literal[True]:
    """Rename one or more nested motion mixer nodes to new_name, rewriting
    source{trk}_{clip} parms on sibling mixers that referred to the old
    name. For Scene-row rename the inputs are typically siblings of
    different parents that share a clip name; per-parent unique_name
    resolution may yield slightly different actual names.
    """
def deleteNestedSources(nested_mixer_paths: Iterable[str]) -> Literal[True]:
    """Destroy nested motion mixer nodes at the given paths.

    Any timeline clip instances whose source{}_{} parms refer to the deleted
    clip names will be left orphaned (matches manual node destroy).
    """
