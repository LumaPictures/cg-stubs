# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Sequence
from past.builtins import cmp as cmp
from typing import NotRequired, TypedDict

class _AssetInfo(TypedDict):
    descriptive_name: str
    category_name: str
    depends_on: list[str]
    otl_file: str
    icon_type: str | None
    is_nested: bool
    is_apprentice: bool
    houdini_version: str
    is_indie: NotRequired[bool]

class _DependencyInfo(TypedDict):
    contents: dict[str, _AssetInfo]
    missing: list[tuple[str, str]]

IMAGE_ICON_SECTION_NAME: str
SVG_ICON_SECTION_NAME: str

def get_otl_file_info(otl_file: str, skip_nested_namespaces: bool = True) -> _DependencyInfo:
    '''
    Searches an OTL file and return JSON containing dependencies from a node
    type to other node types defined in the OTL.

    skip_nested_namespaces: When True, node types that are embedded inside
        other node types will be ignored (unless there are missing
        dependencies).

    For all the node types defined in the given OTL file, information is
    put in a single block of JSON.  For example, this function might return
    the following:

        {
            "contents": {
                "car": {
                    "descriptive_name": "Car",
                    "category_name": "Object",
                    "depends_on": ["wheel"]
                    "otl_file": "car_and_wheel.otl",
                    "icon_type": None,
                    "is_nested": False,
                    "houdini_version": "12.5.427"
                },
                "wheel": {
                    "descriptive_name": "Wheel",
                    "category_name": "Object",
                    "depends_on": []
                    "otl_file": "car_and_wheel.otl",
                    "icon_type": None,
                    "is_nested": False,
                    "houdini_version": "12.5.427"
                },
            },
            "missing": []
        }

    if "wheel" and "car" are in the OTL file and "car" depends on "wheel".
    Or, it might return:

        {
            "contents": {
                "car": {
                    "descriptive_name": "Car",
                    "category_name": "Object",
                    "depends_on": ["wheel"]
                    "otl_file": "car.otl",
                    "icon_type": None,
                    "is_nested": False,
                    "houdini_version": "12.5.427"
                },
            },
            "missing": [["Object", "wheel"]]
        }

    if "wheel" is not in the OTL file.

    Node types built into Houdini are not included in the output.  The
    result dependency dictionary is not expanded: if A, B, and C are node
    types, A uses B, and B uses C, the dependencies will be {"A": ["B"],
    "B": ["C"]}, not {"A": ["B", "C"]}.

    Note that "icon_type" is one of "png", "svg", or None.
    '''
def is_namespaced_node_type(node_type: hou.OpNodeType) -> bool: ...
def is_nested_node_type(node_type: hou.OpNodeType) -> bool:
    """Return whether this node type is nested inside another node type.

    Note that instances of nested node types can only be created inside
    instances of the containing node type.
    """
def is_nested_node_type_from_definition(definition: hou.HDADefinition) -> bool:
    """Given a defintiion, return whether this node type is nested inside
    another node type.
    """
def scoping_node_type_name(node_type: hou.OpNodeType) -> str: ...
def scoping_node_type_name_from_name(node_type_name: str) -> str: ...
def node_type_name_with_vendor(node_type_name: str, vendor: str) -> str:
    """Given a node type name (which may or may not include the category),
    return a new node type name that adds/changes the vendor (author) prefix.
    """
def full_node_type_name_from_definition(definition: hou.HDADefinition) -> str:
    """Given an HDADefinition, return its full node type name (i.e. in
    Category/name) form.
    """
def node_type_name_without_category(node_type_name: str) -> str:
    '''Given a node type name that may or may not include the node type
    category, return one without any node type category.

    For example, if you pass in "Object/geo" this function returns "geo".
    If you pass in "SideFX::Object/geo", it returns "SideFX::geo".
    '''
def node_type_name_with_category(node_type_name: str, category: str) -> str: ...
def extract_node_type_category_name(node_type_name: str) -> str | None: ...
def get_dependency_info_for_node(node: hou.OpNode, skip_nested_namespaces: bool = True) -> _DependencyInfo:
    '''
    Search the given asset instance and return information about itself
    and the node types it uses, in the same format as get_otl_file_info.

    The value for "missing" in the returned dictionary is always an empty list.
    '''
def is_asset_type(node_type: hou.OpNodeType) -> bool:
    """
    Return whether the given node type is a user-defined asset.
    """
def find_node_type(otl_file: str, node_type_name: str) -> hou.OpNodeType | None:
    """
    Look in an OTL file for the given hou.NodeType and return it.
    Returns None if the OTL file does not contain a node type with
    that name.
    """
def icon_type(node_type: hou.OpNodeType) -> str | None:
    '''
    Return the type of icon file that can be extracted from a node type (either
    "png" or "svg"), or None if the node type does not contain an embedded
    icon.

    Icon references in Houdini can either be the special icon section
    names or they can be normal opdef references.  If it\'s a normal
    reference to a non-SVG file then it must be to a bitmap image, and
    we\'ll convert that to a PNG.
    '''
def read_icon_data(image_file: str) -> tuple[str, bytes | None]:
    """
    Read the icon data from a image file on disk (SVG or raster data),
    convert it into the appropriate format needed by Houdini, and
    return an (icon_section_name, image_data) tuple.
    
    The icon_section_name is where Houdini will store the image if
    it's put into an asset definition, and identifies whether the data
    is svg or raster data.
    """
def save_icon(node_type: hou.OpNodeType, output_file: str, icon_dimensions: Sequence[int]) -> bool:
    """
    Given a node type for an asset that has an icon file, write the
    icon to the given output file.
    """
def set_icon(node_type: hou.OpNodeType, icon_section_name: str, icon_data: str | bytes) -> None:
    """
    Set the icon for an asset to the given raw icon data (.svg or .pic) format,
    storing it in the given section name.
    """
