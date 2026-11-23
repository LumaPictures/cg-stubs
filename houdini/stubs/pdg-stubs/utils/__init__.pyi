import _houfs
import _pdg
import re
import threading
import typing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from io import BufferedReader, TextIOWrapper
from pdg.node import PyNode as PyNode
from typing import Any, Literal, Self, TypeAlias


from typing import TypeAlias
from typing import TypeVar
from typing import TypeVar
_NodeT = TypeVar('_NodeT', bound=PyNode | _pdg.Node)
_ParmValue: TypeAlias = int | float | str | Iterable[int | float | str]
timer_base_cls: TypeAlias = threading.Timer
@typing.overload
def read_file(file_path: str, binary: Literal[False] = ...) -> _houfs.FileReader | TextIOWrapper: ...
@typing.overload
def read_file(file_path: str, binary: Literal[True]) -> _houfs.FileReader | BufferedReader: ...
@typing.overload
def read_file(file_path: str, binary: bool = ...) -> _houfs.FileReader | TextIOWrapper | BufferedReader: ...
def common_path_part(input_files: Sequence[str], suffix: bool = False) -> str: ...
def make_glob_pattern(results: list[tuple[str, str]]) -> list[tuple[str, str]]: ...
@typing.overload
def format_results(results: Iterable[_pdg.File], scheduler: _pdg.SchedulerBase | None, apply_hip: Literal[False] = ..., make_pattern: bool = ..., localize: bool = ...) -> list[tuple[str, str]]: ...
@typing.overload
def format_results(results: Iterable[_pdg.File], scheduler: _pdg.SchedulerBase | None, apply_hip: Literal[True], make_pattern: bool = ..., localize: bool = ...) -> list[tuple[str, str, str]]: ...
@typing.overload
def format_results(results: Iterable[_pdg.File], scheduler: _pdg.SchedulerBase | None, apply_hip: bool = ..., make_pattern: bool = ..., localize: bool = ...) -> list[tuple[str, str]] | list[tuple[str, str, str]]: ...
def natural_sort_key(s: str, _nsre: re.Pattern[str] = ...) -> tuple[int | str, ...]:
    """
    Natural number-aware sort key for string lists
    """

class TickTimer(timer_base_cls):
    """
    Utility class for a recurring timer.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self) -> None: ...

class TimerScope:
    name: str
    start: float | None
    interval: float | None
    def __init__(self, name: str) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...

def print_headless(s: object) -> None: ...
def expand_vars(command: str, job_env: Mapping[str, str]) -> str:
    """
    Expand the given command using env var substitution from the given
    environment dict.  Supports $VAR, ${VAR}
    """
def get_result_data_tag(file_path: str) -> str: ...
def get_result_viewer(file_path: str) -> str: ...
def parmAttribName(port: _pdg.Port, prefix: str | None = None) -> str: ...
def setParmOnItem(item: _pdg.WorkItem, port: _pdg.Port, prefix: str | None = None) -> None:
    """
    Copies the value of the given port to the given workitem.

    setParmOnItem(self, _pdg.workItem, _pdg.Port) -> NoneType

    Does type checking on value an sets the parameter as needed. The value
    can also be a tuple of a float, str or int, which will automatically
    expand to multiple setParam calls with different indices

    If a prefix is provided, this is stripped from the parm name
    """
def setMultiParameter(node: _NodeT, multi_name: str, multi_member_defs: Sequence[tuple[str, _pdg.dataType, int]], multi_member_values: Sequence[Sequence[_ParmValue]], tag: str = '') -> _NodeT:
    """Set a 'multiparm' on a PDG node. Overwrites existing parameters.

    Multiparms don't exist in the PDG world, but this class recreates the logic
    of multiparms and does the right thing as if a multiparm from TOPs was
    converted to spare parameters in PDG.

    Args:
        node:       The PyNode on which to add the parameters.
        multi_name: The name of the multi parm.
        multi_member_defs:   A list of tuples of (name, data_type, vec_size) of
                             the member parms, without the index suffix.
        multi_member_values: A parallel list of tuples of values for the names.
                             Each tuple t should have
                             len(t) == len(multi_member_defs).
        tag:        Tag to apply to any added parameters

    Returns: node
    """
def parseEnvDefinition(job_env_str: str, force: bool = False) -> tuple[dict[str, str], list[str]]:
    '''
    Parses a string in houdini .env format into
    a dict of string : string

    Example:
    # comments
    MYKEY=My Val
    MYKEY2 = "path with spaces"
    # remove a key
    MYKEY3=
    '''
def parseEnvironmentFile(env_filepath: str) -> dict[str, str]: ...
def addItemFromSerialized(item_holder: _pdg.WorkItemHolder, upstream_item: _pdg.WorkItem | None, jsonfilepath_local: str, localizePath: Callable[[str], str] | None = None) -> _pdg.WorkItem:
    """
    Add a new workitem and overwrite it with the data pulled from the given
    json data file.
    """
def parseDatalayerServerAddr(txt: str | None) -> str | None:
    """
    Parses the given text for the Data Layer Server info as written out by
    topcook.py --datalayerserverport.  Returns the endpoint in the format
    ip:port, or None on failure.
    """
