import _apex
import apex
import hou
from apex import mapping_2 as mapping, ragdollutils as ragdollutils
from apex.mapping_2 import ControlEndpoint as ControlEndpoint, MappingCollection as MappingCollection
from apex.ragdollbase import RagdollJointEndpoint as RagdollJointEndpoint, RagdollStateBase as RagdollStateBase, _AnimateState
from apex.ragdolltool_2 import RagdollTool as RagdollTool
from apex.scenebookmarkmanager import SceneBookmarkManager as SceneBookmarkManager
from collections.abc import Container, Iterable, Mapping, Sequence
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Literal, Never

ACTIVE_SRC_COLOR: hou.Color
ACTIVE_DST_COLOR: hou.Color
BROKEN_COLOR: hou.Color
CONSTRAINT_NAME: str
CONSTRAINT_RIG: str

class RagdollConstraintsGadgetEvalMode(Enum):
    REBUILD = 0
    UPDATE = 1
    UPDATE_FROM_POSE = 2

@dataclass
class ConstraintsStateHolder:
    parms: apex.Dict
    channels: hou.Geometry
    selection: list[str]
    handleparms: apex.Dict
    bookmarkdata: apex.Dict

class RagdollConstraintAnchorEndpoint(mapping.ControlEndpoint):
    """
    Defines a custom control endpoint for constraint anchors    
    """
    control_name: str
    character_name: str
    def __init__(self, control_name: str, character_name: str, constraint_name: str, color: hou.Color) -> None: ...
    def color(self) -> hou.Color: ...

class RagdollConstraintsManager:
    """
    Class that stores custom constraints dicts 
    and channels
    self.parms is a dictionnary that stores all the custom constraints
    self.channels is a hou.Geometry() containing the channelprims used
    for animating the constraint parameters    
    """
    parms: apex.Dict
    channels: hou.Geometry
    ATTRIBUTES: ClassVar[dict[str, int | float]]
    _selected_constraints: list[str]
    def __init__(self) -> None: ...
    def createConstraintsCollection(self, tool: RagdollStateBase, active: bool, frame: float) -> MappingCollection | None:
        """
        Creates a mapping collection of all the constraints
        in the manager
        
        parm tool: RagdollTool, this is required to create the RagdollJointEndpoints
        
        parm active: when True, only draw enabled constraints
        
        parm frame: frame to evaluate
        """
    def isConstraintActive(self, constraint_name: str, constraint_dict: apex.Dict, frame: float) -> bool:
        """
        Checks constraints dict and constraints channels for enable and stiffness
        to see if the constraint needs to be displayed in the viewport 
        returns True is the constraint needs to be drawn 
        """
    def getConstraintChannels(self, constraint_name: str) -> list[str]:
        """
        From a constraint name, get all the channels associated with it
        ex:
        constraint1 -> [stiffness, damping, restlength]    
        """
    def getConstraintParms(self, constraint_name: str) -> apex.Dict | None:
        """
        Given a constraint_name get its associated parms dict
        """
    def getConstraintAttribute(self, constraint_name: str, attrib: str) -> _apex._Value | None:
        """
        Given a constraint name and an attribute name, return
        that attributes value    
        """
    def getConstraintVisibility(self, constraint_name: str) -> bool: ...
    def isDuplicateConstraint(self, src_name: str, dst_name: str) -> bool:
        """
        We don't want a user creating a constraint between two joints
        that are already constrained... so if src and dst are the same as 
        an existing constraint, we return true and don't create it    
        """
    def addConstraint(self, constraint_name: str, constraint_dict: apex.Dict) -> None:
        """
        Adds a constraint to the manager
        """
    def removeConstraint(self, constraint_name: str) -> None:
        """
        Removes a constraint from the manager    
        """
    def blastConstraintChannels(self, constraint_name: str) -> None:
        """
        Removes the channel primitives associated with
        a constraint    
        """
    def createConstraint(self, src: str, dst: str, enable: bool = True, stiffness: float = 25.0, damping: float = 1.0, src_pos: hou.Vector3 = ..., dst_pos: hou.Vector3 = ..., src_offset: hou.Matrix4 = ..., dst_offset: hou.Matrix4 = ..., override_angular: bool = False, src_restxform: hou.Matrix4 = ..., dst_restxform: hou.Matrix4 = ..., visible: bool = True, disablecollisions: bool = False, lock: bool = False) -> apex.Dict:
        """
        Creates a constraint dictionary   
        """
    def updateSelectedConstraints(self, constraint_name: str) -> None: ...
    def getSelectedConstraints(self) -> list[str]: ...
    def setSelectedConstraints(self, constraints: list[str]) -> None: ...
    def setSelectedConstraintsFromSelHandler(self, lines: Iterable[str]) -> None: ...
    def clearSelectedConstraints(self) -> None: ...
    def hasSelectedConstraints(self) -> bool: ...
    def createConstraintFromSelection(self, selection: Mapping[hou.SimpleDrawable, Iterable[hou.Prim]], scene: apex.Scene, graph: str) -> tuple[Literal[False], None] | tuple[Literal[True], list[str]]:
        """    
        From a viewport selection, create a custom constraint
        
        """
    def getConstraintFromGadgetMappingName(self, mapping_name: str) -> tuple[str, apex.Dict] | None:
        """
        Given a mapping name get the dictionary corresponding to it  
        mapping_name is formatted this way: {src}<->{dst}
        so splitting that we can get src and dst
        """
    def getGadgetMappingNameFromConstraint(self, cst_name: str) -> str: ...
    def deleteSelectedConstraints(self) -> bool:
        """
        Hitting del key in the state while a constraint(s) is selected
        deletes it    
        """
    def destroyConstraintNodes(self, rig: apex.Graph, constraints: apex.Dict) -> None: ...
    def _loadParms(self, constraints: hou._OptionDict) -> None:
        """
        Loads the parms from the scene and sets
        last_constraint_index    
        """
    def computeAnchorRotationOffset(self, src_xform: hou.Matrix3, dst_xform: hou.Matrix3) -> hou.Matrix3:
        """
        When creating a custom constraint we want the anchors original rotations
        to be preserved otherwise the solver tries to match their orientations
        which causes crazy twists on the first simulated frame    
        """
    def overrideAngularStiffness(self, value: bool, constraint_name: str) -> None: ...
    def setConstraintVisibility(self, on: bool, constraint_name: str) -> None: ...
    def setConstraintProperty(self, value: _apex._ValueArg, constraint_name: str, property_name: str) -> None: ...
    def validateParms(self) -> None:
        """
        Make sure all the keys exist in the parms dict
        if a key does not exist, set it to default
        this should not happen 
        but because we added a key for angular override
        older dicts don't have that key and will cause the 
        solver to assert    
        """
    def createConstraintAnchorHandles(self, scene: apex.Scene, graph: str, constraint: apex.Dict, name: str, src_offset: hou.Matrix3) -> None:
        """
        calls the ConstraintRigBuilder which adds to the rig the necessary nodes
        to add handles to the constraint gizmo
        """
    def resetRig(self, rig: apex.Graph) -> None: ...

class RagdollConstraintRigBuilder:
    """
    Given a graph, performs operations to create or destroy 
    the necessary APEX Nodes for constraints
    This class mainly exists to group all the methods in one place and
    not pollute the constraint manager with apex rig related methods
    """
    rig: apex.Graph
    cst_name: str
    constraint: apex.Dict | dict[str, Never]
    tag: str
    color: hou.Color
    def __init__(self, rig: apex.Graph, cst_name: str, constraint: apex.Dict | dict[str, Never]) -> None: ...
    def resetRig(self) -> None: ...
    def buildConstraintRig(self, offset: hou.Matrix3) -> None: ...
    def destroyConstraintRig(self) -> None:
        """
        When a constraint is deleted we want to remove the relevant nodes
        associated with the constraint.
        Because we tag all the nodes with the constraint name, 
        we can find them by tagsand delete them
        however some nodes might have more than one constraint tag, 
        which means they need to persist, but that tag needs to be removed
        """
    def updateOffsets(self) -> None: ...

class RagdollBookmarkManager(SceneBookmarkManager):
    """
    For feature parity with normal constraints we want to be able to
    have bookmarks for when constraints are active    
    """
    ragdolltool: RagdollTool
    constraints_manager: RagdollConstraintsManager
    def __init__(self, state: _AnimateState, type_name: str, constraints_manager: RagdollConstraintsManager, tool: RagdollTool) -> None: ...
    def loadSavedBookmarks(self, data: Mapping[str, hou._OptionValue] | apex.Dict | None) -> None: ...
    def addConstraintBookmarks(self, labels: Iterable[str], frame_range: hou.Vector2 | Sequence[float], data: Iterable[_apex._ValueArg]) -> None:
        """
        Called when creating a constraint / constraints in the state when
        a frame range is selected. 
        Creates a bookmark for each constraint
        """
    def removeConstraintBookmarks(self, names: Iterable[str]) -> None:
        """
        Given a Tuple of constraint names, remove associated bookmarks    
        """
    def addConstraintBookmark(self, label: str, frame_range: hou.Vector2 | Sequence[float], data: _apex._ValueArg, layer: str, color: hou.Color = ...) -> hou.Bookmark | None:
        """
        Wrapper around steps needed to create a bookmark    
        """
    def showSelectedBookmarks(self, names: Container[str]) -> None: ...
    def getInfoFromBookmarkID(self, bookmark_id: int) -> tuple[str, int, int] | None: ...
    def getBookmarkIDFromConstraintName(self, name: str) -> int | None:
        """
        Given a constraint name, return the associated bookmark_id    
        """
    def getConstraintNameFromBookmarkName(self, bookmark_name: str) -> str: ...
    def getTransientData(self) -> apex.Dict:
        """
        this is a wrapper around transientData to make sure we never return
        None     
        """
    def clearTransientEntries(self) -> None: ...
    def onBookmarkInteractionFinishedEvent(self, bookmark_id: int) -> None: ...
    def onBookmarkDeletedEvent(self, bookmark_id: int) -> None:
        """
        we need to get the info before deleting otherwise we don't have access
        to it    
        the bookmark_id == bookmark.sessionId()
        """

def createConstraintMappingCollection(channels: hou.Geometry, mappingcollection: mapping.MappingCollection) -> mapping.MappingCollection:
    """
    Creates a mapping collection based on match world transforms
    channel prims that evaluate to >.5 or if mwt * stiffness > threshold   
    This creates a list of joint names. It then iterates through the mapping
    looking for these names and adds an entry to the mapping collection for 
    every hit.
    """
def setMappingGadgetAttributes(gadget: mapping.MappingGadget) -> None:
    """
    Sets attributes on mapping gadget
    """
