import _apex
import apex
import hou
from _apexscene import ChannelPrimBindings as ChannelPrimBindings, ControlManager as ControlManager, Scene as Scene
from enum import StrEnum

class CameraCommands(StrEnum):
    SetCameraFromView = 'setCameraFromView'
    CreateCameraFromView = 'createCameraFromView'
    SetViewFromCamera = 'setViewFromCamera'

class SceneCamera:
    rig_path: str
    camera_path: str
    Tag: str
    def __init__(self, rig_path: str, camera_path: str, scene: Scene) -> None: ...
    def setViewportCameraParms(self, viewport: hou.GeometryViewport) -> None:
        """
        Called by the scene animate in setViewFromCamera to set the view
        for an extra camera from our camera primitive geometry
        """
    def findNode(self) -> int | None:
        """
        Finds the APEX node in the graph with the camera tag    
        """
    def findController(self) -> str | None:
        """
        the sidefx::camera tag determines which TransformObject on the
        camera rig should be updated when moving the camera through viewport
        interaction.
        """
    def findControllersToReset(self) -> list[str]:
        """
        the sidefx::resetlocal tag determines which TransformObject on the
        camera rig should be reset when moving the camera through viewport
        interaction.
        """
    def getRestTransform(self) -> hou.Matrix4:
        """
        If a camera coming into the scene has a non-identity transform
        setCameraFromView needs to account for that to avoid double xforms    
        """
    def rig(self) -> apex.SceneGraph: ...
    def rigGraph(self) -> _apex.Graph: ...
    def animBinding(self) -> ChannelPrimBindings | None: ...
    def controlManager(self) -> ControlManager: ...
    def controlPaths(self) -> list[str]: ...
    def name(self) -> str: ...
    @property
    def scene(self) -> Scene | None: ...
