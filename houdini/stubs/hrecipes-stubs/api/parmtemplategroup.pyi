# Houdini stubs generated from Houdini 22.0.466

import hou
from . import parmtemplate as parmtemplate, parmtemplatemapper as parmtemplatemapper, utils as utils
from .. import rtypes as rtypes
from collections.abc import Generator, Mapping, MutableMapping
from typing import Any

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
def serializeParmTemplateOrder(parmtemplate_data: rtypes.ParmTemplateDataDict, base_folder_name: str = '__topfolder') -> dict[str, list[str]]:
    """generates a linearized dictionary representing the parm order of each parameter and folder in a
    given folder as a string array. This additional metadata is necessary in order to sort parm template
    dictionaries that are loaded from apex dicts or from
    geometry, since the dict order is not kept here

    {
    '__topfolder': ['myparm1', 'myparm2', 'MySubFolder', 'mylastparm'],
    'MySubFolder': ['mysubparm1', 'mysubparm2'],
    ...
    }
    """
def isParmTemplateBundleData(data: object) -> bool: ...
def isParmTemplateBundleDataList(data: _T) -> bool | _T: ...
def allParmTemplates(group_or_folder: hou.ParmTemplateGroup | hou.FolderParmTemplate) -> Generator[hou.ParmTemplate, None, None]:
    """
    Generator to use for iterating over the parameter template of the incoming parm template group.
    """
def renameConditional(pt: hou.ParmTemplate, cond_type: hou.EnumValue[hou.parmCondType], mapping: Mapping[str, str]) -> None: ...
def renameTag(tags: MutableMapping[str, str], tag_name: str, mapping: Mapping[str, str]) -> None: ...
def adjustTemplateProperties(pt: hou.ParmTemplate, mapping: Mapping[str, str]) -> None: ...
def resolveNameConflict(ptg_old: hou.ParmTemplateGroup, ptg_new: hou.ParmTemplateGroup, output_dict: dict[str, str] = ...) -> tuple[hou.ParmTemplateGroup, dict[str, str]]: ...
def hasOrderingIndex(data: rtypes.ParmTemplateDataDict, recursive: bool = True) -> bool:
    """returns whenever the parmtemplate data dictionary has at least one 'ordering_index' key or not.
    :param data: parmtemplate data dictionary.
    :param recursive: whenever to check the entire nested structure.
    :returns: whenever the data has ordering index
    """
def updateParmTemplateOrder(data: rtypes.ParmTemplateDataDict, recursive: bool = True) -> rtypes.ParmTemplateDataDict:
    """generates a new nested parmtemplate data dictionary with correct ordering index. Ordering index is needed to restore
    the correct dictionary entry order when the data is saved in such a way that the dictionary order is not preserved.
    :param data: parmtemplate data dictionary.
    :param recursive: whenever to update the entire nested structure.
    :returns: the updated parmetemplate data dictionary.
    """
def removeParmTemplateOrder(data: rtypes.ParmTemplateDataDict, recursive: bool = True) -> rtypes.ParmTemplateDataDict:
    """generates a new nested parmtemplate data dictionary without an ordering index. Ordering index is needed to restore
    the correct dictionary entry order when the data is saved in such a way that the dictionary order is not preserved.
    :param data: parmtemplate data dictionary.
    :param recursive: whenever to update the entire nested structure.
    :returns: the updated parmetemplate data dictionary.
    """
def dataForAllParmTemplates(node: hou.OpNode, **opts: Any) -> rtypes.ParmTemplateDataDict:
    """
    This method gathers all parmtemplates that found on the node.
    The _getParmTemplateData() method inside networkitems.py decides whenever to call this method
    or dataForSpareParmTemplateOnly() which will record block of spare parameters only.

    Recording all paramtemplates is not ideal, as when a node type receives new parameters, applying
    'outdated' parmtemplate structure to the node will scramble the parameters.

    Long story short, pick your poison...
    """
def dataForSpareParmTemplateOnly(node: hou.OpNode, **opts: Any) -> rtypes.ParmTemplateBundleDataList | None:
    """
    This method finds a list of continuous blocks of spare parameters. The _getParmTemplateData() method inside
    networkitems.py decides whenever to call this method or dataForSpareParmTemplateOnly()

    This should be the ideal choice over dataForAllParmTemplates(), however, handling folder templates is a nightmare;
    for which a TamplateMapper class was created inside parmtemplatemapper.py.

    However, this method relies on a couple of factors when editing the interface using Edit Parameter Interface window:
    * Users don't move existing tab folders out of their tab set.
    * When users place a spare tab folder as first tab in a tab set, they must not move any other tab folders
    out of the set, or rename existing tab names.
    * Users should not change the hierarchy of folders, for example, place a spare folder as the first entry, and
    place all existing folders and parameters inside that.

    If these happen, there is a risk of spare parameters are not placed correctly.
    However, these rules are pretty standard, and user discouraged from such practices anyway.

    Long story short, pick your poison...
    """
def parmTemplateAsData(node: hou.OpNode, name: str = '', children: bool = True, **opts: Any) -> rtypes.ParmTemplateDataDict | None:
    """
    This returns the data for a selected parmtemplate inside a folder.
    In case of folder templates, when inclusive is set to True, it returns the child templates as well.

    This is used to generate data for hou.Node.parmTemplateAsData()
    """
def parmTemplateChildrenAsData(node: hou.OpNode, name: str = '', **opts: Any) -> rtypes.ParmTemplateDataDict | None:
    """
    This returns the data for a selected parmtemplate children inside a folder.
    """
def parmTemplateGroupFromData(data: rtypes.ParmTemplateDataDict) -> hou.ParmTemplateGroup:
    """
    Builds a hou.ParmTemplateGroup object using the incoming data.
    """
def setFromData(node: hou.OpNode, data: rtypes.ParmTemplateDataDict, **opts: Any) -> dict[str, hou.ParmTuple]:
    """
    Overwrites the node's parmtemplategroup with the parmtemplategroup generated using the provided data.
    The _setParmTemplates() method inside networkitems.py decides whenever to call this method
    or mergeFromTemplateBundleListData()

    """
def mergeFromTemplateBundleListData(node: hou.OpNode, data: rtypes.ParmTemplateBundleDataList | rtypes.ParmTemplateBundleData, **opts: Any) -> dict[str, hou.ParmTuple]:
    """
    Merges the node's parmtemplategroup with the template clusters generated using the provided data.
    The _setParmTemplates() method inside networkitems.py decides whenever to call this method
    or mergeFromTemplateBundleListData()

    Each template cluster block has its own key to refer to the operation by which to merge the templates together.
    """
def mergeParmTemplateDictData(node: hou.OpNode, data: rtypes.ParmTemplateDataDict, operation: str = 'append', parm_name: str = '', rename_conflicts: bool = True, **opts: Any) -> dict[str, hou.ParmTuple]:
    """
    Merges the node's parmtemplategroup with the parmtemplategroup generated using the provided data.
    This is used for various hou.Node function extensions.

    """
