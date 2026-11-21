from collections.abc import Callable, Collection, Sequence
from typing import Literal, TypedDict, overload

import PySide6.QtGui
import PySide6.QtWidgets

import hou

_NodeDataSelection = TypedDict(
    "_NodeDataSelection",
    {
        "Parameters": list[hou.Parm | hou.ParmTuple],
        "Attributes": list[tuple[hou.Attrib, int]],
        "Transforms": list[tuple[hou.OpNode, str, str | None]],
        "Bounding Boxes": list[tuple[hou.OpNode, str]],
        "Custom": list[tuple[hou.OpNode, str]],
    },
    total=False,
)

_NodeDataInitialSelection = TypedDict(
    "_NodeDataInitialSelection",
    {
        "Parameters": Sequence[hou.Parm | hou.ParmTuple],
        "Attributes": Sequence[tuple[hou.Attrib, int]],
        "Transforms": Sequence[tuple[hou.Node, str, str | None]],
        "Bounding Boxes": Sequence[tuple[hou.Node, str | None]],
        "Custom": Sequence[tuple[hou.Node, str]],
    },
    total=False,
)

def openTypePropertiesDialog(
    self: hou.ui,
    node_or_node_type: hou.Node | hou.NodeType,
    promote_spare_parms: bool = ...,
    immediately_save: bool = ...,
) -> None: ...
def selectFile(
    self: hou.ui,
    start_directory: str | None = ...,
    title: str | None = ...,
    collapse_sequences: bool = ...,
    file_type: hou.EnumValue[hou.fileType] = ...,
    file_types: Collection[hou.EnumValue[hou.fileType]] = ...,
    pattern: str | None = ...,
    default_value: str | None = ...,
    multiple_select: bool = ...,
    image_chooser: bool | None = ...,
    chooser_mode: hou.EnumValue[hou.fileChooserMode] = ...,
    width: int = ...,
    height: int = ...,
) -> str: ...
@overload
def selectNode(
    self: hou.ui,
    relative_to_node: hou.Node | None = ...,
    initial_node: hou.Node | None = ...,
    node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ...,
    title: str | None = ...,
    width: int = ...,
    height: int = ...,
    multiple_select: Literal[False] = ...,
    custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...,
) -> str | None: ...
@overload
def selectNode(
    self: hou.ui,
    relative_to_node: hou.Node | None = ...,
    initial_node: hou.Node | None = ...,
    node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ...,
    title: str | None = ...,
    width: int = ...,
    height: int = ...,
    *,
    multiple_select: Literal[True],
    custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...,
) -> tuple[str, ...] | None: ...
@overload
def selectNode(
    self: hou.ui,
    relative_to_node: hou.Node | None = ...,
    initial_node: hou.Node | None = ...,
    node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ...,
    title: str | None = ...,
    width: int = ...,
    height: int = ...,
    multiple_select: bool = ...,
    custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...,
) -> str | tuple[str, ...] | None: ...
def createQtIcon(self: hou.ui, icon_name: str, width: int | None = ..., height: int | None = ...) -> PySide6.QtGui.QIcon: ...
def mainQtWindow(self: hou.ui) -> PySide6.QtWidgets.QWidget | None: ...
def qtStyleSheet(self: hou.ui) -> str: ...
def selectAttrib(
    self: hou.ui,
    initial_selection: Sequence[tuple[hou.Attrib, int]] | None = ...,
    multiple_select: bool = ...,
    expand_components: bool = ...,
    width: int = ...,
    height: int = ...,
) -> list[tuple[hou.Attrib, int]] | tuple[()]: ...
def setApplicationTheme(self: hou.ui, name: str, save: bool = ...) -> None: ...
def selectNodeData(
    self: hou.ui,
    title: str | None = ...,
    message: str | None = ...,
    width: int = ...,
    height: int = ...,
    initial_selection: _NodeDataInitialSelection | None = ...,
    node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ...,
    multiple_select: bool = ...,
    include_data_type_headers: bool = ...,
    include_parms: bool = ...,
    include_object_transforms: bool = ...,
    include_geometry_bounding_boxes: bool = ...,
    include_geometry_attributes: bool = ...,
    expand_components: bool = ...,
    custom_data_callback: Callable[[hou.OpNode], Sequence[str]] | None = ...,
    custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...,
    help_url: str | None = ...,
) -> _NodeDataSelection: ...
def parameterPaneTabs(
    self: hou.ui, node: hou.Node | None, include_node_editors: bool = ...
) -> list[hou.ParameterEditor | hou.NetworkEditor]: ...
def setParmFilterInEditors(self: hou.ui, node: hou.Node, parm_names: str) -> bool: ...
def scrollToParmsInEditors(
    self: hou.ui,
    parms: hou.Parm | hou.ParmTuple | list[hou.Parm] | list[hou.ParmTuple] | list[hou.Parm | hou.ParmTuple],
    pos: hou.EnumValue[hou.scrollPosition] = ...,
) -> bool: ...
def setMultiParmTabInEditors(self: hou.ui, parm: hou.Parm | hou.ParmTuple, index: int) -> bool: ...
def switchTabsToParmInEditors(self: hou.ui, parm: hou.Parm | hou.ParmTuple) -> bool: ...
def sharedLayoutDataSource(self: hou.ui) -> hou.AssetGalleryDataSource: ...
def setSharedLayoutDataSource(self: hou.ui, data_source: hou.AssetGalleryDataSource) -> None: ...
def reloadSharedLayoutDataSource(self: hou.ui) -> None: ...
def isValidObject(self: hou.ui, hom_obj: object) -> bool: ...
