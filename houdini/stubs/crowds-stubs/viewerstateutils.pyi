import hou
from collections.abc import Sequence

class AgentJointSelector:
    """
    Utility class to manage drawing and selecting an agent's joints in a viewer
    state.
    """
    def __init__(self, scene_viewer: hou.SceneViewer, state_name: str) -> None: ...
    def reset(self, agent: hou.Agent, joints: Sequence[int], marker_scale: float) -> None:
        """
        Rebuilds the joint markers given a hou.Agent and list of joint indices.
        The previous selection will be maintained if the agent definition is
        the same as before.
        """
    def handleMouseEvent(self, ui_event: hou.ViewerEvent) -> bool:
        """
        Updates the selected or located joint from a mouse event. Returns True
        if the selected joint has changed.
        """
    def show(self, enabled: bool) -> None:
        """
        Toggles the visibility of the joint markers.
        """
    def selectedJoint(self) -> int:
        """
        Returns the index of the selected joint, or -1 if nothing is selected.
        """
    def agent(self) -> hou.Agent | None:
        """
        Returns the hou.Agent for which the markers are being drawn.
        """
    def jointTransform(self, joint_idx: int) -> hou.Matrix4:
        """
        Returns the world-space transform of the specified joint, including the
        agent's overall transform.
        """
