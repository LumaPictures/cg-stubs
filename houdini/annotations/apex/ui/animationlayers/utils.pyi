from collections.abc import Sequence

import hou
from _apexscene import Scene
from apex.ui.animationlayers.membership import AnimationLayerMembershipModel
from apex.ui.animationlayers.model import AnimationLayersModelHandle
from apex.ui.animationlayers.panel import AnimationLayersPanel

NODE_INTERFACE_NAMES: tuple[str, str, str]

def getAnimPath(scene: Scene, collection_name: str) -> str: ...
def getRigFromCollection(scene: Scene, collection_name: str) -> str | None: ...
def createModel(scene_viewer: hou.SceneViewer | None = ...) -> AnimationLayersModelHandle: ...
def createMembershipModel(scene_viewer: hou.SceneViewer | None = ...) -> AnimationLayerMembershipModel: ...
def updateModel(
    model: AnimationLayersModelHandle | None,
    membership_model: AnimationLayerMembershipModel | None,
    panel: AnimationLayersPanel | None = ...,
) -> None: ...
def selectLayers(layers: Sequence[str], cur_node: hou.Node | None = ...) -> None: ...
