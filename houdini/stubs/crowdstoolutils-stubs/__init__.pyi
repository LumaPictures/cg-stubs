import hou
import typing
from houtypes import ShelfToolKwargs
from typing import Literal, Sequence

SOLVER_SOURCES_INPUT: int
SOLVER_STATES_INPUT: int
SOLVER_TRANSITIONS_INPUT: int

def populate(agent_objects: Sequence[hou.ObjNode], source_object: hou.ObjNode | None, default_state: str = '') -> hou.ObjNode: ...
def populateInteractive(kwargs: ShelfToolKwargs) -> None: ...
def chooseStatesToCreate(source_geo: hou.Geometry, dopnet: hou.OpNode | None) -> list[str]: ...
def simulate(source_object: hou.ObjNode) -> tuple[hou.DopNode, hou.DopNode]:
    """ Sets up a crowd simulation for the agents in source_object.
        Returns the merge nodes for states and transitions.
    """
def simulateInteractive(kwargs: ShelfToolKwargs) -> None:
    """ Create crowd dop sim based on user input or default setup if none
    """
@typing.overload
def selectSOPGeometry(prompt: str, allow_multisel: Literal[False] = ..., allowed_types: Sequence[str] = ...) -> hou.ObjNode: ...
@typing.overload
def selectSOPGeometry(prompt: str, allow_multisel: Literal[True], allowed_types: Sequence[str] = ...) -> list[hou.ObjNode]: ...
@typing.overload
def selectSOPGeometry(prompt: str, allow_multisel: bool = ..., allowed_types: Sequence[str] = ...) -> hou.ObjNode | list[hou.ObjNode]: ...
def selectState(dopnet: hou.OpNode, message: str) -> hou.DopNode | None:
    """ Prompts the user to select one of the states in the crowd simulation
        (or all states). Returns the crowd state DOP, or None if all states
        were selected.
    """
def findCrowdSim() -> hou.OpNode: ...
def findCrowdSolver(dopnet: hou.OpNode) -> hou.DopNode: ...
def findStates(dopnet: hou.OpNode) -> tuple[list[hou.DopNode], list[str]]:
    """ Returns a list of the crowd state nodes and state names."""
def wireNodeInState(node: hou.DopNode, state_node: hou.DopNode | None, crowdsolver: hou.DopNode) -> None:
    """ Wire the given node into the state's stream. If state_node is None, the
        node is wired just before the crowd solver's state input, so it will
        apply to all states.
    """
def addterrain(kwargs: ShelfToolKwargs) -> None:
    """ Add terrain object to the crowd simulation.
    """
def addobstacle(kwargs: ShelfToolKwargs) -> None:
    """ Add obstacle object to the crowd simulation.
    """
def addClip(agent_obj: hou.ObjNode, input_type: str, subnet: hou.ObjNode | None, clipname: str, filepath: str | None = None, lopnode: hou.LopNode | None = None) -> hou.SopNode: ...
def bakeAgent(input_type: str, subnet: hou.ObjNode | None, filepath: str | None, agentname: str, clipname: str, lopnode: hou.LopNode | None = None) -> hou.ObjNode: ...
def bakeAgentInteractive(kwargs: ShelfToolKwargs) -> None: ...
def addClipInteractive(kwargs: ShelfToolKwargs) -> None: ...
def crowdpath(kwargs: ShelfToolKwargs) -> None:
    """ Ask user for curve object and add it as path to the crowd sim.
    """
def crowdlookat(kwargs: ShelfToolKwargs) -> None:
    """ Ask user for lookat object and which state to add it to the crowd sim
    """
def crowdpaintdensity(kwargs: ShelfToolKwargs) -> None:
    """ Create setup to paint density for crowdsource
    """
def addcollisionlayer(kwargs: ShelfToolKwargs) -> None:
    """ Add a collision layer to an agent.
    """
def configurejoints(kwargs: ShelfToolKwargs) -> None:
    """ Add an Agent Configure Joints node and a test simulation.
    """
def crowdtargetposition(kwargs: ShelfToolKwargs) -> None:
    """ Add a target position steering force that agents will try to reach
    """
def crowdagentcam(kwargs: ShelfToolKwargs) -> None:
    """ Create cameras attached to the agent transforms
    """
def applyPresetForKnownAgents(node: hou.OpNode, agentname: str) -> bool:
    """
    Applies presets for built-in characters such as mocapbiped1, if the node
    has a legacy preset or recipe node preset with that name.
    """
def findInputAgentName(node: hou.SopNode, input_index: int = 0, group_parm_name: str = 'group') -> str:
    """
    Finds the 'agentname' for the agent primitive from the node's input
    geometry, or returns the empty string.
    """
def findInputAgent(node: hou.SopNode, input_index: int = 0, group_parm_name: str = 'group') -> hou.Agent | None:
    """ Finds the agent primitive from the node's input geometry, or returns
        None.
    """
def findInputAgentDefinitions(node: hou.SopNode, frame: float | None = None, input_index: int = 0, group_str: str | None = None, group_type: hou.EnumValue[hou.geometryType] | None = ...) -> tuple[hou.AgentDefinition, ...] | list[hou.AgentDefinition]:
    """ Finds the unique agent definitions from the node's input geometry."""
def findCrowdObject(dopnode: hou.DopNode) -> hou.DopObject | None: ...
def findDopAgentDefinitions(node: hou.DopNode) -> tuple[hou.AgentDefinition, ...] | list[hou.AgentDefinition]:
    """ Finds the unique agent definitions in the processed DOP object."""
def findAgent(geo: hou.Geometry | None, group_str: str = '') -> hou.Agent | None:
    """ Finds the agent primitive from the given geometry, or returns None."""
def findAgentDefinitions(geo: hou.Geometry, group_str: str = '', group_type: hou.EnumValue[hou.geometryType] | None = ...) -> tuple[hou.AgentDefinition, ...] | list[hou.AgentDefinition]:
    """ Wrapper around hou.crowds.findAgentDefinitions that does some exception
        handling.
    """
def buildMenuStringList(names: Sequence[str]) -> list[str]:
    ''' Duplicates each element in a list of strings.
        For example, ["walk", "run"] becomes ["walk", "walk", "run", "run"]
    '''
def _unpackClipProperties(crowd_geo: hou.Geometry, group_str: str, group_type: hou.EnumValue[hou.geometryType] | None) -> hou.Geometry:
    """
    Unpacks the clip properties from the agent definition.
    This is used for SOPs that don't have an explicit clip properties input,
    such as motion paths.
    """
def buildClipMenu(node: hou.SopNode, include_clip_properties: bool = False, clip_properties_input: int = -1, input_index: int = 0, group_str: str = '', group_type: hou.EnumValue[hou.geometryType] | None = ...) -> list[str]:
    """ Build a menu containing the available clip names for an agent."""
def buildMotionPathClipMenu(node: hou.SopNode) -> list[str]:
    """
    Builds a menu containing the available clip names for the agents
    associated with the group of motion paths.
    The SOP must have the standard two inputs for motion paths and agents.
    """
def buildDopClipMenu(node: hou.DopNode) -> list[str]:
    """ Build a menu containing the available clip names for an agent in the
        processed DOP object, including those defined in the clip properties.
    """
def buildClipChannelMenu(node: hou.SopNode) -> list[str]:
    """
    Build a menu containing the channel names from all of the agent's clips.
    """
def buildDopStateMenu(node: hou.DopNode) -> list[str]:
    """ Build a menu containing the states in the crowd simulation."""
def buildChannelMenu(node: hou.SopNode) -> list[str]:
    """ Build a menu containing the channel names from an agent's rig."""
def buildTransformMenu(node: hou.SopNode) -> list[str]:
    """ Build a menu containing the transform names from an agent's rig."""
def buildTransformGroupMenu(node: hou.SopNode, input_index: int = 0) -> list[str]:
    """ Build a menu containing the available transform groups."""
def buildDopTransformGroupMenu(node: hou.DopNode) -> list[str]:
    """ Build a menu containing the available transform groups for an agent in
        the processed DOP object.
    """
def buildMotionPathTransformGroupMenu(node: hou.SopNode) -> list[str]:
    """
    Builds a menu containing the available transform groups for the agents
    associated with the group of motion paths.
    The SOP must have the standard two inputs for motion paths and agents.
    """
def buildLayerMenu(node: hou.SopNode, frame: float | None = None) -> list[str]:
    """ Build a menu containing the available layer names."""
def buildShapeMenu(node: hou.SopNode, frame: float | None = None) -> list[str]:
    """ Build a menu containing the available shape names."""
def buildShapeDeformerMenu() -> list[str]:
    """ Build a menu containing the available shape deformer names."""
def buildMetadataMenu(node: hou.SopNode, input_index: int = 0, group_parm: str | None = None) -> list[str]:
    """ Build a menu containing the available metadata keys."""
def selectFromTreeView(node: hou.OpNode, parmtuple: hou.ParmTuple, names: Sequence[str], paths: Sequence[str], exclusive: bool = True) -> None:
    """ Edit a parm via a tree chooser that selects from a list of paths."""
def selectJoint(node: hou.SopNode, parmtuple: hou.ParmTuple, exclusive: bool = True) -> None:
    """ Open a tree chooser to select a joint name."""
def findInputStateNames(node: hou.OpNode, known_nodes: set[hou.Node] | None = None) -> list[str]:
    """
    Return a list of the crowd states that the DOP is operating on, via its
    inputs. This is similar to opstreamname, but uses the 'statename' parameter
    and doesn't generate a group string.
    """

INVALID_INTERMEDIATE_TYPES: frozenset[str]

def findInputTriggerName(node: hou.OpNode, input_index: int = 0) -> str:
    """
    Find the name of the trigger point attribute generated by the input node.
    """
def computeRotationLimits(node: hou.SopNode, instance: int | str) -> None:
    """ Determine joint limits by analyzing the agent's animation clips.
    """
def createLimitsForCollisionLayer(node: hou.SopNode) -> None:
    """ Add an auto-computed joint limit for each non-root transform with a
        shape attached to it in the collision layer.
    """
