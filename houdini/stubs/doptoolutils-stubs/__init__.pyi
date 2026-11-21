# Houdini stubs generated from Houdini 22.0.466

import hou
import toolutils
from collections.abc import Callable as Callable, Container, Iterable, MutableSequence, Sequence
from houtypes import ShelfToolKwargs
from toolutils import OrientInfo as OrientInfo
from typing import Protocol

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Mapping
from typing import Any
from typing import TypeAlias
from typing import TypeVar
_OpNodeT = TypeVar('_OpNodeT', bound=hou.OpNode)
_ControlDefault: TypeAlias = bool | Sequence[str] | Sequence[float]
_ControlParmSpec: TypeAlias = tuple[str, str, str, int, _ControlDefault] | tuple[str, str, str, int, _ControlDefault, Mapping[str, Any]]
_RemovalChange: TypeAlias = tuple[hou.OpNode, bool, str, str]
class _InitObjectFunc(Protocol):
    def __call__(self, info: ObjectTypeInfo, dopobjectnode: hou.DopNode, solvernode: hou.DopNode, objectnode: hou.ObjNode, sopnode: hou.SopNode, subtype: str | None = ...) -> object: ...

class _InitDopFunc(Protocol):
    def __call__(self, info: ObjectTypeInfo, dopobjectnode: hou.DopNode, solvernode: hou.DopNode, subtype: str | None = ...) -> object: ...

def initDopNetwork(dopnet: hou.OpNode) -> None:
    """ Initializes a dopnetwork with gravity
    """
def createNewDopNetwork(root: hou.OpNode = ..., name: str | None = None, init_dopnet: bool = True) -> hou.OpNode:
    """ Creates the AutoDopNetwork.
    
        By default, the dop network is created at '/obj' with the name
        'AutoDopNetwork'.
    """
def createNewSimulation() -> None:
    """ This method is called by the Create New Simulation menu button
        under the simulation (brain) icon.
    """
def chooseImportNodeForDistribution(creator: hou.Node) -> hou.SopNode | None:
    """ Lets the user choose a node that is importing the given creator node.

        Returns None if there are no such nodes.
    """
def getCurrentDopNetwork(name: str | None = None) -> hou.OpNode:
    """ Find the DOP Network that is to contain the automatically 
        generated DOP nodes for our interactive DOP tools.
    """
def checkDopNetworkIsPlayer(dopnet: hou.OpNode) -> None: ...
def objectHasGeometry(objectnode: hou.ObjNode) -> bool:
    """ Check if a scene level object node contains any SOP nodes, and
        therefore creates any geometry.
    """
def isObjectSimulated(objectnode: hou.ObjNode) -> bool:
    """ Check if the object is already associated with a DOP object.
        Any geometry with a dopobject attribute and an DOP Import SOP in
        the SOP cook chain is assumed to be simulated. Empty geometry
        isn't simulated.
    """
def hasObjectSolverType(dopobject: hou.DopData | None, searchsolvertype: str) -> bool:
    """ Returns true if the given dop data type exists as solver data
        on the given dop object.  This includes all subdata of the Solver,
        so this works through multisolvers
    """
def getObjectSolverType(dopobject: hou.DopData | None) -> str | None:
    """ Returns the name of the DOP data type for the solver attached to a
        given DOP Object.
        This will return the multisolver, if present, so likely you should
        use hasObjectSolverType instead.
    """
def getDopNodeSolverNode(dopnode: hou.DopNode) -> hou.DopNode | None: ...
def getDopObjectSolverNode(dopobject: hou.DopData) -> hou.DopNode | None:
    """ Returns the node for the solver attached to a given DOP Object. """
def getSolverPosition(dopsolvernode: hou.Node) -> int:
    """ Returns the position of the supplied solver in the standard ordering 
        of DOP Solver types. This ordering is designed to provide the
        best results in the majority of situations for having solvers that
        interact with each other.
    """
def getDopDataCreator(dopdata: hou.DopData) -> hou.DopNode:
    """ Returns the DOP node that created the supplied piece of DOP data. """
def getDopObjectCreator(dopobject: hou.DopData) -> hou.DopNode:
    """ Returns the DOP node that created the supplied DOP Object. """
def getNodesImportingCreator(creator_object: hou.Node) -> list[hou.SopNode]:
    """ Finds all the nodes that are importing the given object and have the
        the render flag set.
    """
def findSolverInInput(dopnode: _OpNodeT, solvertype: str | None) -> _OpNodeT | None:
    """ Finds a node of the given solver type attached to the inputs
        of dopnode.  Will detect if the dopnode is a multisolver, in
        which case the first input is ignored.
        This function looks for node type name component matches, which means 
        that if solvertype specifies only a basename, eg 'hda', then 
        it will also find higher versions and operators in non-global namespace,
        eg 'hda::1.5', 'userx::hda', 'usery::hda::1.2', etc.
    """
def findSolverNode(dopnode: _OpNodeT, solvertype: str | None) -> _OpNodeT | None:
    """ Checks all the ouputs of dopnode to see if their is a node
        of solver type.  It also, however, will detect multisolvers
        and then chase up their solver branches looking
        for any solvers attached of this type.
        This function looks for a node whose type base name matches the given
        solvertype, which means that, for example, solvertype 'hda' will try 
        to find higher versions and operators in non-global namespace as well,
        eg 'hda::1.5', 'userx::hda', 'usery::hda::1.5', etc.
    """
def nodeHasSolverNode(dopnode: hou.OpNode, solvertype: str | None) -> bool:
    """ Check if the given dop node has the given
        solver connected as a descendant.  This is likely the safest
        way to see if something is a particle fluid, for example.
    """
def objectHasSolverNode(dopobject: hou.DopData, solvertype: str | None) -> bool:
    """ Check if the given dop object's node creator has the given
        solver connected as a descendant.  This is likely the safest
        way to see if something is a particle fluid, for example.
    """
def objectFluidType(dopobject: hou.DopData) -> str | None:
    """ Heuristics to determine the type of fluid you have.
        Results are particlefluid, fluid, smoke, fire.
    """
def nodeFluidType(dopnode: hou.OpNode) -> str | None:
    """ Heuristics to determine the type of fluid you have.
        Results are particlefluid, fluid, smoke, fire.
    """
def nodeFluidSolverNode(dopnode: _OpNodeT) -> _OpNodeT | None:
    """ Heuristics to determine the fluid solver node attached
        most directly to the given dopnode.
    """
def enforceWiringOrder(firstnode: hou.DopNode, secondnode: hou.DopNode) -> bool:
    """ Mandates that first node is to the left of second node in
        the merge node that first accepts the two instances.
        One trick is that we want this in the direction of
        the displayNode, this simplifies the problem a fair bit
    """
def getSourceSOPNode(dopobject: hou.DopData) -> hou.OpNode | None:
    """
    Returns the SOP node that the DOP object's geometry was imported from.
    """
def getSourceObjectNode(dopobject: hou.DopData) -> hou.ObjNode | None:
    """
    Returns the OBJ node that the DOP object's geometry was imported from.
    """
def getSimulatedDopObject(objectnode: hou.ObjNode) -> hou.DopObject | None:
    """ Checks to see if the object is associated with a DOP object.
        If so, returns the DOP Object it is associated with.
    """
def getSimulatedDopNode(objectnode: hou.ObjNode) -> hou.DopNode | None:
    """ Checks to see if the object is associated with a DOP object.
        If so, returns the DOP Node it is associated with.
    """
def mergeSolver(solvernode: hou.DopNode) -> None:
    """ Connects a DOP Solver node into the final merge node in a generated
        DOP Network. Solvers are connected in a particular order based on
        the solver type, so we can't simply connect the solver to the merge
        node.
    """
def createSolver(dopsolvertype: str, mergeobjects: bool, secondarysolvers: list[str] | None = None) -> hou.DopNode:
    """ Creates a DOP Solver node for the specified solver type. If the
        mergeobjects parameter is True, then all object for this solver
        type should be fed through the same solver node, and so we will
        return any existing DOP Solver node of this type. Otherwise we
        create a new solver node for each object.
        The secondarysolvers parameter specifies a list of additional solver
        types to use when searching for an existing solver.
    """
def addObjectToSolver(dopobjectnode: hou.OpNode, solvernode: hou.OpNode, mergeobjects: bool) -> None:
    """ Adds a DOP Object to an existing DOP Solver node. This function
        creates a merge node if necessary.
    """
def removeDopObjectsFromSimulation(dopnode: hou.DopNode | None, dopobjects: Container[hou.DopData], changes: MutableSequence[_RemovalChange]) -> None:
    """ This function destroys nodes or changes their group fields to
        eliminate all processing of the objects being removed.
    """
def ensureAllOrNoneObjectsListed(dopobjects: Sequence[hou.DopData]) -> list[hou.DopData]:
    """ Go through every selected DOP object and make sure that
        for each creator DOP node, either all or none of the objects on
        that node have been selected.
    """
def dopObjectsRemoveFromSimulation(dopobjects: Sequence[hou.DopData]) -> None:
    """ Remove all specified DOP Objects from the simulation. This involves
        deleting DOP nodes associated with these DOP Object, and deleting
        any SOP nodes that extract information about these DOP Objects.
    """
def getNodesToDestroyWhenRemovingModifiers(dopmodifiers: Iterable[hou.DopData]) -> list[hou.DopNode]: ...
def dopModifiersRemoveFromSimulation(dopmodifiers: Iterable[hou.DopData]) -> None: ...
def selectedDopObjectsRemoveFromSimulation(scriptargs: ShelfToolKwargs, prompt: str | None = None) -> None: ...
def genericSetDopObjectActiveState(info: ObjectTypeInfo, dopobject: hou.DopObject, active: int) -> None:
    """ There is no standard method for changing the active state of a DOP
        object. Only specialized versions of this function can actually
        change an object's active state.
    """
def selectedDopObjectsSetActiveState(scriptargs: ShelfToolKwargs, active: int, prompt: str | None = None) -> None:
    """ Set the active state of a group of DOP Objects. """
def appendDopIOCache(dopimportfield: hou.SopNode, cache_name: str | None = None) -> hou.SopNode:
    """
    Append a File Cache to a node such as DOP Import Fields.
    """
def createDopIO(parent: hou.OpNode, name: str | None, cache_name: str | None) -> tuple[hou.SopNode, hou.SopNode]:
    """
    Creates and returns a DOP Import Fields and File Cache pair, equivalent to
    the DOP I/O macro.
    """
def createObjectImportingDop(dopobjectnode: hou.DopNode, objname: str | None) -> tuple[hou.ObjNode, hou.SopNode]:
    """ Creates a new object that will hold a DOP import SOP for pulling
        the infomation from a DOP object.
    """
def genericDopObjectImport(dopobjectnode: hou.DopNode, objectnode: hou.OpNode, sopnode: hou.SopNode | None = None) -> hou.SopNode:
    """ Creates a DOP Import SOP for pulling the information from a DOP
        Object back into the source scene level object.
    """
def genericDopObjectInit(info: ObjectTypeInfo | None, dopobjectnode: hou.DopNode, solvernode: hou.DopNode | None, objectnode: hou.ObjNode, sopnode: hou.SopNode | None, subtype: str | None = None) -> hou.SopNode:
    """ Generic initialization of dop objects.  Creates a dopimport
        and sets up the usetransform flag.  Returns the resulting
        dopimport.
    """
def findOrCreateNamedMerge(solvernode: hou.OpNode, mergetype: str) -> hou.DopNode:
    """ Creates a merge node as an input to the given solvernode.
        This function tries to resolve the different meanings of
        green inputs as they aren't always at the same absolute
        offset.

        Valid mergetypes are pre,advect, vel, post, and force.
    """
def findOrCreateMergeInput(solvernode: hou.OpNode, inputnum: int) -> hou.DopNode:
    """ Creates a merge node as inputnum input to the solvernode.  If a
        merge node already exists, return it.  If a non merge node
        exists, it is made the first input of the new merge node.
    """
def genericConvertToDopObject(objectnode: hou.ObjNode, dopobjecttype: str, nodename: str | None, exact_node_type: bool = True, nosopcooking: bool = False, subtype: str | None = None) -> hou.DopNode:
    """ Creates a DOP Object from a scene level object. The specific type
        of DOP Object to create is determined by the dopobjecttype parameter,
        which is the name od a DOP node type.
    """
def genericDopConverterTool(sceneviewer: hou.SceneViewer, dopobjecttype: str, nodename: str | None, prompt: str | None = None, exact_node_type: bool = True, subtype: str | None = None) -> hou.DopNode | None:
    """ Creates DOP Objects of a particular type from a scene level object
        selection.
    """
def getGroupString(dopobjects: Sequence[hou.DopObject], useglob: bool) -> str:
    """ Determine if the selected DOP objects are all the objects in the
        simulation.
    """
def wireNodeAtEnd(dopnet: hou.OpNode, newdopnode: hou.OpNode, set_current: bool = True) -> None:
    """ Wires up the node after the current display DOP, but keeps it above the
        Output DOP (if one exists).
    """
def genericDopFilterCreate(dopobjects: Sequence[hou.DopObject], nodetypename: str, nodename: str | None, setgroup: bool, exact_node_type: bool = True) -> hou.DopNode | None:
    """ Creates a generic DOP node that modifies a group of DOP Objects.
        This includes most forces like Gravity and Fan, as well as many
        other simple DOP nodes which don't require extra selections or
        user input.
    """
def genericDopFilterTool(sceneviewer: hou.SceneViewer, nodetypename: str, nodename: str | None, prompt: str | None = None, exact_node_type: bool = True) -> hou.DopNode | None:
    """ A generic tool for creating DOP nodes that modify a group of DOP
        Objects. This function prompts the user to select a group of DOP
        Objects, then creates the filter DOP node.
    """
@toolutils.reformatPermissionErrors
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, orient: OrientInfo | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ A generic tool for creating DOP nodes. It delegates to the standard
        node creation tool when invoked from a network editor. In the scene
        viewer, it delegates to genericDopConverterTool for DOP Object
        creation nodes, or genericDopFilterTool for all other DOP nodes.
    """
def convertToDeformingObject(scriptargs: ShelfToolKwargs, isdeforming: bool) -> hou.OpNode | None:
    """ Create a StaticObject DOP setup for deforming geometry. """
def setupDeformingObject(dopobjectnode: hou.OpNode, isdeforming: bool) -> None: ...
def buildControlNull(ownernode: hou.OpNode, name: str, parmlist: Iterable[_ControlParmSpec]) -> hou.OpNode:
    """ Builds a null of the given name and coloured a pleasant blue.
        Then populates it with parmlist, a list of tuples of
        (type, name, label, vectorsize, default)
        type is a string from 'toggle', 'string', 'int', 'float'.
        default must be a tuple.
        Resulting node returned.
    """
def convertToGrains(dopobjectnode: hou.DopNode) -> None:
    """ Customize particle fluid dopnet for grains
    """
def createLavaMaterial() -> hou.VopNode: ...
def addMeltOutputProcessing(dopobjectnode: hou.OpNode, inputnode: hou.SopNode) -> hou.SopNode: ...
def addTemperatureToViscosity(fluidnode: hou.DopNode, solvernode: hou.OpNode) -> None: ...
def makeMoltenLiquid(fluidnode: hou.DopNode, solvernode: hou.OpNode) -> None: ...
def addTemperatureToEmitColor(inputnode: hou.SopNode) -> hou.SopNode: ...
def particlefluidDopObjectInit(info: ObjectTypeInfo | None, dopobjectnode: hou.DopNode, solvernode: hou.DopNode, objectnode: hou.ObjNode | None, sopnode: hou.SopNode | None, subtype: str | None = None) -> None:
    """ Setup the particle fluid specific parameters
        Note that info, objectnode, and sopnode may be None.
        A None for objectnode implies an empty fluid should be created.
    """
def particlefluidDopInit(info: ObjectTypeInfo | None, dopobjectnode: hou.DopNode, solvernode: hou.DopNode, subtype: str | None = None) -> None: ...

class ObjectTypeInfo:
    secondarysolvers: list[str] | None
    initDopFunc: _InitDopFunc | None
    initObjectFunc: _InitObjectFunc
    makeActiveFunc: Callable[[ObjectTypeInfo, hou.DopObject, int], object]
    solvertype: str
    mergeobjects: bool
    prompt: str | None
    objecttype: str | None
    def __init__(self) -> None: ...

theDopObjectTypeDict: dict[str, ObjectTypeInfo]
theAutoDopNetName: str
theSolverOrder: list[str]
theRigidBodyInfo: ObjectTypeInfo
theRigidBodyFracturedInfo: ObjectTypeInfo
theRigidBodyPackedInfo: ObjectTypeInfo
theClothInfo: ObjectTypeInfo
theFEMSolidInfo: ObjectTypeInfo
theFEMHybridInfo: ObjectTypeInfo
theFluidInfo: ObjectTypeInfo
theParticleFluidInfo: ObjectTypeInfo
theFLIPFluidInfo: ObjectTypeInfo
theSandInfo: ObjectTypeInfo
theSmokeInfo: ObjectTypeInfo
theStaticInfo: ObjectTypeInfo
theWireInfo: ObjectTypeInfo
thePopGeneratorDict: dict[str, Callable[[ShelfToolKwargs], None]]
