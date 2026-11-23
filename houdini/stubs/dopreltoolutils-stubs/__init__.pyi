import hou
from collections.abc import Callable as Callable, Sequence
from houtypes import ShelfToolKwargs

def validateCloth(dopobject: hou.DopData, affected: bool) -> None:
    """ Only cloth affected objects, and no affector objects. """
def validateRBD(dopobject: hou.DopData, affected: bool) -> None:
    """ Only RBD affected objects, and any affector object. """
def checkNotPackedObject(dopobject: hou.DopData | None) -> None:
    """ Raises an error if the user attempts to create a constraint with
        RBD Packed Objects, which only support constraint networks. """
def validateBullet(dopobject: hou.DopData, affected: bool) -> None:
    """ Only Bullet affected objects, and any affector object. """
def validateRBDorBullet(dopobject: hou.DopData, affected: bool) -> None:
    """ Only RBD or Bullet affected objects, and any affector object. """
def validateSource(dopobject: hou.DopData, affected: bool) -> None:
    """ Only smoke, fluid, and sand affected objects, and any affector
        object.
    """
def validateWire(dopobject: hou.DopData, affected: bool) -> None:
    """ Only wire affected objects, and no affector objects. """
def genericRelToolSetParms(dopnode: hou.DopNode, affectedobjects: Sequence[hou.DopObject], affectorobjects: Sequence[hou.DopObject], mutual: bool) -> None:
    """ Sets the affector and affected object parameters on a relationship
        DOP node. These DOPs can have one of a few different names for the
        various parameters, so we test for the existence of various choices.
    """
def genericConstraint(sceneviewer: hou.SceneViewer, nodetypename: str, validateobjfunc: Callable[[hou.DopData, bool], object] | None, mutual: bool, allowaffector: bool, nodename: str | None, prompt: str | None, exact_node_type: bool) -> hou.DopNode | None:
    """ This function is similar to the standard DOP filter tool, but is for
        DOP relationships, which require selecting two sets of objects.
        Unlike the genericRelationship function, only one selection is
        requested of the user.
    """
def genericRelationship(sceneviewer: hou.SceneViewer, nodetypename: str, validateobjfunc: Callable[[hou.DopData, bool], object] | None, mutual: bool, wantaffector: bool, needaffector: bool, multiaffected: bool, multiaffector: bool, nodename: str | None, affected_prompt: str | None, affector_prompt: str | None, exact_node_type: bool) -> hou.DopNode | None:
    """ This function is similar to the standard DOP filter tool, but is for
        DOP relationships, which require selecting two sets of objects.
    """
def genericRelationshipTool(scriptargs: ShelfToolKwargs, nodetypename: str, validateobjfunc: Callable[[hou.DopData, bool], object] | None, mutual: bool, wantaffector: bool, needaffector: bool, multiaffected: bool, multiaffector: bool, nodename: str | None = None, affected_prompt: str | None = None, affector_prompt: str | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ Delegates the creation of a DOP relationship node to the standard
        DOP node creation tool if we are in a network editor, or the
        specialized genericRelationship function if we are in a scene
        viewer.
    """
def genericConstraintTool(scriptargs: ShelfToolKwargs, nodetypename: str, validateobjfunc: Callable[[hou.DopData, bool], object] | None, mutual: bool, allowaffector: bool, nodename: str | None = None, prompt: str | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ Delegates the creation of a DOP relationship node to the standard
        DOP node creation tool if we are in a network editor, or the
        specialized genericConstraint function if we are in a scene
        viewer.
    """
