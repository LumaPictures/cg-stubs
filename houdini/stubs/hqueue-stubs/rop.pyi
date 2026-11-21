import hou
from collections.abc import Mapping

def getHFSSettings(hq_rop: hou.OpNode) -> dict[str, str]:
    """Return a str-to-str dictionary containing the HFS path values
       stored in the given HQueue ROP node.

    The dictionary will either store a single HFS path value that is universal
    to all supported OSes or will store a single HFS path value per supported
    OS.
    """
def getFarmDirectoriesToCreate(hq_node: hou.OpNode) -> list[str]:
    '''Return a list of directory paths that should be created on the farm
    as specified by the "Create Directories" parameter in the given HQueue ROP node.
    '''
def getHQueueCommands(hfs_dict_or_hq_rop: Mapping[str, str] | hou.RopNode, num_cpus: int = 0) -> dict[str, str] | None:
    """Return the dictionary of commands to start hython, Python, and mantra
    using the given dictionary of HFS path values or based on the settings
    specified in the given HQueue ROP node.
    
    Return None if an error occurs when reading the commands
    from the HQueueCommands file.

    If `num_cpus` is greater than 0, then we add a -j option
    to each command so that the application is run with a maximum
    number of threads.
    """
