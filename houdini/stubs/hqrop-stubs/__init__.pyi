# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable, Iterable, Mapping
from hqueue.server import _JobSpec, _XMLRPCValue
from typing_extensions import NotRequired, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmValue: TypeAlias = int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None
class _HQRopParms(TypedDict, extra_items=_ParmValue | tuple[_ParmValue, ...]):  # type: ignore[call-arg]
    """The parameters of an HQueue ROP, from getBaseParameters().

    The HQueue Render and Simulation ROPs add their own (parameter values, mostly).
    """
    rop: hou.OpNode
    name: str
    assign_to: str
    combine_output: bool
    clients: str
    client_groups: str
    dirs_to_create: list[str]
    environment: dict[str, str]
    resources: dict[str, int]
    hfs: dict[str, str]
    hq_server: str
    open_browser: int
    priority: int
    hip_action: str
    autosave: int
    warn_unsaved_changes: int
    report_submitted_job_id: int
    skip_file_dependecy_dialog: int
    submittedBy: NotRequired[str]
    hip_file: NotRequired[str]
    local_hip_file: NotRequired[str]
    emailTo: str
    emailReasons: list[str]
    tries_left: NotRequired[int]
    tries_different_client: NotRequired[bool]

class _FileInfo(TypedDict):
    path: str
    size: int
    checksum: str

def submitJob(parms: _HQRopParms, submit_function: Callable[[_HQRopParms], object]) -> None:
    """Submits a job with the given parameters and function after checking to
    see if the project files need to be copied or not.

    parms -- The parameters of the job.
    submit_function -- The function that actually submits the job.
        It will be passed `parms`.
    """
def getOutputParm(rop_node: hou.OpNode | None) -> hou.Parm | None:
    """Return the output file parameter from the given ROP node.

    Return None if `rop_node` is None or if it is not a recognized
    output driver.
    """
def getOutputParmPattern(rop_node: hou.OpNode | None) -> str | None:
    """Return the file pattern in the ROP node's output parameter.
    
    Return None if no output parameter could be found.
    """
def getOutputDirVariable(rop_node: hou.OpNode | None) -> str | None:
    """Return the name of the Houdini variable that expands to the 
    output directory of the given ROP node, without a trailing /.

    Return None if no valid output directory variable could be determined.
    """
def checkPath(path: str) -> str | None:
    """Returns the name ofthe Houdini variable that the given path starts with,
    without the trailing /.

    Returns None if no valid output directory variable could be determined.
    """
def getRenderSettingsNode(usdrender_rop_node: hou.OpNode | None) -> hou.OpNode | None:
    """Returns the node with the matching RenderSettings primitive as
    the given USD Render ROP.
    
    Returns None if 'usdrender_rop_node' is None or if the RenderSettings
    node does not exist."""
def getOutputDriver(rop_node: hou.OpNode | None) -> hou.OpNode | None:
    '''Returns the node which does the rendering/simulation work.

    For eg, if a hq_sim ROP points to a wedge ROP which points to a
    Geometry ROP, then this function will return the Geometry ROP.

    This function skips over all "pointer" ROPs.
    
    Return None if the Output Driver parameter is empty or points to
    a node path that does not exist.  Also return None `hq_rop_node` is None
    or if the Output Driver parameter does not exist.
    '''
def getOutputDriverString(rop_node: hou.OpNode) -> str | None:
    """Return the node set in the Output Driver parameter of 'rop node'.

    Returns None if the there is no Output Driver parameter.
    """
def getFrames(hq_rop_node: hou.OpNode | None) -> tuple[int, ...]:
    """Return a tuple of frame numbers that the given HQueue ROP node
    is configured to render."""
def getFileInfosFromFileReferences(file_references: Iterable[tuple[hou.Parm | None, str]], hq_rop_node: hou.OpNode | None) -> list[_FileInfo]:
    """Return a sequence of file_info dictionaries corresponding to the
    files matching the given file references.
    """
def getBaseParameters() -> _HQRopParms:
    """Return a dictionary of the base parameters used by all HQueue ROPs."""
def getEnvVariablesToSet(hq_node: hou.OpNode) -> dict[str, str]:
    """Return a dictionary of environment variables to set on the client
    machine when processing a job."""
def getResourcesToSet(hq_node: hou.OpNode) -> dict[str, int]:
    """Return a dictionary of resources and respective counts to set
    on the client machine when processing a job."""
def checkBaseParameters(parms: _HQRopParms) -> bool:
    """Check the values of the given parameters.
    
    Return True if all the parameter values are valid and False otherwise.
    """
def checkOutputDriver(output_driver_string: str, _visited_nodes: set[str] | None = None) -> bool: ...
def displayError(msg: str, exception: BaseException | None = None) -> None:
    """Pop up a message dialog to display the given error message.
    
    If the ui is unavailable, then it writes the message to the console.
    """
def displayWarning(msg: str) -> None:
    """Pop up a message dialog to display the given warning.
    
    If the ui is unavailable, then it writes the message to the console.
    """
def displayMessage(msg: str) -> None:
    """Pop up a message dialog to display the given message.
    
    If the ui is unavailable, then it writes the message to the console.
    """
def warnOrAutoSaveHipFile(parms: _HQRopParms) -> bool:
    """Automatically save the current .hip file or display a warning
    to the user about unsaved changes.

    This function is meant to be called before an HQueue job submission
    as a way of informing the user about unsaved changes that may not
    trickle down to the HQueue farm.

    Return True if the job submission should continue on.
    Return False if the user chose to cancel the job submission.
    """
def sendJob(hq_server: str, main_job: _JobSpec, open_browser: int, report_submitted_job_id: int) -> bool:
    """Send the given job to the HQ server.
    
    If the ui is available, either display the HQ web interface or display the
    id of the submitted job depending on the value of `open_browser` and 
    'report_submitted_job_id'.
    """
def getHipFile(parms: _HQRopParms) -> str | None:
    """Return the hip file, pefixed with a network folder         
     variable if possible."""
def expandHQROOT(path: str, hq_server: str) -> str:
    """Return the given file path with instances of $HQROOT expanded
    out to the mount point for the HQueue shared folder root."""
def getHQROOT(hq_server: str) -> str | None:
    """Query the HQueue server and return the mount point path 
    to the HQueue shared folder root.

    Return None if the path cannot be retrieved from the server.
    """
def getEnvRoot(hq_server: str, name: str, is_client: bool = False) -> str | None:
    """Query the HQueue server and return the mount point path
    to the root of the HQueue shared folder with the given name.

    Return None if the path cannot be retrieved from the server.
    """
def getNetworkFolderVars(hq_server: str) -> list[str] | None: ...
def substituteWithFolderVar(hq_server: str | None, file_path: str, expand_frame_variables: bool = True) -> str | None:
    '''Replace the beginning of the given path with "$HQROOT".
    
    Return the new path.  If the original path is not under HQueue\'s shared
    network file system, return the original path.  Return None if an error
    occurs.
    '''
def substituteNonHQVariables(file_path: str, expand_frame_variables: bool = True) -> str:
    """Returns the file path with all the variables that are not HQ specfic
    expanded.
    """
def buildContainingJobSpec(job_name: str, hq_cmds: Mapping[str, Mapping[str, str]], parms: _HQRopParms, child_job: _JobSpec) -> _JobSpec:
    """Return a job spec that submits the child job and waits for it.
    
    The job containing the child job will not run any command.
    """
def doesHQServerExists(hq_server: str) -> bool:
    """Check that the given HQ server can be connected to.
    
    Returns True if the server exists and False if it does not. Furthermore,
    it will display an error message if it does not exists."""
def selectClients(hq_server: str, clients_parm: hou.Parm) -> None:
    """Select clients registered on the HQueue server from a list.

    A modal dialog pops-up displaying a list of all the client machines 
    on the HQueue farm.  The user selects the machines from the list
    and clicks on OK to populate the `clients_parm` parameter with the
    selection.
    """
def selectClientGroups(hq_server: str, client_groups_parm: hou.Parm) -> None:
    """Select client groups on the HQueue server from a list.

    A modal dialog pops-up displaying a list of all the client groups
    on the HQueue farm.  The user selects the groups from the list
    and clicks on OK to populate the `client_groups_parm` parameter with the
    selection.
    """
def getClients(hq_server: str) -> list[str] | None:
    """Return a list of all the clients registered on the HQueue server.
    
    Return None if the client list could not be retrieved from the server.
    """
def getResources(hq_server: str) -> list[dict[str, _XMLRPCValue]] | None:
    """Returns a list of dictionaries where each dictionary represents a resource.
    
    Return None if the resource list could not be retrieved from the server.
    """
def getHQueueServerMachineFromURL(hq_server_url: str) -> str: ...
def getSelectedFileReferences(output_dir_variable: str) -> tuple[tuple[hou.Parm | None, str], ...]:
    """Returns the required file references when
    the file dependency dialog is to be skipped. 
    """
def copyProjectFilesToSharedFolder(hq_rop: hou.RopNode, parms: _HQRopParms) -> bool:
    """Copy the render project's files to the target location
    specified in `parms`.
    
    Return True if the copy is successful.  Return False otherwise.
    The user is first prompted by the file dependency dialog to
    choose the files to be copied to the shared folder.
    """
def checkForRecursiveChain(hq_node: hou.OpNode) -> bool:
    """Checks to see if the HQueue node is an ancestor to its output driver."""
