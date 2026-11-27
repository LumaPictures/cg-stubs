import _apex
import apex.stateutils_2 as asu
import hou
from _apexscene import Scene as Scene
from apex.control_2 import ControlManager as ControlManager, controlName as controlName, controlRigPath as controlRigPath, splitControlPath as splitControlPath
from apex.utils import addAnimateStateUndo as addAnimateStateUndo, loadGraph as loadGraph
from collections.abc import Callable as Callable, Collection, Container, Iterable, Mapping, MutableSequence, Sequence
from typing import Final, Literal, Protocol

from typing import TypeAlias
from apex.effecttool import _BakeKwargs
from statehud.parmutils import _HUDParmValue
from typing import TypeAlias
_FrameSetLike: TypeAlias = 'FrameSetBase | Container[float]'
_CtrlParms: TypeAlias = dict[str, tuple[str, _apex._Value | None]]
_ParmValues: TypeAlias = Mapping[str, _apex._Value | None] | _apex.Dict
_BakeParms: TypeAlias = Mapping[str, _HUDParmValue] | _BakeKwargs
_BakeSource: TypeAlias = 'BakeSourceXformBase | BakeSourceParmsBase'
class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only its shared members."""

BLEND_TRANSFORM_GRAPH: str
BAKE_SOURCE_XFORM: Final[int]
BAKE_SOURCE_PARMS: Final[int]
BIT_MAP: dict[str, int]

def setupInverseRigGraph(graph: _apex.Graph, invertgraph: _apex.Graph | None = None) -> _apex.Graph:
    """
    Sets up an inverse rig graph for the control's matching 'pattern' in the
    'graph'

    :param graph: The rig graph to invert
    :type graph: apex.Graph
    :param invertgraph: The invert graph parts matching the rig. this is an optional
    graph to customize the inversion process per rig
    :type graph: apex.Graph
    :return: The inverted rig graph
    :rtype: apex.Graph
    """
def setInverRigGraphPattern(graph: _apex.Graph, pattern: str, all_controls_pattern: str | None = None) -> tuple[_apex.Dict, _apex.Graph]:
    """

    :param graph: _description_
    :param pattern: _description_
    """

class InverseRig:
    """
    Initialize an inverse rig for a rig from the APEX Scene Animate state's
    scene.
    This should be used for computing the inputs necessary to force the controls
    of a rig to be at specific world space positions.

    :param scene: The viewer state's scene
    :type scene: apex.Scene()
    :param rig_path: The path in the scene's data to the rig's apex.SceneGraph()
    :type rig_path: str
    :param pattern: An apex pattern to match the rig's controls that should
                    be inverted.
    :type pattern: str
    """
    rig_path: str
    use_inverter: bool
    default_parms: _apex.Dict
    inverter: _apex.Graph | None
    pattern: str
    all_controls_pattern: str
    def __init__(self, scene: Scene, rig_path: str, pattern: str = '*', all_controls_pattern: str | None = None, use_inverter: bool = False) -> None: ...
    @property
    def scene(self) -> Scene | None: ...
    def invertRig(self, pattern: str = '*', all_controls_pattern: str | None = None) -> None:
        """
        Resets the inverse rig using a different control pattern.
        
        :param pattern: An apex pattern to match the rig's controls that
                        should be inverted.
        :type pattern: str
        """
    @property
    def inverse_graph(self) -> _apex.Graph | None:
        """always fetch the invert rig rig directly from the scene

        :return: _description_
        """
    def setParm(self, key: str, val: _apex._ValueArg) -> None:
        """
        Sets the value for one of the inverse rig's parameters.

        :param key: The name of the parameter to set.
        :type key: str
        :param val: The value of the parameter
        :type val: A valid apex graph's parameter
        """
    def setupTRSParms(self) -> None:
        """
        Evaluates the post constraint parameters for the rig from the scene and sets
        those parameters into the parameters of the inverse rig graph.
        """
    def setCtrlXform(self, ctrl_name: str, xform: hou.Matrix4 | None = None, xform_offset: hou.Matrix4 | None = None) -> None:
        """
        Sets the target transform for a control and sets the corresponding parameter
        in the inverse graph.
        """
    def setCtrlAbstract(self, parms: _apex.Dict) -> None:
        """
        Sets the target abstract values inputs for a control and sets the corresponding parameter
        in the inverse graph.
        """
    def evaluateCtrl(self, ctrl_path: str) -> _CtrlParms:
        """
        Evaluates the inverted parameters for a control from the inverse graph.

        :param ctrl_path: The path in the scene to the control
        :type ctrl_path: str
        :return: A dictionary from the evaluated components to a pair of the
                 corresponding parameter name and value.
                 Euler filters are applied to all rotation parameters, using
                 the prevous value of the parameter as the hint.
        :rtype: dict
        """
    def evaluateCtrls(self, ctrl_paths: Collection[str], output_pattern: str | None = None) -> dict[str, _CtrlParms]:
        """
        Evaluates the inverted parameters for a list of controls from the
        inverse graph.

        :param ctrl_paths: The paths in the scene to the controls
        :type ctrl_path: tuple of str
        :return: A dictionary from the control paths to a dictionary from the
                 evaluated components to a pair of the corresponding parameter
                 name and value.
                 Euler filters are applied to all rotation parameters, using
                 the prevous value of the parameter as the hint.
        :rtype: dict
        """
    def getControlOutputPattern(self, ctrl_paths: Iterable[str], ctrl_mgr: ControlManager) -> str: ...
    def updateInputGeometriesFromScene(self) -> None:
        """
        Use the 'update_sops' rig property to transfer animated geometry from
        the current scene.
        """

class FrameSetBase:
    def __init__(self) -> None: ...
    def contains(self, frame: float) -> bool: ...
    def __contains__(self, frame: float) -> bool: ...

class FrameSetCache(FrameSetBase):
    def __init__(self) -> None: ...
    def clearCache(self) -> None: ...

class FrameSetAnd(FrameSetCache):
    frame_sets: MutableSequence[_FrameSetLike]
    def __init__(self, frame_sets: MutableSequence[_FrameSetLike] = ...) -> None: ...
    def addFrameSet(self, frame_set: _FrameSetLike) -> None: ...

class FrameSetOr(FrameSetCache):
    frame_sets: MutableSequence[_FrameSetLike]
    def __init__(self, frame_sets: MutableSequence[_FrameSetLike] = ...) -> None: ...
    def addFrameSet(self, frame_set: _FrameSetLike) -> None: ...

class FrameSetNot(FrameSetBase):
    frame_set: FrameSetBase
    def __init__(self, frame_set: FrameSetBase) -> None: ...

class FrameSet(FrameSetCache):
    frames: MutableSequence[float]
    def __init__(self, frames: MutableSequence[float] = ...) -> None: ...
    def addFrame(self, frame: float) -> None: ...
    def addFrames(self, frames: Iterable[float]) -> None: ...

class RangeFrameSet(FrameSetBase):
    start_frame: float
    end_frame: float
    def __init__(self, start_frame: float, end_frame: float) -> None: ...

class ChannelFrameSet(FrameSetCache):
    channel_prims: list[hou.ChannelPrim]
    def __init__(self) -> None: ...
    def addChannelPrimitive(self, channel_prim: hou.ChannelPrim) -> None: ...

def componentsToInt(components: Container[str]) -> int:
    """
    Converts a 'trs' component string to an integer interpretable by the
    transform::Blend callback.
    """

class BakeSourceXformBase:
    """
    The base class used to bake a 4x4 matrix into the componets of a Transform
    control.

    :param components: The trs components to be cracked from the matrix
    :type components: str
    :param frame_set: A searchable object that defines the set of frames
                      for which this bake source is valid
    :type frame_set: None or a searchable object
    :param xform_offset: Optional offset applied to the transform in worldspace
    :type xform_offset: hou.Matrix4
    """
    components: str
    components_int: int
    frame_set: _FrameSetLike | None
    def __init__(self, components: str = '*', frame_set: _FrameSetLike | None = None, xform_offset: hou.Matrix4 | None = ...) -> None: ...
    def addControlsToManager(self, scene: Scene, ctrl_mgr: ControlManager) -> None:
        """
        Adds all controls needed for evaluation and baking into the given
        control manager.

        :param scene: An apex scene.
        :type scene: apex.Scene
        :param ctrl_mgr: A control manager to update
        :type ctrl_mgr: apex.control_2.ControlManager
        """
    def doBakeAtFrame(self, frame: float) -> bool:
        """
        Returns whether to use this bake source when baking at the given frame.
        This is determined by the frame_set.

        :return: Whether to use this bake source when baking at 'frame'
        :rtype: bool
        """
    def type(self) -> Literal[0]:
        """
        Returns the type of the bake source.

        :return: The type of the bake
        :rtype: int
        """
    def blendGraph(self) -> _apex.Graph | None:
        """
        Returns the graph used to apply the matrix blending. If None, the
        default graph will be used.

        :return: The graph to blend the control's initial matrix to the
                 returned matrix.
        :rtype: apex.Graph or None
        """
    def bakeXform(self, frame: float, target_ctrl_path: str, ctrl_mgr: ControlManager, blend_graph: _apex.Graph, blend_parms: _apex.Dict) -> hou.Matrix4 | None:
        """
        Blend this bake source's transform matrix with a target control's
        matrix at the given frame.

        :param frame: The frame at which to bake
        :type frame: float
        :param target_ctrl_path: The path to the control in which to bake the transform.
        :type target_ctrl_path: str
        :param ctrl_mgr: The control manager setup in addControlsToManager. This should
                         contain all source and target controls.
        :type ctrl_mgr: apex.control_2.ControlManager
        :param blend_graph: A graph to blend the source transform with the target transform
        :type blend_graph: apex.Graph
        :return: The result of blending the source and target transforms.
        :rtype: hou.Matrix4
        """
    def xform(self, frame: float, ctrl_mgr: ControlManager) -> hou.Matrix4 | None:
        """
        Evaluates and returns this bake source's transform at the given frame.

        :param frame: The frame at which to evaluate the transform
        :type frame: float
        :param ctrl_mgr: The control manager setup in addControlsToManager. This should
                         contain all source and target controls.
        :type ctrl_mgr: apex.control_2.ControlManager
        :return: The source transform at the given frame or None. If None is returns,
                 the control will not be baked.
        :rtype: hou.Matrix4 or None
        """
    def doApplyEulerFilter(self) -> bool:
        """
        Returns whether to apply Euler filtering to the rotation parameters.

        :return: Whether to apply an Euler filter.
        :rtype: bool
        """
    def xform_offset(self) -> hou.Matrix4 | None:
        """
        Evaluates and returns this bake source's transform offset in world space.

        :return: This baker source's transform offset
        :rtype: hou.Matrix4
        """

class BakeSourceParmsBase:
    """
    The base class used to bake a parameter values directly into the componets
    of a rig's control.

    :param components: The control's components to bake
    :type components: str
    :param frame_set: A searchable object that defines the set of frames
                      for which this bake source is valid
    :type frame_set: None or a searchable object
    """
    components: Collection[str]
    frame_set: _FrameSetLike | None
    def __init__(self, components: str | Collection[str] = '*', frame_set: _FrameSetLike | None = None) -> None: ...
    def addControlsToManager(self, scene: Scene, ctrl_mgr: ControlManager) -> None:
        """
        Adds all controls needed for evaluation and baking into the given
        control manager.

        :param scene: An apex scene.
        :type scene: apex.Scene
        :param ctrl_mgr: A control manager to update
        :type ctrl_mgr: apex.control_2.ControlManager
        """
    def doApplyEulerFilter(self) -> bool:
        """
        Returns whether to apply Euler filtering to the rotation parameters.

        :return: Whether to apply an Euler filter.
        :rtype: bool
        """
    def doBakeAtFrame(self, frame: float) -> bool:
        """
        Returns whether to use this bake source when baking at the given frame.

        :return: Whether to use this bake source when baking at 'frame'
        :rtype: bool
        """
    def type(self) -> Literal[1]:
        """
        Returns the type of the bake source.

        :return: The type of the bake
        :rtype: int
        """
    def bakeParms(self, frame: float, target_ctrl_path: str, scene: Scene, ctrl_mgr: ControlManager, orig_parms: _apex.Dict) -> dict[str, _apex._Value | None] | None:
        """
        Computes the new values for the target control's parameters at the given
        frame and returns them in a dictionary

        :param frame: The frame at which to bake
        :type frame: float
        :param target_ctrl_path: The path to the control in which to bake the parameters.
        :type target_ctrl_path: str
        :param scene: The apex scene
        :type scene: apex.Scene
        :param ctrl_mgr: The control manager setup in addControlsToManager. This should
                         contain all source and target controls.
        :type ctrl_mgr: apex.control_2.ControlManager
        :param orig_parms: The original parameters for the target control.
        :type orig_parms: apex.Dict
        :return: A dictionary of the target controls new parameter values
        :rtype: apex.Dict
        """
    def parms(self, frame: float, scene: Scene, ctrl_mgr: ControlManager) -> _ParmValues:
        """
        Returns the parameters to bake into the target control at the given frame.

        :param frame: The frame at which the parameters are being baked.
        :type frame: float
        :param scene: The apex scene.
        :type scene: apex.Scene
        :param ctrl_mgr:
        :type ctrl_mgr: apex.control_2.ControlManager
        :return: The parameters to bake into the target control by component.
        :rtype: apex.Dict
        """

class BakeSourceXform(BakeSourceXformBase):
    """
    A basic bake source deriving from BakeSourceXformBase for baking a specific
    transform into a rig control.

    :param xform: The transform matrix to bake into the target control.
    :type xform: hou.Matrix4
    :param components: The trs components to be cracked from the matrix
    :type components: str
    :param frame_set: A searchable object that defines the set of frames
                      for which this bake source is valid
    :type frame_set: None or a searchable object
    """
    def __init__(self, xform: hou.Matrix4, components: str = '*', frame_set: _FrameSetLike | None = None, xform_offset: hou.Matrix4 | None = ...) -> None: ...
    def xform(self, frame: float, ctrl_mgr: ControlManager) -> hou.Matrix4:
        """
        An overload of BakeSourceXformBase.xform(...) function that simply returns
        this bake source's transform to bake into the control.
        The frame and ctrl_mgr inputs are only here to satisfy the overload.

        :param frame:
        :type frame: float
        :param ctrl_mgr:
        :type ctrl_mgr: apex.control_2.ControlManager
        :return: This bake source's transform
        :rtype: hou.Matrix4
        """
    def setXform(self, xform: hou.Matrix4) -> None:
        """
        Update the _xform data member.

        :param xfor: a new xform for the control.
        :type xform: hou.Matrix4
        """

class BakeSourceParms(BakeSourceParmsBase):
    """
    A bake source deriving from BakeSourceParmsBase for baking a specific set
    of parameters into a rig control.

    :param components: The control's components to bake
    :type components: str
    :param frame_set: A searchable object that defines the set of frames
                      for which this bake source is valid
    :type frame_set: None or a searchable object
    """
    def __init__(self, parms: _ParmValues, components: str | Collection[str] = '*', frame_set: _FrameSetLike | None = None) -> None: ...
    def parms(self, frame: float, scene: Scene, ctrl_mgr: ControlManager) -> _ParmValues:
        """
        An overload of the BakeSourceParmsBase.parms(...) function that simply
        returns the bake source's parameter dictionary to bake into the control.
        The frame and scene inputs are only here to satisfy the overload.
        
        An example dictionary would be:
        parms = apex.Dict({
            't': hou.Vector3(1,2,3),
            'r': hou.Vector3(4,5,6),
            'x': 1.0
        })

        :param frame:
        :type frame: float
        :param scene:
        :type scene: apex.Scene
        :return: The bake source's parameter dictionary
        :param ctrl_mgr:
        :type ctrl_mgr: apex.control_2.ControlManager
        :rtype: apex.Dict
        """
    def setParms(self, parms: _ParmValues) -> None:
        """
        Change the self._parms dict.

        :param parms: New dict for all the parameters.
        :type parms: apex.Dict
        """

class BakeSourceControlXform(BakeSourceXformBase):
    """
    A bake source deriving from BakeSourceXformBase for baking the
    transform of one control into another control with an optional
    offset.
    This operates as if there were a constraint between the two controls.

    :param ctrl_path: A path to the source control.
    :type ctrl_path: str
    :param components: The trs components to be cracked from the matrix
    :type components: str
    :param offset: An optional offset matrix between the source control and the
                   transform matrix that should be used as the source.
    :type offset: hou.Matrix4
    :param frame_set: A searchable object that defines the set of frames
                      for which this bake source is valid
    :type frame_set: None or a searchable object
    """
    ctrl_path: str
    offset: hou.Matrix4 | None
    def __init__(self, ctrl_path: str, components: str = '*', offset: hou.Matrix4 | None = None, frame_set: _FrameSetLike | None = None, xform_offset: hou.Matrix4 | None = ...) -> None: ...
    def addControlsToManager(self, scene: Scene, ctrl_mgr: ControlManager) -> None:
        """
        An overload of the BakeSourceXformBase.addControlsToManager function
        that adds the source control to the control manager.

        :param scene: An apex scene.
        :type scene: apex.Scene
        :param ctrl_mgr: The control manager to extend.
        :type ctrl_mgr: apex.control_2.ControlManager
        """
    def xform(self, frame: float, ctrl_mgr: ControlManager) -> hou.Matrix4 | None:
        """
        An overload of the BakeSourceXformBase.xform function
        that retreives returns the source control's xform, optionally
        multiplied by the offset.

        :param frame: Unused
        :type frame: float
        :param ctrl_mgr: The control manager setup in addControlsToManager. This should
                         contain all source and target controls.
        :type ctrl_mgr: apex.control_2.ControlManager
        :return: The transform matrix of the source control optionally multiplied
                 by the offset or None
        :rtype: hou.Matrix4 or None
        """

class BakeSourceControlParms(BakeSourceParmsBase):
    """
    A bake source deriving from BakeSourceParmsBase for baking the parameters
    from one control into the parameters for another control.

    :param ctrl_path: The source control path
    :type ctrl_path: str
    :param components: The control's components to bake
    :type components: str
    """
    ctrl_path: str
    def __init__(self, ctrl_path: str, components: str | Collection[str] = '*', frame_set: _FrameSetLike | None = None) -> None: ...
    def addControlsToManager(self, scene: Scene, ctrl_mgr: ControlManager) -> None:
        """
        An overload of the BakeSourceParmsBase.addControlsToManager function
        that adds the source control to the control manager.

        :param scene: An apex scene.
        :type scene: apex.Scene
        :param ctrl_mgr: The control manager to extend.
        :type ctrl_mgr: apex.control_2.ControlManager
        """
    @staticmethod
    def parmsForControl(scene: Scene, ctrl_mgr: ControlManager, ctrl_path: str) -> dict[str, _apex._Value | None]:
        """
        A static function that retreives the post constraint parameters for a
        control, packing them in a dictionary from the generic components to
        the value of the component, ignoring actual name of the parameter.

        :param scene: An apex scene.
        :type scene: apex.Scene
        :param ctrl_mgr: The control manager setup in addControlsToManager. This should
                         contain all source and target controls.
        :type ctrl_mgr: apex.control_2.ControlManager
        :param ctrl_path: The path to the source control
        :type ctrl_path: str
        :return: A dictionary from the component strings to the values of the given
                 control's component parameters.
        :rtype: dict
        """
    def parms(self, frame: float, scene: Scene, ctrl_mgr: ControlManager) -> dict[str, _apex._Value | None]:
        """
        An overload of the BakeSourceParmsBase.parms function that retreives
        the source control's post constraint parameters in a format that is
        usable by BakeSourceParmsBase.bakeParms

        :param frame: Unused
        :type frame: float
        :param scene: The active apex scene
        :type scene: apex.Scene
        :param ctrl_mgr: The control manager setup in addControlsToManager. This should
                         contain all source and target controls.
        :type ctrl_mgr: apex.control_2.ControlManager
        :return: A dictionary from the component strings to the values of the source
                 control's component parameters.
        :rtype: dict
        """

class RigBaker:
    """
    An APEX class for managing and excuting bake actions into the controls of a
    specific rig.

    :param scene: The active scene
    :type scene: apex.Scene
    :param rig_path: The path to the target rig
    :type rig_path: str
    :param bake_map: A map from the target controls of the bake to their Bake
                     Sources. All target controls in this dictionary must be
                     controls of the target rig
    :type bake_map: dict from str to a bake source deriving from BakeSourceXformBase or BakeSourceParmsBase
    :param write_to_muted_layer: Whether baking to a muted layer is enabled. This should be enabled when creating new override layers.
    :type write_to_muted_layer: bool
    :param buffer_keys: If true, the keys will only be written to the channel
                          primitives when `writeBufferedKeys` is called.
    :type buffer_keys: bool
    """
    rig_path: str
    bake_map: Mapping[str, _BakeSource]
    write_to_muted_layer: bool
    buffer_keys: bool
    key_buffer: list[tuple[float, _apex.Dict | None]]
    ctrl_mgr: ControlManager
    blend_graph: _apex.Graph
    prim_pattern: str
    prev_channel_geo: hou.Geometry | None
    inverse_rig: InverseRig | None
    def __init__(self, scene: Scene, rig_path: str, bake_map: Mapping[str, _BakeSource], write_to_muted_layer: bool = True, buffer_keys: bool = False) -> None: ...
    @property
    def scene(self) -> Scene | None: ...
    def doBakeAtFrame(self, frame: float) -> bool:
        """
        Returns whether the baker should bake at the current frame.

        :param frame: The frame
        :type frame: Int or Float
        """
    def getEvaluatedBakeParms(self, frame: float) -> _apex.Dict | None:
        """
        Evaluates new parameters for the target rig at the given frame based
        upon the bake map and sets them into the keys of the channel primitives

        :param frame: The frame at which to bake.
        :type frame: float
        """
    def bakeAtFrame(self, frame: float, add_new: bool = True) -> None:
        """
        Bakes the new parameters for the target rig at the given frame based
        upon the bake map and sets them into the keys of the channel primitives

        :param frame: The frame at which to bake.
        :type frame: float
        :param add_new: Whether to create a new key in the channel primitives if
                        none exists
        :type add_new: bool
        """
    def writeBufferedKeys(self, add_new: bool = True) -> None:
        """
        Writes all of the keys in the key buffer to the channel primitives bindings
        """
    def getChannelGeo(self) -> hou.Geometry | None:
        """
        Returns the channel primitive geometry for the rig on the current
        animation layer.
        """
    def forEachChannel(self, fn: Callable[[hou.ChannelPrim], object]) -> None:
        """
        Runs a function on each channel that can be altered by the rig
        baker.

        :param fn: The function to run.
        :type fn: A function pointer that takes a channel primitive.
        """
    def startBakeUndo(self) -> bool:
        """
        Backups the current version of the channel primitive geometry
        to start an undo block.
        """
    def endBakeUndo(self, state: _AnimateState, name: str = 'Bake Animation') -> bool:
        """
        Adds a SetChannelUndo block with the changes from the bake.

        :param state: The viewer state.
        :type state: A viewer state.
        :param name: The name of the undo block
        :type name: String
        """
    def updateInputGeometriesFromScene(self) -> None: ...

def bakeLayerWeightRanges(scene: Scene, key_frame_ranges: Sequence[Sequence[float]]) -> None:
    """
    Sets up the weight channel of the active layer to mask in only the given
    key frame ranges.
    
    :param scene: The active scene.
    :type scene: apex.Scene
    :param key_frame_ranges: The ranges to mask in.
    :type key_frame_ranges: tuple of (float, float)
    """
def getRigControlToChannelMapFromGeo(scene: Scene, rig_path: str, anim_geo: hou.Geometry, ctrl_paths: Iterable[str], components: Container[str] = '*') -> dict[str, dict[str, list[int]]] | None: ...
def getRigControlToChannelMap(scene: Scene, rig_path: str, ctrl_paths: Iterable[str], layer: str = '', components: Container[str] = '*') -> dict[str, dict[str, list[int]]] | None: ...
def getResampledFrames(resample: int, start_frame: int, end_frame: int) -> list[int]:
    """
    Builds a unique sorted list of resampled frames for baking.
    """
def getExistingFrames(scene: Scene, ctrl_paths: Iterable[str], layer: str | None = None) -> list[float]:
    """
    Builds a unique sorted list of all of the keyed frames across the parameters
    of a list of controls.
    """
def buildControlFrameSets(scene: Scene, ctrl_paths: Iterable[str], layer: str | None = None) -> dict[str, ChannelFrameSet]:
    """
    Builds a dictionary from control paths to frame sets with all of
    the existing keys on the control's parameters.
    """

class BakeKeyingParms:
    """
    A class which is used to retrieve and store the list
    of baking parameters that are used for determining 
    the sets of keys to bake for each control.

    This class takes in the dictionary from the bake tab and an optional
    additional set of frames to bake.
    """
    keep_existing: bool
    resample: int
    start: int
    end: int
    extra_frames: list[float]
    def __init__(self, kwargs: _BakeParms, extra_frames: Iterable[float] = ...) -> None: ...

class BakeLayerParms:
    """
    A class which is used to retrieve and store the list
    of baking parameters that are used for creating a new layer
    for the baked animation.

    This class takes in the dictionary from the bake tab and an optional
    prefix and suffix for the newly baked layer
    """
    bake_to_new_layer: bool
    additive: bool
    layer_prefix: str
    layer_suffix: str
    def __init__(self, kwargs: _BakeParms, layer_prefix: str = '', layer_suffix: str = '') -> None: ...
    def layerName(self, layer_name: str) -> str: ...

def buildFrameSetsForControls(scene: Scene, ctrl_paths: Iterable[str], keying_parms: BakeKeyingParms, layer: str | None = None) -> tuple[list[float], list[float], dict[str, ChannelFrameSet | FrameSetOr]]:
    """
    Using many common baking options, this function will return a list of frames
    to bake on, a list of keyed frames to delete, and valid frame sets for each
    control.

    :param scene: The Scene on which to run the bake.
    :type scene: apex.Scene
    :param ctrl_paths: The list of controls to generate the frame sets for.
    :type ctrl_paths: List of String
    :param keying_parms: The keying parameters for the bake
    :type keying_parms: BakeTimingParms
    """
def bakeControlParms(state: _AnimateState, ctrl_paths: Iterable[str], keying_parms: BakeKeyingParms, layer_parms: BakeLayerParms) -> None:
    """
    Bake Controls from the viewer state based upon their post constraint
    parameters and add an undo block for the bake.
    The frame range for the bake is the selection range if it exists and
    the playbar range otherwise.

    :param state: The viewer state.
    :type state: A viewer state class.
    :param ctrl_paths: The controls to bake.
    :type ctrl_paths: String list
    :param keying_parms: The keying parameters for the bake.
    :type keying_parms: BakeKeyingParms
    :param layer_parms: The layer parameters for the bake.
    :type layer_parms: BakeLayerParms
    """
def bakeControls(state: _AnimateState, rig_bakers: Collection[RigBaker], keying_parms: BakeKeyingParms, layer_parms: BakeLayerParms, post_process_channels: Callable[[hou.ChannelPrim], object] | None = None, pre_bake_frame: Callable[[float], object] | None = None) -> None:
    """
    Bake Controls from the viewer state based upon their rig bakers and
    add an undo block for the bake.

    :param state: The viewer state.
    :type state: A viewer state class.
    :param rig_bakers: The rig bakers to bake
    :type rig_bakers: RigBaker list
    :param keying_parms: The keying parameters for the bake.
    :type keying_parms: BakeKeyingParms
    :param layer_parms: The layer parameters for the bake.
    :type layer_parms: BakeLayerParms
    :param post_process_channels: After baking, this function will be called
                                  on each channel primitive to post process
                                  the channels. Before this is called, the
                                  channels slopes will be smoothed.
    :type post_process_channels: A function or None
    :param pre_bake_frame: Just before a frame is baked, this function will be
                           with the frame that will be baked
    :type pre_bake_frame: A function or None
    """
def bakeTransforms(scene: Scene, ctrl_paths_: Sequence[str], ctrl_transforms: Sequence[hou.Matrix4 | _ParmValues], ctrl_dict_first_index: int, frames: Iterable[float], buffer_keys: bool = False, convert_to_apex_dicts: bool = False) -> None:
    """
    Bake Controls from the scene based on a list of transforms.
    :param scene: The active scene.
    :type scene: apex.Scene
    :param ctrl_paths: The control paths to bake.
    :type ctrl_paths: String list
    :param ctrl_transforms: The control transforms for the baking with a
     transform per control multiplied by the number of frames.
    :type ctrl_transforms: hou.Matrix4 list or an apex.Dict for abstract
     control values.
    :param ctrl_dict_first_index: The first ctrl index that isn't a hou.Matrix.
    :tyoe ctrl_dict_first_index: Int
    :param frames: An iterable object of the frames to bake on.
    :type frames: An iterable object of Floats.
    :param buffer_keys: If true, the new keys will be buffered and then written
                        out at the end of baking. This should be used when
                        writing a key would alter the baked value of the next key.
    :type buffer_keys: Bool
    :param convert_to_apex_dicts: If true, the dict entries are convert from a
                        dict() to an apex.Dict()
    :type param convert_to_apex_dicts: Bool
    """
