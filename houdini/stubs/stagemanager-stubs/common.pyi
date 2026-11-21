import hou
from enum import Enum, IntEnum

class _Kind(Enum):
    assembly = 'assembly'
    group = 'group'
    component = 'component'
    subcomponent = 'subcomponent'

ICON_SIZE: int
MARGIN: int
KINDS: list[str]
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

class Column(IntEnum):
    NAME = 0
    ACTIVATION = 1
    VISIBILITY = 2
    SELECTABILITY = 3
    KIND = 4
    REF_FILE_PATH = 5
    REF_PRIM_PATH = 6
    REF_AS_PAYLOAD = 7
    VARIANT_SETS = 8
    INSTANCEABLE = 9
    COUNT = 10

class Source(str, Enum):
    FILE = 'File Browser'
    ASSET = 'Asset Catalog'

class ChangeType(str, Enum):
    CREATE = 'create'
    EDIT = 'edit'
    DELETE = 'delete'
    COPY = 'copy'
    MOVE = 'move'

ACTIVE_COLUMNS: list[str]
COLUMN_ICONS: list[dict[int, hou.qt.Icon] | None]
