import subprocess
import threading
import typing
from Queue import Queue
from collections.abc import Iterable, MutableMapping, MutableSequence
from houtypes import JSONValue
from typing import Literal

verbose_log: bool

def printLog(msg: str) -> None:
    """
    Print handler for helpful debugging.
    """
def getDeadlineCommand() -> str:
    """
    Finds and returns the Deadline command with full path on current platform, 
    or empty string if not found.
    Requires that Deadline be installed and DEADLINE_PATH environment path 
    is setup.
    """
@typing.overload
def callDeadlineCommand(arguments: Iterable[str], hideWindow: bool = ..., readStdout: Literal[True] = ...) -> str | tuple[bytes, bytes]: ...
@typing.overload
def callDeadlineCommand(arguments: Iterable[str], hideWindow: bool, readStdout: Literal[False]) -> str | tuple[str, str]: ...
@typing.overload
def callDeadlineCommand(arguments: Iterable[str], *, readStdout: Literal[False]) -> str | tuple[str, str]: ...
@typing.overload
def callDeadlineCommand(arguments: Iterable[str], hideWindow: bool = ..., readStdout: bool = ...) -> str | tuple[bytes, bytes] | tuple[str, str]: ...
def getDeadlineCommandProc(arguments: MutableSequence[str], environment: MutableMapping[str, str] = ..., hideWindow: bool = True) -> subprocess.Popen[bytes] | str:
    """
    Returns a new process with Deadline command running in interactive mode.
    """
def getJobTaskInfo(dlcmd_intr: DeadlineCmdInteractive, job_id: int | str, task_id: int | str) -> tuple[bool, JSONValue]:
    """
    Returns (result, task info) of the task of the specified job.
    """
def failJob(dlcmd_intr: DeadlineCmdInteractive, job_id: int | str) -> tuple[bool, JSONValue]:
    """
    Stops the specified job and marks it as failed.
    Returns (result, output).
    """
def failJobs(dlcmd_intr: DeadlineCmdInteractive, job_ids: Iterable[str]) -> tuple[bool, JSONValue]:
    """
    Stops the specified job and marks it as failed.
    Returns (result, output).
    """
def appendJobFrameRange(dlcmd_intr: DeadlineCmdInteractive, job_id: int | str, frame_range: str) -> tuple[bool, JSONValue]:
    """
    Appends the given frame range to the job therefore making Deadline schedule 
    a new task for this frame. frame_range should be a string with format: start-end
    Examples: '0-5' '1-4', '10-20'
    """
def setJobExtraInfoKeyValue(dlcmd_intr: DeadlineCmdInteractive, job_id: int | str, key: str, value: str) -> tuple[bool, JSONValue]:
    """
    Set the given key-value pair as part of given job's extra info.
    """
def executeScript(dlcmd_intr: DeadlineCmdInteractive, path: str) -> None:
    """
    Executes the given deadline script on the farm.
    """

class DeadlineCmdInteractive:
    """
    Starts an interactive Deadline command process. Allows to submit commands
    and retrieve output. Output will be in json format.
    Use submitCommandAndGetOutput to submit and wait for output.
    submit_command_timeout is the timeout in seconds to wait after submitting a command
    """
    submit_commmand_timeout: float
    dlcmd_proc: subprocess.Popen[bytes] | str | None
    repo_command_arg: str
    msg_queue: Queue[JSONValue] | None
    msg_thread: threading.Thread | None
    cmd_lock: threading.Lock
    def __init__(self, submit_command_timeout: float) -> None: ...
    def startProcess(self, repo_command_arg: Iterable[str], environment: MutableMapping[str, str]) -> None:
        """Start the interactive deadlinecommand subprocess.

        Send commands to the interactive process to query and manipulate
        Deadline jobs.
        """
    def stopProcess(self) -> None: ...
    def submitCommand(self, cmd: str) -> None: ...
    def getNextOutputResult(self) -> tuple[bool, JSONValue]:
        """
        Returns the next output result from the deadline command process
        as a booleon (success or not), and json dict of the actual result.
        """
    def submitCommandAndGetOutput(self, cmd: str) -> tuple[bool, JSONValue]:
        """
        Submits given cmd, and returns tuple of boolean and stdout from process.
        """
