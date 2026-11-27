from collections.abc import Iterable
from typing import Literal, TypedDict, type_check_only

import hou

@type_check_only
class _PerspectiveCameraParms(TypedDict):
    win: tuple[float, float]
    winsize: tuple[float, float]
    projection: Literal["perspective"]
    aperture: float
    focal: float
    nearclip: float

@type_check_only
class _OrthoCameraParms(TypedDict):
    win: tuple[float, float]
    winsize: tuple[float, float]
    projection: Literal["ortho"]
    orthowidth: float

def checkParmsWriteable(node: hou.OpNode, parms: Iterable[str]) -> bool: ...
def applyCameraTransform(
    node: hou.OpNode,
    view_transform: hou.Matrix4,
    pivot: hou.Vector3,
    parent_transform: hou.Matrix4,
    time: float,
) -> bool: ...
def cameraParms(viewport: hou.GeometryViewport) -> _PerspectiveCameraParms | _OrthoCameraParms: ...
def createCameraInCurrentState(
    viewer: hou.SceneViewer,
    viewport: hou.GeometryViewport,
    view_transform: hou.Matrix4,
    node: hou.Node,
) -> bool: ...
def changeCameraViewInCurrentState(
    viewer: hou.SceneViewer,
    viewport: hou.GeometryViewport,
    view_parms: hou.GeometryViewportCamera,
    view_transform: hou.Matrix4,
    camera: str,
    node: hou.Node | None,
    time: float,
) -> bool: ...
def warnAboutParms(viewer: hou.SceneViewer, viewport: hou.GeometryViewport) -> None: ...
def warnAboutCameraCOP(viewer: hou.SceneViewer, viewport: hou.GeometryViewport) -> None: ...
