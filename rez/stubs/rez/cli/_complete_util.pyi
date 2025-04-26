import typing
from _typeshed import Incomplete
from rez.vendor.argcomplete import CompletionFinder as CompletionFinder, USING_PYTHON2 as USING_PYTHON2, debug as debug, default_validator as default_validator, split_line as split_line, sys_encoding as sys_encoding  # type: ignore[import-not-found]
from typing import Any

class RezCompletionFinder(CompletionFinder):
    _parser: Any
    always_complete_options: bool
    exclude: None
    validator: Any
    wordbreaks: str
    completions: typing.Generator[Any, None, None]
    def __init__(self, parser, comp_line, comp_point) -> None: ...

def ConfigCompleter(prefix, **kwargs): ...
def PackageCompleter(prefix, **kwargs): ...
def PackageFamilyCompleter(prefix, **kwargs): ...
def ExecutablesCompleter(prefix, **kwargs): ...

class FilesCompleter:
    files: bool
    dirs: bool
    file_patterns: Any
    def __init__(self, files: bool = True, dirs: bool = True, file_patterns: Incomplete | None = None) -> None: ...
    def __call__(self, prefix, **kwargs): ...

class CombinedCompleter:
    completers: list[Any]
    def __init__(self, completer, *completers) -> None: ...

class AndCompleter(CombinedCompleter):
    def __call__(self, prefix, **kwargs): ...

class SequencedCompleter(CombinedCompleter):
    arg: Any
    def __init__(self, arg, completer, *completers) -> None: ...
    def __call__(self, prefix, **kwargs): ...
