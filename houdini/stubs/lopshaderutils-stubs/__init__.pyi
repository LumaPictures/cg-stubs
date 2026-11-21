# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs
from pxr import Usd

theMaterialOutputTypeFromName: dict[str, str]

def showError(msg: str, title: str) -> None: ...
def importBaseParameters(kwargs: ParmCallbackKwargs) -> None:
    """ Populates the shader node with new spare parameters 
        created from the input attributes of the base USD primitive. 
        The base primitive is specified in 'shader_baseprimpath' parameter.
    """
def selectBaseUsdMaterial(node: hou.OpNode) -> str | None:
    """ Pops up a dialog to select a USD Material from a stage associated
        with the given node.
    """
def configureMaterialNode(node: hou.VopNode | None, usd_material_path: str | None) -> None:
    """ Creates necessary spare parameters on the node, so that 
        it reflects the USD Material primitive.
        The VOP node will translate back to the original material path.
    """
def configureDerivedMaterialNode(node: hou.VopNode | None, usd_material_path: str | None) -> None:
    """ Creates necessary spare parameters on the node, so that 
        it reflects the given USD Material primitive.
        The VOP node will translate to a new material that derives
        (specializes) from the orignal material prim.
    """
def importBaseParametersFromPrim(node: hou.OpNode, usd_prim: Usd.Prim) -> None:
    """ Populates the node with new spare parameters created from the 
        input attributes of the given USD primitive. 
    """
def setupMatPrimPathProperty(node: hou.OpNode, usd_path: str, add_button: bool = False) -> None:
    """ Creates and sets the spare parm for USD primitive path.
    """
def setupDerivedMatPrimPathProperty(node: hou.OpNode, usd_path: str, add_button: bool = False) -> None:
    """ Creates and sets the spare parm for the base USD primitive path.
    """
def selectPrimFromInputOrFile(kwargs: ParmActionButtonKwargs) -> None:
    """ Material/shader-centric prim selection.
    """
