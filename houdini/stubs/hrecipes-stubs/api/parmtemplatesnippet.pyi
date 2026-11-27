import hou
from . import utils as utils
from .. import rtypes as rtypes
from collections.abc import Mapping, MutableSequence
from hutil.pprint import pprint as pprint
from os.path import split as split
from typing import Any, Sequence, TypedDict

from typing import TypeVar
from typing import TypeVar
_D = TypeVar('_D', bound=Mapping[str, object])
class ParmTemplateSnippetData(TypedDict, total=False):
    parms: rtypes.ParmDataDict
    parmtemplates: rtypes.ParmTemplateBundleData
    source_script: str

def nested_set(dic: dict[str, Any], keys: Sequence[str], value: object) -> None: ...
def nameToLabel(name: str) -> str:
    """process the name for be a pretty label"""
def reorderKeys(data: _D, ordered_names: MutableSequence[str] = ..., names_to_end: Sequence[str] = ...) -> _D: ...
def updateParmTemplateOrder(data: Mapping[str, rtypes.ParmTemplateData], recursive: bool = True) -> rtypes.ParmTemplateDataDict:
    """generates a new nested parmtemplate data dictionary with correct ordering index. Ordering index is needed to restore
    the correct dictionary entry order when the data is saved in such a way that the dictionary order is not preserved.
    :param data: parmtemplate data dictionary.
    :param recursive: whenever to update the entire nested structure.
    :returns: the updated parmetemplate data dictionary.
    """
def findParmTemplateInData(data: rtypes.ParmTemplateDataDict, name: str, type_filters: Sequence[str] | None = None) -> tuple[rtypes.ParmTemplateData | None, str]:
    """finds the parmtemplate of a given name from the nested parmtemplate structure and returns its data.
    Use type_filters to limit what parameter templates to search for. For example, [hou.parmTemplateInterfaceType.FolderSimple, ]
    will only look for simple folders.
    :param data: parmtemplate data dictionary
    :param name: name of the parameter template in data to search for
    :param type_filters: a list of hou.parmTemplateInterfaceType entries that limits the type of parmtemplates to search for
    :returns: The data for the found parmtemplate or None
    """
def popParmTemplateData(data: rtypes.ParmTemplateData | rtypes.ParmTemplateBundleData, name: str, type_filters: Sequence[str] | None = None, update_ordering: bool = True) -> rtypes.ParmTemplateData | None:
    """removes a parmtemplate of a given name from the nested parmtemplate structure. This will also ensure to update all
    ordering indexes in the nested structure if any has been found. Use type_filters to limit what parameter templates to search for.
    For example, [hou.parmTemplateInterfaceType.FolderSimple, ] will only look for simple folders.
    :param data: parmtemplate data dictionary
    :param name: name of the parameter template in data to remove
    :param type_filters: a list of hou.parmTemplateInterfaceType entries that limits the type of parmtemplates to search for
    """
def insertParmTemplateData(data: Mapping[str, rtypes.ParmTemplateData], name: str, parm_template: rtypes.ParmTemplateData, at_index: int = -1, at_key: str = '', before_key: bool = True, update_ordering: bool = True) -> rtypes.ParmTemplateDataDict: ...
def removeParmTemplateFromData(data: rtypes.ParmTemplateDataDict, name: str, type_filters: Sequence[str] | None = None) -> rtypes.ParmTemplateDataDict:
    """removes a parmtemplate of a given name from the nested parmtemplate structure. This will also ensure to update all
    ordering indexes in the nested structure if any has been found. Use type_filters to limit what parameter templates to search for.
    For example, [hou.parmTemplateInterfaceType.FolderSimple, ] will only look for simple folders.
    :param data: parmtemplate data dictionary
    :param name: name of the parameter template in data to remove
    :param type_filters: a list of hou.parmTemplateInterfaceType entries that limits the type of parmtemplates to search for
    """
def parmTemplateNames(data: rtypes.ParmTemplateDataDict, ignore_folders: bool = True, ignore_multiparm_instances: bool = False, type_filters: Sequence[str] | None = None) -> list[str]:
    """retrieves the names of all parmtemplates from the nested parmtemplate structure. Use type_filters to limit
    what parameter templates to search for. For example, [hou.parmTemplateInterfaceType.FolderSimple, ] will only look for simple folders.
    The function can also ignore any multiparm instance template from returning; those are names that contain '#' key.
    :param data: parmtemplate data dictionary
    :param ignore_folders: ignores folder templates.
    :param ignore_multiparm_instances: ignores templates that are child templates of a multiparm parent template.
    :param type_filters: a list of hou.parmTemplateInterfaceType entries that limits the type of parmtemplates to search for
    :returns: a string list of parameter template names
    """
def reorderTemplateData(data: rtypes.ParmTemplateData) -> rtypes.ParmTemplateData: ...
def splitName(name: str) -> tuple[str, str]:
    """splits the end of the string based on '_', '#' and digits and returns the two splits."""
def addHashToName(name: str, count: int = 0) -> str: ...
def removeHashFromName(name: str, count: int = 0) -> str: ...
def isMultiparmInstance(name: str) -> bool: ...
def updateName(name: str, parent_name: str, parent_template: rtypes.ParmTemplateData | rtypes.ParmTemplateBundleData) -> str: ...
def findParentTemplate(data: rtypes.ParmTemplateDataDict, folder_path: str = '') -> tuple[rtypes.ParmTemplateDataDict | rtypes.ParmTemplateData | None, str]: ...

class DataManager:
    def __init__(self, node: hou.OpNode | None = None, container_folder_name: str = 'parameters', default_folder_type: str = ...) -> None: ...
    def data(self) -> ParmTemplateSnippetData: ...
    def setData(self, data: ParmTemplateSnippetData) -> None: ...
    def parms(self) -> rtypes.ParmDataDict: ...
    def setParms(self, data: rtypes.ParmDataDict) -> None: ...
    def clearData(self) -> None: ...
    def setDefaultFolderType(self, folder_type: str) -> None:
        """Sets the type of folder that is created when nested folder structures have to be created.

        :param folder_type: one of [hou.parmTemplateInterfaceType.FolderTabs,
                                    hou.parmTemplateInterfaceType.FolderSimple,
                                    hou.parmTemplateInterfaceType.FolderCollapsible]
        """
    def node(self) -> hou.OpNode | None: ...
    def parmTemplateBlock(self) -> rtypes.ParmTemplateBundleData: ...
    def parmTemplates(self) -> rtypes.ParmTemplateDataDict: ...
    def setParmTemplates(self, data: rtypes.ParmTemplateDataDict) -> None: ...
    def sourceScript(self) -> str | None: ...
    def setSourceScript(self, script: str = '') -> None: ...
    def setContainerFolder(self, folder_name: str) -> None: ...
    def folderTemplateData(self, label: str, folder_type: str | None = None) -> rtypes.ParmTemplateData: ...
    def ensureBaseKeys(self) -> None: ...
    def ensureContainer(self) -> None: ...
    def ensureFolderPath(self, data: rtypes.ParmTemplateDataDict, folder_path: str = '') -> rtypes.ParmTemplateDataDict | None: ...
    def parmTemplateNames(self, ignore_folders: bool = True, ignore_multiparm_instances: bool = False, type_filters: Sequence[str] | None = None) -> list[str]: ...
    def reorderParmValues(self) -> None: ...
    def setParmValue(self, name: str, data: rtypes.ParmUnionData | rtypes.MultiParmInstanceDataList, update_ordering: bool = False, multiparm_parent: str = '') -> None: ...
    def removeParmValue(self, name: str, update_ordering: bool = False) -> None: ...
    def removeParameters(self, parm_names: Sequence[str] = ...) -> None: ...
    def addParameter(self, name: str, parmtemplate_data: rtypes.ParmTemplateData | None, folder_path: str = '', value: rtypes.ParmData | None = None, at_index: int = -1, at_key: str = '', before_key: bool = True) -> None:
        """Adds a parameter into the data.

        :param name: The name of the parameter to add. If there is an existing entry with the same name, it will be overwritten.
        :param parmtemplate_data: The rtypes.ParmTemplateData that will be inserted into the template structure.
        :param folder_path: A single string representing the name of the folder under which to insert this new parameter.
        If the folder cannot be found, the parameter will be inserted at the top. Optionally, if you provide a UNIX path,
        a folder hierarchy will be created based on the default folder type.
        :param value: The value of the parameter.
        :param at_index: At which index to insert the parmtemplate data. The default -1 means to place it at the end.
        :param at_key: Instead of an index, find the parameter name where the parmtemplate data has to be inserted.
        :param before_key: When at_parmname is given, this decides whenever to insert this parmtemplate data before
        or after the parmname.
        """
    def addFolder(self, name: str, label: str, folder_type: str | None = None, folder_path: str = '', value: rtypes.MultiParmInstanceDataList = ..., at_index: int = -1, at_key: str = '', before_key: bool = True, parm_names: Sequence[str] = ..., new_parm_templates: rtypes.ParmTemplateDataDict = ..., template_kwargs: rtypes.ParmTemplateData | None = None) -> None:
        """Adds a folder parameter into the data.

        :param name: The name of the folder to add. If there is an existing entry with the same name, it will be overwritten.
        :param label: The label of the folder. If not given, it is created from name.
        :param folder_type: The type of the folder to create, which has to be a folder type of hou.parmTemplateInterfaceType.
        :param folder_path: A single string representing the name of the folder under which to insert this new parameter.
        If the folder cannot be found, the parameter will be inserted at the top. Optionally, if you provide a UNIX path,
        a folder hierarchy will be created based on the default folder type.
        :param value: The value of the parameter. You can get this by calling hou.Parm.MultiParmInstancesAsData() on a multiparm parent parameter.
        :param at_index: At which index to insert the parmtemplate data. The default -1 means to place it at the end.
        :param at_key: Instead of an index, find the parameter name where the parmtemplate data has to be inserted.
        :param before_key: When at_parmname is given, this decides whenever to insert this parmtemplate data before
        or after the parmname.
        :param parm_names: A list of existing string parameter names that will be placed under this new folder.
        :param new_parm_templates: Any ParmTemplateDataDict that needs to be inserted under this folder.
        :param template_kwargs: Extra folder-template keys to merge onto the folder template (e.g.
        disable_when, hide_when, joins_with_next, hidden).
        """
    def updateFromInterface(self) -> bool | None:
        """updates the data according to the existing parm interface.
        """
    def __bool__(self) -> bool: ...
