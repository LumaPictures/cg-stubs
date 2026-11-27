import hou
from curvestate.curve3.controller import Curve3Controller

class Curve3ChannelManager:
    scene_viewer: hou.SceneViewer
    controller: Curve3Controller
    channel_list: hou.ChannelList | None
    last_channel_id: tuple[int, ...] | None
    posted_channel_update: bool
    channels_added: bool
    last_group: str
    is_updating_channels: bool
    def __init__(self, scene_viewer: hou.SceneViewer, controller: Curve3Controller) -> None: ...
    def on_enter(self, node: hou.OpNode | None) -> None: ...
    def selected_point_channel_prims(self, anim_geo: hou.Geometry | None = ...) -> list[hou.ChannelPrim]: ...
    def selected_curve_channel_prims(self, anim_geo: hou.Geometry | None = ...) -> list[hou.ChannelPrim]: ...
