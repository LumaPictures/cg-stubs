# Houdini stubs generated from Houdini 22.0.466

import hou
import string
from collections.abc import Iterable, Sequence
from houtypes import ShelfToolKwargs
from typing import Literal

from typing import TypeVar
from typing import TypeVar
_NodeT = TypeVar('_NodeT', bound=hou.OpNode)
def calculateDiameter(diamobject: hou.ObjNode | hou.SopNode) -> float:
    """Calculates the approximated diameter of the specified object
       If the diameter is 0, return 1
    """
def setupPyroSource(fluidsource: hou.SopNode, noisenode: hou.SopNode | None, diam: float, scale: float) -> None:
    """scale fluidsource values relative to source scale
    """
def setupFLIPSource(fluidsource: hou.SopNode, fluidnode: hou.DopNode, sourcesink: str, diam: float) -> None: ...
def setupFLIPSourceForPyro(fluidsource: hou.SopNode, fluidnode: hou.DopNode, diam: float) -> None: ...
def buildRenameNode(objectnode: hou.ObjNode, fromfield: str, tofield: str) -> hou.SopNode:
    """ Returns a new node, a child of object node, that will rename
        the field fromfield to the field tofield.
    """
def linkParms(destnode: hou.OpNode, srcnode: hou.OpNode, parmlist: Iterable[str]) -> None:
    """ Creates a ch() link in the dest node pointing to the source
        node for each parm in the parmlist.  The two nodes must
        have matching parm names.
    """
def deleteBoundingBox(object: hou.ObjNode, sop: hou.SopNode) -> None:
    """ Appends a node to sop that deletes the bounding box group.
        Sets the render, and only render, flag to this so things
        render nicely.
    """
def buildMotionOverride(name: str, bypass: bool) -> hou.DopNode:
    """ Builds a SIM_Motion setup to be keyframeable with
        no extra channels.  Bypasses by default if so requested.
    """
def findBestGroupNode(fluidnode: _NodeT) -> _NodeT:
    """ Searches descendants of fluidnode for a group node that
        should be used for relationships rather than the groupnode.
        Currently we only accept a post-switch group node where that
        switch is suspected to have been made by an upres merge.
    """
def findDopIONodes(dopnode: hou.OpNode, nodetype: str = 'dopimportfield') -> list[hou.SopNode]:
    """ Finds all DOP I/O nodes that import this DOP node.  Locates
        it by finding all DOP I/O nodes one level deep in Objects
        and then checking to see if their autodopnetwork
        and dopscreatedby match.
    """
def findImportingFluidBox(fluidnode: hou.OpNode) -> hou.SopNode | None:
    """ Finds a DOP I/O node that imports this fluidnode.  Locates
        it by finding all DOP I/O nodes one level deep in Objects
        and then checking to see if their autodopnetwork
        and dopscreatedby match.
    """
def buildRelationshipExpression(node: hou.DopNode) -> str:
    """ Builds the appropriate expression to refer to this node inside
        a relationship string.  Ie, dopobjscreatedby for fluidnodes
        and chs() for group nodes.
    """
def getExpression(node: hou.OpNode | None, parmname: str) -> str | None:
    """ Returns the expression for the given parmname.  If it is not
        an expression or the parm or node doesn't exist returns None.
    """
def transferRelationships(oldnode: hou.DopNode, newnode: hou.DopNode) -> None:
    """ For all nodes inside the dopnet given, search for
        relationship nodes.  If the affector or affectee is a
        dopscreatedby or group channel reference to oldnode, change it
        to the approriate expression for new node.
    """
def createMaterial(galleryname: str, nodename: str) -> hou.VopNode:
    """ Creates a material from the gallery and installs into /mat.
        Returns the result.  Note if it already exists, it will
        create a new one!
    """
def findOrCreateMaterial(galleryname: str, nodename: str) -> tuple[hou.VopNode, bool]:
    """ Searches the gallery for a matching material and installs it
        into /mat.  Returns the resulting material.  Note that if a
        material already exists of this name, it will be used instead!
    """
def createSmokeMaterial() -> hou.VopNode:
    """ Creates an official smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createSprayMaterial() -> hou.VopNode:
    """ Creates an official spray material in /mat.  Returns existing
        one if it already exists.
    """
def createWhitewaterMaterial() -> hou.VopNode:
    """ Creates an official whitewater material in /mat.  Returns existing
        one if it already exists.
    """
def createSteamMaterial() -> hou.VopNode:
    """ Creates an official steam material in /mat.  Returns existing
        one if it already exists.
    """
def createMistMaterial() -> hou.VopNode:
    """ Creates an official mist material in /mat.  Returns existing
        one if it already exists.
    """
def createBillowySmokeMaterial() -> hou.VopNode:
    """ Creates an official smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createHotSmokeMaterial() -> hou.VopNode:
    """ Creates an official smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createMushroomMaterial() -> hou.VopNode:
    """ Creates an official smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createFlameSmokeMaterial() -> hou.VopNode:
    """ Creates an official smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createBlackSmokeMaterial() -> hou.VopNode:
    """ Creates an official smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createFlameMaterial() -> hou.VopNode:
    """ Creates an official flame material in /mat.  Returns existing
        one if it already exists.
    """
def createDSDFlameMaterial() -> hou.VopNode:
    """ Creates an official flame material in /mat.  Returns existing
        one if it already exists.
    """
def createLiquidMaterial() -> hou.VopNode:
    """ Creates an official liquid surface material in /mat.  Returns existing
        one if it already exists.
    """
def createLiquidSmokeMaterial() -> hou.VopNode:
    """ Creates an official liquid smoke material in /mat.  Returns existing
        one if it already exists.
    """
def createUniformVolumeMaterial() -> hou.VopNode:
    """ Creates an official uniform volume material in /mat
    """
def createUniformVolumeOceanMaterial() -> hou.VopNode:
    """ Creates an official uniform ocean volume material in /mat
        Always builds a new one as we will be setting displacement channels.
    """
def createBlueConeMaterial() -> hou.VopNode:
    """ Creates an official blue cone material in /mat.  Returns existing
        one if it already exists.
    """
def convertRelTypeToToken(reltype: str) -> str:
    """ Converts a relationship type, such as Source, into the
        appropriate token such as SIM_RelationshipoSource.
    """
def findOrCreateMergeRelationship(reltype: str, forcecreate: bool = False) -> hou.DopNode:
    """ Searches the auto-net for a given type of merge relationship.
        If it doesn't exist, create it.  The relationship name is
        something like Source, Empty, etc.
    """
def createRelationship(fluidnode: hou.DopNode, dopnode: hou.DopNode, sourcesink: str) -> None:
    """ Creates a relationship of type sourcesink between the
        fluidnode (as the affectee) and the DOP Node (as the
        affector).  This uses the dopobjscreatedby function to ensure
        node renames are properly handled.  If the specified nodes
        are Group DOPs, a chs() expression will be built to the
        group's name.
    """
def convertObjectToSourceSink(fluidnode: hou.DopNode, objectnode: hou.ObjNode, sourcesink: str, subtype: str | None = None, addnoise: bool = True) -> hou.DopNode:
    """ The chosen object is added to the simulation as a static
        object and set as a source or sink relationship to the rest of
        the simulation.

        sourcesink can be Source, Sink, Pump for the static object
        approach. Prefixing Apply_ will instead use a sourceapply.
        Postfixing _Surface to an Apply_ will setup for emission from
        the surface.

        Ideally, it is to be added to the target fluid's source
        relationship, but for technical constraints we only guarantee
        it is added to that network.  Since selection will change
        the current fluid network, we don't have to worry about
        setting the network.

        We special case particle fluids when they are the target
        as we have special source/sink nodes in these cases.
    """
def applySourceSink(fluidnode: hou.DopNode, objectnode: hou.ObjNode, sourcesink: str) -> hou.DopNode:
    """ A sourceapply is added to the fluid object.  This will
        directly import the objectnode if it isn't simulated.  If
        the object node is a live simulation, it will add the name
        of it to the sourceapply source object.

        The assumption is we have been prefixed by a
        convertObjectToSourceSink
    """
def createMaterialFromFluidType(fluidtype: str) -> hou.VopNode: ...
def createRenderNode(objectnode: hou.OpNode, dopnode: hou.OpNode, fluidtype: str, isupres: bool) -> hou.SopNode:
    """ Creates a dopimportfield inside objectnode that extracts the
        expected fields from dopnode given it being fluidtype.
        isupres flags that this is the upres stage so we should
        set the presets appropriately.
    """
def createObjectImportingFromFluid(dopnode: hou.DopNode, fluidtype: str, buildmat: bool = True) -> hou.SopNode:
    """ Creates a new object importing fluid from dopnode
        of the given type.  Returns the display node of the created
        object.
    """
def createEmptyFluidBox(sceneviewer: hou.PaneTab, fluidtype: str, buildmat: bool = True, prohibited: Iterable[str] = ...) -> tuple[hou.DopNode, hou.SopNode]:
    """ Creates a new fluid object in DOPs and exports appropriately
        to Objects.  Returns the (dopnode, fieldnode) creating/importing
        the fluid.
        prohibited parameter is a list of solver nodes that the current DOPNET
        may not contain. If there is a solver node in the current DOPNET that is
        in this list, a new DOPNET is created instead.
    """
def dopEmptyFluidBox(scriptargs: ShelfToolKwargs, fluidtype: str, prompt: str | None = None, buildmat: bool = True, containerinstance: bool = False) -> tuple[hou.DopNode, hou.SopNode]:
    """ Create an empty smoke or fluid box and export it to Objects
        Returns (dopnode, fieldnode), dopnode is what creates
        this fluid in DOPs and fieldnode is the node that imports it
        it in Sops.
    """
def createForSourceSink(createtype: str, subtype: str | None = None) -> hou.DopNode | None: ...
def isSparsePyroObject(fluidnode: hou.DopNode) -> bool: ...
def computeFluidDiameter(fluidnode: hou.DopNode) -> float:
    """ Estimates a diameter for a fluid container
    """
def selectedConvertToSourceSink(scriptargs: ShelfToolKwargs, sourcesink: str, objprompt: str | None = None, fluidprompt: str | None = None, autoconvert: bool = True, createifempty: str | None = None, subtype: str | None = None) -> None:
    """ Import selected objects to AutoDop and make sourcesink
        relationships.
    """
def createSopAttribVolume(fluidnode: hou.OpNode, objectnode: hou.ObjNode, sourcesink: str) -> hou.SopNode:
    """
    converts objects into a volumes for a dop smoke sim
    the script uses the type (sink/source/pump) and mode (sort of geometry) to set up operators
    """
def selectedConvertToAttribSource(scriptargs: ShelfToolKwargs, sourcesink: str, dopname: str, attribname: str, attribtype: str | None, mergemethod: str | None = None, rangein: Sequence[float] | None = None, rangeout: Sequence[float] | None = None, targetrate: float | None = None, increaserate: float | None = None, decreaserate: float | None = None, objprompt: str | None = None, fluidprompt: str | None = None, autoconvert: bool = True) -> None:
    """ Import selected objects to AutoDop and make sourcesink
        relationships.
    """
def embedDopInFluid(embedobject: hou.DopData, fluidobject: hou.DopData) -> None:
    """ Embeds the specified DOP_Object into the DOP_Object fluidobject
        embed object will be driven by the fluid object within the
        fluid object's field of influence
    """
def embedDopInFluidByNodes(embednode: hou.DopNode, embedtype: str, fluidnode: hou.DopNode, sourcetype: str) -> None:
    """ Embeds the fluid of type embedtype and owned by embednode
        inside the fluid of sourcetype owned by fluidnode.
    """
def embedObjectInFluid(objectnode: hou.ObjNode, fluidobject: hou.DopObject) -> None:
    """ Embeds the specified OBJ_Node into the DOP_Object fluidobject.
    """
def embedInFluid(kwargs: ShelfToolKwargs) -> None:
    """ Selected object is added to set to float in the found fluid
        solver.
    """
def seedVorticlesInFluid(fluidnode: hou.DopNode) -> hou.DopNode:
    """ Seed vorticles inside the given fluid object.
        Returns the vorticlenode
    """
def seedVorticles(kwargs: ShelfToolKwargs) -> None:
    """ Add a bounding box of vorticles to the selected simulation
    """
def initVelocityOfFluid(fluidnode: hou.DopNode) -> hou.SopNode:
    """ Initialize the velocity of the given object.
        Returns the volume velocity node.
    """
def initVelocity(kwargs: ShelfToolKwargs) -> None:
    """ Sets the initial velocity of the container from a SOP network.
    """
def convertObjectToFluidtype(fluidobject: hou.DopData, objectnode: hou.ObjNode, fluidtype: str) -> None:
    """ object node is used as initial conditions into fluidobject
        according to the fluid type.
    """
def convertSelectedToFluidtype(kwargs: ShelfToolKwargs, fluidtype: str) -> None:
    """ Select geometry and apply convertToFluid to it.
    """
def resizeFluidToMatch(fluidnode: hou.DopNode, matchobject: hou.ObjNode | None) -> hou.DopNode:
    """ Resizes the fluid dynamic object fluidobject according
        to match object.
    """
def resizeFluid(kwargs: ShelfToolKwargs) -> None:
    """ Select fluid and set it up to be resizeable.
    """
def parentFluidTo(fluidnode: hou.DopNode, parentobject: hou.ObjNode | None) -> None:
    """ Parents the fluid dynamic object fluidobject to parent object.
    """
def parentFluid(kwargs: ShelfToolKwargs) -> None:
    """ Select fluid and set it up to be parented.
    """
def buildNodeName(result: str | None, field_name: str) -> str:
    """ Suffixes first paramater with second, but handles cases
        of first parm being None
    """
def addFieldToObject(fluidobject: hou.DopData, fieldname: str, fieldvizname: str) -> hou.DopNode:
    """ Add Field inside the given fluid object.
    """
def addField(kwargs: ShelfToolKwargs) -> None:
    """ Selects an object and prompts for the type of field to add.
        Then adds it.
    """
def upresSmokeSelectSameNet(kwargs: ShelfToolKwargs) -> None:
    """ Selects a fluid sim to upres.  Creates the upres simulation
        in the same network as that sim using a switch dop
        to select upres mode.
    """
def upresSelect(kwargs: ShelfToolKwargs) -> None:
    """ Selects a fluid sim to upres.  Will then create a new DOP
        network to hold the resulting upresed sim.
    """
def solverinputnodes(solver: hou.Node) -> list[list[int | list[hou.Node]]]:
    """
    creates a seperated list for the node specified, containing all the
    ancestor nodes for every independent input. ie: [[1,[x,x,x]],[2,[y,y,y]]]
    """
def upresSmoke(fluidnode: hou.DopNode, buildmat: bool = True, fluidlocation: hou.SopNode | None = None, solver: hou.DopNode | None = None) -> None: ...
def spliceUpresSim(fluidnode: hou.DopNode, fieldnode: hou.SopNode | None, upresnode: hou.DopNode, upresfieldnode: hou.SopNode) -> None:
    """ Splices a upres sim with a normal res sim assuming both are in
        the same network.  Also updates our upresfieldnode to
        object merge in the needed fields from fieldnode for proper
        rendering.
    """
def upresSmokeSameNet(fluidnode: hou.DopNode, buildmat: bool = True) -> tuple[hou.DopNode, hou.SopNode]:
    """ Given a fluidnode builds the upres version of it.  This is
        built in the same network as the fluid node but switches
        are put in place to try and ensure we can disable the
        uprespath.

        The generated nodes are left unwired in the net.  The
        (upresfluidnode, fieldnode) is returned.
    """

CLUSTER_CHOICE: str
CLUSTER_CHOICE_MESSAGE: string.Template
SLICE_CHOICE: str
SLICE_CHOICE_MESSAGE: string.Template
NO_PARITION_CHOICE: str
NO_PARITION_CHOICE_MESSAGE: str
CANCEL_CHOICE: str

def distributeSimulation(kwargs: ShelfToolKwargs, prompt: str | None = None, invalid_selection_message: str | None = None) -> None:
    """ Selects a fluid object to distribute and then invokes
        the correct distribution method.
    """
def distributeClusterSimulation(creator_object: hou.DopNode, fluidtype: str | None) -> None:
    """ Prepares the the file for a cluster based distribution.
    """
def distributeGridSimulation(activepane: hou.PaneTab, fluidobject: hou.DopData) -> None:
    """ Adds the net border exchange node and builds a control
        panel to setup the distribution of a grid based fluid sim.
    """
def buildFluidBoxWithUpres(kwargs: ShelfToolKwargs, fluidtype: str, buildmat: bool = True) -> tuple[tuple[hou.DopNode, hou.SopNode], tuple[hou.DopNode, hou.SopNode]]:
    """ Builds a fluid solver and fluid box complete with a tame
        upres choice.
    """
def targetDrivenSmoke(fluidobject: hou.DopData, goalobject: hou.ObjNode) -> None:
    """ goalobject is made a target goal of fluidobject.
    """
def targetDrivenSmokeSelect(kwargs: ShelfToolKwargs) -> None:
    """ Selects smoke & target shape, then creates a target
        driven effect from the smoke to the target.
    """
def createSopSourceForDop(fluidnode: hou.DopNode, objectnode: hou.ObjNode, sourcesink: str, subtype: str | None = None, addnoise: bool = False) -> hou.SopNode | Literal[0]: ...
def applysopSourceSink(fluidnode: hou.DopNode, sourcenode: hou.SopNode, sourcesink: str) -> tuple[hou.DopNode, hou.DopNode]: ...
def convertmodeto(sourcesink: str) -> Literal['Surface', 'Points', 'Volume']: ...
def converttypeto(sourcesink: str, solvernode: str = 'smokesolver::2.0') -> list[str]:
    """
    returns the correct preset values used for setting up the fluidsource operator
    """
def converttypetodop(sourcesink: str, solvernode: str = 'smokesolver::2.0') -> str:
    """
    returns the correct preset used for setting up the source volume operator
    """
def sourcesolvertype(solvernode: hou.DopNode) -> str:
    """
    a solver of a type pyro or upres can represent multiple fluid types
    this function returns the correct type based on the mode the solver is in.
    """
def renamevolume(fluidsource: hou.SopNode, outnull: hou.SopNode, number: int = 1, name: str = 'rename') -> hou.SopNode: ...
def addpumpcolsource(objecttoconvert: hou.SopNode, preset: str, solvernode: str) -> tuple[hou.SopNode, list[hou.SopNode]]: ...
def addfluidsource(objecttoconvert: hou.SopNode, preset: str, mode: int, volumeattribute: str, addnoise: bool = False) -> tuple[hou.SopNode, list[hou.SopNode]]: ...
def haspointattribute(samplenode: hou.SopNode, attribute: str = 'v') -> bool: ...
def count(objecttoconvert: hou.SopNode, mode: str = 'Volume') -> int: ...
def setupmultifield(dopnode: hou.DopNode) -> None:
    """
    function sets up multi parm visualization
    """
def getImportedFields(dopionode: hou.SopNode) -> list[str]: ...
def addFieldImport(dopionode: hou.SopNode, objname: str, fieldname: str, visible: int | str) -> None: ...
