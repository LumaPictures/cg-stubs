from enum import Enum

import hou

ICON_SIZE: int
MARGIN: int
KINDS: list[str]
class _Kind(Enum):
    assembly = "assembly"
    group = "group"
    component = "component"
    subcomponent = "subcomponent"

Kind: type[_Kind]
PRIMPATH_PATTERN: str
STATE_NAME: str
CHOOSER_ICON: hou.qt.Icon
CLEAR_ICON: hou.qt.Icon
RELOAD_ICON: hou.qt.Icon
SPLIT_WINDOW_ICON: hou.qt.Icon
SETTINGS_ICON: hou.qt.Icon
ICONSVIEW_ICON: hou.qt.Icon
TREEVIEW_ICON: hou.qt.Icon
BACK_ICON: hou.qt.Icon
UP_ICON: hou.qt.Icon
PRIM_PICKER_ICON: hou.qt.Icon
ADD_CHILD_ICON: hou.qt.Icon
DELETE_PRIM_ICON: hou.qt.Icon
VISIBLE_ICONS: dict[int, hou.qt.Icon]
ACTIVE_ICONS: dict[int, hou.qt.Icon]
SELECTABLE_ICONS: dict[int, hou.qt.Icon]
ACTIVE_COLUMNS: list[str]
COLUMN_ICONS: list[dict[int, hou.qt.Icon] | None]
