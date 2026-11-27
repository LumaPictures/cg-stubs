import hou
from collections.abc import Iterable
from enum import StrEnum
from typing import Literal, TypedDict

class _PerspectiveCameraParms(TypedDict):
    win: tuple[float, float]
    winsize: tuple[float, float]
    projection: Literal['perspective']
    aperture: float
    focal: float
    nearclip: float

class _OrthoCameraParms(TypedDict):
    win: tuple[float, float]
    winsize: tuple[float, float]
    projection: Literal['ortho']
    orthowidth: float

def checkParmsWriteable(node: hou.OpNode, parms: Iterable[str]) -> bool: ...
def applyCameraTransform(node: hou.OpNode, view_transform: hou.Matrix4, pivot: hou.Vector3, parent_transform: hou.Matrix4, time: float) -> bool: ...
def cameraParms(viewport: hou.GeometryViewport) -> _PerspectiveCameraParms | _OrthoCameraParms: ...
def createCameraInCurrentState(viewer: hou.SceneViewer, viewport: hou.GeometryViewport, view_transform: hou.Matrix4, node: hou.Node) -> bool:
    """
    Allow the current state to deal with creating the camera, returning True if
    the state handled it.
    """
def changeCameraViewInCurrentState(viewer: hou.SceneViewer, viewport: hou.GeometryViewport, view_parms: hou.GeometryViewportCamera, view_transform: hou.Matrix4, camera: str, node: hou.Node | None, time: float) -> bool:
    """
    Allow the current state to deal with view changes for cameras, returning
    True if the state handled it.
    """

class ViewErrorMessages(StrEnum):
    PARMS_NOT_WRITEABLE = 'Camera Parms are not writeable !'
    ONLY_COP_CAMERA = 'Only Camera COP nodes are editable'

def warnAboutParms(viewer: hou.SceneViewer, viewport: hou.GeometryViewport) -> None: ...
def warnAboutCameraCOP(viewer: hou.SceneViewer, viewport: hou.GeometryViewport) -> None: ...
