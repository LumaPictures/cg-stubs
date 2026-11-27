import apex
import hou
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs
from kinefx.stateutils import ViewerStateDisplayOptions
from kinefx.ui.rigvisualisers import KinefxRigVisualiser
from spriteutils import SpriteGadget

UPAXIS_GRAPH: str
SKEL_GRAPH_PARM: str
SCALEFACTOR_GRAPH_PARM: str
GROUP_GRAPH_PARM: str
GHOST_GRAPH: str
GEO_GRAPH_PARM: str
GEO_GRAPH_OUTPUT: str
COLOR_GRAPH_PARM: str
ALPHA_GRAPH_PARM: str
GADGET_NAME: str

class JointGadget:
    """
    creates a simple joint visualizer that is based on the kinefx Rig visualizer. We do not support any direct
    interaction with the skeleton though and we purely use this wrapper to visualize the
    orientations and the skeleton hierarchy
    we extend it with the functionality of a twist visualizer, NOTE: this one might need to be moved to to the
    kinefx rig visualizer module
    we extend it further more with a semi transparent visualizers for a reference geometry to place the joints
    more easily
    """
    scene_viewer: hou.SceneViewer
    name: str
    rigvis_drawable: KinefxRigVisualiser | None
    display_options: ViewerStateDisplayOptions
    upaxis_drawable: hou.GeometryDrawable | None
    upaxis_geo: hou.Geometry
    skeleton: hou.Geometry
    reference_drawable: hou.GeometryDrawable | None
    reference_drawables: list[hou.GeometryDrawable]
    reference_color: hou.Vector4
    reference_line_color: hou.Vector4
    reference_color_light: hou.Vector4
    reference_line_color_light: hou.Vector4
    reference_geo: hou.Geometry
    sprite_gadget: SpriteGadget
    upaxis_graph: apex.Graph
    rig_line_drawable: hou.GeometryDrawable | None
    reference_line_drawable: hou.GeometryDrawable | None
    show_upaxis: bool
    upaxis_scale: float
    upaxis_scale_step: float
    show_reference_geo: bool
    show_skeleton: bool
    show_reference_line: bool
    reference_alpha: float
    skeleton_ignore_group: str
    light_mode: bool
    def __init__(self, scene_viewer: hou.SceneViewer, name: str | None = None) -> None: ...
    def initGraphs(self) -> None:
        """load the tag graph from the registry and compile at once"""
    def initDrawables(self) -> None:
        """creates all the drawables relevant for the gadget and shows them"""
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def show(self, on: bool = True) -> None:
        """shows or hides all the gadget elements if they are set to be visible"""
    def showAxis(self, on: bool) -> None:
        """sets the visibility of the axes drawable of the rig visualizer"""
    def showUpVector(self, on: bool) -> None:
        """sets the visibility of the twist joint visualizer"""
    def showLink(self, on: bool) -> None:
        """sets the visibility of the joint link drawable of the rig visualizer"""
    def showReference(self, on: bool) -> None:
        """shows the ghosted reference geometry of a the character that we want as a helper to place our joints properly"""
    def showReferenceLine(self, on: bool) -> None: ...
    def showSkeleton(self, on: bool) -> None: ...
    def setSkeleton(self, skeleton: hou.Geometry) -> None:
        """sets the skeleton of """
    def setReferenceGeometry(self, geo: hou.Geometry) -> None:
        """
        process the given geometry to be semi transparent and without a texture to be used as a ghosted
        geo reference for better joint placement
        """
    def getReferenceGeometry(self) -> hou.Geometry | None:
        """
        process the given geometry to be semi transparent and without a texture to be used as a ghosted
        geo reference for better joint placement
        """
    def setDefaultTwistScale(self, geo: hou.Geometry | None = None) -> None:
        """calculate the default scale for the twist visualizer based on the height of the provided joint geometries
        or based on a given input geometry

        :param geo: an optional input geometry to be used as a height reference for the twist drawable scale,
        defaults to None
        """
    def setUpAxisGeometry(self, skeleton: hou.Geometry) -> None:
        """
        generate a twist geometry with sem-itransparent colored square faces along the secondary and tertiary axis. We
        want to attach that geometry to joints in order to help determining the correct twist orientations of joints
        and in order to quickly catch orientation misalignments between joints

        :param skeleton: the reference skeleton that is to get a twist axis preview
        """
    def setLineGeometry(self, skeleton: hou.Geometry) -> None: ...
    def clear(self) -> None:
        """hides and removes all drawables of the gadget"""
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """handles sprite selection"""
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """handles the scaling of the axis based on mouse scroll plus ctrl"""
