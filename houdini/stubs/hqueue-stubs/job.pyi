# Houdini stubs generated from Houdini 22.0.466

import typing
from . import houdini as houdini
from collections.abc import Mapping
from typing import Literal

@typing.overload
def getCommandDict(hfs_dict: Mapping[str, str], num_cpus: int = ..., command: Literal[''] | None = ...) -> dict[str, dict[str, str]]: ...  # type: ignore[overload-overlap]
@typing.overload
def getCommandDict(hfs_dict: Mapping[str, str], num_cpus: int, command: str) -> dict[str, str]: ...
@typing.overload
def getCommandDict(hfs_dict: Mapping[str, str], num_cpus: int = ..., *, command: str) -> dict[str, str]: ...
def getCommand(hfs_dict: Mapping[str, str], command: str, platform: str, num_cpus: int = 0) -> str:
    """
    Return the platform-specific command using the given dictionary of 
    HFS path values.
    """
def getCommands(hq_cmds: Mapping[str, dict[str, str] | str], cmd_key: str, script: str | None = None) -> dict[str, str]:
    '''Return platform-specific job commands defined by `cmd_key` and `script`.

    Return a dictionary where the keys are the supported platforms
    (i.e. linux, windows, macos) and the values are the shell commands to be 
    executed for the job. `cmd_key` is a key into the `hq_cmds` dictionary and
    should be either "hython", "python", "karma" or "mantra".

    The optional `script` argument indicates whether the job should
    execute a script file.  If `script` is None, then the job should run
    the commands from hq_cmds[cmd_key] as-is.
    '''
