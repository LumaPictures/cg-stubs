# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Iterable, MutableSequence, Sequence
from houtypes import ShelfToolKwargs
from typing import Literal

from typing import TypeAlias
from collections.abc import Callable
from typing import TypeAlias
_ParmOp: TypeAlias = Callable[[float, float], float]
_ParmSetEntry: TypeAlias = tuple[str, float | list[tuple[float, float]], _ParmOp] | tuple[str, int | float | str | hou.Parm | list[tuple[float, float]], None]
PROHIBITED_SOLVERS: list[str]

def op_mult(val: float, diam: float) -> float:
    """ Multiplies val by diam
    """
def op_multsquare(val: float, diam: float) -> float:
    """ Multiplies val by diam^2
    """
def op_div(val: float, diam: float) -> float:
    """ Divides val by diam
    """
def createNewPyroShop(pyrosolver: hou.OpNode) -> hou.ShopNode:
    """ Creates a new pyro shop inside /shop for us to initalize to
        our favorite settings.  Returns said shop.
    """
def createNewPyroShopPreset(pyrosolver: hou.OpNode, preset: str) -> hou.ShopNode:
    """ Creates a new pyro shop inside /shop and applies the
        given preset name to it.
    """
def disableGravity(fluidnode: hou.OpNode) -> None:
    """ Tries to find the global gravity node.  If it finds one, it
        removes this node from the influence by adding ^node to the
        groupmask.
    """
def applyParmSet(node: hou.OpNode, diam: float, parmlist: Iterable[_ParmSetEntry]) -> None:
    """ List of parms in (parmname, val, OP) tuples where OP
        not None means we should apply the binary OP function to val
        and diam to compute the final value of val.
        If val is a list, it must be a list of (val, frame) pairs
        and we will keyframe accordingly.
    """
def buildRamp(node: hou.OpNode, parm: str, interp: str, ramplist: Sequence[tuple[float, float]]) -> None:
    """ Sets up a ramp multiparm according to the list of ramp
        keyframe pairs.
    """
def buildColorRamp(node: hou.OpNode, parm: str, interp: str, ramplist: Sequence[tuple[float, Sequence[float]]]) -> None:
    """ Sets up a color ramp multiparm according to the list of ramp
        keyframe pairs.
    """
def applyKeySet(node: hou.OpNode, parmname: str, keylist: Iterable[tuple[float, float]]) -> None:
    '''
    Functon that applies a list of (index,value) pairs as keyframes to a parameter.
    Ie: applyKeySet(hou.node("."),"gasexpand",[(0.5,10),(1,20)])
    '''
def selectObject(kwargs: ShelfToolKwargs, prompt: str, force_newobj: bool = False) -> tuple[hou.ObjNode, hou.BoundingBox, float]:
    """ Prompt the user to select an object.  Returns
        (object, bbox, diam)
    """
def clusterRasterization(noisenode: hou.SopNode) -> None:
    """ Enables separate rasterization for each cluster.
    """
def cluster(fuelsource: hou.Node = ...) -> list[hou.SopNode | None]:
    """ Set Up Clustering, return list of new geo and instancepoints
    """
def clustertrail(fuelsource: hou.Node = ...) -> list[hou.SopNode | None]:
    """ Set Up Clustering, return list of new geo and instancepoints
    """
def sparseExplosion(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sparse pyro explosion from the selected object
    """
def sparseFireball(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sparse pyro explosion from the selected object
    """
def sparseSmokeStack(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sparse pyro simulation of a rising smoke stack
    """
def sparseFire(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sparse fire simulation from the selected object
    """
def fireball(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes the bomb from which to build a
        explosion.
    """
def explosion(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes the bomb from which to build a
        explosion.
    """
def volcano(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes the source from which to build a
        volcano.
    """
def smokeTrail(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes an emitter of a smoke trail.
    """
def billowySmoke(kwargs: ShelfToolKwargs, clustering: bool = False) -> None:
    """ Selected object becomes an emitter of hot billowy smoke.
    """
def makeColored(kwargs: ShelfToolKwargs) -> None:
    """ Selected smoke object gets its color fields set up.
    """
def coloredSmoke(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes an emitter of colorful smoke with a noisy velocity field.
    """
def burn(kwargs: ShelfToolKwargs, smokeon: bool = True, clustering: bool = False) -> None:
    """ Selected object becomes a continuous source of fuel igniting
        on creation.
    """
def candle(kwargs: ShelfToolKwargs, smokeon: bool = False) -> None:
    """ Selected object becomes a small continuous source of fuel igniting
        on creation.
    """
def wispy(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes an emitter of wispy smoke.
    """
def dryice(kwargs: ShelfToolKwargs) -> None:
    """ Selected object becomes an emitter of cold dry ice.
    """
def buildLabel(node: hou.OpNode, p: str, token: str, defname: str, i: int) -> list[str]:
    """ Given a parameter name prefix, p, build the string
        pair of the token and parameter name if the enable is set.
        defname is used as the label if no internal name is given.
        i is the index to work with.
    """
def buildUserLabel(node: hou.OpNode, p: str, token: str, defname: str, i: int) -> list[str]:
    """ Given a parameter name prefix, p, build the string
        pair of the token and parameter name if the enable is set.
        defname is used as the label if no internal name is given.
        i is the index to work with.
    """
def buildPyroModifiers(node: hou.OpNode, style: str, ismaterial: bool) -> list[str]:
    """ Builds the modifier menu for the pyro shader.  Returns a list
        of token/label pairs to be given as the modifier choices.
        style is one of 'mod', 'vmod', 'noise', 'base' for modifier lists
        ('mod', all types, includes None); vector modifiers ('vmod',  
        fields only, and None); noise presence ('noise', none means 
        everywhere, no noise fields); all base fields 
        ('base', no none); field modifier base ('mfbase', no none)
        noise parameter modifiers ('nmod', all fields plus none)
    """
def incominggeotype(geoNode: hou.SopNode = ...) -> Literal['Points', 'Volume', 'Surface']: ...
def geoiterate(prims: Iterable[hou.Prim] = ...) -> list[int]: ...
def findfluidnode(startnode: hou.Node | None = ..., usednodes: MutableSequence[hou.Node] = ..., searchnode: str = 'fluidsource') -> list[hou.Node] | None: ...
