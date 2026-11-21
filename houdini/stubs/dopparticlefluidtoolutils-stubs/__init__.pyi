import hou
from collections.abc import Iterable, Sequence
from houtypes import ShelfToolKwargs

def op_mult(val: float, diam: float) -> float:
    """ Multiplies val by diam
    """
def op_multsquare(val: float, diam: float) -> float:
    """ Multiplies val by diam^2
    """
def op_div(val: float, diam: float) -> float:
    """ Divides val by diam
    """
def createMist(kwargs: ShelfToolKwargs) -> None:
    """ Selects a fluid sim for generating mist.  Will then
        create a new DOP  to hold the resulting whitewater sim.
    """
def createMistFromNode(sceneviewer: hou.PaneTab, fluidnode: hou.OpNode) -> hou.DopNode:
    """ Creates a mist solver from a given node.
    """
def createWhitewaterEmitter(dopnet: hou.OpNode, prefixname: str, sourcenode: hou.OpNode, pointcount: float, inheritvel: float) -> hou.DopNode:
    """ Creates the POP/source replicate paradigm, returns the
        final node in this chain
    """
def createWhitewaterImport(prefixname: str, dopobject: hou.OpNode, sizeparm: hou.Parm, foamlocparm: hou.Parm | None = None) -> hou.ObjNode:
    """ Creates a node to import from a dopobject as a white
        water look/sim.
    """
def createWhitewater(kwargs: ShelfToolKwargs) -> None:
    """ Selects a fluid sim for generating whitewater .  Will then
        create a new DOP  to hold the resulting whitewater sim.
    """
def createWhitewaterSource(fluidnode: hou.OpNode, nameprefix: str) -> hou.SopNode:
    """ Creates a source for white water
        Returns the created source  object
    """
def createWhitewaterFromNode(fluidnode: hou.OpNode) -> tuple[hou.DopNode, hou.DopNode]:
    """ Post selection, creates a white water from a given
        DOP node
    """
def distributeWhitewaterSimulationClustered(activepane: hou.SceneViewer, wwobject: hou.DopObject) -> None:
    """ Adds an operator to partition the emission source into clusters that
        are then simulated separately.
    """
def distributeWhitewaterSimulationSliced(activepane: hou.SceneViewer, wwobject: hou.DopObject) -> None:
    """ Adds in the netslice exchange and a control panel
        to operate the tracker
    """
def createCondensationPOPFluid(kwargs: ShelfToolKwargs) -> None:
    """ Creates a simple POP simulation with fluid forces.
    """
def createSculptedFluid(scriptargs: ShelfToolKwargs) -> None: ...
def sliceSimByPlane(scriptargs: ShelfToolKwargs, slicetype: str) -> None:
    """ The user selects an existing cutting plane or simulation
        object.  A new cutting plane is made a child of this.
    """
def getParticleFluidSliceCount(fluidobject: hou.DopObject) -> int:
    """ Returns the number of slices in the fluidobject. A value of 1 means
        that there is no slicing.
    """
def distributeParticleFluidSimulation(activepane: hou.SceneViewer, fluidobject: hou.DopObject) -> None:
    """ Adds in the netslice exchange and a control panel
        to operate the tracker
    """
def createflipbox(sceneviewer: hou.PaneTab, center: hou.Vector3 | Sequence[float], size: hou.Vector3 | Sequence[float]) -> tuple[hou.SopNode, hou.DopNode]:
    """ Creates a flip fluid box at the given center and size
    """
def flipBox(kwargs: ShelfToolKwargs) -> hou.DopNode:
    """ Creates a fluid tank of flip particles for the user
        to play with.
    """
def sourceParticleAttribFromVolume(flipnode: hou.OpNode, sourcesop: hou.OpNode, dopname: str, sourcename: str, destname: str, attribtype: str | None, mergemethod: str | None = None, rangein: Sequence[float] | None = None, rangeout: Sequence[float] | None = None, targetrate: float | None = None, increaserate: float | None = None, decreaserate: float | None = None) -> hou.DopNode:
    """ Giving the flipnode add a Source Particle Attrib DOP to it.
    """
def createdeleteboundary(dopimport: hou.OpNode, box: hou.OpNode, boundscale: Iterable[float], do_layout: bool = True) -> hou.SopNode: ...
def createoceanboxtwo(sceneviewer: hou.PaneTab, preset: str, center: hou.Vector3 | Sequence[float], size: hou.Vector3 | Sequence[float], followobj: hou.ObjNode | None, beachobj: hou.ObjNode | None, createspectrum: bool, createbeach: bool, createguide: bool, createnarrowband: bool, createextended: bool) -> tuple[hou.SopNode, hou.SopNode, hou.DopNode, hou.DopNode]:
    """ Creates a flip fluid box at the given center and size
    """
def createoceanbox(sceneviewer: hou.PaneTab, preset: str, center: hou.Vector3 | Sequence[float], size: hou.Vector3 | Sequence[float], followobj: hou.ObjNode | None, beachobj: hou.ObjNode | None, createspectrum: bool, createbeach: bool) -> tuple[hou.SopNode, hou.SopNode | None, hou.SopNode, hou.SopNode, hou.SopNode | None, hou.DopNode, hou.DopNode]:
    """ Creates a flip fluid box at the given center and size
    """
def createoceansourcetwo(preset: str, createspectrum: bool, createbeach: bool, createguide: bool, createnarrowband: bool, createextended: bool, kwargs: ShelfToolKwargs) -> tuple[hou.SopNode, hou.SopNode, hou.DopNode, hou.DopNode]:
    """ Creates a wave tank of flip particles to be all splashy
        and render ready.
    """
def createoceansource(preset: str, createspectrum: bool, createbeach: bool, kwargs: ShelfToolKwargs) -> tuple[hou.SopNode, hou.SopNode, hou.SopNode, hou.DopNode, hou.DopNode]:
    """ Creates a wave tank of flip particles to be all splashy
        and render ready.
    """
def createadvectpop(solver: hou.OpNode, advectsource: hou.OpNode, oceansource: hou.OpNode, scale: float) -> hou.DopNode: ...
def waveTank(kwargs: ShelfToolKwargs) -> None: ...
def guidedOceanLayer(kwargs: ShelfToolKwargs) -> None: ...
def flatTank(kwargs: ShelfToolKwargs) -> None: ...
def oceanFlatTank(kwargs: ShelfToolKwargs) -> None: ...
def beachTank(kwargs: ShelfToolKwargs) -> None: ...
def inStage() -> bool: ...
def oceanFromSpectra(oceansurface: hou.ObjNode, gridsize: float, gridres: int, foamcam: str | None, spectra: Sequence[hou.SopNode], oceanproc: hou.LopNode | None, kwargs: ShelfToolKwargs) -> hou.SopNode: ...
def smallOcean(kwargs: ShelfToolKwargs) -> None: ...
def largeOcean(kwargs: ShelfToolKwargs) -> None: ...
def makeObjectViscous(flipnode: hou.OpNode) -> hou.DopNode:
    """ Giving the flipnode set up viscosity for it.
        No-op if already is.
    """
def makeViscous(kwargs: ShelfToolKwargs) -> None:
    """ Turn on viscosity for the selected FLIP objects.
    """
def particlefluidFindNamedMergeFromNode(dopnode: hou.OpNode, mergetype: str) -> hou.DopNode:
    """ Giving a DOP Node, find the particle fluid solver attached
        to the object.  Then look for the merge node off the
        semantically named input, creating a merge node if not
        present, and returning that merge node.
    """
def particlefluidConvertToEmitterOrSink(fluidobject: hou.DopData | None, dopnode: hou.OpNode | None, sopnode: hou.OpNode | None, emitterorsink: str) -> hou.DopNode:
    """ We add to the selected dopnode an emitter or sink which
        loads from objectnode.  If sopnode is None, we use
        default ellipse/box.  If dopnode is None, we look at
        fluidobject's creator.
    """
def particlefluidAddEmitterOrSink(kwargs: ShelfToolKwargs, emitterorsink: str) -> None:
    """ Selects a fluid object to be the destination.  If none
        selected, creates a new particle fluid.
    """
def convertToFLIP(dopobjectnode: hou.OpNode, nosopcooking: bool = False) -> None:
    """ Customize particle fluid dopnet into a FLIP dopnet
        nosopcooking disables any potential cooking of SOPs, and
        requires the caller is willing to setup the limits, etc.
    """
def createSteam(kwargs: ShelfToolKwargs) -> None:
    """ Selects a fluid sim for generating steam.  Will then
        create a new DOP  to hold the resulting whitewater sim.
    """
def createSteamFromNode(sceneviewer: hou.PaneTab, fluidnode: hou.OpNode) -> hou.DopNode:
    """ Creates a steam solver from a given node.
    """
def createSteamImport(prefixname: str, dopobject: hou.OpNode, sizeparm: hou.Parm | None) -> hou.ObjNode:
    """ Creates a node to import from a dopobject as a steam
        look/sim.
    """
def createSteamSource(fluidnode: hou.OpNode, nameprefix: str) -> hou.SopNode:
    """ Creates a source for steam
        Returns the created source  object
    """
def collideWithFluid(sourcenode: hou.OpNode, dopnode: hou.OpNode, solvernode: hou.OpNode) -> None: ...
def particleFluidSuction(fluidobject: hou.DopData, goalobject: hou.ObjNode) -> None:
    """ goalobject is made a target goal of fluidobject.
    """
def particleFluidSuctionSelect(kwargs: ShelfToolKwargs) -> None:
    """Selects fluid & suction object, then creates a suction
    effect driving the fluid into the target.
    """
def createCrownSplash(kwargs: ShelfToolKwargs) -> hou.DopNode:
    """ Creates a crown splash effect using a flip fluid box,
        an emitter and surface tension
    """
def createDripParticleFluid(kwargs: ShelfToolKwargs) -> hou.DopNode:
    """ Creates a dripping fluid effect using a continuous sphere emitter
        and surface tension
    """
