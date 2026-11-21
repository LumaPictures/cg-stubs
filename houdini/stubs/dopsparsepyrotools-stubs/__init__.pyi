# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Iterable
from houtypes import HDANodeEventKwargs, ParmActionButtonKwargs, ParmCallbackKwargs, ShelfToolKwargs
from hrecipes import rtypes as rtypes
from typing import TypedDict

class _PyroLightPreset(TypedDict):
    dist_color: hou.Color
    dist_intensity: float
    dist_exposure: float
    dist_rotate: hou.Vector3
    env_color: hou.Color
    env_intensity: float
    env_exposure: float

SMOKE_LIGHT_BROWN_COLOR: hou.Color
SMOKE_DARK_BROWN_COLOR: hou.Color
SMOKE_LIGHT_GREY_COLOR: hou.Color
SMOKE_DARK_GREY_COLOR: hou.Color
SMOKE_BLACK_COLOR: hou.Color
pyro_shader_ref_data: rtypes.ParmDataDict
pyrosource_parms: dict[str, str]

def activePaneToOBJ(kwargs: ShelfToolKwargs) -> None: ...
def propagatePyroSourceSpreadRamps(node: hou.SopNode) -> None:
    """ Due to a bug with multiplarms, we have to do a dummy read on the ramps
        that are 2 levels deep; otherwise, there is a race condition on the first
        evaluation of the inner parameter. This function can be removed once that
        issue is resolved.
    """
def copyParmSet(dstnode: hou.OpNode, srcnode: hou.OpNode, parmset: Iterable[tuple[str, str]]) -> None:
    """ Copies the values of the parameters from the source node to the
        destination. parmset is a list of tuples: (destination parameter, source
        parameter).
    """
def copyRampParm(dstnode: hou.OpNode, dstramp: str, srcnode: hou.OpNode, srcramp: str) -> None:
    """ Copies the ramp parameter from the source to the destination.
    """
def createSparsePyroDOP(root: hou.OpNode, network_name: str, source_name: str, set_emission: bool) -> tuple[hou.DopNode, hou.DopNode, hou.DopNode]:
    """ Creates a new object-level DOP network and sets up a sparse pyro object,
        sparse pyro solver, and a volume source inside it. Returns a tuple of
        these nodes in the listed order.
    """
def createSparsePyroImportAndMat(objnode: hou.DopNode, name: str, sceneviewer: hou.SceneViewer) -> None:
    """ Creates the import network for the sparse pyro simulation and sets up a
        material for it, pulling visualization information from the sparse pyro
        object.
    """
def createSparseCampfire(kwargs: ShelfToolKwargs) -> None:
    """ Creates a campfire simulation using the sparse pyro solver.
    """
def sopGPUBurst(kwargs: ShelfToolKwargs, make_in_sop: bool = False) -> hou.SopNode:
    """ Creates a GPU-based burst at the SOP level
        If make_in_sop is True, all nodes are put down in the current SOP
        location; otherwise, location needs to be picked in the viewport, and
        new nodes will be placed in an object-level geometry node.
    """
def sopGPUTorch(kwargs: ShelfToolKwargs, make_in_sop: bool = False) -> hou.SopNode:
    """ Creates a GPU-based torch fire at the SOP level
        If make_in_sop is True, all nodes are put down in the current SOP
        location; otherwise, location needs to be picked in the viewport, and
        new nodes will be placed in an object-level geometry node.
    """
def sopMuzzleFlash(kwargs: ShelfToolKwargs, make_in_sop: bool = False) -> hou.SopNode:
    """ Creates a Muzzle Flash at the SOP level
        If make_in_sop is True, all nodes are put down in the current SOP
        location; otherwise, location needs to be picked in the viewport, and
        new nodes will be placed in an object-level geometry node.
    """
def createSpreadingFireSource(srcgeo: hou.SopNode, diam: float, deforming: bool) -> tuple[hou.SopNode, hou.SopNode]:
    """ Creates the rasterizer from the given source geo for
        spreading fire, including a hot spot to ignite
        Returns the rasterizer and spreader.
    """
def spreadingFireSourceSetup(volsrc: hou.OpNode, numparm: str, prefix: str) -> None:
    """ Sets up the spreading fire's source imports
    """
def spreadingFireSolverSetup(solver: hou.OpNode) -> None:
    """ Configures a solver for spreading fire.
    """
def createSopSpreadingFire(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sop-level spreading fire from selected object.
    """
def createSpreadingFire(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sparse spreading fire simulation from the selected object.
    """
def sopSpreadingFire(kwargs: ShelfToolKwargs) -> None:
    """ Creates a sparse spreading fire simulation in the SOP network
    """
def sopSpreadingFireFromNode(kwargs: ShelfToolKwargs, srcgeo: hou.SopNode) -> None:
    """ Creates a sop level spreading fire from the given node
    """
def setLast(kwargs: ShelfToolKwargs | ParmCallbackKwargs, node: hou.OpNode) -> None:
    """ Somme common functionality to apply on the last generate node.
    """
def createBillowySmoke(kwargs: ShelfToolKwargs, usedops: bool = False) -> None:
    """ Creates a thick smoke rising from a torus
    """
def sopBillowySmoke(kwargs: ShelfToolKwargs) -> None:
    """ Creates a thick smoke rising from a torus
    """
def sopBillowySmokeFromNode(kwargs: ShelfToolKwargs, smoke_base: hou.SopNode, usedops: bool) -> None:
    """ Creates thick smoke from reference SOP
    """
def createFireball(kwargs: ShelfToolKwargs, usedops: bool = False) -> None:
    """ Creates a simple fireball explosion
    """
def sopFireball(kwargs: ShelfToolKwargs) -> None:
    """ Creates a simple fireball explosion
    """
def sopFireballFromNode(kwargs: ShelfToolKwargs, pyroburstsource: hou.SopNode, usedops: bool) -> None:
    """ Creates fireball from reference SOP
    """
def createFireballShockwave(kwargs: ShelfToolKwargs, usedops: bool = False) -> None:
    """ Creates a simple fireball with shockwave
    """
def sopFireballShockwave(kwargs: ShelfToolKwargs) -> None:
    """ Creates a simple fireball with shockwave
    """
def sopFireballShockwaveFromNode(kwargs: ShelfToolKwargs, pyroburstsource_fireball: hou.SopNode, usedops: bool) -> None:
    """ Creates a simple fireball with shockwave from reference SOP
    """
def setupBasicExplosion(kwargs: ParmCallbackKwargs) -> None:
    """ Generates a pyrosolver with basic explosion setup when invoked from the Quick Setup menu of the Pyro Burst Source node.
        
    """
def createAerialExplosion(kwargs: ShelfToolKwargs, usedops: bool = False) -> None:
    """ Creates an aerial explosion with trails.
    """
def sopAerialExplosion(kwargs: ShelfToolKwargs) -> None:
    """ Creates an aerial explosion with trails.
    """
def sopAerialExplosionFromNode(kwargs: ShelfToolKwargs, add: hou.SopNode, usedops: bool) -> None:
    """ Creates an aerial explosion with trails.
    """
def createGroundExplosion(kwargs: ShelfToolKwargs, usedops: bool = False) -> None:
    """ Creates an ground explosion with trails.
    """
def sopGroundExplosion(kwargs: ShelfToolKwargs) -> None:
    """ Creates an ground explosion with trails.
    """
def sopGroundExplosionFromNode(kwargs: ShelfToolKwargs, add: hou.SopNode, usedops: bool) -> None:
    """ Creates a large scale ground explosion with trails.
    """
def createBonfire(kwargs: ShelfToolKwargs, usedops: bool = False) -> None:
    """ Creates a bonfire setup
    """
def sopBonfire(kwargs: ShelfToolKwargs) -> None:
    """ Creates an bonfire setup
    """
def sopBonfireFromNode(kwargs: ShelfToolKwargs, tube: hou.SopNode, usedops: bool = False) -> None:
    """ Creates a bonfire setup
    """
def createDOPSeedField(pyrosolver: hou.SopNode) -> hou.DopNode | None:
    """ Creates a simple dopnetwork to calculate and visualize speed field.
        It will be created inside the editable dop context.

        :param pyrosolver: The pyrosolver sopnode to apply speef field to.
    """
def rasterizeFromPyroSource(inputnode: hou.SopNode, pyrosourcenode: hou.SopNode) -> hou.SopNode:
    """ Creates a Volume Rasterize Attributes node that is tightly linked to Pyro Burst Source
        and Pyro Trail Source

        :param inputnode: The node that is connected to the input of this the new Volume Rasterize Attribute node.
        :param pyrosourcenode: Either a Pyro Burst Source or a Pyro Trail Source node. Most of the time this is the same as the inputnode.
    """
def buildBlockPair(parent: hou.SopNode, name: str, begintype: str, endtype: str, wire_to_end: bool) -> tuple[hou.SopNode, hou.SopNode]:
    """ Builds a pair of block nodes, a begin and an end, and links
        them together nicely.

        wire_to_end means to wire to second input on node creation.
    """
def setupTrailSimNetwork(node: hou.SopNode, trailtype: str | None = None) -> hou.SopNode:
    """ Generate a Trail Sim Setup that matches the Pyro Ballistic Paths

        :param node: The node the generated network connects to

        :param trailtype: the default generates a default particle simulation, 'trailsim' will generated pyro trails, while 'sparkssim' will create a simulation for sparks.

    """
def setupTrailSim(kwargs: ParmCallbackKwargs, trailtype: str | None = None) -> hou.SopNode:
    """ Generate a Trail Sim Setup that matches the Pyro Ballistic Paths
    """
def setupSparkTrail(particletrail: hou.SopNode) -> None: ...
def setupTimeBlend(timeblend: hou.SopNode) -> None: ...
def setupBallisticSparks(kwargs: ParmCallbackKwargs) -> None: ...
def setupDebrisSim(kwargs: ParmCallbackKwargs) -> None: ...
def torchGenerator(subnet: hou.SopNode) -> None: ...
def debrisGenerator(parent: hou.OpNode) -> hou.SopNode: ...
def setupBlastWaveRings(kwargs: ParmCallbackKwargs) -> hou.SopNode:
    """ Generate a Blast Rings with matching Blastwave.
    """
def setupCullVSourceAttrib(kwargs: ParmCallbackKwargs, ctype: str, keep: str) -> None:
    """ Generate a Vex Wrangle to only keep 'v' attribute on selected component.
    """
def setupStartFrameVis(kwargs: ParmCallbackKwargs) -> None:
    """ Generate a Vex Wrangle to color points when timeline's time is equal or larger then the point's 'startframe' point attribute value.
    """
def setupSourceVolume(kwargs: ParmCallbackKwargs) -> None:
    """ Generate a Source Volume Setup
    """
def setupSinglePoint(kwargs: ParmCallbackKwargs) -> None:
    """ Generates a single point with the add node
    """
def setupSharpenVolume(node: hou.SopNode, volumename: str = 'density') -> hou.SopNode:
    """ Generates a subnet with voluemconvolve3 node with predefined sharpening settings.

        :param node: The volumeconvolve will be placed under this node.
        :param volumename: The name of the volume to sharpen.
    """
def linkMaterialToSolver(solver_node: hou.SopNode, shader_node: hou.VopNode, use_data: bool = False) -> None:
    """ Links the pyro solver node and shader node together. The shader node will
        gain channel references pointing to the corresponding parts of
        the look node. 
    """
def linkMaterialToLook(look_node: hou.SopNode, shader_node: hou.VopNode, use_data: bool = False) -> None:
    """ Links the look node and shader node together. The shader node will
        gain channel references pointing to the corresponding parts of
        the look node. 
    """
def dereferenceMaterial(node: hou.OpNode, use_data: bool = False) -> None:
    """ Breaks any backwards links from the shop_materialpaths material
        to us.
    """
def createPyroShader(kwargs: ShelfToolKwargs | ParmCallbackKwargs, isreference: bool = False, create_previewshader: bool = True, assignshader: bool = True, shaderpath: str | None = None) -> hou.VopNode | None:
    """ Creates a new Pyro Shader and overrides the Material Path. 

        :param isreference: Creates a reference link between the look node and the shader
        :param create_previewshader: Creates an additional xpu pyro preview shader with a collect node.
        :param assignshader: Don't assign shader to the look node when generating stage setup.
        :param shaderpath: Predifined matnet path, when given the display message ui will not be envoked.
    """
def createPyroMaterial(node: hou.SopNode, isreference: bool = False, assignmaterial: bool = True, materialpath: str = '') -> None:
    """ Creates a new Pyro Material subnet.

        :param node: The node that invokes the shader creation, this should be a SOP Pyro Solver or a SOP Pyro Bake
        Volume.
        :param isreference: Creates a reference link between the look node and the material.
        :param assignmaterial: Don't assign material to the look node when generating stage setup.
        :param materialpath: Predefined matnet path, when given the display message ui will not be invoked.
    """
def createMatchingPyroPreviewShader(pyroshader: hou.VopNode, isreference: bool = False) -> hou.VopNode: ...
def combinePyroShaders(pyroshader: hou.VopNode, previewshader: hou.VopNode) -> hou.VopNode: ...
def createRenderGeometry(node: hou.SopNode, convert: bool = False) -> hou.ObjNode:
    """ Creates an object level geometry container user mantra rendering.

        :param node: The last sop node in the network chain that generates the geometry to be rendered.

        :param convert: When True, the parent of node will be used as the render geometry, otherwise a new object level Geometry object is created that merges in the geometry from the given node.

    """
def createOutput(node: hou.SopNode, useNull: bool = False, name: str | None = None) -> hou.SopNode:
    """ Creates a SOP Output or a Null node to be used as a reference at the end of the hierarchy.

        :param node: The last sop node in the network chain that generates the geometry to be rendered.

        :param useNull: Use SOP Output or a SOP Null as the output node.

        :param name: Optional name of the node after the prefix.

    """
def createStageSOPImport(stage: hou.OpNode, sopnode: hou.SopNode, name: str) -> tuple[hou.LopNode, str]:
    """ Creates a sopimport for karma rendering in the given stage.

        :param stage: The stage to contain the SOP Import node

        :param sourcenode: The node used to invoke this script. This is usually a SOP Pyro Solver or a Pyro Bake Volume node.

    """
def createStageRenderGeometrySettings(stage: hou.OpNode, blurscale: float = 1, emission: int | None = False, emitscale: float = 1) -> hou.LopNode:
    """ Creates a LOP Geometry Settings for rendering volumes.
    """
def createStageMatLib(stage: hou.OpNode, primpath: str | None = None) -> hou.LopNode:
    """ Creates a LOP Material for rendering volumes.
    """
def setStageMaterial(kwargs: ParmCallbackKwargs, matlib: hou.LopNode, islink: bool = True) -> None: ...
def getSelectedPyroLightPreset(idx: int = 0) -> _PyroLightPreset: ...
def createStageDistLight(stage: hou.OpNode, rotate: hou.Vector3 = ..., color: hou.Color = ..., intensity: float = 1, exposure: float = 0) -> hou.LopNode:
    """ Creates a LOP Distance Light for rendering volumes.
    """
def createStageEnvLight(stage: hou.OpNode, color: hou.Color = ..., intensity: float = 1, exposure: float = 0, envmap: str = '') -> hou.LopNode:
    """ Creates a LOP Dome Light for rendering volumes.
    """
def createOBJCam(kwargs: ParmCallbackKwargs) -> hou.ObjNode:
    """ Creates an object level camera for rendering volumes.
    """
def createStageCam(kwargs: ParmCallbackKwargs, stage: hou.OpNode) -> tuple[hou.LopNode, str]:
    """ Creates a LOP Camera for rendering volumes.
    """
def createStageKarma(stage: hou.OpNode, cameraprimpath: str) -> hou.LopNode:
    """ Creates a LOP Karma for rendering volumes.
    """
def createVolumeLight(looknode: hou.SopNode, render_geo: hou.ObjNode | None = None) -> hou.ObjNode:
    """ Creates an object level volume light for mantra rendering.

        :param looknode: The node containing the shop_materialpath attribute. This is usually a SOP Pyro Solver or a Pyro Bake Volume node.

        :param render_geo: The geometry containing the volumes to be rendered.

    """
def createEnvLight(color: hou.Color = ..., intensity: float = 1, exposure: float = 0, envmap: str = '') -> hou.ObjNode:
    """ Creates an object level Environment Light for rendering volumes.
    """
def createDistLight(rotate: hou.Vector3 = ..., color: hou.Color = ..., intensity: float = 1, exposure: float = 0) -> hou.ObjNode:
    """ Creates an object level Distance Light for rendering volumes.
    """
def createMantra(node: hou.TopNode) -> hou.TopNode:
    """ Creates a ROP Mantra node for the output of SOP Pyro Solver of Pyro Bake Volume.
    """
def hasEmission(node: hou.SopNode) -> int | None: ...
def getPyroNodeName(node: hou.SopNode) -> str: ...
def lightPresetUI() -> tuple[int, ...]: ...
def createRenderStage(node: hou.SopNode, output: hou.SopNode, stage: hou.OpNode) -> None: ...
def stageSetup(kwargs: ParmCallbackKwargs) -> None:
    """ Creates a ready to render lopnet setup for the output of SOP Pyro Solver of Pyro Bake Volume.
    """
def renderSetup(kwargs: ParmCallbackKwargs, create_render_geo: bool = True, create_vlight: bool = True, create_envlight: bool = True, create_distlight: bool = True, create_cam: bool = True, create_shader: bool = False, create_mantra: bool = True) -> None:
    """ Creates an object level light rig
    """
def applySmokeSourcePreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Smoke Presest on the Pyro Solver's Source tab.
    """
def applyFireSourcePreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Fire Presest on the Pyro Solver's Source tab.
    """
def applyExplosionSourcePreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Fire Presest on the Pyro Solver's Source tab.
    """
def applySmokeLookPreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Smoke Presest on the Pyro Solver's Look tab.
    """
def applyFireLookPreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Fire Presest on the Pyro Solver's Look tab.
    """
def applySmokeExportPreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Smoke Presest on the Pyro Solver's Export tab.
    """
def applyFireExportPreset(kwargs: HDANodeEventKwargs) -> None:
    """ Applies Fire Presest on the Pyro Solver's Export tab.
    """
def setupSDFCollision(kwargs: ParmCallbackKwargs) -> None:
    """ Creates a Vdb From Polygons node the generate the collision volume.
    """
def addColorSource(kwargs: ParmCallbackKwargs) -> None:
    """ Add and attidion source to the SOP Pyro Solver to source color.
    """
def createReferenceBound(kwargs: ParmCallbackKwargs) -> None:
    """ Creates a box with the size of the pyro domain and links the size parameters.
    """
def createPyroLook(kwargs: ParmCallbackKwargs) -> None:
    """ Creates a default Pyro Bake Volume node.
    """
def optimizeExports(kwargs: ParmCallbackKwargs) -> None:
    """ Enables disk space saving optimizations on the Export/Post-Process section of the SOP Pyro Solver.
    """
def cacheSim(kwargs: ParmCallbackKwargs) -> None:
    """ Generates a file cache to save simulation
    """
def AASeed(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AALifeSpan(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AADistanceThreshold(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAInitialSize(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AADirection(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAMuzzleLength(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AASpreadAngle(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AATrailLength(kwargs: ParmActionButtonKwargs, geoclass: str = 'primitive') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AATrailRadius(kwargs: ParmActionButtonKwargs, geoclass: str = 'primitive') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AASpreadStartAngle(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAAzimuthAngle(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAAzimuthStartAngle(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AALineLength(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AARingLineLength(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AALineStart(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AARoundness(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AANumberOfTrailings(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAPointsPerPoint(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AATrailingSeparation(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AATrailingPointSeparation(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AATrailingDepth(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAStartFrame(kwargs: ParmActionButtonKwargs | ParmCallbackKwargs, geoclass: str = 'point') -> hou.SopNode:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AATrailDuration(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAFrameDuration(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AASpeedScale(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAOutwardExpansion(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAInteriorExpansion(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAExteriorExpansion(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AADirectionalExpansion(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AADirectionalTranslation(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAVelocityScale(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AADrag(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAMass(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AAFadeAge(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def AASourceAttrib(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksAlpha(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksLenstart(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Creates an attribute adjust node for randomizing the lenstart attribute
        for the particle trail SOP.
    """
def sparksLenend(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Creates an attribute adjust node for randomizing the lenend attribute
        for the particle trail SOP.
    """
def sparksTailWidth(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksHeadWidth(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksValue(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksColor(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksSplitPercent(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksPointsPerPoint(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksSplitStartAngle(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksSplitEndAngle(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksVelocityScale(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def sparksSplitDuration(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGeneratePointSeparation(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateLength(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateWidth(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateShapeDistortScale(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateFlatten(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateRotation(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateSecondaryIteration(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateSecondaryDisplacement(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateSecondarySpread(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def CloudShapeGenerateCloudSpecies(kwargs: ParmActionButtonKwargs, geoclass: str = 'point') -> None:
    """ Generates Attribute Adjust nodes for using parameters provided by the pyro source tools.

    geoclass will set the 'Class' parameter on the AA node.
    """
def hgdValuesFromDropletSize(d: float) -> tuple[float, float, float, float]:
    """
    This model provides a meaningful and intuitive single parameter for the Henyey-Greenstein-Drain model. 
    
    Calculates anisotropy, secondary mix, secondary anisotropy, and secondary shape values for Henyey-Greenstein-Drain
    function in this given order; using a droplet size input (µm).

    The logic for this function is taken from An Approximate Mie Scattering Function for Fog and Cloud Rendering by NVIDIA
    https://research.nvidia.com/labs/rtr/approximate-mie/publications/approximate-mie-supplemental.pdf

    Original paper:
    https://research.nvidia.com/labs/rtr/approximate-mie/publications/approximate-mie.pdf
    """
def volumeLimitFalloff(falloff: float = 0, start_level: float = 0, max_density: float = 1, density_threshold: float = 0.001) -> float:
    """
    Calculates the necessary volume ray bounces with a given falloff.
    """
def createMaskedPyroMaterial(kwargs: ShelfToolKwargs, pyrotype: str | None = None) -> hou.VopNode:
    """
    Creates a subnet, configured to be masked for specific VOP nodes, by
    using the 'tabmenumask' spare parameter.

    prototype can be: None, smoke, fire, scatter, cloud, bakedcloud, uniformvolume
    """
