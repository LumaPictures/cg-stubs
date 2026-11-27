import subprocess
import threading
from collections.abc import Iterable, MutableMapping, MutableSequence
from queue import Queue
from typing import Literal, overload

from houtypes import JSONValue

verbose_log: bool

def printLog(msg: str) -> None: ...
def getDeadlineCommand() -> str: ...

# "" when deadlinecommand isn't found; the process's (stdout, stderr), or ("", "") when
# `readStdout` is False.
@overload
def callDeadlineCommand(
    arguments: Iterable[str], hideWindow: bool = ..., readStdout: Literal[True] = ...
) -> str | tuple[bytes, bytes]: ...
@overload
def callDeadlineCommand(
    arguments: Iterable[str], hideWindow: bool, readStdout: Literal[False]
) -> str | tuple[str, str]: ...
@overload
def callDeadlineCommand(
    arguments: Iterable[str], *, readStdout: Literal[False]
) -> str | tuple[str, str]: ...
@overload
def callDeadlineCommand(
    arguments: Iterable[str], hideWindow: bool = ..., readStdout: bool = ...
) -> str | tuple[bytes, bytes] | tuple[str, str]: ...

# Looser than the overloads, as pyright can't tie the `output, errors` it infers to
# `readStdout`; the stub only has the overloads.
def callDeadlineCommand(
    arguments: Iterable[str], hideWindow: bool = ..., readStdout: bool = ...
) -> str | tuple[bytes | str, bytes | str]: ...

# "" when deadlinecommand isn't found.
def getDeadlineCommandProc(
    arguments: MutableSequence[str],
    environment: MutableMapping[str, str] = ...,
    hideWindow: bool = ...,
) -> subprocess.Popen[bytes] | str: ...

# (ok, the "result" of deadlinecommand's JSON output), which depends on the command: a job id, a
# dict of task info, ...  Or (False, an error message).
def getJobTaskInfo(
    dlcmd_intr: "DeadlineCmdInteractive", job_id: int | str, task_id: int | str
) -> tuple[bool, JSONValue]: ...
def failJob(dlcmd_intr: "DeadlineCmdInteractive", job_id: int | str) -> tuple[bool, JSONValue]: ...
def failJobs(
    dlcmd_intr: "DeadlineCmdInteractive", job_ids: Iterable[str]
) -> tuple[bool, JSONValue]: ...
def appendJobFrameRange(
    dlcmd_intr: "DeadlineCmdInteractive", job_id: int | str, frame_range: str
) -> tuple[bool, JSONValue]: ...
def setJobExtraInfoKeyValue(
    dlcmd_intr: "DeadlineCmdInteractive", job_id: int | str, key: str, value: str
) -> tuple[bool, JSONValue]: ...
def executeScript(dlcmd_intr: "DeadlineCmdInteractive", path: str) -> None: ...

class DeadlineCmdInteractive:
    submit_commmand_timeout: float
    # getDeadlineCommandProc() returns "" when deadlinecommand isn't found.
    dlcmd_proc: subprocess.Popen[bytes] | str | None
    repo_command_arg: str
    # The json.loads() of each line deadlinecommand outputs.
    msg_queue: Queue[JSONValue] | None
    msg_thread: threading.Thread | None
    cmd_lock: threading.Lock
    def __init__(self, submit_command_timeout: float) -> None: ...
    def startProcess(
        self, repo_command_arg: Iterable[str], environment: MutableMapping[str, str]
    ) -> None: ...
    def submitCommand(self, cmd: str) -> None: ...
    def getNextOutputResult(self) -> tuple[bool, JSONValue]: ...
    def submitCommandAndGetOutput(self, cmd: str) -> tuple[bool, JSONValue]: ...
