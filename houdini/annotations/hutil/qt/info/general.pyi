from collections.abc import Iterable, Iterator, Mapping, Sequence

import PySide6.QtGui

import hou
from hutil.qt.pluto import colors

BATCH_SIZE: int
UNUSED_POINTS_LABEL: str
DEFAULT_NODE_COLOR: PySide6.QtGui.QColor
EXCLUSIVE_VIZ_TYPES: tuple[str, str]
LIGHTING_CATEGORY: str
VIZ_CATEGORY: hou.EnumValue[hou.viewportVisualizerCategory]
VISUALIZER_EVENTS: tuple[hou.EnumValue[hou.viewportVisualizerEventType], hou.EnumValue[hou.viewportVisualizerEventType], hou.EnumValue[hou.viewportVisualizerEventType], hou.EnumValue[hou.viewportVisualizerEventType], hou.EnumValue[hou.viewportVisualizerEventType]]
TIME_FORMAT_12HR: str
TIME_FORMAT_24HR: str
DATE_FORMAT: str
DATETIME_FORMAT: str
IDENTITY_MATRIX: hou.Matrix4
prim_type_renames: dict[str, str]
attr_type_to_name: dict[hou.EnumValue[hou.attribType], str]
name_to_attr_type: dict[str, hou.EnumValue[hou.attribType]]
group_list_type_to_name: dict[hou.EnumValue[hou.groupListType], str]
group_type_to_class_name: dict[type[hou.PrimGroup | hou.PointGroup | hou.VertexGroup | hou.EdgeGroup], str]
name_to_group_list_type: dict[str, hou.EnumValue[hou.groupListType]]
attr_data_type_to_name: dict[hou.EnumValue[hou.attribData], str]
num_type_to_brief_name: dict[hou.EnumValue[hou.numericData], str]
num_type_to_full_name: dict[hou.EnumValue[hou.numericData], str]
brief_qualifier: dict[str, str]
type_name_to_plural: dict[str, str]
image_storage_name: dict[hou.EnumValue[hou.imageLayerStorageType], str]
image_storage_name_brief: dict[hou.EnumValue[hou.imageLayerStorageType], str]
xform_order_codes: dict[str, str]
usd_base_kinds: tuple[str, str, str, str, str]
usd_categories: dict[str, Sequence[str]]
usd_category_lookup: dict[str, str] | None
prim_count_renames: dict[str, str]
prim_type_icons: dict[str, str]
color_cycle: list[colors.NamedColor]

def naturalSortKey(s: str) -> tuple[str | int, ...]: ...
def invertedPrimCategories(cat_to_types: Mapping[str, Iterable[str]]) -> dict[str, str]: ...
def getUsdPrimCategoryLookup() -> dict[str, str]: ...
def usdPrimAliases() -> Iterator[str]: ...
def usdLightTypes() -> Iterator[str]: ...
