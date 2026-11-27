from collections.abc import Mapping
from datetime import datetime
from typing import Any, TypedDict

from houtypes import JSONLike

import hou
from hrecipes import rtypes

# What loadMetadata() keeps in memory for a recipe, read from its data section.
_RecipeMetadata = TypedDict(
    "_RecipeMetadata",
    {
        "author": str,
        "created": str | None,
        "data_version": str | None,
        "houdini_version": str | None,
        "comment": str,
        "recipe_category": rtypes.RecipeCategory,
        "data_category": str,
        "data_process_order": float,
        "parmname_patterns": list[str],
        "parmtype_patterns": list[str],
        "nodetype_patterns": list[str],
        "multiparm_operation": str,
        "visible": bool,
        "submenu": str,
        "nodetype_category": str | None,
        "nodetype_name": str | None,
        "vop_containertype": str | None,
        "parmtype_name": str | None,
        "parmname": str,
        "icon": str,
        "tool_types": list[rtypes.ToolType],
        "tool_labels": list[str],
        "tab_submenus": list[str],
        "shelf_tab": str,
        "shelf_ordering_index": int,
        "help_url": str,
        "example": bool,
        "network_categories": list[str],
        "prompt_type": str,
        "prompt_messages": list[str],
        "prompt_bboxes": list[list[float]],
        "prompt_posparms": list[str],
        "name": str,
        "name_components": tuple[str, str, str, str],
        "basename": str,
        "name_with_category": str,
        "title": str,
        "data_section_name": str,
        "pre-script_section_name": str,
        "post-script_section_name": str,
        "dop_license_needed": bool,
    },
)

ICON_NAME_BY_RECIPE_CATEGORY: dict[rtypes.RecipeCategory, str]

class AssetIO:
    data_section_name: str
    pre_script_section_name: str
    post_script_section_name: str
    pretty: bool
    def __init__(self, nodetype: hou.OpNodeType, definition: hou.HDADefinition | None = ...) -> None: ...
    def findSection(self, section_name: str) -> hou.HDASection | None: ...
    def loadRecipeData(self) -> rtypes._RecipeFileData | None: ...
    def saveRecipeData(self, recipe_data: Mapping[str, object]) -> None: ...
    def loadData(self) -> rtypes._RecipeDataPayload: ...
    def loadRecipePreScript(self) -> str: ...
    def saveRecipePreScript(self, script: str) -> None: ...
    def loadRecipePostScript(self) -> str: ...
    def saveRecipePostScript(self, script: str) -> None: ...
    def loadMetadata(self) -> _RecipeMetadata: ...
    def saveMetadata(self, metadata: Mapping[str, JSONLike]) -> None: ...
    def deleteDefinition(self) -> None: ...
    def location(self) -> str: ...
    def setTitle(self, title: str) -> None: ...
    def lastModified(self) -> datetime: ...
    def isReadOnly(self) -> bool: ...
    def usedDefinition(self) -> hou.HDADefinition: ...
    def __bool__(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
