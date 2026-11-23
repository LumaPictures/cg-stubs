import hou
from collections.abc import Sequence

def addParmTuple(self: hou.HDADefinition, parm_template: hou.ParmTemplate, in_folder: Sequence[str] = ..., create_missing_folders: bool = False) -> None:
    '''
addParmTuple(self, parm_template, in_folder=(),
create_missing_folders=False)

    Add a parameter tuple to this node type\'s parameters. Houdini places
    the new parameter at the bottom of the parameters in a particular
    folder.


    parm_template
        An instance of a hou.ParmTemplate subclass that describes the
        parameter.

    in_folder
        A sequence of folder name strings to tell Houdini which folder
        to put the parameter in. If this sequence is empty, the
        parameter will go in top level set of folders. It it is, for
        example, ("Transform",), the parameter is added inside the
        Transform folder. If it is ("Transform", "Options"), it will go
        inside the Options folder inside the Transform folder.

    create_missing_folders
        Whether Houdini should create folders specified in in_folder
        that do not already exist. If this parameter is True, you can
        create folders without having to call
        hou.HDADefinition.addParmFolder.

    Note that this method can add a single folder by passing a
    hou.FolderParmTemplate for parm_template.

    See also hou.HDADefinition.replaceParmTuple.

    This method is deprecated in favor of
    hou.HDADefinition.setParmTemplateGroup.

'''
def replaceParmTuple(self: hou.HDADefinition, parm_tuple_name: str, parm_template: hou.ParmTemplate) -> None:
    """
replaceParmTuple(self, parm_tuple_name, parm_template)

    Replace an existing parameter tuple with a new one. The old
    parameter tuple is removed and the new one is added in its place.


    parm_tuple_name
        The name of the parameter tuple to replace. Raises
        hou.OperationFailed if no parameter tuple exists with this name.

    parm_template
        A hou.ParmTemplate describing the new parameter tuple.

    The new parameter tuple may or may not have the same name as the old
    one. By providing a parameter tuple with the same name, you can
    modify an existing parameter tuple. The following example function
    changes the definition of the asset to make a parameter tuple
    visible or invisible in all nodes of that type.

    To show or hide a parameter in just one instance of a node, use
    hou.ParmTuple.hide.

    To change a spare parameter on a node, use
    hou.OpNode.replaceSpareParmTuple or hou.OpNode.setParmTemplateGroup.

    This method is deprecated in favor of
    hou.HDADefinition.setParmTemplateGroup.

"""
def removeParmTuple(self: hou.HDADefinition, name: str) -> None:
    """
removeParmTuple(self, name)

    Remove a parameter tuple from this node type's parameters.

    See also hou.HDADefinition.addParmTuple and
    hou.HDADefinition.removeParmFolder.

    This method is deprecated in favor of
    hou.HDADefinition.setParmTemplateGroup.

"""
def addParmFolder(self: hou.HDADefinition, folder_name: str, in_folder: Sequence[str] = ..., parm_name: str | None = None, create_missing_folders: bool = False) -> None:
    '''
addParmFolder(self, folder_name, in_folder=(), parm_name=None,
create_missing_folders=False)

    Adds a folder to this node type\'s parameters.


    folder_name
        The name of the folder that is displayed in the parameter
        dialog.

    in_folder
        A sequence of folder name strings to indicate where the folder
        should go. If this sequence is empty, the folder will go in top
        level set of folders. It it is, for example, ("Transform",), the
        folder is added inside the Transform folder. If it is
        ("Transform", "Options"), it will go inside the Options folder
        inside the Transform folder.

    parm_name
        The name of the underlying parameter tuple corresponding to the
        set of folders. For example, the folders in a set might be named
        Transform, Subnet, and Controls, and these correspond to one
        parameter tuple named, say, \'stdswitcher0\'. The value of the
        parameter in this tuple is the index of the folder that is open.

        If this is the first folder to go in the set, parm_name is used
        as the parameter name. Otherwise, it is ignored and Houdini uses
        the parameter name of the first folder in the set.

        If this is the first folder in the set and parm_name is None, it
        will default to \'folder0\'. If parm_name is already in use,
        Houdini automatically generates a unique name.

    create_missing_folders
        Whether Houdini should create folders specified in in_folder
        that do not already exist. If this parameter is True, you can
        use this method to add nested folders in one call.

    Note that you can add folders by passing a hou.FolderParmTemplate to
    the addSpareParmTuple method, so this method is deprecated. Note
    also that addSpareParmTuple is deprecated in favor of
    setParmTemplateGroup.

    See also the removeParmFolder and addParmTuple methods.

    This method is deprecated in favor of setParmTemplateGroup.

'''
def removeParmFolder(self: hou.HDADefinition, folder: Sequence[str]) -> None:
    '''
removeParmFolder(self, folder)

    Remove an empty folder from this node type\'s parameters.


    folder
        A sequence of folder names. For example, to remove the Output
        folder, pass in ("Output",) and not "Output".

    Raises hou.OperationFailed if the folder does not exist or it is not
    empty. Use hou.HDADefinition.removeParmTuple to remove all the
    parameters inside the folder before calling this method.

    See also addParmFolder, hou.ParmTemplateGroup.remove, and
    hou.ParmTemplateGroup.findFolder.

    This method is deprecated in favor of
    hou.HDADefinition.setParmTemplateGroup.

'''
def uncompressedContents(self: hou.HDADefinition) -> str:
    """
uncompressedContents(self) -> str

    Return a string containing the data of the uncompressed Contents
    section.

    The Contents section consists of data in the CPIO format
    representing the child nodes used to create a node instance of the
    HDA.

    Prefer hou.HDADefinition.binaryUncompressedContents to this as the
    Contents can contain packets of binary data.

    See also hou.HDADefinition.parsedContents.

"""
def binaryUncompressedContents(self: hou.HDADefinition) -> bytes:
    """
binaryUncompressedContents(self) -> str

    Return a bytes object containing the data of the uncompressed
    Contents section.

    The Contents section consists of data in the CPIO format
    representing the child nodes used to create a node instance of the
    HDA.

    Prefer this to hou.HDADefinition.uncompressedContents as the
    Contents can contain packets of binary data.

    See also hou.HDADefinition.parsedContents.

"""
def parsedContents(self: hou.HDADefinition) -> tuple[tuple[str, bytes], ...]:
    """
parsedContents(self) -> tuple of (str, str)

    Return a list of (name, value) pairs of the parsed from the Contents
    section.

    The Contents section consists of the child nodes used to create a
    node instance of the HDA.

    See also hou.HDADefinition.uncompressedContents.

"""
