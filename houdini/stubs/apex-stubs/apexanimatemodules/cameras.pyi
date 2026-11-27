import hou
from apex.apexanimatemodules.base import ApexAnimateBaseModule as ApexAnimateBaseModule, _AnimateState as _BaseState
from apex.camerautils import CameraCommands as CameraCommands, SceneCamera as SceneCamera
from houtypes import SceneViewerEventKwargs, ViewerStateCommandKwargs, ViewerStateEnterKwargs, ViewerStateKwargs
from typing import Protocol
from typing_extensions import TypedDict, Unpack

class _AnimationPreferences(TypedDict):
    autokey: bool
    autocommit: bool
    autokeytuples: bool

class _AnimateState(_BaseState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def _getSceneNodeGeometry(self) -> hou.Geometry | None: ...
    def flashError(self, msg: str, duration: float = ...) -> None: ...
    def reloadFromGeometry(self, *, force: bool = ...) -> None: ...

class _ViewportEventKwargs(TypedDict):
    event_type: hou.EnumValue[hou.geometryViewportEvent]
    desktop: hou.Desktop
    viewer: hou.SceneViewer
    viewport: hou.GeometryViewport

class ApexAnimateCameras(ApexAnimateBaseModule):
    """
    This class is owned by the APEX Animate state and has access to
    all of its variables.

    It implements all of the functions necessary to manage cameras in the
    APEX Aniamte viewer state.
    """
    def __init__(self, state: _AnimateState) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ On viewer state enter event
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """ On viewer state exit event
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool:
        """ Implements the commands for managing cameras
        """
    def updateViewsFromCameras(self) -> None:
        """
        Update all viewports looking through an extra camera

        We go through all viewports and check if they are looking
        through a scene camera
        if they are, then we look up the camera name and update
        the view accordingly

        """
    def setExtraCameras(self) -> None:
        """
        When loading the scene, populate the viewport camera pill menu
        with our cameras found in rigs.
        we go through the characters and look for camera geometry
        and construct the camera name like /char/camera_name
        ie. /mycamerarig.char/camera_1
        """
    def onCameraSwitched(self) -> None:
        """
        Called when the viewport pill menu is switched to a new camera
        When viewing through a scene/extra camera, we want to hide its
        associated drawables so they don't obstruct the view
        """
    def onSceneViewerEvent(self, kwargs: SceneViewerEventKwargs) -> None:
        """Respond to viewer events relevant to the active Animate state."""
    def _onCameraSwitched(self, **kwargs: Unpack[_ViewportEventKwargs]) -> None: ...
    def setViewportCamera(self, camera_path: str, viewport: hou.GeometryViewport) -> None: ...
    def lockCameraToView(self) -> None: ...
    def setCameraFromView(self, camera_path: str, xform: hou.Matrix4) -> bool:
        """
        Called when the scene/extra camera has been moved through viewport
        interaction.
        This method lets us set the channel primitives associated with our rig
        to find the control which needs to be edited, we look for
        the sidefx::camera and sidefx::resetlocal tags
        """
    def createCameraFromView(self, args: ViewerStateCommandKwargs) -> bool:
        """
        Called when New Camera is clicked in the viewport pill menu
        """
    def setViewFromCamera(self, vp: hou.GeometryViewport, camera_path: str) -> None:
        """
        Called when the pill menu is set to an extra camera
        We need to give it the camera parameters of our 
        extra camera by calling viewport.setCameraParms    
        """
    def clearExtraCameras(self) -> None:
        """
        When exiting the animate state, we want to clear all of our extra
        cameras to make sure they don't show up in the pill menu anymore
        """
    def createCameraNode(self, parent_node: hou.Node) -> str:
        """
        returns the path to the newly created camera drawable
        """
    @property
    def state(self) -> _AnimateState: ...
