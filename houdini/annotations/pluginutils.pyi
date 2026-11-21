import re
import types
from collections.abc import Callable, Generator, Iterable, Mapping, Sequence
from typing import Any, TypeVar

_T = TypeVar("_T")

MODULE_CACHE: dict[str, tuple[types.ModuleType, float]]
LIST_CACHE: dict[tuple[tuple[str, ...], str, str], Sequence[str]]
CHECK_MOD_TIMES: bool
split_exp: re.Pattern[str]

def invalidateCache() -> None: ...
def loadModule(
    filepath: str, silent: bool = ..., context: Mapping[str, Any] | None = ...
) -> types.ModuleType | None: ...
def findModules(
    dirname: str,
    path_dirs: Sequence[str] | None = ...,
    file_pattern: str = ...,
    include_shadowed: bool = ...,
    reverse: bool = ...,
    pathvar: str | None = ...,
    order_key: str | None = ...,
) -> list[str]: ...
def findFunctions(
    dirname: str,
    fn_name: str,
    path_dirs: Sequence[str] | None = ...,
    file_pattern: str = ...,
    include_shadowed: bool = ...,
    reverse: bool = ...,
    pathvar: str | None = ...,
    order_key: str | None = ...,
) -> Generator[Callable[..., Any], None, None]: ...
def runFunctions(
    dirname: str,
    fn_name: str,
    args: Iterable[Any] = ...,
    kwargs: Mapping[str, Any] | None = ...,
    path_dirs: Sequence[str] | None = ...,
    file_pattern: str = ...,
    include_shadowed: bool = ...,
    reverse: bool = ...,
    pathvar: str | None = ...,
    order_key: str | None = ...,
) -> list[Any]: ...
def pipelineFunctions(
    dirname: str,
    fn_name: str,
    main_arg: _T,
    args: Iterable[Any] = ...,
    kwargs: Mapping[str, Any] | None = ...,
    path_dirs: Sequence[str] | None = ...,
    file_pattern: str = ...,
    include_shadowed: bool = ...,
    reverse: bool = ...,
    pathvar: str | None = ...,
    order_key: str | None = ...,
) -> _T: ...
def typedPipeline(
    dirname: str,
    fn_name: str,
    main_arg: dict[str, Any],
    args: Iterable[Any] = ...,
    kwargs: Mapping[str, Any] | None = ...,
    path_dirs: Sequence[str] | None = ...,
    file_pattern: str = ...,
    include_shadowed: bool = ...,
    reverse: bool = ...,
    set_fields: Iterable[str] = ...,
    datetime_fields: Iterable[str] = ...,
    pathvar: str | None = ...,
    order_key: str | None = ...,
) -> dict[str, Any]: ...
def runSnapshotMetadataPlugins(
    meta_dict: dict[str, Any],
    args: Iterable[Any] = ...,
    kwargs: Mapping[str, Any] | None = ...,
    dirname: str = ...,
    fn_name: str = ...,
    set_fields: Iterable[str] = ...,
    datetime_fields: Iterable[str] = ...,
    pathvar: str | None = ...,
) -> dict[str, Any]: ...
