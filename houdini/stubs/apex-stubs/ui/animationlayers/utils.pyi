import hou
from .commands import Commands as state_commands, sceneViewer as sceneViewer
from .membership import AnimationLayerMembershipModel as AnimationLayerMembershipModel
from .model import AnimationLayersModel as AnimationLayersModel, AnimationLayersModelHandle as AnimationLayersModelHandle, BASE_LAYER_NAME as base_layer
from _apexscene import Scene as Scene
from apex.ui.animationlayers.panel import AnimationLayersPanel as AnimationLayersPanel
from collections.abc import Sequence

Commands = state_commands
BASE_LAYER_NAME = base_layer
PANEL_INTERFACE_NAME: str
NODE_INTERFACE_NAMES: tuple[str, str, str]

def getAnimPath(scene: Scene, collection_name: str) -> str: ...
def getRigFromCollection(scene: Scene, collection_name: str) -> str | None: ...
def createModel(scene_viewer: hou.SceneViewer | None = None) -> AnimationLayersModelHandle:
    """
    Create a new AnimationLayersModel, optionally setting the scene_viewer it
    is tied to.
    """
def createMembershipModel(scene_viewer: hou.SceneViewer | None = None) -> AnimationLayerMembershipModel:
    """
    Create a new AnimationLayerMembershipModel, optionally setting the scene_viewer it
    is tied to.
    """
def updateModel(model: AnimationLayersModelHandle | None, membership_model: AnimationLayerMembershipModel | None, panel: AnimationLayersPanel | None = None) -> None:
    """
    Updates the given model by passing it to all Animation Layer panels.
    """
def selectLayers(layers: Sequence[str], cur_node: hou.Node | None = None) -> None:
    """
    Selects the rows corresponding to each layer.
    """
