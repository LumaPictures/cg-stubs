import hou
from .. import rtypes as rtypes
from collections.abc import Mapping
from datetime import datetime
from houtypes import JSONLike
from hutil.pprint import pprint as pprint
from typing import TypedDict

_RecipeMetadata = TypedDict('_RecipeMetadata', {'author': str, 'created': str | None, 'data_version': str | None, 'houdini_version': str | None, 'comment': str, 'recipe_category': rtypes.RecipeCategory, 'data_category': str, 'data_process_order': float, 'parmname_patterns': list[str], 'parmtype_patterns': list[str], 'nodetype_patterns': list[str], 'multiparm_operation': str, 'visible': bool, 'submenu': str, 'nodetype_category': str | None, 'nodetype_name': str | None, 'vop_containertype': str | None, 'parmtype_name': str | None, 'parmname': str, 'icon': str, 'tool_types': list[rtypes.ToolType], 'tool_labels': list[str], 'tab_submenus': list[str], 'shelf_tab': str, 'shelf_ordering_index': int, 'help_url': str, 'example': bool, 'network_categories': list[str], 'prompt_type': str, 'prompt_messages': list[str], 'prompt_bboxes': list[list[float]], 'prompt_posparms': list[str], 'name': str, 'name_components': tuple[str, str, str, str], 'basename': str, 'name_with_category': str, 'title': str, 'data_section_name': str, 'pre-script_section_name': str, 'post-script_section_name': str, 'dop_license_needed': bool})
ICON_NAME_BY_RECIPE_CATEGORY: dict[rtypes.RecipeCategory, str]

class AssetIO:
    '''Class to determine valid dataOpNodeTypes and handle input/output of data and script from its associated
    definition using the validated sections.

    The default session names are:
        - "data.recipe.json" for the recipe\'s data
        - "pre-script.recipe.py" for the python script to run before creation.
        - "post-script.recipe.py" for the python script to run after creation.
    '''
    data_section_name: str
    pre_script_section_name: str
    post_script_section_name: str
    pretty: bool
    def __init__(self, nodetype: hou.OpNodeType, definition: hou.HDADefinition | None = None) -> None: ...
    def findSection(self, section_name: str) -> hou.HDASection | None:
        """
        Looks for a specific section name.
        """
    def loadRecipeData(self) -> rtypes._RecipeFileData | None:
        """
        Loads the entire content of the data section including the data and other metadata.
        """
    def saveRecipeData(self, recipe_data: Mapping[str, object]) -> None:
        """
        Saves the recipe data into the section given by AssetIO.data_section_name
        """
    def loadData(self) -> rtypes._RecipeDataPayload:
        """
        Loads only the 'data' key from the content of the data section.
        """
    def loadRecipePreScript(self) -> str:
        """
        Loads the pre-python script for the recipe.
        """
    def saveRecipePreScript(self, script: str) -> None:
        """
        Saves pre-python script into the section given by AssetIO.pre_script_section_name
        """
    def loadRecipePostScript(self) -> str:
        """
        Loads the post-python script for the recipe.
        """
    def saveRecipePostScript(self, script: str) -> None:
        """
        Saves post-python script into the section given by AssetIO.post_script_section_name
        """
    def loadMetadata(self) -> _RecipeMetadata:
        """
        Collects all the info/metadata that is good to keep in memory for fast access for xml menus and manager.
        """
    def saveMetadata(self, metadata: Mapping[str, JSONLike]) -> None:
        """
        Saves info/metadata into the recipe data section given by AssetIO.data_section_name
        """
    def deleteDefinition(self) -> None: ...
    def location(self) -> str: ...
    def setTitle(self, title: str) -> None: ...
    def lastModified(self) -> datetime:
        """
        Returns the last modification time of all sessions.
        """
    def isReadOnly(self) -> bool: ...
    def usedDefinition(self) -> hou.HDADefinition:
        """
        Return the currently used definition.
        """
    def __bool__(self) -> bool: ...
