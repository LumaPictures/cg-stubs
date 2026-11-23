import doptoolutils
import hou
from collections.abc import Mapping, Sequence
from houtypes import ShelfToolKwargs

def dopObjectInit(info: doptoolutils.ObjectTypeInfo, dopobjectnode: hou.DopNode, solvernode: hou.DopNode | None, objectnode: hou.ObjNode, sopnode: hou.SopNode, subtype: str | None = None) -> None:
    """ Specializes the DOP Object node initialization process for RBD
        Object creation nodes of various kinds (RBD Object, RBD Glue Object,
        etc).
    """
def fracturedDopObjectInit(info: doptoolutils.ObjectTypeInfo, dopobjectnode: hou.DopNode, solvernode: hou.DopNode | None, objectnode: hou.ObjNode, sopnode: hou.SopNode, subtype: str | None = None) -> None:
    """ Specializes the DOP Object node initialization process for RBD
        Fractured and Glue Objects.
    """
def packedDopObjectInit(info: doptoolutils.ObjectTypeInfo, dopobjectnode: hou.DopNode, solvernode: hou.DopNode | None, objectnode: hou.ObjNode, sopnode: hou.SopNode, subtype: str | None = None) -> None:
    """ Specializes the DOP Object node initialization process for RBD Packed
        Objects.
    """
def getKeyframeDopForDopObject(dopobject: hou.DopObject) -> hou.DopNode:
    """ Find the RBD Keyframe Active DOP that controls the active state and
        position keyframing for a particular RBD Object. If no Keyframe Active
        DOP exists for this object, one is created.
    """
def setDopObjectActiveState(info: doptoolutils.ObjectTypeInfo, dopobject: hou.DopObject, active: int) -> hou.DopNode:
    """ Changes the active state of an RBD Object. This is done by creating
        (or modifying an existing) RBD Keyframe Active DOP that is associated
        with this one RBD Object.
    """
def setGroupString(rbdnode: hou.DopNode, node: hou.DopNode, groupstring: str) -> None:
    """ Sets the group parameter of node to be groupstring.  Has
        the extra feature that if all of the rbdnode's objects are
        accounted for in groupstring, it uses * instead
    """
def makeObjectBreakable(rbdlist: Sequence[str | hou.DopNode | hou.ObjNode | None]) -> hou.DopNode | None:
    """ Giving the rbdnode, append a voronoifractureconfigureobject to it.
        No-op if one is already present.
    """
def makeBreakable(kwargs: ShelfToolKwargs) -> None:
    """ Convert the RBD objects to breakable one by adding
        voronoifractureconfigure object if not already present.
        Do this by passing a list of object-creator pairs.
    """
def makeObjectAutoFreeze(rbdobject: hou.DopData) -> hou.DopNode:
    """ Giving the rbdnode, append a rbdautofreeze to it.
        No-op if one is already present.
    """
def makeAutoFreeze(kwargs: ShelfToolKwargs) -> None:
    """ Convert the RBD objects to breakable one by adding
        rbdautofreeze object if not already present.
    """
def makeObjectImpactAnalysis(rbdobject: hou.DopData, rbdsolver: hou.DopNode) -> hou.DopNode: ...
def makeImpactAnalysis(kwargs: ShelfToolKwargs) -> None:
    """ Add ImpactAnalysis Solver to RBD Objects in Dop Network
    """
def buildGlueConstraintNode(dopnet: hou.OpNode, strength: float = 10000) -> hou.DopNode: ...
def buildSoftConstraintNode(dopnet: hou.OpNode) -> hou.DopNode: ...
def buildPinConstraintNode(dopnet: hou.OpNode) -> hou.DopNode: ...
def buildConstraintInputNode(sopsolver: hou.DopNode) -> hou.SopNode: ...
def addConstraintNetworkSolver(dopnet: hou.OpNode, name: str, constraintnet: hou.DopNode) -> hou.DopNode:
    """ Set up a SOP Solver and wire it into the constraint network DOP."""
def addGlueNetworkSolver(dopnet: hou.OpNode, constraintnet: hou.DopNode) -> hou.DopNode:
    """ Set up the default SOP Solver for glue constraint networks, which just
        deletes broken glue bonds."""
def buildGlueNetworkDOPNodes(dopnet: hou.OpNode, nodename: str, soppath: str) -> hou.DopNode:
    """ Set up the constraint network DOP and its associated nodes for a glue
        constraint network.
        Returns the constraint network DOP node.
    """
def buildConstraintNetworkDOPNodes(dopnet: hou.OpNode, dopobjnode: hou.DopNode | None, nodename: str, soppath: str, constraint_nodes: list[hou.DopNode], set_current: bool = True) -> hou.DopNode:
    """ Set up the constraint network DOP and its associated nodes.
        Returns the constraint network DOP node.
    """
def buildGlueNetworkGeometry(sopnode: hou.SopNode) -> hou.SopNode:
    """ Given a SOP Node whose geometry has a 'name' primitive attribute, builds
        the constraint network geometry.
        Returns the last node of the SOP chain.
    """
def createGluedObject(kwargs: ShelfToolKwargs, use_packed: bool) -> None:
    """ Create an RBD Packed Object or RBD Fractured Object whose pieces are
        glued together.
    """
def createRagdollObject(kwargs: ShelfToolKwargs) -> None:
    """ Create an RBD Packed Object from agent primitives, and set up
        constraints for ragdolls.
    """
def createRagdollConstraintNetwork(dopnet: hou.OpNode, dopobjnode: hou.DopNode, sopnode: hou.SopNode) -> hou.DopNode:
    """ Build the constraint network for a ragdoll.
    """
def createPackedRBDInstances(objnode: hou.ObjNode, pointsnode: hou.SopNode, geonode: hou.SopNode, nameprefix: str, attribstocopy: Sequence[str], enable_packing: bool = True) -> hou.DopNode:
    """ Sets up an RBD Packed Object for instancing.
        Returns the newly created DOP node.
    """
def createRBDGrains(kwargs: ShelfToolKwargs) -> None:
    """ Select an object and turn it into a pile of sand, simulated as RBD
        spheres.
    """
def createCompoundProxyObjects(kwargs: ShelfToolKwargs, selectedobjects: Sequence[hou.ObjNode], source_geo: Mapping[hou.ObjNode, hou.SopNode]) -> None:
    """
        Create the RBD Packed Object DOPs along with a Transform Pieces setup.
    """
def createSphereProxy(kwargs: ShelfToolKwargs) -> None: ...
def createConvexProxy(kwargs: ShelfToolKwargs) -> None: ...
def createSopRBDFromObject(objnode: hou.ObjNode, collidenode: hou.ObjNode | None = None, guidenode: hou.ObjNode | None = None, style: str = 'fracture') -> hou.SopNode:
    """ Creates a new object to turn the objnode into the given
        style and simulate at SOP level.  Collides with optional
        collidenode. Uses option guidenode for guiding.
    """
def createSopRBD(scriptargs: ShelfToolKwargs, style: str = 'fracture') -> None:
    """ Select and object and make a SOP based rbd solve out
        of it.
    """
