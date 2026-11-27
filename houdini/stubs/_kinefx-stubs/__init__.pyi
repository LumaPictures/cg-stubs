from collections.abc import Sequence
from typing import Any, ClassVar, TypedDict

import hou

# The options of a motion mixer cook.  Keys are optional, and a value of the wrong type is ignored
# (the cook then fails for an outputmode that isn't a str), except scenegeo.
class _MixerFetchOptions(TypedDict, total=False):
    time: float
    outputmode: str
    mixerkey: str
    character: str
    outputlabels: bool
    color: tuple[float, float, float]
    times: Sequence[float]
    animationclip: str
    onlyanimation: bool
    keepanimation: bool
    deletekeys: bool
    starttime: float
    scenegeo: hou.Geometry
from typing import Any, ClassVar, overload

class MotionMixerCache:
    def __init__(self) -> None:
        """__init__(self: _kinefx.MotionMixerCache) -> None"""
    def clearParmPointers(self) -> None:
        """clearParmPointers(self: object) -> None"""
    def fetch(self, arg0: hou.Geometry, arg1: hou.SopNode, arg2: _MixerFetchOptions) -> None:
        """fetch(self: object, arg0: object, arg1: object, arg2: dict) -> None"""
    def getEffectPivots(self) -> dict[str, hou.Matrix4]:
        """getEffectPivots(self: object) -> object"""

class NameManager:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _kinefx.NameManager) -> None

        2. __init__(self: _kinefx.NameManager, arg0: list[str]) -> None
        """
    @overload
    def __init__(self, arg0: Sequence[str]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _kinefx.NameManager) -> None

        2. __init__(self: _kinefx.NameManager, arg0: list[str]) -> None
        """
    def addName(self, arg0: str) -> tuple[str, bool]:
        """addName(self: _kinefx.NameManager, arg0: str) -> tuple

        Add the given name to the name manager's registry and returnthe new name after renaming and whether the name was changed
        """
    def addNames(self, arg0: Sequence[str]) -> tuple[list[str], list[int]]:
        """addNames(self: _kinefx.NameManager, arg0: list[str]) -> tuple

        Add the given names to the name manager's registry and returnthe new names after renaming and the indexes of the changed names
        """

class computeHierarchyResult:
    __members__: ClassVar[dict[str, computeHierarchyResult]] = ...  # read-only
    BadRoot: ClassVar[computeHierarchyResult] = ...
    FoundCycle: ClassVar[computeHierarchyResult] = ...
    IncompleteTraversal: ClassVar[computeHierarchyResult] = ...
    NoRoots: ClassVar[computeHierarchyResult] = ...
    Success: ClassVar[computeHierarchyResult] = ...
    __entries: ClassVar[dict[str, tuple[computeHierarchyResult, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _kinefx.computeHierarchyResult, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _kinefx.computeHierarchyResult) -> int"""
    def __int__(self) -> int:
        """__int__(self: _kinefx.computeHierarchyResult) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def applyEffectToAttribute(geo: hou.Geometry, effectname: str, attribname: str, timeinc: float, component: int = ...) -> None:
    """applyEffectToAttribute(geo: object, effectname: str, attribname: str, timeinc: float, component: int = -1) -> None

    Apply a motion effect to a float attribute on a geometry, typically from an extracted MotionClip.
    """
def buildLinkTemplate(arg0: hou.Geometry) -> None:
    """buildLinkTemplate(arg0: object) -> None

    Build a set of template points for creating 'link' geometry between points
    """
def combineParameterTransform(arg0: hou.Matrix4, arg1: hou.Vector3, arg2: int, arg3: int, arg4: hou.Vector3, arg5: hou.Vector3, arg6: hou.Vector3, arg7: hou.Vector3, arg8: hou.Vector3, arg9: int, arg10: int) -> hou.Matrix4:
    """combineParameterTransform(arg0: object, arg1: object, arg2: int, arg3: int, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: int, arg10: int) -> object

    Layer the given trs values onto an input local transform.
    """
def computeHierarchy(py_geo: hou.Geometry, outputchildren: bool = ..., sort: bool = ...) -> computeHierarchyResult:
    """computeHierarchy(py_geo: object, outputchildren: bool = False, sort: bool = False) -> _kinefx.computeHierarchyResult

    Compute skeleton hierarchy
    """
def extractParameterTransform(arg0: hou.Matrix4, arg1: hou.Matrix4, arg2: int, arg3: int, arg4: int, arg5: int, arg6: hou.Vector3, arg7: hou.Vector3, arg8: hou.Vector3, arg9: hou.Vector3) -> None:
    """extractParameterTransform(arg0: object, arg1: object, arg2: int, arg3: int, arg4: int, arg5: int, arg6: object, arg7: object, arg8: object, arg9: object) -> None

    Extract the parameter required to modify the inputlocal to match local.
    """
def getPackedFolderPaths(py_geo: hou.Geometry) -> list[str]:
    """getPackedFolderPaths(py_geo: object) -> list[str]

    Return an array of strings containing paths to packed folders in the geometry
    """
def getPackedMotionClipDataIds(arg0: hou.Geometry, arg1: int) -> str:
    """getPackedMotionClipDataIds(arg0: object, arg1: int) -> str

    Get the data ids from a named packed primitive.
    """
def getPointTransform(arg0: hou.Geometry, arg1: int, arg2: hou.Matrix4) -> None:
    """getPointTransform(arg0: object, arg1: int, arg2: object) -> None

    Get the full transform of the given point from the given geometry
    """
def getPointTransforms(arg0: hou.Geometry, arg1: str) -> list[float]:
    """getPointTransforms(arg0: object, arg1: str) -> list[float]

    Get the full transforms of all the points from the given geometry as a flat array of floats
    """
def initializeJointNames(py_geo: hou.Geometry, prefix: str) -> None:
    '''initializeJointNames(py_geo: object, prefix: str) -> None

    Initialize joint name attributes in the format "prefix" + str(i)
    '''
def isNodeDependentOnNodeParms(node: hou.Node, other_node: hou.Node) -> bool:
    """isNodeDependentOnNodeParms(node: object, other_node: object) -> bool

    Determine if a given node is referenced by one of the parms of the second node
    """
def makeRigidGeo(arg0: hou.Geometry) -> None:
    """makeRigidGeo(arg0: object) -> None

    Makes all matrices in the transform attribute rigid
    """
def motionMixerAddClipEffect(node: hou.Node, track_i: int, clip_i: int, fxtype: str) -> list[str]:
    """motionMixerAddClipEffect(node: object, track_i: int, clip_i: int, fxtype: str) -> list[str]

    Add an effect to a Motion Mixer clip.
    """
def motionMixerAddClips(node: hou.Node, track_i: int, source_names: Sequence[str], frame: float) -> list[str]:
    """motionMixerAddClips(node: object, track_i: int, source_names: list[str], frame: float) -> list[str]

    Add a clip to a Motion Mixer.
    """
def motionMixerAddTrack(node: hou.Node, track_i: int = ...) -> str:
    """motionMixerAddTrack(node: object, track_i: int = -1) -> str

    Add a track to a Motion Mixer.
    """
def motionMixerAddTrackEffect(node: hou.Node, track_i: int, fxtype: str) -> list[str]:
    """motionMixerAddTrackEffect(node: object, track_i: int, fxtype: str) -> list[str]

    Add an effect to a Motion Mixer track.
    """
def motionMixerBeginCopyBuffer() -> bool:
    """motionMixerBeginCopyBuffer() -> bool

    Begin a Motion Mixer Copy Buffer Block. Returns True if it was opened successfully.
    """
def motionMixerBlockModify(node: hou.Node, on_off: bool, propagate: bool) -> None:
    """motionMixerBlockModify(node: object, on_off: bool, propagate: bool) -> None

    Start or End a block modification on a MotionMixer
    """
def motionMixerClipEffectInfo(node: hou.Node, fxname: str, fxtype: str) -> list[str]:
    """motionMixerClipEffectInfo(node: object, fxname: str, fxtype: str) -> list[str]

    Get a clip effect info. Returns a empty array, or a 4 elements arraywith the fullpaths to myNode, myNodeBegin, myNodeOut and myNodeCook.
    """
def motionMixerCopy(node: hou.Node, selection: Sequence[str]) -> None:
    """motionMixerCopy(node: object, selection: list[str]) -> None

    Copy a Motion Mixer Tracks, Clips or Sources to the MotionMixer Copy Paste Buffer.
    """
def motionMixerCopyBufferContent() -> list[str]:
    """motionMixerCopyBufferContent() -> list[str]

    Returns the Motion Mixer Copy Buffer Content.
    """
def motionMixerEffectOutputRange(node: hou.Node, fx_name: str) -> list[float]:
    """motionMixerEffectOutputRange(node: object, fx_name: str) -> list[float]

    Return a Motion Mixer Effect Output Range.
    """
def motionMixerEndCopyBuffer() -> bool:
    """motionMixerEndCopyBuffer() -> bool

    Begin a Motion Mixer Copy Buffer Block. Returns True if it was opened successfully.
    """
def motionMixerExtractTransformsFromSkels(geo: hou.Geometry, rig_path: str, skel_paths: Sequence[str]) -> list[Any]:
    """motionMixerExtractTransformsFromSkels(geo: object, rig_path: str, skel_paths: list[str]) -> object

    Extract transforms from skels.
    """
def motionMixerFetch(mixercache: MotionMixerCache | None, geo: hou.Geometry, node: hou.SopNode, kwargs: _MixerFetchOptions) -> None:
    """motionMixerFetch(mixercache: object, geo: object, node: object, kwargs: dict) -> None

    Return a cooked geometry of the mixer at the given time using the cookkey.
    """
def motionMixerJson(node: hou.Node) -> str:
    """motionMixerJson(node: object) -> str

    Return a Motion Mixer JSON.
    """
def motionMixerPackedClipJSON(node: hou.Node, index: int) -> str:
    """motionMixerPackedClipJSON(node: object, index: int) -> str

    Return a json string containing a source clip json information.
    """
def motionMixerPackedClipsJSON(node: hou.Node) -> str:
    """motionMixerPackedClipsJSON(node: object) -> str

    Return a json string containing all source clips json information.
    """
def motionMixerPackedClipsNames(node: hou.Node) -> list[str]:
    """motionMixerPackedClipsNames(node: object) -> list[str]

    Return an array of strings containing the source clip names.
    """
def motionMixerPaste(node: hou.Node, f: float, f_align: float | None, stretch_factor: float, target: str, do_cut: bool, cut_start: float, cut_end: float) -> list[str]:
    """motionMixerPaste(node: object, f: object, f_align: object, stretch_factor: float, target: str, do_cut: bool, cut_start: float, cut_end: float) -> list[str]

    Paste a Motion Mixer Tracks, Clips or Sources from the MotionMixer Copy Paste Buffer.
    """
def motionMixerSetColor(geo: hou.Geometry, color: Sequence[float]) -> None:
    """motionMixerSetColor(geo: object, color: list[float]) -> None

    Set the color attribute to a constant color.
    """
def motionMixerTrackEffectInfo(node: hou.Node, fxname: str, fxtype: str) -> list[str]:
    """motionMixerTrackEffectInfo(node: object, fxname: str, fxtype: str) -> list[str]

    Get a track effect info. Returns a empty array, or a 4 elements arraywith the fullpaths to myNode, myNodeBegin, myNodeOut and myNodeCook.
    """
def motionMixerUsedClips(node: hou.Node, add_deps: bool) -> list[list[str] | dict[str, str] | dict[str, set[str]]] | None:
    """motionMixerUsedClips(node: object, add_deps: bool) -> object

    Returns None on failure or a list with 3 entries, [all_nested_clips, all_nested_clips_paths, used_nested_clips_by_mixer].
    """
def postmulTransformAttrib(arg0: hou.Geometry, arg1: str) -> None:
    """postmulTransformAttrib(arg0: object, arg1: str) -> None

    Post-multiply transform attribute with another attribute
    """
def premulTransformAttrib(arg0: hou.Geometry, arg1: str) -> None:
    """premulTransformAttrib(arg0: object, arg1: str) -> None

    Pre-multiply transform attribute with another attribute
    """
def randomColorByHierarchy(arg0: hou.Geometry) -> None:
    """randomColorByHierarchy(arg0: object) -> None

    Generate a random color for the joints on a given geometry based upon hierarchy
    """
def removeNegativeScales(arg0: hou.Geometry) -> None:
    """removeNegativeScales(arg0: object) -> None

    Remove the negative scale from all matrices in the transform attribute
    """
def restorePoseFromAttrib(arg0: hou.Geometry, arg1: str) -> None:
    """restorePoseFromAttrib(arg0: object, arg1: str) -> None

    Set the current rig pose from a Matrix4 attribute on the geometry
    """
def sequencePointAttrib(geo: hou.Geometry, attribname: str, ptname: str, component: int = ...) -> list[float]:
    """sequencePointAttrib(geo: object, attribname: str, ptname: str, component: int = 0) -> list[float]

    Return a flat array of attribute values for a point with the given name.
    """
def setPointTransforms(arg0: hou.Geometry, arg1: str, arg2: Sequence[float]) -> None:
    """setPointTransforms(arg0: object, arg1: str, arg2: list[float]) -> None

    Set the full transforms of the given list of point indices on the given geometry from a flat array of floats
    """
def updateLinkTemplate(arg0: hou.Geometry, arg1: hou.Geometry, arg2: float) -> None:
    """updateLinkTemplate(arg0: object, arg1: object, arg2: float) -> None

    Build a set of template points for creating 'link' geometry between points
    """
