from typing import Literal, Required, TypedDict

import hou

VIEWER_UNKNOWN: Literal["unknown"]
VIEWER_SCENE: Literal["scene"]
VIEWER_COP: Literal["cop"]
SETTING_DRAW_PRIMTYPE: Literal["curve3_draw_primtype"]
SETTING_DRAW_ORDER: Literal["curve3_draw_order"]
SETTING_DRAW_NEW_ANCHORTYPE: Literal["curve3_draw_new_anchortype"]
SETTING_EDIT_PLANE: Literal["curve3_edit_plane"]
SETTING_EDIT_SHOW_HANDLE: Literal["curve3_edit_show_handle"]
SETTING_EDIT_PREVIEW_CURVE: Literal["curve3_edit_preview_curve"]
SETTING_SYNCHRONIZE_KEYS: Literal["curve3_synchronize_keys"]
SETTING_SOFT_TRANSFORM_RADIUS: Literal["curve3_soft_transform_radius"]
SETTING_SOFT_TRANSFORM_ENABLED: Literal["curve3_soft_transform_enabled"]
SETTING_APPROX_SHAPE_DEL: Literal["curve3_approx_shape_del"]
SETTING_CONVERT_MATCH_POLY: Literal["curve3_convert_match_poly"]
SETTING_CONVERT_DIVS: Literal["curve3_convert_divs"]
SETTING_MODE_TABS: Literal["curve3_mode_tabs"]
SETTING_SHOW_FRAME_GUIDE: Literal["curve3_show_frame_guide"]
SETTING_SHOW_FRAME_GUIDE_COMPONENTS: Literal["curve3_show_frame_guide_components"]
SETTING_GUIDE_SCALE: Literal["curve3_guide_scale"]
SETTING_ORIENT_SCALE_CHANGE_ALL_SELECTED: Literal["curve3_orient_scale_change_all_selected"]
SETTING_LIVE_UPDATE_MODE: Literal["liveupdate"]
TOOL_MODE_ITEMS: list[tuple[str, str, str]]
PRIMTYPE_TOKEN_CANONICAL: dict[str, str]
PRIMTYPE_ITEMS: list[tuple[str, str]]
EDIT_PLANE_MODE_ITEMS: list[tuple[str, str]]
NEW_ANCHORTYPE_ITEMS: list[tuple[str, str]]
TOOLBAR_OPERATION_BUTTONS: list[tuple[str, str, str, str]]
TOOLBAR_HELP: dict[str, str]
TOOLBAR_BUTTON_COMMANDS: dict[str, str]
TOOLBAR_GROUP_ITEMS: list[tuple[str, list[str]]]
HUD_KEY_LABEL: Literal["label"]
HUD_KEY_KEY: Literal["key"]
CHANNEL_VECTOR_COMPONENTS: tuple[str, str, str]
CHANNEL_VECTOR_PREFIXES: tuple[str, str]
CHANNEL_SCALAR_SUFFIXES: tuple[str, str]
CHANNEL_SUFFIXES: tuple[str, ...]
CHANNEL_SUFFIXES_STR: str
FRAME_GUIDE_MODE_ITEMS: list[tuple[str, str]]
PREVIEW_CURVE_MODE_ITEMS: list[tuple[str, str]]
AUTO_RING_FALLOFF_RANGE: tuple[float, float]
INSERT_PREVIEW_POINT_COLOR: tuple[float, float, float, float]
POINT_STYLE_SMOOTH: hou.EnumValue[hou.drawableGeometryPointStyle]
POINT_STYLE_BROKEN: hou.EnumValue[hou.drawableGeometryPointStyle]
POINT_STYLE_BALANCED: hou.EnumValue[hou.drawableGeometryPointStyle]
POINT_STYLE_AUTO: hou.EnumValue[hou.drawableGeometryPointStyle]
LINE_STYLE_DOTTED: hou.EnumValue[hou.drawableGeometryLineStyle]
LINE_STYLE_SOLID: hou.EnumValue[hou.drawableGeometryLineStyle]
AXIS_NORMALS: tuple[hou.Vector3, hou.Vector3, hou.Vector3]
ZERO_VEC: hou.Vector3
WHITE_VEC4: hou.Vector4
UNDO_DELETE_POINT: str
UNDO_MOVE_TANGENT: str
UNDO_MOVE_SELECTION: str
UNDO_DRAW: str
UNDO_INSERT_POINT: str
UNDO_CHANGE_SELECTION: str
UNDO_CHANGE_SCALE: str
UNDO_CHANGE_ORIENT: str
UNDO_REPULL_TANGENT: str
UNDO_PULL_CURVE: str
HUD_EDIT_HINTS: list[hou._HudRow]
HUD_DRAW_HINTS: list[hou._HudRow]
HUD_ORIENT_HINTS: list[hou._HudRow]
HUD_SCALE_HINTS: list[hou._HudRow]
VEC4_ORIGIN: hou.Vector4
CONVERT_ACTIONS: dict[str, str]
OP_ACTIONS: dict[str, tuple[str, bool]]
PARM_ACTIONS: dict[str, str]
# How a node parm drives a settings HUD widget and the controller (see the comment in the source).
# SETTINGS_NODE_ONLY_OWNERS entries have no hud_sync/outer_name, and may have a default.
class _SettingBinding(TypedDict, total=False):
    parm: Required[str]
    value_kind: Required[Literal["bool", "int", "float", "string"]]
    hud_sync: Literal["parm", "slider", "toggle", "buttonstrip"]
    runtime_apply: Required[
        Literal[
            "controller_parm_int",
            "controller_parm_raw",
            "controller_method_bool",
            "controller_method_float",
            "controller_method_int",
            "controller_method_string",
            "controller_method_index_token",
        ]
    ]
    runtime_target: Required[str]
    runtime_target_args: list[str]
    runtime_items: list[tuple[str, str]]
    outer_name: str
    default: bool | int | float | str

SETTINGS_HUD_NODE_OWNERS: dict[str, _SettingBinding]
SETTINGS_NODE_ONLY_OWNERS: dict[str, _SettingBinding]
TOOL_SET: set[str]
