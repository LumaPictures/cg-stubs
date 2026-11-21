from .callback import *
import _pdg
import hou
import logging
import typing
from collections.abc import Iterable, Mapping, MutableMapping, Sequence
from houtypes import ParmCallbackKwargs
from typing import Any

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_EnvT = TypeVar('_EnvT', bound=Mapping[str, str])
_ParmValue: TypeAlias = int | float | str | Iterable[int | float | str]
_FileTuple: TypeAlias = tuple[str, str, int, bool]
class PyScheduler(PythonCallback):
    """
    Base class for schedulers implemented in Python
    """
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None:
        """
        __init__(self, _pdg.Scheduler, str) -> NoneType

        Initializes the Scheduler with a C++ scheduler reference and name
        """
    def __setitem__(self, key: str, value: _ParmValue) -> None:
        '''
        __setitem__(self, str, value) -> NoneType

        Assigns a parameter port value, using the syntax node["param"] = value
        The value must be an int, float or string.
        NOTE: Cannot be used in __init__
        '''
    def initLogger(self, logger: logging.Logger, log_level: int | str) -> None:
        """
        Initialize the logger to write out to stdout
        with minimum log level.
        (Unused - Use _verboseLog instead)
        """
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult:
        """
        [virtual] Called when the scheduler should schedule a work item.
        Returns True on success, else False.

        Must be implemented by PyScheduler subclasses.

        work_item   _pdg.WorkItem
        """
    def onScheduleStatic(self, dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], ready_items: Sequence[_pdg.WorkItem]) -> None:
        """
        [virtual] Called when the scheduler should process a static
        dependency graph.

        dependencies    _pdg.WorkItem map of dependencies
        dependents      _pdg.WorkItem map of dependents
        ready_items     _pdg.WorkItem array of work items
        """
    @staticmethod
    def hasServiceSupport() -> bool:
        """
        [virtual] Indicates whether the scheduler type supports starting and
        stopping PDG services
        """
    def startService(self, service: _pdg.Service) -> bool:
        """
        [virtual] Called when the scheduler should start a PDG service. This
        method will start the mqserver process and the service pool processes.

        Must be implemented by PyScheduler subclasses.
        """
    def stopService(self, service: _pdg.Service) -> bool:
        """
        [virtual] Called when the scheduler should stop a PDG service. This
        method will stop the mqserver process and all service pool processes.

        Must be implemented by PyScheduler subclasses.
        """
    def workItemSucceeded(self, workitem_id: int, index: int, cook_duration: float, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a workitem signals success.
        """
    def workItemCancelled(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a workitem signals cancelled.
        """
    def workItemFailed(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a workitem signals failure.
        """
    def workItemKeepalive(self, workitem_id: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a workitem keepalive RPC is received.
        Can be used as a mechanism to time-out farm jobs.
        """
    def workItemStartCook(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a workitem signals started.
        """
    def workItemSetCustomState(self, workitem_id: int, index: int, custom_state: str, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a custom state string should be added
        to a workitem
        """
    def workItemSetCookPercent(self, workitem_id: int, index: int, cook_percent: float = -1.0, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a cook progress percentage should be
        added to a workitem
        """
    def workItemAppendLog(self, workitem_id: int, index: int, log_data: str, log_type: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when log data is added to a workiem
        """
    def workItemAddOutput(self, workitem_id: int, subindex: int, result: str | bytes, tag: str, checksum: int, jobid: str = '', active_only: bool = False) -> None:
        """
        Called by mixin when a workitem signals file result data reported.
        """
    def workItemAddOutputs(self, workitem_id: int, subindex: int, results: Sequence[str | bytes], tags: str | Sequence[str], checksums: Sequence[int], jobid: str = '', active_only: bool = False) -> None:
        """
        Called by mixin when a workitem signals file result data array reported.
        """
    def workItemInvalidateCache(self, workitem_id: int, subindex: int, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals that its cached should be invalidated
        """
    def releaseJobSlots(self, workitem_id: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a work item wants to release
        the scheduler slots it currently occupies.
        """
    def acquireJobSlots(self, workitem_id: int, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a work item wants to (re)acquire
        the scheduler slots it previously released.
        """
    def workItemSetStringAttribArray(self, workitem_id: int, subindex: int, attr_name: str, data: Sequence[str], jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals a string array attribute reported.
        """
    def workItemSetIntAttribArray(self, workitem_id: int, subindex: int, attr_name: str, data: Sequence[int], jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals a int array attribute reported.
        """
    def workItemSetFloatAttribArray(self, workitem_id: int, subindex: int, attr_name: str, data: Sequence[float], jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals a float array attribute reported.
        """
    def workItemSetFileAttribArray(self, workitem_id: int, subindex: int, attr_name: str, data: Iterable[_FileTuple], jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals a file array attribute reported.
        """
    def workItemSetDictAttribArray(self, workitem_id: int, subindex: int, attr_name: str, data: Iterable[str], jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals a dict array attribute reported.
        """
    def workItemSetStringAttrib(self, workitem_id: int, subindex: int, attr_name: str, attr_value: str, attr_index: int, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals string attribute element reported.
        """
    def workItemSetIntAttrib(self, workitem_id: int, subindex: int, attr_name: str, attr_value: int, attr_index: int, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals int attribute element reported.
        """
    def workItemSetFloatAttrib(self, workitem_id: int, subindex: int, attr_name: str, attr_value: float, attr_index: int, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals float attribute element reported.
        """
    def workItemSetFileAttrib(self, workitem_id: int, subindex: int, attr_name: str, attr_value: _FileTuple, attr_index: int, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals file attribute element reported.
        """
    def workItemSetDictAttrib(self, workitem_id: int, subindex: int, attr_name: str, attr_value: str, attr_index: int, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals dictr attribute element reported.
        """
    def workItemSetPyObjectAttrib(self, workitem_id: int, subindex: int, attr_name: str, attr_value: str, jobid: str = '') -> None:
        """
        Called by mixin when a workitem signals pyobject attribute reported.
        """
    def onSharedServerStarted(self, args: _pdg._SharedServerInfo) -> None:
        """
        Called when a job has started a new sharedserver
        """
    def workItemWarning(self, workitem_id: int, message: str, jobid: str = '') -> None:
        """
        Called by EventDispatchMixin when a workitem sends a warning message.
        """
    def workItemResultServerAddr(self) -> str:
        """
        [virtual] Returns the results server address.  This is the TCP port
        that listens for status being returned by jobs.

        It should be a network address.  Eg: '192.168.1.123:83000'

        """
    def setWorkItemResultServerAddr(self, addr: str) -> None:
        """
        Sets the value of the result server address.
        Set to empty string or None to indicate the result server does not
        exist yet.
        """
    def getStatusURI(self, work_item: _pdg.WorkItem) -> str:
        """
        [virtual] Returns the farm's status URI for the given task.  Should return
        a valid URI or empty string.  Example: 'http://myfarm/status/jobid20'

        work_item   _pdg.WorkItem
        """
    def getLogURI(self, work_item: _pdg.WorkItem) -> str:
        """
        [virtual] Returns the farm's log URI for the given task.  Should return
        a valid URI or empty string.  Example: 'file:///myfarm/tasklogs/jobid20.log'

        work_item   _pdg.WorkItem
        """
    def submitAsJob(self, graph_file: str, node_path: str) -> str | tuple[str | None, Any]:
        """
        [virtual] Called when the scheduler should cook the entire TOP Network as
        a standalone job.  Returns the status URI for the submitted job.

        graph_file      Path to a .hip file containing the TOP Network, relative to
                        $PDG_DIR.
        node_path       Op path to the TOP Network
        """
    def endSharedServer(self, sharedserver_name: str) -> bool:
        """
        [virtual] Returns True on success, else False. Must be implemented by PyScheduler
        subclasses.

        sharedserver_name   shared server name

        End a shared server - should kill the long-running process
        """
    def setParameter(self, name: str, value: _ParmValue, str_expr: bool = False) -> None:
        """
        setParameter(self, str, value, boolean) -> self

        Sets a parameter on the node to a value. Must a int, float or string
        """
    def addParameter(self, name: str, label: str, tag: str | Sequence[str], param_type: _pdg.dataType, size: int = 1) -> _pdg.Port:
        """
        addParameter(self, str, str, strm _pdg.dataType, int) -> _pdg.Port

        Adds a custom parameter to the node with a given name, label, tag, type,
        and size. The size defaults to 1.
        """
    def setParameters(self, parameters: Mapping[str, _ParmValue] | None = None, **kwargs: _ParmValue) -> None:
        """
        setParameters(self, dict, **kwargs) -> self

        Batch sets parameters on the node from a dictionary or keyword
        args dictionary
        """
    def setValue(self, param_name: str, value: _ParmValue, index: int = 0) -> None:
        """
        setValue(self, str, value, int) -> self

        Sets the value of a node parameter
        """
    def setValues(self, values: Mapping[str, _ParmValue] | None = None, **kwargs: _ParmValue) -> None:
        """
        setValues(self, dict, **kwargs) -> self

        Batch sets the values of parameters
        """
    def resolveBaseEnvironment(self, parmprefix: str, node: _pdg.Node | None, work_item: _pdg.WorkItem | None, remove_list: Iterable[str] = ..., affix: str = '') -> dict[str, str]:
        """
        Returns an initial environment for a job, based on local env if
        indicated.
        """
    def resolveEnvParams(self, parmprefix: str, work_item: _pdg.WorkItem | None, escapeforshell: bool = True, affix: str = '') -> tuple[dict[str, str], list[str]]:
        """
        Parses a scheduler environment dict from a node, and merges
        with any scheduler node settings.
        Assumes the parm names follow the standard prefix convention.
        Returns environement dict and list of empty names as:
        ( {Name:Value}, [Name] )

        parmprefix      - the pdg::scheduler parm prefix
        work_item       - check for work_item overrides on it's node (optional)
        escapeforshell  - escape backslashes with more backslashes
        """
    def resolvePathMapping(self, job_env: MutableMapping[str, str], b64encode: bool = False) -> str | None: ...
    def addCommonJobEnvVars(self, job_env: MutableMapping[str, str], work_item: _pdg.WorkItem | None, verbosity: int = 0) -> None: ...
    def createJobDirsAndSerializeWorkItems(self, work_item: _pdg.WorkItem | None) -> None:
        """
        Creates the necessary intermediate directories for the job,
        and serializes the work item. Uses local paths.

        work_item      The work item object to serialize.
        """
    def getLocalLogDir(self) -> str:
        """
        Return the local log directory.
        """
    def getLocalDataDir(self) -> str:
        """
        Return the local data directory.
        """
    def initHoudiniMaxThreads(self, work_item: _pdg.WorkItem | None, parm_prefix: str, default_val: _T) -> int | _T:
        """
        Helper for setting up HOUDINI_MAXTHREADS
        """
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str:
        """
        [virtual].  Replace the special PDG tokens in the given command with
        scheduler-specific values.
        """
    def __getitem__(self, key: str) -> _pdg.Port: ...

def convertEnvMapToUTF8(job_env: _EnvT) -> _EnvT:
    """
    Converts the key-value pairs in job_env to utf8 encoding.
    """
@typing.overload
def evaluateParamOr(scheduler: PyScheduler, node: _pdg.Node | None, prefix: str, key: str, work_item: _pdg.WorkItem | None, default_value: str, toggle_prefix: str | None = ...) -> str: ...
@typing.overload
def evaluateParamOr(scheduler: PyScheduler, node: _pdg.Node | None, prefix: str, key: str, work_item: _pdg.WorkItem | None, default_value: bool, toggle_prefix: str | None = ...) -> bool: ...
@typing.overload
def evaluateParamOr(scheduler: PyScheduler, node: _pdg.Node | None, prefix: str, key: str, work_item: _pdg.WorkItem | None, default_value: int, toggle_prefix: str | None = ...) -> int: ...
@typing.overload
def evaluateParamOr(scheduler: PyScheduler, node: _pdg.Node | None, prefix: str, key: str, work_item: _pdg.WorkItem | None, default_value: float, toggle_prefix: str | None = ...) -> float: ...
def submitGraphAsJob(kwargs: ParmCallbackKwargs, topnode: hou.TopNode, sched_name: str, quiet: bool = False) -> str | tuple[str | None, Any]:
    """
    Helper function for the Submit Graph as Job button on
    scheduler TOP nodes, calls the scheduler submitAsJob function.

    kwargs : keyword args of callback (not used)
    topnode : the hou.TopNode of the scheduler to do the submission
    sched_name : Nice name of the scheduler to display in dialog
    quiet : False means don't show a dialog or print a message.
    """
def saveToPython(node: hou.OpNode, classname: str = '', description: str = '', file_path: str = '', tab_submenu: str = 'Schedulers') -> None: ...
