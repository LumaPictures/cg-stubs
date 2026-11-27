import _apex
import apex
import hou
from apex.apexsoputils import _PythonSnippetKwargs
from collections.abc import Iterable, MutableSet, Sequence
from typing import Never, TypedDict

class _BakeKwargs(TypedDict):
    animgeo: hou.Geometry
    scenegeo: hou.Geometry
    animationclip: str
    onlyanimation: bool
    keepanimation: bool
    deletekeys: bool
    nodepath: str
    start_time: float
    end_time: float

class _SmoothMotionKwargs(_PythonSnippetKwargs, extra_items=_apex._ValueArg): ...  # type: ignore[call-arg]

class NodeInputOutput:
    node: int | None
    input_parm: int | list[int] | None
    output: int | None
    wire_name: str
    input_parm_a: int
    input_parm_b: int
    xforminput_parm: int
    input_local_parm: int
    input_restlocal_parm: int
    input_t: int
    input_r: int
    input_s: int
    input_xord: int
    input_rord: int
    def __init__(self, a: int | None = None, b: int | list[int] | None = None, c: int | None = None) -> None: ...

class MixerRigsBuilder:
    """
    A rig builder class to be used by a Python snippet SOP with an apex scene
    geometry containing multiple characters.
    """
    geo: hou.Geometry | None
    mode: int
    rigname: str
    skelname: str
    ctrlgroup: str
    cyclegroup: str
    rigpattern: str
    cyclepattern: str
    extractgraph: apex.Graph
    rigname_root: str
    ctrl_names: list[str]
    abstract_controls: apex.Dict | list[Never]
    all_control_data: dict[str, _apex._Value | None]
    DEFORM_RIG_EXT: str
    FX_RIG_EXT: str
    OVER_RIG_EXT: str
    EVAL_RIG_EXT: str
    REST_RIG_EXT: str
    COPY_RIG_EXT: str
    MIXER_ANIM_SKEL: str
    MIXER_ANIM_LOCAL_TRANSFORM: str
    MIXER_ANIM_PARENT_TRANSFORM: str
    MIXER_ANIM_ABSTRACT_CONTROLS: str
    def __init__(self, geo: hou.Geometry | None = None, mode: int = 0, rigname: str = '', skelname: str = '', ctrlgroup: str = '', cyclegroup: str = '', rigpattern: str = '', cyclepattern: str = '') -> None:
        """
            @geo: from Python snippet. A list of hou.Geometry.
            @mode: extract from a packed skeleton or from transform objects.
            @rigname: Base.rig the rig to use when creating the extra rigs.
            @skelname: Base.skel the skeleton to use to extract the ctrlgroup.
            @ctrlgroup': a group syntax string to select the controls to blend.
            @cyclegroup': a group syntax string to select a control to use for cycling.
            @rigpattern': an apex graph path syntax string to select the
                transform object to act on.
            @cyclepattern': an apex graph path syntax string to select the 
                transform object to use for cycling.
        """
    def extractPaths(self, path_pattern: str) -> tuple[str, ...]:
        """ Extract the path folder pattern and return an array of strings."""
    def extractCharacterPath(self, character_path: str, sub_pattern: str) -> str:
        """ Extract the character path folder pattern and return the first path."""
    def pack(self, path: str, geo: hou.Geometry) -> bool:
        """Pack the geo to our self.geo at the given path."""
    def unpack(self, path: str, freeze: bool = True) -> hou.Geometry:
        """Pack the path from our self.geo."""
    def extractAbstractControls(self, graph: apex.Graph) -> apex.Dict:
        """Extract the abtract control names and values from a rig graph."""
    def extractControlSkel(self, graph: apex.Graph, pattern: str) -> hou.Geometry:
        """Extract a skeleton geometry from a rig graph and an apex pattern."""
    def setGlobalAttr(self, geo: hou.Geometry, attr_name: str, attr_value: str) -> None: ...
    def setMotionMixerCycleJoint(self, geo: hou.Geometry, joint_name: str) -> None:
        """Set the motionmixer_cycle_joint global attribute on the geo."""
    def setMotionMixerRootJoint(self, geo: hou.Geometry, joint_name: str) -> None:
        """Set the motionmixer_root_joint global attribute on the geo."""
    def createMixerAnimSkelFromJoints(self, c: str) -> None:
        """
        Create MixerAnim.skel for each character, copying the Base.Skel,
        and keeping only the points matching the ctrlgroup
        Also fills the self.ctrl_names from the skeleton ctrl_group
        """
    def createMixerAnimSkelFromFolder(self, c: str) -> hou.Geometry | None:
        """
        Create the MixerAnim.skel for one character from an existing
        MixerAnim.skel in the packed folders.
        This allows the rigger to define a different hierarchy for blending.
        """
    def createMixerAnimSkelFromTransformObjects(self, c: str) -> None:
        """
        Create MixerAnim.skel for each character, extracting controls from
        the Transform Objects using an apex path pattern.
        Also fills the self.ctrl_names from the skeleton ctrl_group
        """
    def copyRig(self, c: str, rigname_from: str, rigname_to: str) -> None:
        """
        Copy an existing rig file to another path.
        """
    def findOrCreateParmsNode(self, graph: apex.Graph) -> int:
        """ Create a new __parms__ node for the mixer rig. """
    def findOrCreateOutputNode(self, graph: apex.Graph) -> int:
        """ Create a new __output__ node for the mixer rig. """
    def createGetPointTransforms(self, graph: apex.Graph) -> int:
        """
        Create the getPointTransforms setup, promoting the input MixerAnim.skel
        """
    def createGetPointParentTransforms(self, graph: apex.Graph) -> int:
        """
        Create the getPointParentTransforms setup, wiring to the already promoted
        input MixerAnim.skel
        """
    def createGetPointLocalTransforms(self, graph: apex.Graph) -> int:
        """
        Create the getPointLocalTransforms setup, wiring to the already promoted
        input MixerAnim.skel
        """
    def createGetAbstractControls(self, graph: apex.Graph, subnet_parent: int = -1) -> None:
        """
        Create a subnet to get the abstract values from the MixerAnim.
        """
    def createGetAbstractControlsAdditive(self, graph: apex.Graph, subnet_parent: int = -1) -> None:
        """
        Create a subnet to get the abstract values from the MixerAnim.

        If additive is True, also read from the parms input values and do an
        additive blend to act as a Layer. This is used by the FxRig.
        """
    def createAbstractControlsMixerAnimOutput(self, graph: apex.Graph, last_output_geo: int, subnet_parent: int = -1) -> int: ...
    def createSetPointTransformsMixerAnimOutput(self, graph: apex.Graph) -> None:
        """
        Create the setPointTransforms setup, outputing the MixerEval.skel
        It creates a setPointTransforms node followed 2 SetPointAttribValuesByName
        nodes.
        """
    def createSetPointTransformsMixerAnimOutputFxBlend(self, graph: apex.Graph) -> None: ...
    def createSetPointTransformsMixerAnimOutputFxBlend_old(self, graph: apex.Graph) -> None:
        """
        Create the setPointTransforms setup, outputing the MixerEval.skel
        """
    def createSetPointTransformsMixerAnimOutputFxBlend_new(self, graph: apex.Graph) -> None:
        """
        Create the setPointTransforms setup, outputing the MixerEval.skel
        """
    def createMixerEvalRig(self, geo: hou.Geometry) -> None:
        """
        Create a Motion Mixer Eval rig by reading geo and overwriting it
        with the updated graph.
        The Mixer Eval rig, adds a setPointTransforms node and a MixerAnim.skel
        output. It connects all the control rig transform objects to that
        setPointTransforms.
        """
    def createMixerRestRig(self, geo: hou.Geometry) -> None:
        """
        Create a Motion Mixer Rest rig by reading geo and overwriting it
        with the updated graph.
        The Mixer Rest rig promotes all the transforms to a new outputnode.
        """
    def evalRestControlData(self) -> None:
        """
        For the MixerFx restlocal override, we need to know the resttransform
        of TransformObjects that aren't contributing to the blending.

        This does a simple scene invoke, nuking the animation folder and
        fetching the rest_transforms in all_control_data for everything.
        """
    def createMixerDeformRig(self, geo: hou.Geometry) -> None:
        """
        Create a Motion Mixer Deform rig by reading geo and overwrite it
        with the updated graph.
        """
    def createValueNode(self, graph: apex.Graph, node_name: str, node_type: str, parm_value: _apex._ValueArg | None = None, subnet: int = -1) -> int:
        """
        Create a Value<@node_type> node named @node_name and set the parm value.
        """
    def createMatrix4Node(self, graph: apex.Graph, node_name: str, parm_value: hou.Matrix4 | None = None, subnet: int = -1) -> int:
        """
        Create a Value<Matrix4> node named @node_name and set the parm value.
        """
    def addMatrix4(self, graph: apex.Graph, subnet: int, node_name: str, default_value: hou.Matrix4 | None = ...) -> NodeInputOutput:
        """
        Add a Matrix4 node with a default value
        """
    def addInvert(self, graph: apex.Graph, subnet: int, node_name: str) -> NodeInputOutput:
        """
        Add an invert node. No default value.
        """
    def addBuild(self, graph: apex.Graph, subnet: int, node_name: str, ctrl_parms: apex.Dict) -> NodeInputOutput:
        """
        Add an build node. No default value.
        """
    def addBlend(self, graph: apex.Graph, subnet: int, node_name: str, a: NodeInputOutput | None, b: NodeInputOutput | None) -> NodeInputOutput:
        """
        Add a blend node. No default value.
        """
    def addMul(self, graph: apex.Graph, subnet: int, node_name: str, cnx: Sequence[NodeInputOutput]) -> NodeInputOutput:
        """
        Add a multiply node with a list of outputs to connect.
        """
    def addSubnet(self, graph: apex.Graph, node_name: str, parent_id: int = -1) -> int: ...
    def createMixerOverrideRig(self, geo: hou.Geometry, rest_data: apex.Dict, over: bool = False) -> None:
        """
        Create a Motion Mixer Override rig by reading geo and overwriting it
        with the updated graph.
        """
    def createMixerFxRig(self, geo: hou.Geometry, rest_data: apex.Dict, over: bool = False) -> None:
        """
        Create a Motion Mixer Fx rig by reading geo and overwriting it
        with the updated graph.
        """
    def createCharacterRigs(self, c: str) -> None:
        """
        Create Rigs for a single character.

        MixerDeform.rig has all the controls xform input driven directly from 
        the point transform of the skeleton input.

        MixerFx.rig has all the controls restlocal input driven directly from 
        the point transform of the skeleton input.
        """
    def createMixerRigs(self) -> hou.Geometry | None:
        """
        Python Snippet code to create mixer rigs for all the characters in the
        scene.
        """
    def switchToRig(self, ext: str) -> hou.Geometry | None:
        """
        Select a mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """
    def switchToEvalRig(self) -> hou.Geometry | None:
        """
        Select mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """
    def switchToRestRig(self) -> hou.Geometry | None:
        """
        Select mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """
    def switchToDeformRig(self) -> hou.Geometry | None:
        """
        Select mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """
    def switchToFxRig(self) -> hou.Geometry | None:
        """
        Select mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """
    def switchToOverrideRig(self) -> hou.Geometry | None:
        """
        Select mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """
    def switchToBaseRig(self) -> hou.Geometry | None:
        """
        Select mixer rigs for all the characters in the scene.
        This is currently destructive, and copies mixer rigs to the base rig.
        """

class MixerRigBaker:
    """
    A rig baker class to be used by a Python snippet SOP with an apex scene
    geometry containing multiple characters.
    """
    scenegeo: hou.Geometry
    animgeo: hou.Geometry
    scene: apex.Scene
    @classmethod
    def bake(cls, kwargs: _BakeKwargs) -> hou.Geometry:
        """ Class method to do the baking from the kwargs in SOP_MotionMixer.C."""
    def __init__(self, scenegeo: hou.Geometry, animgeo: hou.Geometry) -> None:
        """ Contruct a baker."""
    def createAnimBindings(self, rig_paths: Iterable[str]) -> None:
        """ Add Missing animbindings """
    def bakeToGeo(self, geo: hou.Geometry, kwargs: _BakeKwargs) -> None:
        """
            Perform the bake operation, writting the matching @save_pattern to @geo.
        """

def loadStashSources(node: hou.SopNode) -> None:
    """ Python SOP code for the load_stash_sources SOP in the MotionMixerSetup
    hda."""

class NestedClipsHierarchyBuilder:
    """ Class to build the hierarchy of nested clips instances."""
    all_nested_clips: list[str]
    all_nested_clips_paths: dict[str, str]
    used_nested_clips_by_mixer: dict[str, set[str]]
    def __init__(self, top_mixer: hou.OpNode, add_deps: bool = False) -> None: ...
    def getPath(self, nested_clip_name: str) -> str | None:
        """ Returns the node path of a nested clip name or None"""
    def getFromSourceName(self, source_name: str) -> str | None:
        """ Returns the NestedClip name from a source name such as
            '/*/myclip' or '/electra/myclip'.
            No validation done to check if the character is valid.
        """
    def getChildren(self, nested_clip_name: str, recurse: bool = False) -> set[str] | list[Never]:
        """Get all the children nested clip names of a nested clip name.
        This only returns the direct children.
        """
    def getUsedNestedClips(self, nested_clip_name: str) -> set[str] | list[Never]:
        """Get all nested clip names used by a nested clip.
        This expands the clips recursively."""
    def getParents(self, nested_clip_name: str) -> set[str]:
        """Get the direct parents of a nested clip.
            No caching done.
        """
    def getAllParents(self, nested_clip_name: str) -> set[str]:
        """Get all the parents of a nested clip.
            No caching done.
        """
    def visitAllParentPaths(self, visited: MutableSet[str], nested_clip_name: str) -> None:
        """Mark all the parent paths as visited. """

def validateAnimationClipPath(p: str) -> str: ...
def loadMixerSources(node: hou.SopNode) -> None:
    """ Python SOP code for the load_mixer_sources SOP in the MotionMixerSetup
    hda."""
def declareMixerSources(node: hou.SopNode) -> None:
    """ Python SOP code for the declare_mixer_sources SOP in the MotionMixerSetup
    hda."""

class SmoothMotionPackedFolders:
    """ Python SOP code for the Smooth Motion FX. """
    lastid0: tuple[int, ...] | None
    motionclips: list[tuple[str, apex.Graph, hou.Geometry]]
    geo: hou.Geometry | None
    def __init__(self) -> None: ...
    def createGraph(self) -> apex.Graph:
        """ Create the Apex Graph for SmoothMotion. Prefer to keep it in code
        instead of as an external geo."""
    def run(self, kwargs: _SmoothMotionKwargs) -> hou.Geometry | None:
        """ Run the Smooth Motion on the kwargs from the snippet."""
