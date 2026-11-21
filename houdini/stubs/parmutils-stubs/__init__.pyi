# Houdini stubs generated from Houdini 22.0.466

import hou
import re
from builtins import filter as filter
from collections.abc import Collection, Iterable, Iterator, MutableSequence, Sequence
from typing import Literal

from typing import TypeVar
from typing import TypeVar
_FolderSeq = TypeVar('_FolderSeq', bound=Sequence[hou.FolderParmTemplate])
def getAllParmTemplates(group_or_folder: hou.ParmTemplateGroup | hou.FolderParmTemplate) -> Iterator[hou.ParmTemplate]: ...
def getContainingFolders(parm_template_group: hou.ParmTemplateGroup, parm_name: str) -> tuple[list[hou.FolderParmTemplate], list[int]]: ...
def getContainingFolderLabels(parm_template_group: hou.ParmTemplateGroup, parm_name: str) -> list[str]: ...
def getDeepestCommonFolder(folder_hierarchies: Collection[_FolderSeq]) -> _FolderSeq | list[hou.FolderParmTemplate] | Literal['']:
    """ Given a list of folder strings (slash separated folder labels),
        return the string of deepest common folders.

        If the list is empty an empty string is returned.
    """
def getFoldersFromString(folder_string: str) -> list[str]:
    """ Turns a list of slash separated folder labels into  a list of
        FolderParmTemplates
    """
def replaceParm(ptg: hou.ParmTemplateGroup, indices: Iterable[int], parm_template: hou.ParmTemplate) -> None:
    """ Replaces the parm at 'indices' with 'parm_template' and updates all
        containing folders
    """
def addParmAndContainingFolders(ptg: hou.ParmTemplateGroup, parm_template: hou.ParmTemplate, folder_labels_or_templates: MutableSequence[str] | MutableSequence[hou.FolderParmTemplate], folder_type: hou.EnumValue[hou.folderType] = ...) -> None: ...
def setParmTemplates(ptg: hou.ParmTemplateGroup, parm_templates: Iterable[hou.ParmTemplate]) -> None: ...
def shiftParmIndices(ptg: hou.ParmTemplateGroup, current_indices: Iterable[int], target_indices: Iterable[int]) -> None:
    """ Shifts each folder in the hierarchy to the specified index within it's
        parent folder.
    """
def moveParameterToFolder(ptg: hou.ParmTemplateGroup, parm_name: str, in_folders: MutableSequence[str] | MutableSequence[hou.FolderParmTemplate], folder_type: hou.EnumValue[hou.folderType] = ...) -> None:
    """ Move the parameter to the folders specified by in_folders. The parameter
        is always moved to the bottom of it's folder.

        folder_type sets the type of newly added folders.
    """
def setAllFolderTypes(ptg: hou.ParmTemplateGroup, folder_type: hou.EnumValue[hou.folderType]) -> None: ...
def printFolderHierarchy(ptg: hou.ParmTemplateGroup | hou.ParmTemplate, level: int = 0) -> None: ...
def decodeConditional(cond: str) -> list[list[list[str]]]:
    """ Decodes the conditional string into a list of groups containing lists
        of conditions.

        The conditions consist of a list in the form [parm, op, value]

        For example, { x != 0 } { y > 1 z 3 } decodes to:

        [
            [
                ['x', '!=', '0']
            ],
            [
                ['y', '>', '1'],
                ['z', '==', '3']
            ]
        ]
    """
def encodeConditional(cond: Iterable[Iterable[Iterable[str]]]) -> str: ...
def collectParms(nodes: Iterable[hou.OpNode], parm_name: str) -> Iterator[hou.Parm]: ...
def parmPrepend(nodes: Iterable[hou.OpNode], parm_name: str, string: str) -> None: ...
def parmReplace(nodes: Iterable[hou.OpNode], parm_name: str, old_string: str, new_string: str) -> None: ...
def parmSub(nodes: Iterable[hou.OpNode], parm_name: str, pattern: str | re.Pattern[str], new_string: str) -> None: ...
def makeAbsolutePath(parm: hou.Parm) -> None: ...
def makeRelativePath(parm: hou.Parm) -> None: ...
def selectSceneDataAndCreateParmReference(parm_or_parm_tuple: hou.Parm | hou.ParmTuple) -> None:
    """Prompt to select node data and create a reference to the data from
       the given parameters by creating parameter expressions."""
def selectLocalVarAndCreateReferenceFromParm(parm: hou.Parm) -> None:
    """Prompt to select a local variable that is visible to the parameter's
       node and create an expression on the specified parameter to reference
       the selected component."""
def selectLocalAttribAndCreateReferencesFromParms(parms: Sequence[hou.Parm]) -> None:
    """Prompt to select a local attribute that is visible to the parameter's
       node and create expressions on the specified parameters to reference
       the selected attribute."""
def selectMultipleFilesForParm(parm: hou.Parm) -> None:
    """Function designwed for use with a parameter action script button.

    Presents a file chooser to select multiple files to be entered into a
    single parameter field.
    """
